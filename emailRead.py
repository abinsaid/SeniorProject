import imaplib
import email
from email.header import decode_header
import os
import re
# to get image from the web
import requests
import shutil # to save it locally
import glob
import getpass
import sys

pattern_uid = re.compile(r'\d+ \(UID (?P<uid>\d+)\)')
from_folder = "StudentMailBox"
to_folder = "Moved"

# import traceback

def connectEmail(email):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    password = "Ar@667576"
    imap.login(email, password) # authenticate
    return imap

def logout(imap):
    imap.logout()

def parse_uid(data):
    match = pattern_uid.match(data)
    return match.group('uid')




def moveEmail(imap):
  imap.select(mailbox = from_folder, readonly = False)
  resp, items = imap.search(None, 'All')
  email_ids  = items[0].split()\
 #id=email_ids[i]
  #i=i+1
  print(email_ids)
  #print(email_ids[0])
  latest_email_id = email_ids[-1] # Assuming that you are moving the latest email.
  print(latest_email_id)
  resp, data = imap.fetch(latest_email_id, "(UID)")
  #msg_uid = parse_uid(data[0])
  msg_uid = parse_uid(data[0].decode("utf-8"))
  result = imap.uid('COPY', msg_uid, to_folder)
  #if result[0] == 'OK':
  mov, data = imap.uid('STORE', msg_uid , '+FLAGS', '(\Deleted)')
  imap.expunge()

 

def getEmailAttatchment():
 
# account credentials
# passwdFile ="Ar@667576"
 #test = '123'
 #user = "abinsaid0002@stu.kau.edu.sa"
 #email= "abinsaid0002@stu.kau.edu.sa"
 #passwd = "Ar@667576"
 #textPattern = ""
 # create an IMAP4 class with SSL 
 #imap = imaplib.IMAP4_SSL("imap.gmail.com")
 # authenticate
 #imap.login(user, passwd)

 userEmail= "abinsaid0002@stu.kau.edu.sa"
 imap=connectEmail(userEmail)

 #  selects a mailbox
 status, messages = imap.select("StudentMailBox")
 print("status is ,",status)
 print("msg is ,",messages)

 # number of top emails to fetch 
 
 # total number of emails
 
 messages = int(messages[0])
 numMsg =messages
 N = numMsg
 print('\n')
 print('The number of current mails: ',numMsg)
 # print(imap.list)
 print('\n')
 counter = 16
 for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
        

                # get the email body
            body = msg.get_payload(decode=True).decode()
            print(body)
            #print(body)
                  # =========================================================================

                 ## Set up the image URL and filename
               
            image_url = re.compile('<img src="(.*?)"')
            image_url = image_url.findall(body)[0]
            print("The extracted url of the Image: ",image_url)
                # print(body)

            picFilename = image_url.split("/")[-1]
            print("file is ",picFilename)
            picFilename=str(counter)+".jpg"
            
              
                 # Open the url image, set stream to True, this will return the stream content.
            req = requests.get(image_url, stream = True)

                 # Check if the image was retrieved successfully
            print(req.status_code)
            #print(os.getcwd())
            if req.status_code == 200: 
                       # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
             req.raw.decode_content = True

                       # Open a local file with wb ( write binary ) permission.
             with open(picFilename,'wb') as f:
              shutil.copyfileobj(req.raw, f)
           
             print('Image sucessfully Downloaded: ',picFilename)                

                # mov the files to their correct paths
            src_folder = r"C:\Users\Ammar\Documents\GitHub\SeniorProject"
            dst_folder = r"C:\Users\Ammar\Documents\GitHub\SeniorProject\mailsFolder\\"
                # Search files with .txt extension in source directory
            pattern = "\*.jpg"
            files = glob.glob(src_folder + pattern)

                # move the files with txt extension
            i = 0
            for file in files:
                # extract file name form file path
                 file_name = os.path.basename(file)
                 shutil.move(file, dst_folder + file_name)
                 print('Moved:', file)
                 txtBody= open(r"C:\Users\Ammar\Documents\GitHub\SeniorProject\mailsFolder\\"+str(counter)+".txt","w+",encoding='utf-8')
                 txtBody.write(str(body))
                 counter=counter+1
                 moveEmail(imap)
                 



              
    print("="*100)
    print("="*100)
    print('\n')
    numImgaes = len(os.listdir(dst_folder))
    print()
    
# close the connection and logout
    #imap.close()
    #imap.logout()

getEmailAttatchment()
