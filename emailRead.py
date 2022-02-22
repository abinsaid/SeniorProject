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
passwdFile = open("C:\\Users\\3boody\\Documents\\GitHub\\SmartSchedulingSystem\\passwd.txt", "r")

user = "abinsaid0002@stu.kau.edu.sa"
passwd = passwdFile .read()

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate
imap.login(user, passwd)


def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)
       

#  selects a mailbox
status, messages = imap.select("StudentMailBox")
# number of top emails to fetch 
N = 3
# total number of emails
 
messages = int(messages[0])
print('\n')
print('The number of current mails: ',messages)
# print(imap.list)
print('\n')

for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])

            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to string
                subject = subject.decode(encoding)

            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:", subject)
            print("From:", From)
           
            # print(msg.walk())

            # if the email message is multipart(responsible for HTTP request that HTTP clients construct to send files and data over to a HTTP Server.)
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                         print("null")
                    elif "attachment" in content_disposition:
                        # download attachment
                        filename = part.get_payload()
                            
                        if filename:
                            folder_name = clean(subject)
                            if not os.path.isdir(folder_name):
                                # make a folder for this email (named after the subject)
                                os.mkdir(folder_name)
                            filepath = os.path.join(folder_name, filename)
                            # download attachment and save it
                            open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                  # =========================================================================

                 ## Set up the image URL and filename
               
                image_url = re.compile('<img src="(.*?)"')
                image_url = image_url.findall(body)[0]
                print("The extracted url of the Image: ",image_url)

                picFilename = image_url.split("/")[-1]
              
                 # Open the url image, set stream to True, this will return the stream content.
                req = requests.get(image_url, stream = True)

                 # Check if the image was retrieved successfully
                if req.status_code == 200:
                       # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                     req.raw.decode_content = True
    
                       # Open a local file with wb ( write binary ) permission.
                     with open(picFilename,'wb') as f:
                        shutil.copyfileobj(req.raw, f)
                      
                    
                     print('Image sucessfully Downloaded: ',picFilename)
                   
                else:
                     print('Image Couldn\'t be retreived')

            
                # ================================printing================================
               
                # print("The payload:")
               
                # print(body)
                # tempPic = "<img src=http://kau.edu.sa/Images/211/%D8%A8%D8%B7%D8%A7%D9%82%D8%A9%20%D8%AE%D8%B1%D9%8A%D8%AC/ic3.jpg"
                # pic= re.findall("\A<img", tempPic)
                # print(pic)
                # print('\n')
                
                # ========================================================================

                if content_type == "text/plain":
                    # print only text email parts
                    print(body)
            if content_type == "text/html":
                # if it's HTML, create a new HTML file and open it in browser
                folder_name = clean(subject)
                if not os.path.isdir(folder_name):

                    # make a folder for this email (named after the subject)
                    os.mkdir(folder_name)
                filename = "index.html"
                filepath = os.path.join(folder_name, filename)
                # write the file
                open(filepath, "w").write(body)

                # mov the files to their correct paths
                src_folder = r"C:\Users\3boody\Documents\GitHub"
                dst_folder = r"C:\Users\3boody\Documents\GitHub\SmartSchedulingSystem\mailsFolder\\"
                # Search files with .txt extension in source directory
                pattern = "\*.jpg"
                files = glob.glob(src_folder + pattern)

                # move the files with txt extension
                for file in files:
                # extract file name form file path
                 file_name = os.path.basename(file)
                 shutil.move(file, dst_folder + file_name)
                 print('Moved:', file)

              
                # open in the default browser
                # webbrowser.open(filepath)
            ## Importing Necessary Modules



    print("="*100)
    print("="*100)
    print('\n')
# close the connection and logout
imap.close()
imap.logout()
