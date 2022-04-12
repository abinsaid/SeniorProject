const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const userSchema = new mongoose.Schema({
  // the following varibales neeed to be the same names from the postman request
  studName: { type: String },
  email: { type: String, unique: true },
  pass: { type: String },
  intrest1: { type: Boolean },
  intrest2: { type: Boolean },
  intrest3: { type: Boolean },
  intrest4: { type: Boolean },
  intrest5: { type: Boolean },
  intrest6: { type: Boolean },
});
// we are using this function instead of arrow function to use the 'this.'
// this function encrypt the signed up password
userSchema.pre('save', function (next) {

  const user = this;
  //if the user did not modify their password by the hashing algorithm, dont salt anything
  // هنا بيشيك هل قد دخل الباسوورد في عملية هاشنق قبل كذا او لا
  if (!user.isModified("pass")) {
    return next();
  }
  // salt: random string of characters
  bcrypt.genSalt(10, (err, salt) => {
    try{
    if (err) {
      return next(err);
    }
    // hash the user password
    bcrypt.hash(user.pass, salt, (err, hash) => {
      if (err) {
        return next(err);
      }

      // replace the normal password with the hashed one
      user.pass = hash;
      console.log('hasing is Ok:',user.pass)
      next();
    });
  } catch(err){
    console.log(' : error in hashing!')
  }

});
});                  

module.exports = mongoose.model("users", userSchema);
