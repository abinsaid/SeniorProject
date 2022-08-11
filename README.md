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


### - Database:
- ### Machine Learning Model
 
After the model finish from the analyzing the images, the events info's that has been extracted from the images will be sent into a database after establishing a connection with it by sending a POST REQUEST to it. to do so, we used MongoDB using the following python code: 
```
def insertEvent(jd):
    jsonObject = json.loads(jd)
    # return "test"
    cluster = pymongo.MongoClient("mongodb+srv://Byanati:AAA123321@cluster0.kioeq.mongodb.net/ProjectDB?retryWrites=true&w=majority", connect=False)
    db = cluster["ProjectDB"]
    collection = db["events"]
    post = {

        "Topic": jsonObject["topic"],
        "Instructor":jsonObject["instructor"],
        "Day": jsonObject["day"],
        "Date": jsonObject["date"],
        "Starting": jsonObject["startingTime"],
        "Ending": jsonObject["endingTime"],
        "Link": jsonObject["link"],
        "Technology": jsonObject["intrestTechnology"],
        "SoftSkills":jsonObject["intrestSoftSkills"],
        "Managment":jsonObject["interestManagment"],
        "ImageUrl":jsonObject["image_url"]

    }
    collection.insert_one(post)
    print("event has been added to the database")
```


- ### Events Table
In the MongoDB we have a schema for the project called ProjectDB, and it include two tables: events and users. The events table will store records of each events info's comes from the Machine learning model by receiving a post request from it with the events info. Later, the mobile application will fetch these records into a page in the application for viewing it.

((eventsTable.jpg))

- ### Users Table
The following snapshot reference for the users table, which is responsible for saving any users record store after registering into our application, and as you can see each password for each user is hashed for more security.

((usersTable.jpg))

### - Router (React native BackEnd)
This code establishes a listening server using Node.Js and express Js:
```
const express = require("express");
const app = express();
app.listen(3000, () => console.log("listening..."));
```


- ### Login
This function is used to handle any fetch POST request comes from the Sign in page in the front end after the user try to sign in, then put the input password into hashing method to comare it with the hashed password stored in the database for a better authentication process.
```
const usrTable= mongoose.model("users");
app.post("/Login", async (req, res, next) => {
var { email, inputPass } = req.body;

// this function look for some particular user with the specific email
  const user = await usrTable.findOne({ email });
  ...
  
// generating salt to use it in the hashing function for stronger encryption
    bcrypt.genSalt(10, (err, salt) => {
  ...
  
// hash the user password
      bcrypt.hash(inputPass, salt, (err, hash) => {
  ...
  
// replace the normal password with the hashed one
        inputPass = hash;
  ...
  
  bcrypt.compare(inputPass, user.pass, (err, isMatch) => {
  ...
```


- ### getEvent
This function is used to handle any fetch GET request comes from the Database after the user visit the events page using the application.
```
const eventTable = mongoose.model("events");
app.get("/getEvent", async (req, res) => {
const event = await eventTable.find();
res.send(event)
});
```


- ### signUp
This function is used to handle any fetch POST request comes from the Signup page after the user fill in his credentials and submit it to the application. 
```
app.post("/signup", async (req, res) => {
console.log("\n user post request Accepted!\n");
  // the following varibales need to be the same names from the postman request
  const { studName,email,pass} = req.body;
  console.log(req.body.studName);
    const user = new usrTable({studName,email,pass});
    await user.save();  
```

- ### addEvent
This function is used to handle any fetch POST request comes from the Database after the user visit the events page using the application.
```
app.post("/addEvent", async (req, res) => {
```

## Resulting Application

- ### Home page
The following page represents the first page that the user interacts with when they enter the application, the page who's a button that transport the user into the Login page
((Homepage.jpg))


- ### Login page
This page responsible for taking user email and password as input so the user can authenticate and log in into the application. in case the user doesn’t have an account, he need to press on sign up button to register for an account.
((LoginPage.jpg))


- ### Events page
While loading the event page, a function called useEffect will immediately make a GET request that contain the whole events table and list it in the Events page, it shows all the events that has been analyzed by the machine learning model and stored into the database in the events table. 
((EventsPage.jpg))


- ### Calendar page
After viewing the events page, the student can use the calendar page as reminders by adding various tasks in desired time and date, the user also can modify or delete any task they choose.
((CalenderPage.jpg))
