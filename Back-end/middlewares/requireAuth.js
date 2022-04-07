// this class focus in the sign in 


/*Middleware functions are functions that have access to the request object (req),
the response object (res), and the next function in the application’s request-response cycle.
The next function is a function in the Express router which, when invoked, executes the middleware succeeding the current middleware.
*/
const jwt = require("jsonwebtoken");
const mongoose = require("mongoose");
const User = mongoose.model("users");

module.exports = (req, res, next) => {
const {authorization} = req.headers;
console.log('\n\nentered the authorization')
// authorization === 'Bearer lalfalfaslfsalf
console.log(`authorization:  ${authorization}`) 
// if(!authorization){
    
//     return res.status(401).send({error: ' !!ما عندك صلاحية دخول ي كبتن اطلع برا موقعنا'})
// }

// if the token is valid:

// we get rid of 'Bearer' so we can have a clear token
const token =  authorization.replace('Bearer ','')
console.log('after token replaced')
jwt.verify(token,'MY_SECRET_KEY', async(err,payload)=>{
    console.log('after entering jwt \n')
// err : if something goes wrong get back and err
// payload: whatever information is stuck with our web jason token

if(err){
   
return res.status(401).send({error: 'You must be logged in.' }
)} 
  // userId is comming from payload , use it to look up for the user Id 
  
const {userId} = payload;


const user = await User.findById(userId)

req.user = user;
next()
});

}