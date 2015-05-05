import requests
import smtplib
from time import sleep
import re
while(True):
    try:
        url="http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/HYD_DEL_26-04-2015"
        r=requests.get(url)
        print "Got It"
        g=str(r.text)
        L=re.findall('Rs\.</span>[0-9]{1,},[0-9]{3}</p>',g)
        for price in L:
            print price
        print "No"
    except:
        break
