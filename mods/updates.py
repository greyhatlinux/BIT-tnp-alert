import os
import bs4

def check_update():
    with open('source.txt' , 'r') as f:
    data = f.read()

    os.remove('source.txt')
    
    soup = bs4.BeautifulSoup(data, 'html.parser')

    raw = set(soup.select('#divAnnouncement_d'))
    for i in raw:
        ann = i.text
    new_all = ann.split('\xa0')
    
    with open('announcement.txt' , 'r+') as f:
      prev_all = f.read()
      prev = prev_all.split('\n')
      for i in new_all:
        if ( i not in prev_all):
            f.write(i + "\n")
            with open('new-update.txt', 'a+') as recent:
                recent.write(i + "\n")