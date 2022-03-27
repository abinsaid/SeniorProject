
import React, { useState, useEffect } from 'react';
import { Text, StyleSheet, View, Button, TouchableOpacity, TextInput, ImageBackground, Dimensions, SafeAreaView } from 'react-native';
//   import {GoogleSignin,GoogleSigninButton,statusCodes} from 'react-native-google-signin';
// const {width: WIDTH } = Dimensions.get('window')

const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;

//  onGetUsr = (email) =>{

//  }
export default function Login({ navigation }) {
  
  
   const [email, setEmail] = useState('')
   const [password, setPassword] = useState('')


///////////////////////////////////////////////////////////////////
const [initializing, setInitializing] = useState(true);
  const [user, setUser] = useState();


///////////////////////////////////////////////////////////////////
    return (
        
        <ImageBackground source={require('../images/background.png')} style={styles.backgroundContainer}>
        <View 
        
        style={styles.pageStyle}>
                         <Text
                         style={{textAlign:"center" , fontSize:40}}
                         >Welcome</Text>

            <Text style = {styles.label}>Email:</Text>
            <TextInput style={styles.InputStyle}
            placeholder = "email"
             value={email}
            // // everytime text changes will set the password 
             onChange = {text => setEmail(text)} 
            ></TextInput>

            <Text style = {styles.label}>Password:</Text>
            <TextInput  style={styles.InputStyle}
            placeholder = "password"
             value={password}
            // secureTextEntry
            // //everytime text changes will set the password 
             onChange = {text => setPassword(text)} 
            ></TextInput>
            <TouchableOpacity
            
            onPress={() => {
                    navigation.navigate("Homepage")
                }}
            ><Text style={styles.btnLogin}>Login</Text></TouchableOpacity>
            
            <Text style={{fontWeight:"bold"}}>don't have an account? </Text>
            <TouchableOpacity
                onPress={() => {
                    navigation.navigate("SignUp")
                }}
            ><Text style = {styles.btnSignUp}>Sign Up</Text></TouchableOpacity>

        </View>
        </ImageBackground>
    );
}
const styles = StyleSheet.create({
    pageStyle:{
        flex: 0.8,
        // justifyContent: "space-between",
        backgroundColor:"#bfc0c0"
     
    },
    InputStyle: {
        backgroundColor:"#e8e8e4",
        fontSize: 22,
        borderRadius:7,
        borderColor: 'black',
        borderWidth: 1,
        width: windowWidth * 1,
        height: windowHeight * 0.05,
        marginBottom: 20,
    },
    backgroundContainer: {
        flex: 1,
        width: null,
        height: null,
        alignItems: "center",
        justifyContent: "center",
      },
      btnLogin: {
        width: windowWidth - 75,
        color:'#003049',
        textAlign:'center',
        backgroundColor: '#0AC195CC',
        fontWeight:'bold',
        borderRadius:205 , 
        width: windowWidth - 250,
        height:45,
        fontSize :22,
        marginBottom: 30,
        marginTop: 20,
        paddingTop:7
      },
      btnSignUp: {
        fontWeight:'bold',
        fontSize :22,
        color:'#003049',
        backgroundColor: "#bee1e6",
        width: windowWidth - 250,
        textAlign:'center',
        borderRadius:205 ,
        marginTop:20,

      },
      label: {
       fontSize: 22,
      }
      
});