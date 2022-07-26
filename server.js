const usrModel = require("./Back-end/models/usrModel");
const eventModel = require("./Back-end/models/eventModel");
require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");

//Cross-Origin Resource Sharing
const cors = require("cors");
const bcrypt = require("bcrypt");
const usrTable= mongoose.model("users");
const eventTable = mongoose.model("events");
// const router = express.Router()
// parse the coming Json info associtated with
const bodyParser = require("body-parser");

const app = express();

app.use(cors());
app.use(bodyParser.json());

mongoose.connect("mongodb+srv://Byanati:AAA123321@cluster0.kioeq.mongodb.net/ProjectDB?retryWrites=true&w=majority", { useNewUrlParser: true });
const db = mongoose.connection;

db.on("error", (error) => console.error("error request!"));
db.once("open", () => console.log("connected to database"));

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

app.post("/Login", async (req, res, next) => {
  console.log("\n user sign in post request Accepted!");
  
  var { email, inputPass } = req.body;
  console.log(email , inputPass)

  if (!email || !inputPass) {

    return res.status(401).send({ error: " Most provide email and password!" });
  }
  // this function look for some particular user with the specific email
  const user = await usrTable.findOne({ email });
  console.log(user)
  //if there not user found:
  //HTTP responses:
  // 400 == wrong email
  // 401 == bad request
  // 402 == comparing the password
  // 403 == user not found
  // 406 == wrong password
  // 500 == بقعة
  if (!user) {
    return res.status(403).send({ error: "user not found"});
  }
  try {
    bcrypt.genSalt(10, (err, salt) => {

      if (err) {
        console.log('error inside the bcrypt')
        return;
      }
      // hash the user password
      bcrypt.hash(inputPass, salt, (err, hash) => {
        console.log('entering the hash function')
        if (err) {
          return;
        }
  
        // replace the normal password with the hashed one
        inputPass = hash;
        console.log('this is the input pass after hashing:', inputPass)
        ;
      });
    });
         
      bcrypt.compare(inputPass, user.pass, (err, isMatch) => {
        if (err) {
          return res.status(402).send({ error: "comparing the password"});
        }
        
        if (!isMatch) {
          console.log('error, passwords not matched')
          return res.status(406).send({ error: "The password is incorrect"});
        }
        console.log('FUNCTION IS CORRECT!!')
        return res.status(200).send({result: 'success' });
        
      })
    
    // const token = jwt.sign({ userId: user._id }, "MY_SECRET_KEY");
    // res.send({ token });
  } catch (err) {
    return res.status(500).send({ error: "Error occured"});
  }
});

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

app.get("/getEvent", async (req, res) => {

console.log('we getting the events!!!');
//   const {} = req.body;
const event = await eventTable.find();
// const AnotherEvent = await eventModel.findOne({ _id:'624a8204e92c14dbcd13f221'})
console.log(event)
// console.log(event)
res.send(event)
//   eventModel;
});
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
app.post("/signup", async (req, res) => {
  console.log("==============================================");
  console.log("\n user post request Accepted!\n");

  // the following varibales neeed to be the same names from the postman request
  const {
    studName,
    email,
    pass
    
  } = req.body;
  // console.log(req.body);
  console.log(req.body.studName);
  try {
    const user = new usrTable({
      studName,
      email,
      pass
      
    });
  
    await user.save();
    console.log("\n", user.pass);

    console.log("new student info has been added");
    console.log("===============================");
    // console.log(req.body)

    // if there is an error:
  } catch (err) {
    // console.log(res.status(400).json())
    console.log('email already exists!');
    console.log("===============================");
  }
});

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
app.post("/addEvent", async (req, res) => {
  console.log("==============================================");
  console.log("\n event post request Accepted!\n");
  const { topic, instructor, startDate, endDate } = req.body;

  try {
    const event = new eventTable({ topic, instructor, startDate, endDate });
    await event.save();
    res.send( event );
  } catch (err) {
    res.status(400).json({ message: err.message });
    console.log({ message: err.message });
    // console.log({ message: err.message });
  }
});

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

app.listen(3000, () => console.log("listening..."));