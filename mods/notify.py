import os
import time                       

def email():
    with open('new-update.txt','r') as f:
        data = f.read()
    
    ann = data.split("\n")

    print("Yes, we have new T&P notifications")
    print(ann)
    body = " "
    for new in ann:
        if( new != ''):
            body = body + new + ", "

        mem = ['abc@gmail.com', 'def@gmail.com']
        if(len(body) > 5):
            for member in mem:
                print(mem)
                cmd = "python3 mods/email_test.py " + member + " " + "'" + body + "'"
                os.system(cmd)
                time.sleep(3)
        else:
            print("No new Updates!")
