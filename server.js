const getUsrModel = require("./Back-end/models/usrModel");
const getEventModel = require("./Back-end/models/eventModel");
require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const requireAuth = require("./Back-end/middlewares/requireAuth");
const cors = require("cors");
const jwt = require("jsonwebtoken");
const UserModel = mongoose.model("users");
const eventTable = mongoose.model("events");
// const router = express.Router()
// parse the coming Json info associtated with
const bodyParser = require("body-parser");

const router = express.Router()
// const usrRouter = require("./Back-end/routes/usrRoutes");
// const eventRouter = require("./Back-end/routes/usrRoutes");
// const idCounter =0;
const app = express();

app.use(cors());
// app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
// app.use(usrRouter);
// app.use( eventRouter);

mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true });
const db = mongoose.connection;

db.on("error", (error) => console.error(error));
db.once("open", () => console.log("connected to database"));

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

app.get("/", requireAuth, async (req, res) => {
  console.log("correct log in ");
  // res.send(`Your email: ${req.user.email}`)

  // res.send('this is working FINE!')

  try {
    const users = await getUsrModel.find();
    console.log(users);
    res.json(users);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
// in anytime someone called sign in routes:
app.get("/signin", async (req, res) => {
  // console.log('start of signin')
  const { email, pass } = req.body;

  if (!email || !pass) {
    return res.status(422).send({ error: " Most provide email and password!" });
  }
  // this function look for some particular user with the specific email
  const user = await UserModel.findOne({ email });

  //if there not user found:
  if (!user) {
    return res.status(422).send({ error: "Email not found"});
  }
  try {
    await user.comparePassword(password);
    const token = jwt.sign({ userId: user._id }, "MY_SECRET_KEY");
    res.send({ token });
  } catch (err) {
    return res.status(422).send({ error: "Invalid password or email" });
  }
});

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

app.get("/getEvent", async (req, res) => {

console.log('we getting the events!!!');
//   const {} = req.body;
const event = await getEventModel.find();
// const AnotherEvent = await getEventModel.findOne({ _id:'624a8204e92c14dbcd13f221'})
console.log(event)
// console.log(event)
res.send(event)
//   getEventModel;
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
    pass,
    intrest1,
    intrest2,
    intrest3,
    intrest4,
    intrest5,
    intrest6,
  } = req.body;
  console.log(req.body);
  console.log(req.body.studName);
  try {
    const user = new getUsrModel({
      studName,
      email,
      pass,
      intrest1,
      intrest2,
      intrest3,
      intrest4,
      intrest5,
      intrest6,
    });
    console.log("after the variables creations");

    await user.save();
    console.log("\n", user.pass);

    const token = jwt.sign({ userId: user._id }, "MY_SECRET_KEY");
    console.log("userId: ", user._id, "\n");
    console.log("token is correct");
    // console.log(token)
    //if everything is OK:
    res.send({ token });
    console.log("new student info has been added");
    console.log("===============================");
    // console.log(req.body)

    // if there is an error:
  } catch (err) {
    console.log("error in token");
    res.status(400).json({ message: err.message });
    console.log({ message: err.message });
    console.log("===============================");
  }
});

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

// app.get('/getEvent', async (req,res)=>{
//     const {topic,instructor,startDate,endDate} = req.body
// })

app.post("/addEvent", async (req, res) => {
  console.log("==============================================");
  console.log("\n event post request Accepted!\n");
  const { topic, instructor, startDate, endDate } = req.body;

  try {
    const event = new eventTable({ topic, instructor, startDate, endDate });
    await event.save();
    res.send({ event });
  } catch (err) {
    res.status(400).json({ message: err.message });
    console.log({ message: err.message });
  }
});

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

app.listen(3000, () => console.log("listening..."));

module.exports = router
