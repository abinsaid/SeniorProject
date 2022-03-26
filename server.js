
require('dotenv').config()
const express = require('express')
const mongoose = require('mongoose')
// const bodyParser = require('body-parser')

const app = express()

mongoose.connect(process.env.DATABASE_URL);
const db = mongoose.connection

db.on('error',(error) => console.error(error))
db.once('open', () => console.log('connected to database'))

// let the server accept Json
app.use(express.json())

const TestRouter = require('./routes/usrRoutes')
app.use('/usrRoutes', TestRouter)



app.listen(3000,() => console.log('server started!!'))