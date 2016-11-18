"""This script send emails to my wingmates according to cleaing schedual."""
#!/usr/bin/python
import smtplib
import time

# This is the mailing list consist of my wingmates.
myList = [
    ['shivang.nagaria@students.iiit.ac.in'],
    ['shivang.nagaria@students.iiit.ac.in',
        'prajjwal.khariya@students.iiit.ac.in'],
    ['sanket.markan@students.iiit.ac.in',
        'hemant.kasat@research.iiit.ac.in'],
    ['sanket.shah@research.iiit.ac.in',
        'raj.manvar@students.iiit.ac.in'],
    ['manan.bhandari@research.iiit.ac.in',
        'toshad.salwekar@students.iiit.ac.in'],
    ['aditya.motwani@students.iiit.ac.in',
        'anirudh.dahiya@research.iiit.ac.in'],
    ['neeraj.battan@research.iiit.ac.in',
        'shreyash.shriyam@students.iiit.ac.in'],
    ['aagam.shah@research.iiit.ac.in',
        'deepanshu.jain@students.iiit.ac.in']
]

def send_mail(mailing_list, whoseTurn):
    "This function send emails according to cleaniess schedual."
    print whoseTurn
    sender = "Safai Samiti<safaiSamiti@2ndFloorE.iiit.ac.in>"
    subject = "Reminder: It's your turn to clean wing"
    subbody = "Today is your turn to clean our wing, kindly do it.\n"
    subbody += "Thanks for your cooperation."
    for email in mailing_list:
        reciever = email.split('@')[0]
        server = email.split('@')[1]
        body = 'Hi,%s\n%s' % (reciever.split('.')[0], subbody)
        print body
        message = 'Subject: %s\nFrom: %s\nTO: %s\n\n%s' %(
                subject, sender, reciever, body)
        try:
            host = smtplib.SMTP(server)
            host.sendmail(sender, [email], message)
            host.quit()
        except:
            print "Mail not sent."

today_day = time.localtime().tm_mday
turn = today_day%14 + 1
print today_day, turn

send_mail(myList[0], turn)
