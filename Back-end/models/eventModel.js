const mongoose = require("mongoose");


const eventSchema = new mongoose.Schema({
    topic:{ type: String , required: true},
    instructor: { type: String},
    startDate: { type: String},
    endDate: { type: String },
  
  })

  module.exports = mongoose.model("events", eventSchema);