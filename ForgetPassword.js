import React, { useState } from 'react';
import { Text, StyleSheet, View, Button, TouchableOpacity, TextInput } from 'react-native';
import { Dimensions } from 'react-native';

const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;

export default function ForgetPassword({navigation}){
    
    return (
        <View style={styles.ViewStyle}>
            
            <Text>Email:</Text>
            <TextInput style={styles.InputStyle}
            ></TextInput>

            <Text>New Password:</Text>
            <TextInput style={styles.InputStyle}
            ></TextInput>

            <Text>Confirm New Password:</Text>
            <TextInput  style={styles.InputStyle}
            ></TextInput>

            <TouchableOpacity
            onPress={()=>{
                navigation.navigate("Login")
            }}
            ><Text>Confirm</Text></TouchableOpacity>
            
           
        </View>
    );
}
const styles = StyleSheet.create({
    ViewStyle:{
        flex: 0.3,
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
});