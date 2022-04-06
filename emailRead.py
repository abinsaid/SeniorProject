import imaplib
import email
from email.header import decode_header
import os
import re
# to get image from the web
import requests
import shutil # to save it locally
import glob
# import traceback



# account credentials
# passwdFile ="Ar@667576"
test = '123'
user = "abinsaid0002@stu.kau.edu.sa"
passwd = "Ar@667576"
textPattern = ""
# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate
imap.login(user, passwd)

#  selects a mailbox
status, messages = imap.select("StudentMailBox")
print("status is ,",status)
print("msg is ,",messages)

# number of top emails to fetch 
N = 10
# total number of emails
 
messages = int(messages[0])
print('\n')
print('The number of current mails: ',messages)
# print(imap.list)
print('\n')
counter = 1
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
                  # =========================================================================

                 ## Set up the image URL and filename
               
            image_url = re.compile('<img src="(.*?)"')
            image_url = image_url.findall(body)[0]
            print("The extracted url of the Image: ",image_url)
                # print(body)

            picFilename = image_url.split("/")[-1]
            print("file is ",picFilename)
            picFilename=str(counter)+".jpg"
            counter=counter+1
              
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
            for file in files:
                # extract file name form file path
                 file_name = os.path.basename(file)
                 shutil.move(file, dst_folder + file_name)
                 print('Moved:', file)

              
    print("="*100)
    print("="*100)
    print('\n')
# close the connection and logout
imap.close()
imap.logout()
