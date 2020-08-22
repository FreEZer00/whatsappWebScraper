from bs4 import BeautifulSoup
from selenium import webdriver
import time
import string
from datetime import datetime, timedelta
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

victim = 'Laura'

def parse_date(s):
	array = s.split(" ")
	if len(array) >4:
		return array[2] + " " + array[4] 
	else:
		if array[2] == 'heute':
			return datetime.now().strftime("%d.%m.%Y") + " " + array[3]
		else:
			return datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y') + " " + array[3]

def check_user_time(elem):
	try:
		last_login=elem[0].div.next_sibling.span["title"]
	except Exception as e:
		last_login="not available"

	if last_login.startswith('online'):
		return datetime.now().strftime("%d.%m.%Y %H:%M:%S")
	elif last_login.startswith('zuletzt online'):
		return parse_date(last_login)
	else:
		return False

def single_check(my_driver):
		old_res =""
		while True:
			user_soup = BeautifulSoup(my_driver.page_source, 'lxml')
			nameCon= user_soup.findAll("div", {"class":'_3V5x5'})
			user_name = nameCon[0].div.div.span["title"]
			res = check_user_time(nameCon)
			if (res != old_res):
				if res != False:
					print(user_name + ": " +res)
					old_res = res
			time.sleep(2)

def all_of_em(nameCon_copy):
	res = check_user_time(nameCon_copy)
	if res != False:
		print(user_name + ": " +res)


driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

a=""
while a!='y':
	a = raw_input('Have you scanned the QRCode? (Enter y) - ')


i=1
users = driver.find_elements_by_class_name('_2WP9Q') #_25Ooe _2FBdJ	_2wP_Y	_3j7s9
for user in users:
	user.click()
	time.sleep(2)
	user_soup = BeautifulSoup(driver.page_source, 'lxml')
	nameCon= user_soup.findAll("div", {"class":'_3V5x5'})
	found_user_name=nameCon[0].div.div.span["title"]
	if found_user_name.startswith(victim):
		single_check(driver)
