import bs4                        
import requests

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def log_in():

    options = Options()
    options.headless = True
    driver = Firefox(executable_path='/usr/bin/geckodriver', options=options)

    driver.get('http://placement.bitmesra.ac.in/Login.aspx')
    print("Website Accessed!")
    print("Logging in!")

    name = driver.find_element_by_name('txtUsername')
    name.send_keys('<registered email>')

    email = driver.find_element_by_name('txtPassword')
    email.send_keys('<your password>')

    driver.find_element_by_id("imgSubmit").click()
    print("Loggged in!")

    print("Gettig updates...")

    res = requests.get("http://placement.bitmesra.ac.in/Student/StudentLanding.aspx")

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    driver.get('http://placement.bitmesra.ac.in/Student/StudentLanding.aspx')

    with open ("source.txt", 'w') as f:   
        f.write(driver.page_source)

    print("Collected T&P updates!")
    print("Loggig out.")
    driver.quit()