
import React, { useState, useEffect } from 'react';
import { Text, StyleSheet, View,Linking, Button, TouchableOpacity, TextInput, ImageBackground, Dimensions, SafeAreaView } from 'react-native';
//   import {GoogleSignin,GoogleSigninButton,statusCodes} from 'react-native-google-signin';
const {width: WIDTH } = Dimensions.get('window')

const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;

//  onGetUsr = (email) =>{

//  }
export default function Login({ navigation }) {
     var res;
   const [email, setEmail] = useState('')
   const [inputPass, setPassword] = useState('')

///////////////////////////////////////////////////////////////////
  const handleValidation = () => {
//  console.log('inside handleValidation')
  //   if (!pass || !email.includes('@stu.kau.edu.sa') )  {
     
  //     console.log(" Most provide valid email and password!\n");
  //  }  else { 
     try{
    fetch("http://192.168.1.100:3000/Login", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email,
        inputPass,
      }),
    }).then((response) => 
            {
              // console.log(inputPass)
              // console.log('inside response')
              if(response.status == '400'){
              console.log("error: email is not registered")
            } else if(response.status == '401'){
              console.log('error: Most provide email and password!')
            } else if(response.status == '402'){
              console.log('error: provided password comparision is wrong')
            } else if(response.status == '403'){
              console.log('error: wrong email')
            } else if(response.status == '406'){
              console.log('error: wrong password')
            }
            else if(response.status == '200'){
              console.log('Correct log in!')
              navigation.navigate("Home")
            } else{  console.log("None of the if's are working ")
                    console.log(response.status)}
          })
  } catch (err) {
    console.log("Connection is wrong!");
        // console.log(json.user)
    }
  }
    return (
        
        <ImageBackground source={require('../FrontEndImages/lll.jpg')} style={styles.backgroundContainer}>
        <View style={styles.ViewStyle}>
        
        <Text
        style={{textAlign:"center" , fontSize:30}}
        >Login to your account</Text>
        <Text>
          {"\n"}
          
         
        </Text>
            <Text style={{fontSize:21, color:'black',fontWeight:'bold'}}>Email:</Text>
            <TextInput style={styles.InputStyle}
            // placeholder = "email"
         
            // // everytime text changes will set the password
             
            onChangeText={(value) => {setEmail(value)}}
            value={email}
            ></TextInput>
            <Text>
          {"\n"}
        </Text>
        <Text style={{fontSize:21, color:'black',fontWeight:'bold'}}>Password:</Text>
            <TextInput  style={styles.InputStyle}
            // placeholder = "password"
            
            // secureTextEntry
            // //everytime text changes will set the password 
            onChangeText={(value) => setPassword(value)}
            value={inputPass}
            ></TextInput>
            </View>
            <View>
            <Text>
          {"\n"}          
        </Text>

        {/* for new lines */}
        <Text>
          {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"}          
          {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"}          
          {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"} {"\n"}          
          {"\n"} {"\n"} {"\n"} {"\n"} {"\n"}           
        </Text>
            <TouchableOpacity
            
            onPress= {handleValidation}
            ><Text style={styles.btnLogin}>Login</Text></TouchableOpacity>
            
            <Text style=
            {{fontWeight:"bold",
              marginTop:30, color:'#d8e2dc'}}>don't have an account? </Text>
            <TouchableOpacity
                onPress={() => {
                    navigation.navigate("SignUp")
                }}
            ><Text style={styles.btnSignUp}>Sign Up</Text></TouchableOpacity>
            </View>
        
        </ImageBackground>
    );
}
const styles = StyleSheet.create({
    ViewStyle:{
        flex: 0.9,
        opacity:0.5,
        // justifyContent: "space-between",
        backgroundColor:"white",
        borderRadius:21,
        position:'absolute',
        padding:40,
        marginTop:100
     
    },
    ViewBtn:{
     marginBottom:10
    },

    InputStyle: {
        backgroundColor:"#e8e8e4",
        fontSize: 22,
        borderRadius:7,
        borderColor: 'black',
        borderWidth: 1,
        paddingRight:10,
        width: windowWidth * 0.8,
        height: windowHeight * 0.05
    },
    backgroundContainer: {
        flex: 1,
        width: null,
        height: null,
        alignItems: "center",
        justifyContent: "center",
      },
      btnLogin: {
        width: WIDTH - 75,
        color:'#d8e2dc',
        textAlign:'center',
        backgroundColor: '#008192',
        fontWeight:'bold',
        borderRadius:205 , 
        width: WIDTH - 250,
        height:45,
        fontSize :22,
        // marginBottom: 30,
        // marginTop: 70,
        paddingTop:7,
        // position:'relative',
        // top:220
      },
      btnSignUp: {
        width: WIDTH - 75,
        color:'#d8e2dc',
        textAlign:'center',
        backgroundColor: '#008192',
        fontWeight:'bold',
        borderRadius:205 , 
        width: WIDTH - 250,
        height:45,
        fontSize :22,
        marginBottom: 30,
        // marginTop: 20,
        paddingTop:7,
        
        
        // top:240
      }
      
      
});