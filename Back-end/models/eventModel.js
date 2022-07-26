const mongoose = require("mongoose");


const eventSchema = new mongoose.Schema({
    topic:{ type: String , required: true},
    instructor: { type: String},
    day: { type: String},
    date: { type: String},
    starting: { type: String},
    ending: { type: String },
    link: { type: String },
    technology: { type: String },
    softSkills: { type: String },
    management: { type: String },
    imageUrl: { type: String },
  
  })

  module.exports = mongoose.model("events", eventSchema);