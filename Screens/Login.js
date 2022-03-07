import React, { useState } from 'react';
import { Text, StyleSheet, View, Button, TouchableOpacity, TextInput, ImageBackground } from 'react-native';
import { Dimensions } from 'react-native';
const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;

export default function Login({ navigation }) {

    return (
        <ImageBackground source={require('../images/background.png')} style={styles.backgroundContainer}>
        <View 
       
        style={styles.ViewStyle}>
                         <Text
                         style={{textAlign:"center" , fontSize:40}}
                         >Welcome</Text>

            
            
            <Text>Email:</Text>
            <TextInput style={styles.InputStyle}
            ></TextInput>

            <Text>Password:</Text>
            <TextInput  style={styles.InputStyle}
            ></TextInput>
            <TouchableOpacity
            style={{
                backgroundColor: '#0AC195CC',
                borderRadius:5,
                width:windowWidth,
                Height:windowHeight
            }}
            onPress={()=>{

            }}
            ><Text style={{textAlign:"center" , fontSize:30}}>Login</Text></TouchableOpacity>
            
            <Text style={{fontWeight:"bold"}}>don't have an account? </Text>
            <TouchableOpacity
                onPress={() => {
                    navigation.navigate("SignUp")
                }}
            ><Text>Sign Up</Text></TouchableOpacity>
        </View>
        </ImageBackground>
    );
}
const styles = StyleSheet.create({
    ViewStyle:{
        flex: 0.5,
        justifyContent: "space-between",
        backgroundColor:"white"
     
    },
    InputStyle: {
        backgroundColor:"white",
        fontSize: 22,
        borderRadius:7,
        borderColor: 'black',
        borderWidth: 1,
        width: windowWidth * 1,
        height: windowHeight * 0.05
    },
    backgroundContainer: {
        flex: 1,
        width: null,
        height: null,
        alignItems: "center",
        justifyContent: "center",
      }
});