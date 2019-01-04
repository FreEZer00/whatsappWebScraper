from bs4 import BeautifulSoup
from selenium import webdriver
import time
import string
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

a=""
while a!='y':
	a = raw_input('Have you scanned the QRCode? (Enter y) - ')


i=1
users = driver.find_elements_by_class_name('_25Ooe') #_2FBdJ	_2wP_Y	_3j7s9
for user in users:
	user.click()
	time.sleep(2)
	user_soup = BeautifulSoup(driver.page_source, 'lxml')
	nameCon= user_soup.findAll("div", {"class":'_1WBXd'})
	user_name=nameCon[0].div.div.span["title"]
	try:
		last_login=nameCon[0].div.next_sibling.span["title"]
	except Exception as e:
		last_login="not available"
	print(str(i) + " " + user_name + ": " +repr(last_login))
	i=i+1