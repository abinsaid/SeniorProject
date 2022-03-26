
import React, { useState, useEffect } from "react";
import {Text,Alert,StyleSheet,View,Button,TouchableOpacity,TextInput,Input,ImageBackground,Dimensions,Form,SafeAreaView} from "react-native";
import Checkbox from "react-native-checkbox-animated";
// import CheckBox from '@react-native-community/checkbox';

// import CheckBox from 'react-native-check-box'
// import { MongoUsr } from "../DataBase/users";


// import e from "express";

const windowWidth = Dimensions.get("window").width;
const windowHeight = Dimensions.get("window").height;

// const [toggleCheckBox, setToggleCheckBox] = useState(false)

  // }
  // onUsrAdded = (usr) => {};
  
export default function SignUp() {

  // const [checked, setChecked] = useState(false);

  const [studName, setName] = useState('');
  const [email, setEmail] = useState('');
     const [pass, setPassword] = useState('');

  // const [toggleCheckBox, setToggleCheckBox] = useState(false)

  const student = { studName, email, pass };
   
const onClickListener = () => {
  if(studName){
    if(email){
      if(pass){

        console.log({student})

      } else{console.log("pls enter password")}
      } else{console.log("pls enter email")}
      } else{console.log("pls enter student name")}  
    
      
}
  // const handleSubmit = () => {
  
  //   // setIsPending(true);
  // try{
  //   fetch("https://localhost:3000/usrRoutes", {
  //     method: "POST",
  //     headers: { "Content-Type": "application/json" },
  //     body: JSON.stringify(student),
  //   }).then(() => {
  //     console.log("new student info has been added");
  //   });
  // } catch(err){
  //   console.log('Connection is wrong!')
    
  // }
  // };

 
//  const initialValues = {username: "", email:"", password:""};
//  const [formValues, setFormValues] = useState(initialValues);

//  const handleChange = (e) =>{
//   e.preventDefault();
//    const{name, value} = e.target;
//    setFormValues({...formValues,[name]: value});
//  }

  return (
    
    <ImageBackground
      source={require("../images/background.png")}
      style={styles.backgroundContainer}
    >
      <View style={styles.ViewStyle}>
      
      {/* <Form onSubmit{}> */}
        <TextInput
          placeholder="name"
       
        onChangeText={(value) => setName(value)}
        value={studName}
          style={styles.InputStyle}
        ></TextInput>

        <TextInput
          placeholder="email"
          onChangeText={(value) => setEmail(value)}
          value={email}
          style={styles.InputStyle}
        ></TextInput>

        <TextInput
          placeholder="password"
           secureTextEntry
          // everytime text changes will set the password
          onChangeText={(value) => setPassword(value)}
          value = {pass}

          style={styles.InputStyle}
        ></TextInput>
        
         

        <TouchableOpacity 
        onPress={onClickListener} 
        >
          <Text>Confirm</Text>
         {/* <Text>{ console.log("info's are stored!: "+ {student})}</Text> */}
        </TouchableOpacity>

        {/* </Form> */}
        {/* <View>
        <CheckBox
        label="your label here"
        onValueChange={val => setChecked(val)}
        checked={checked}
      />
  </View> */}
      </View>
      
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  ViewStyle: {
    flex: 0.55,
    justifyContent: "space-between",
    backgroundColor: "#e8e8e4",
  },
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  checkboxContainer: {
    flexDirection: "row",
    marginBottom: 20,
  },
  checkbox: {
    alignSelf: "center",
  },
  label: {
    // margin: 5,
  },

  InputStyle: {
    backgroundColor: "white",
    fontSize: 22,
    borderRadius: 6,
    borderColor: "black",
    borderWidth: 1,
    width: windowWidth * 1,
    height: windowHeight * 0.05,
  },
  backgroundContainer: {
    flex: 1,
    width: null,
    height: null,
    alignItems: "center",
    justifyContent: "center",
  },
});
