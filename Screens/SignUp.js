
import React, { input,Label, useState, useEffect } from "react";
import {Text,Alert,StyleSheet,View,Button,Element,TouchableOpacity,TextInput,Input,ImageBackground,Dimensions,Form,SafeAreaView} from "react-native";
import CheckBox from 'expo-checkbox';

const windowWidth = Dimensions.get("window").width;
const windowHeight = Dimensions.get("window").height;


export default function SignUp() {


  // declare the user variables and their intrests
  const [studName, setName] = useState('');
  const [email, setEmail] = useState('');
     const [pass, setPassword] = useState('');

     const [ITCheckBox, setITCheckBox] = useState(false)
     const [cyberCheckBox, setCyberCheckBox] = useState(false)
     const [AICheckBox, setAICheckBox] = useState(false)
     const [gameCheckBox, setGameCheckBox] = useState(false)
     const [webCheckBox, setWebCheckBox] = useState(false)

     const [otherCheckBox, setOtherCheckBox] = useState(false)

  const student = { studName, email, pass,ITCheckBox,cyberCheckBox,AICheckBox,gameCheckBox,webCheckBox,otherCheckBox};
   
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
      <View style={styles.PageStyle}>
      <Text style ={styles.h1}>Register your info</Text>
       {/* for new lines: */}
       <Text></Text>

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
        
         <Text></Text>
  <View style={styles.checkboxContainer}>
  
  <CheckBox style={styles.checkbox}
    disabled={false}
    placeholder="IT"
    value={ITCheckBox}
    onValueChange={(newValue) => setITCheckBox(newValue)}
  />
  <Text style={styles.label}> IT related</Text>
      </View>
      {/* ////////////////////////// */}

      <View style={styles.checkboxContainer}>
  
  <CheckBox style={styles.checkbox}
    disabled={false}
    placeholder="cyber"
    value={cyberCheckBox}
    onValueChange={(newValue) => setCyberCheckBox(newValue)}
  />
  <Text style={styles.label}> Cyber Security </Text>
      </View>
      {/* ////////////////////////// */}

      <View style={styles.checkboxContainer}>
  
  <CheckBox style={styles.checkbox}
    disabled={false}
    placeholder="AI"
    value={AICheckBox}
    onValueChange={(newValue) => setAICheckBox(newValue)}
  />
  <Text style={styles.label}> AI related</Text>
      </View>
      {/* ////////////////////////// */}

      <View style={styles.checkboxContainer}>
  
  <CheckBox style={styles.checkbox}
    disabled={false}
    placeholder="game"
    value={gameCheckBox}
    onValueChange={(newValue) => setGameCheckBox(newValue)}
  />
  <Text style={styles.label}> Game development </Text>
      </View>
      {/* ////////////////////////// */}<View style={styles.checkboxContainer}>
  
  <CheckBox style={styles.checkbox}
    disabled={false}
    placeholder="Web"
    value={webCheckBox}
    onValueChange={(newValue) => setWebCheckBox(newValue)}
  />
  <Text style={styles.label}> Web development </Text>
      </View>
      {/* ////////////////////////// */}
      <View style={styles.checkboxContainer}>
  
  <CheckBox style={styles.checkbox}
    disabled={false}
    placeholder="other"
    value={otherCheckBox}
    onValueChange={(newValue) => setOtherCheckBox(newValue)}
  />
 
  <Text style={styles.label}> other </Text>
      </View>

      {/* for new lines: */}
      <Text>{"\n"}{"\n"}{"\n"}</Text>
     

      
      <TouchableOpacity 
        onPress={onClickListener} 
        >
          <Text style = {styles.btnConfirm}>Confirm</Text>
       
        </TouchableOpacity>
      </View>

    </ImageBackground>

    
  );
}

const styles = StyleSheet.create({
  PageStyle: {
    flex: 0.85,
    width: windowWidth ,
    // justifyContent: "space-between",
    backgroundColor: "#e8e8e4",
  },
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  checkboxContainer: {
    flexDirection: "row",
    alignItems:"",
    // marginBottom: 20,
  },
  checkbox: {
    alignSelf: "center",
    margin: "center"
  },
  label: {
  //  margin: "center"
  },

  InputStyle: {
    backgroundColor: "white",
    fontSize: 22,
    borderRadius: 6,
    borderColor: "black",
    borderWidth: 1,
    width: windowWidth - 100,
    height: windowHeight * 0.05,
    marginRight:40,
    alignSelf:'center',
    paddingLeft:5,
    borderWidth: 1,

  },
  backgroundContainer: {
    flex: 1,
    width: null,
    height: null,
    alignItems: "center",
    justifyContent: "center",
    
  },
  checkbox: {
    alignSelf: "center",
   
  },
  checkboxContainer: {
    flexDirection: "row",
    // alignSelf: "center",
    marginLeft:70,
    width: windowWidth -100,
    // borderWidth: 1,
    
    // marginBottom: 20,
  },
  label: {
    fontSize: 22,
    marginBottom:5,
    // paddingTop:2
  },
   TextFields: {

  }, 
  btnConfirm: {
    fontWeight:'bold',
        fontSize :22,
        color:'#003049',
        backgroundColor: "#48cae4",
        width: windowWidth - 300,
        textAlign:'center',
        borderRadius:170 ,
        marginLeft:20,
        

  },
  h1:{
  fontSize: 30,
  fontWeight:'bold',
  alignSelf:'center'

  }
});
