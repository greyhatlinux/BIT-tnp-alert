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

    updates.check_updates()

    print("Emailing the new updates, if any")
    notify.email()


    with open('source.txt', 'w') as file: pass
    os.remove('ann.txt')
    os.rename(r'new-ann.txt', r'ann.txt')

    with open('job-source.txt', 'w') as file: pass
    os.remove('companies.txt')
    os.rename(r'new-companies.txt', r'companies.txt')


    print("Done!")


