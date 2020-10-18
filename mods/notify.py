import os
import bs4                        
import requests

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def email():
    with open('new-update.txt','r') as f:
    data = f.read()
    ann = data.split("\n")
    for i in ann :
        options = Options()
        options.headless = True
        driver = Firefox(executable_path='/usr/bin/geckodriver', options=options)
        url = "https://docs.google.com/forms/d/e/1FAIpQLSfo4EhBEeuytHxdvFRxBbZWANVOiwMiq_KmDFys6vnk4BzCdA/viewform?usp=pp_url&entry.857248467=VishalGorai&entry.194809400=" + i
        driver.get(url)
        submit = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonFilled")
        print("Sending Notification!")
        submit[0].click()