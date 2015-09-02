import requests
import smtplib
import time
from time import sleep
import datetime
import re
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import inch,mm,cm
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
today=datetime.datetime.today()
user="Abishek Bansal"
sub="Flight Details"
server='myserver'     # put servername
email='myemailAddress@server'

shiv="Shivang Script Services"

while(True):
    doc=SimpleDocTemplate("flight_lite.pdf",pagesize=A4,rightMargin=72,leftMargin=27,topMargin=72,bottomMargin=18)
    Story=[]
    logo="python_script.png"
    img=Image(logo,1*inch,1*inch)
    Story.append(img)
    styles=getSampleStyleSheet()
    Story.append(Spacer(1,31))
    Story.append(Paragraph(shiv,styles["Heading1"]))
    Story.append(Spacer(1,12))
    for i in range(0,10):
        today+=datetime.timedelta(i)
        date=str(today).split()[0]
        date=date.split("-")
        date=str(date[2])+"-"+str(date[1])+"-"+str(date[0])
        url=str("http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/HYD_DEL_"+date)
        try:
            r=requests.get(url)
        except:
            print "No"
            continue
        g=str(r.text)
        L=re.findall('[0-9]{1,},[0-9]{3}',g)
        may=[]
        final=500000
        for price in L:
            price=int(str(price).replace(',',''))
            if price<=final:
               final=price
        may.append(final)
               #Story.append(Paragraph(str("Rs.")+str(price)+str(","),styles["Normal"]))
                #Story.append(Spacer(1,12))
        if len(may)>=1:
            Story.append(Spacer(1,12))
            Story.append(Paragraph(str("Flights on ")+str(date),styles["Normal"]))
            Story.append(Spacer(1,12))
            for profit in may:
                Story.append(Paragraph(str("Rs.")+str(profit)+" ",styles["Normal"]))
    Story.append(Spacer(1,12))
    Story.append(Spacer(1,12))
    Story.append(Paragraph('pdf generated on '+str(datetime.datetime.today()).split()[0],styles["Normal"]))
    Story.append(Paragraph('By Shivang Nagaria',styles["Heading3"]))
    doc.build(Story)
    print "fetched"
#mailing the pdf
    msg=MIMEMultipart()
    msg['Subject']=sub
    msg['From']=shiv
    msg['To']=user
    body=MIMEText("""Hello Abhishek,Flight details attached\n\nShivang Nagaria""")
    msg.attach(body)
    f=open('flight_lite.pdf','rb')
    att=MIMEApplication(f.read(),_subtype="pdf")
    att.add_header('Content-Disposition','attachment',filename="shivang.pdf")
    f.close()
    msg.attach(att)
#mesg=MIMEMultipart()
#msg.attach(MIMEText(file("/home/shivang/ITWS/python/flight_lite.pdf").read()))
#mesg.attach(MIMEText(file("/home/shivang/ITWS/python/flight_lite.pdf").read()))
    send=smtplib.SMTP(server)
    send.sendmail("shivang.nagaria@students.iiit.ac.in",[email],msg.as_string())
    send.quit()
    print "send"
    t=24*60*60
    sleep(t)
