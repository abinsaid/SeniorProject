const express = require('express')
const router = express.Router()

const usr = require('../models/usr')



// //creating one 
router.post('/', async (req,res) => {
 const usr1 = new usr({
    usrName: req.body.usrName, 
    email: req.body.email,
    password: req.body.password
 } )
 try{
     const newUsr = await usr1.save()
     res.status(201).json(newUsr)
 } catch(err){
     res.status(400).json({message: err.message})
 }
 

})


// getting all 
router.get('/',async(req,res) => {
    // res.send('this is working FINE!')

    try{
        const users = await usr.find()
        res.json(users)
        } catch(err){
         res.status(500).json({message: err.message})
        }

})

module.exports = router





// // getting one
// router.get('/:id',(req,res) => {
//   res.send(req.params.id)
// })
