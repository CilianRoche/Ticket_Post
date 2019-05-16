import sys,os,selenium,getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#Buttons and elements to find
path = 'C:/scripts/tickets/ticket_import_template.csv'
chromedriver = 'C:/Scripts/chromedriver/chromedriver.exe'
link = 'https://fcnhelpdesk/helpdesk/WebObjects/Helpdesk.woa'
usernameXpath = '//*[@id="userName"]'
passwordXpath = '//*[@id="password"]'
loginXpath = '//*[@id="dialog"]/div[1]/a/div/div[2]'
settingsXpath = '//*[@id="navigation"]/div[1]/div[9]/a/div'
importOptioXpath = '//*[@id="preferences-menu"]/div/div[23]/span[2]'
importTicketsXpath = '//*[@id="preferences-menu"]/div/div[24]/ul/li[5]/a'
typeXpath = '//*[@id="ImporterUpdateContainer"]/form/table/tbody/tr/td/table/tbody/tr[8]/td[2]/div[1]/input[2]'
fileXpath = '//*[@id="ImporterUpdateContainer"]/form/table/tbody/tr/td/table/tbody/tr[10]/td[2]/div[1]/table/tbody/tr/td[1]/input'
csvXpath = '//*[@id="ImporterUpdateContainer"]/form/table/tbody/tr/td/table/tbody/tr[8]/td[2]/div[1]/input[2]'
importButton = '//*[@id="ImporterUpdateContainer"]/form/table/tbody/tr/td/table/tbody/tr[11]/td/table/tbody/tr/td[2]/div/a/div/div[2]'

def get_cred():
    username = 'cproche'
    password = getpass.getpass()
    return username,password

def headless_chrome():
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chromedriver, chrome_options=options)
	return driver

creds = get_cred()
driver = headless_chrome()
driver.get(link)
driver.maximize_window()
driver.find_element_by_xpath(usernameXpath).send_keys(creds[0])
driver.find_element_by_xpath(passwordXpath).send_keys(creds[1])
driver.find_element_by_xpath(loginXpath).click()
driver.find_element_by_xpath(settingsXpath).click()
driver.find_element_by_xpath(importOptioXpath).click()
time.sleep(1)
driver.find_element_by_xpath(importTicketsXpath).click()
driver.find_element_by_xpath(csvXpath).click()
menu = driver.find_element_by_xpath(fileXpath)
menu.send_keys('C:/scripts/tickets/ticket_import_template.csv')
driver.find_element_by_xpath(importButton).click()
time.sleep(4)
