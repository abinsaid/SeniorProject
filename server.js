const usrModel = require("./Back-end/models/usrModel");
require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const requireAuth = require('./Back-end/middlewares/requireAuth')
const cors = require("cors");
const jwt = require('jsonwebtoken')
const usr = require('./Back-end/models/usrModel')

// parse the coming Json info associtated with
const bodyParser = require("body-parser");
const usrRouter = require("./Back-end/routes/usrRoutes");

const app = express();

app.use(cors());
// app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use("/usrRoutes", usrRouter);


mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true });
const db = mongoose.connection;

db.on("error", (error) => console.error(error));
db.once("open", () => console.log("connected to database"));

app.get('/',requireAuth,async(req,res) => {
    console.log('correct log in ')
    // res.send(`Your email: ${req.user.email}`)
   
    // res.send('this is working FINE!')

    try{
        const users = await usrModel.find()
        console.log(users)
        res.json(users)
        } catch(err){
         res.status(500).json({message: err.message})
        }

})

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
// in anytime someone called sign in routes:
app.get('/signin',async(req,res)=>{
    // console.log('start of signin')
    const {email,pass} = req.body

    if(!email || !pass){
        return res.status(422).send({error: ' Most provide email and password!'})
    }
     // this function look for some particular user with the specific email
   const user = await UserModel.findOne({email})

   //if there not user found:
   if(!user){
       return res.status(422).send({error:'Email not found'})
   }
   try{
   await user.comparePassword(password)
   const token = jwt.sign({userId:user._id},'MY_SECRET_KEY')
   res.send({token})
} catch(err){
    return res.status(422).send({error:'Invalid password or email'})
}
})

//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

app.post('/signup', async (req,res) => {
    console.log('==============================================')
    console.log('\n post request Accepted!\n')
   
    // the following varibales neeed to be the same names from the postman request 
    const { studName, email,pass,intrest1,intrest2,intrest3,intrest4,intrest5,intrest6} = req.body;
    console.log(req.body)
    console.log(req.body.studName)
    try{
   const user = new usr({studName,email,pass,intrest1,intrest2,intrest3,intrest4,intrest5,intrest6});
   console.log('after the variables creations')
    
   await user.save()
   console.log('\n',user.pass)
    
    const token = jwt.sign({userId: user._id},'MY_SECRET_KEY');
    console.log('userId: ',user._id,'\n')
    console.log('token is correct')
    // console.log(token)
        //if everything is OK:
    res.send({token})
   console.log("new student info has been added");
   console.log('===============================')
    // console.log(req.body)

     // if there is an error:
 } catch(err){
    console.log('error in token')
     res.status(400).json({message: err.message})
     console.log({message: err.message})
     console.log('===============================')
 }
 
})

app.listen(3001, () => console.log("listening..."));


