# SeniorProject

## Problem Definition
With this huge number of emails that we receive everyday it has become a bit difficult and challenging to know the content of your email. Sometimes you might be interested to register for a seminar/event but due to the stack of emails you received you didn’t notice the event announcement.
And this is not it, giving that it’s a bit annoying that you are receiving emails about events that are out of your scope of interested, it is inconvenient that is a law student gets emails about an event regarding AI or any other event that requires a technical background, these problems cause a lot of students to ignore the events that are being hosted by their university.

## Introduction

The project is about a student Mobile application that showcase different kinds of college events by extracting the college events from the email into the mobile application in an event page and the application has a calander page so the student can organize the events that he/she is intrested 

## Implementation

The project has been constructed using three parts: Machine learning model using python, Mobile application using React Native, and Database using MongoDB.

### - Machine Learning Model:
- ### Emails extraction
is responsible for extracting each email that appears in the student's mailbox, at first, from connectEmail() function we establish a network connection to the mail box using imab protocol with imaplib library using the function login() which will need the student's credentials as parameters to enter the email. After the login and enter the mailbox.
```
def connectEmail(email):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    password = "********"
    imap.login(email, password) # authenticate
    return imap

def logout(imap):
   ...

def parse_uid(data):
   ...

def moveEmail(imap):
   ...
   
def getEmailAttatchment():
   ...
```

After login and entering the mailbox, we create a loop sized as many emails in the box as there so we can extract all of them and take the images from it to add them into our machine learning model.
```
messages = int(messages[0])
 numMsg =messages
 
 N = numMsg
 print('\n')
 print('The number of current mails: ',numMsg)
 if(numMsg==0):
     print("no new email")
     sys.exit()
 
 # print(imap.list)
 print('\n')
 counter = numMsg
 for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
```
- ### reading and analyzing the images:

