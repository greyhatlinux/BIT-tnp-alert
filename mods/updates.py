import os
import bs4

def check_updates():
    with open('source.txt' , 'r') as f:
      data = f.read()

    soup = bs4.BeautifulSoup(data, 'html.parser')

    all_ann = soup.select('#tbodydetail #trjafrequest #subject')

    with open ("new-ann.txt", 'a+') as f:   
        for ann in all_ann:
            f.write(ann.text + '\n')


def check_jobs():

    with open('job-source.txt', 'r') as f:
        data = f.read()

    soup = bs4.BeautifulSoup(data, 'html.parser')

    all_comp = soup.select('#data-table-hrteam #Joblist #trlist #name')

    with open ("new-companies.txt", 'a+') as f:   
        for comp in all_comp:
            f.write(comp.text + '\n')