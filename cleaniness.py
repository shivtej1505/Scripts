#!/usr/bin/python
import smtplib
import time

toList = [
    ['shivang.nagaria@students.iiit.ac.in'],
    ['shivang.nagaria@students.iiit.ac.in','prajjwal.khariya@students.iiit.ac.in'],
    ['sanket.markan@students.iiit.ac.in','hemant.kasat@research.iiit.ac.in'],
    ['sanket.shah@research.iiit.ac.in','raj.manvar@students.iiit.ac.in'],
    ['manan.bhandari@research.iiit.ac.in','toshad.salwekar@students.iiit.ac.in'],
    ['aditya.motwani@students.iiit.ac.in','anirudh.dahiya@research.iiit.ac.in'],
    ['neeraj.battan@research.iiit.ac.in','shreyash.shriyam@students.iiit.ac.in'],
    ['aagam.shah@research.iiit.ac.in','deepanshu.jain@students.iiit.ac.in']
]


def sendMain(mailTo,turn):
    print turn
    sender = "Safai Samiti<safaiSamiti@2ndFloorE.iiit.ac.in>"
    subject = "Reminder: It's your turn to clean wing"
    body = "Today is your turn to clean our wing, kindly do it.\nThanks for your cooperation."
    for email in mailTo:
        reciever = email.split('@')[0]
        server = email.split('@')[1]
        fullBody = 'Hi,%s\n%s' % (reciever.split('.')[0], body)
        print fullBody
        Msg = 'Subject: %s\nFrom: %s\nTO: %s\n\n%s' %(subject,sender,reciever,fullBody)
        try:
            remoteServer = smtplib.SMTP(server)
            remoteServer.sendmail(sender,[email],Msg)
            remoteServer.quit()
        except SMTPError:
            print "Mail not sent."

day = time.localtime().tm_mday
turn = day%14 + 1
print day,turn

sendMain(toList[0],turn)
