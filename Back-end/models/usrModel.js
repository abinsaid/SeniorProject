const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
// const { hash } = require("bcrypt");
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

  console.log('inside the userSchema.pre')
  const user = this;
  //if the user did not modify their password by the hashing algorithm, dont salt anything
  if (!user.isModified("pass")) {
    console.log('entering the IsModified function')
    return next();
  }
  // salt: random string of characters
  bcrypt.genSalt(10, (err, salt) => {
    if (err) {
      return next(err);
    }
    // hash the user password
    bcrypt.hash(user.pass, salt, (err, hash) => {
      console.log('entering the hash function')
      if (err) {
        return next(err);
      }

      // replace the normal password with the hashed one
      user.pass = hash;
      next();
    });
  });
});                  

/* this function is a comparsion between the existing password and the 
 password used in the log in */ 
userSchema.methods.comparePasswordS = function (candidatePassword) {
  const user = this;
  return new Promise((resolve, reject) => {

    //pass for test // hashed and // salted pass
    bcrypt.compare(candidatePassword, user.pass, (err, isMatch) => {
      if (err) {
        return reject(err);
      }

      if (!isMatch) {
        return reject(false);
      }

      resolve(true);
    });
  });
};

module.exports = mongoose.model("users", userSchema);