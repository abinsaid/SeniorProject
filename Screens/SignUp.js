import React, { useState } from 'react';
import { Text, StyleSheet, View, Button, TouchableOpacity, TextInput,ImageBackground } from 'react-native';
import { Dimensions } from 'react-native';

const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;

export default function SignUp() {
    return (
        <ImageBackground source={require('../images/background.png')} style={styles.backgroundContainer}>

    <View style={styles.ViewStyle}>
        <TextInput
            placeholder="First Name"
            style={styles.InputStyle}>
        </TextInput>

        <TextInput
            placeholder='Last Name'
            style={styles.InputStyle}>
        </TextInput>
        <TextInput
            placeholder='Email'
            style={styles.InputStyle}>
        </TextInput>

        <TextInput
            placeholder='UID'
            style={styles.InputStyle}>
        </TextInput>

        <TextInput
            placeholder='Password'
            style={styles.InputStyle}>
        </TextInput>

        <TextInput
            placeholder='Confirm Password'
            style={styles.InputStyle}>
        </TextInput>

        <TouchableOpacity><Text>Confirm</Text></TouchableOpacity>

    </View>
    </ImageBackground>
    );
}

const styles = StyleSheet.create({
    ViewStyle:{
        flex: 0.55,
        justifyContent: "space-between",
        backgroundColor:"white"
    },
    
    InputStyle: {
        backgroundColor:"white",
        fontSize: 22,
        borderRadius:6,
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