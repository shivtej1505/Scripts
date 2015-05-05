#!/usr/bin/python
import requests
import pynotify 
from time import sleep
url="http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=ASHOKLEY&illiquid=0&smeFlag=0&itpFlag=0"
def Notify(final):
    pynotify.init('test')
    p=pynotify.Notification("Average Price",final)
    p.show()
    return
while True:
    try:
        r=requests.get(url)
        s=str(r.text)
        start=s.find('averagePrice')
        end=start+21
        k=s[start:end]
        final=k.split('"')[2]
        Notify(final)
    except:
        print "Request Failed"
    try:
        sleep(10)
    except KeyboardInterrupt:
        print "Bye"
        break
