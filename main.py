import modules

if __name__ == "__main__":
    options = Options()
    options.headless = True
    driver = Firefox(executable_path='/usr/bin/geckodriver', options=options)
    wait = WebDriverWait(driver, timeout=2)

    print("Googling the website!")
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
            f.write(i)
            with open('new-update.txt', 'a+') as recent:
                recent.write(i)



    with open('new-update.txt', 'r') as recent:
        if(recent.read()):
            print(recent.read())
            print("mailing")
    print("Thank you!")


