from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

logo =  """\033[1;37;1m     
  
██████╗ ██╗██╗██╗  ██╗ █████╗ ██████╗ ██╗
██╔══██╗██║██║██║  ██║██╔══██╗██╔══██╗██║
██████╔╝██║██║███████║███████║██████╔╝██║
██╔══██╗██║██║██╔══██║██╔══██║██╔══██╗██║
██████╔╝██║██║██║  ██║██║  ██║██║  ██║██║
╚═════╝ ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
                                         
██████╗ ██╗   ██╗██╗     ███████╗██╗  ██╗
██╔══██╗██║   ██║██║     ██╔════╝╚██╗██╔╝
██████╔╝██║   ██║██║     █████╗   ╚███╔╝ 
██╔══██╗██║   ██║██║     ██╔══╝   ██╔██╗ 
██║  ██║╚██████╔╝███████╗███████╗██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                         

-----------------------------------------------"""

def menu():
	os.system('clear')
	print(logo)
	print('[1] Random Uid Crack')
	print('[2] Contact To Owner')
	print('[0] Exit')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		md()
	elif opt =='2':
		Contact()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()

def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1;33;40m", end = "")
    print(47*'\033[1;37;1m-')
    sp("\033[1;37;1m[?] Enter the 2 factor code by google authenticator\n")
    print(47*'\033[1;37;1m-')
    apr = str(input('\033[1;37;1m[?] Enter Code : '))
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;32;40m", end = "")
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    print(">>", line, "\n")

print("\033[1;33;40m", end = "")
os.system('clear')
print(logo)
sp("\033[1;37;1m[+] Login With Email/Number \n")
print(47*'\033[1;37;1m-')
USERNAME = str(input('[?] Enter Email/Number : '))
print("\033[1;33;40m", end = "")
print(47*'\033[1;37;1m-')
sp("\033[1;37;1m[+] Enter Your Facebook Password\n")
print(47*'\033[1;37;1m-')
PASSWORD = str(input('[?] Enter : '))
login()
print("\033[1;33;40m", end="")
cid = str(input("➣Enter your convo or inbox I'd link: "))
curl = 'https://mbasic.facebook.com/messages/t/' + str(cid)
np1 = str(input("➣Enter Tatta Name: "))
np = str(input("➣Enter notepad file name: "))
t = int(input("➣Enter TIME: "))
print('\n')
print("\033[1;34;40m", end = "")
print('BIIH4RI RULL3X 4LW4YS 0N FIIR3')
print ('THIIS T00L CR34T3 BY BIH4RI B4BU', '\n')
while True:
    try:
        f = open(np, 'r')
        lines = f.readlines()
        f.close()
        count = 0
        flag = False

        for i, line in enumerate(lines):
            if i < count:
                continue  # Skip lines that have already been sent
            if len(line) > 3:
                if count != 0:
                    sleep(t)
                findtextchat(curl)
                sendtextconvo(str(np1) + line)
                e = datetime.datetime.now()
                print("\033[1;32;40m", end="")
                print(" --> Convo I'd Link  :--", cid)
                print(e.strftime("--> BIH4RU RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("--> Message Successfully Sent By  BiiHaRii DoN :D ::-->> ", np1, line, "\n")
                count += 1
                if count % 10 == 0:
                    sleep(10)
            if i == len(lines) - 1:
                flag = True
        if flag:
            count = 0
            flag = False
    except Exception as e:
        d = datetime.datetime.now()
        print("\033[1;31;40m", end="")
        print(d.strftime("--> BIIH4RI RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
        print("-->> Some error occurred...Waiting for 30 seconds before retrying...", e, "\n")
        sleep(30)
