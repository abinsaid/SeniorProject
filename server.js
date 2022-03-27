
require('dotenv').config()
const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const TestRouter = require('./routes/usrRoutes')

const app = express()

app.use(bodyParser.json())
app.use('/usrRoutes', TestRouter)


mongoose.connect(process.env.DATABASE_URL,{ useNewUrlParser: true});
const db = mongoose.connection

db.on('error',(error) => console.error(error))
db.once('open', () => console.log('connected to database'))

// let the server accept Json



app.listen(3000,() => console.log('server started!!'))