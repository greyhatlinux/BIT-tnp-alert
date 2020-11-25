import os
import bs4
import time                       
import requests


mem = ['abc@gmail.com', 'def@gmail.com']
def email():
    print("Looking for Notifications")

    with open('new-ann.txt','r') as f:
      new_ann = f.read()
      
    with open('ann.txt','r') as f:
      old_ann = f.read()

    ann = ""

    new_upd = new_ann.split("\n")
    old_upd = old_ann.split("\n")


    for update in new_upd:
      if (update not in old_upd):
          ann = ann + update + ", "
      else:
        break

    print(ann)
  
    if(len(ann) > 5):
      print("Yes, there are new notifications")
      ann = "New Notifications: " + ann
      for member in mem:
        print(mem)
        print("mailing")
        cmd = "python3 mods/email_test.py " + member + " " + "'" + ann + "'"
        os.system(cmd)
        time.sleep(3)
    else:
      print("No new notifications!")

    # ------------------------------------------------------------
    # emailing job updates if any

    print("Looking for Jobs")

    with open('new-companies.txt','r') as f:
      new_job = f.read()
      
    with open('companies.txt','r') as f:
      old_job = f.read()

    job_data = ""

    new_comp = new_job.split("\n")
    old_comp = old_job.split("\n")

    for comp in new_comp:
      if (comp not in old_comp):
          job_data = job_data + comp + ", "
      else:
        break

    print(job_data)

    if(len(job_data)>5):
      print("Yes, there are new Jobs!")
      job_data = "New Jobs : " + job_data
      for member in mem:
        print(mem)
        print("mailing")
        cmd = "python3 mods/email_test.py " + member + " " + "'" + job_data + "'"
        os.system(cmd)
        time.sleep(3)
    else:
      print("No new Jobs")