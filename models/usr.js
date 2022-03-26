const mongoose = require('mongoose');

const usrSchema = new mongoose.Schema({
  usrName: {type: String},
  email: {type: String},
  password: {type: String}
});


module.exports = mongoose.model('usr', usrSchema);
