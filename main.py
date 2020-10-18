import os
import sys
import bs4                        
import requests

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

pwd = os.getcwd() + "/mods"
sys.path.insert(0, pwd)

from mods import notify
from mods import logging
from mods import updates

if __name__ == "__main__":

    print("Googling the website!")

    logging.log_in()

    check_updates()

    print("Emailing the new updates, if any")
    notify.email()
    with open('new-update.txt', 'w') as file: pass
    print("Done!")


