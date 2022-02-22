import React, { Component } from "react";
import {
  StyleSheet,
  Text,
  View,
  Button,
  TouchableOpacity,
  ImageBackground,
  Image,
  Dimensions,
} from "react-native";
 import { TextInput } from "react-native-gesture-handler";
import bgImage from "./images/background.png";
import icon from "./images/icon.png";

const {width: WIDTH } = Dimensions.get('window')
export default class SmartSchedulingSystem extends Component {
  render() {
    return (
      <ImageBackground source={bgImage} style={styles.backgroundContainer}>
        <View>
          <Image source={icon} style={styles.icon} />
          <Text style={styles.iconText}>Smart Scheduling System</Text>
          <Text style={styles.subIconText}>For every minute spent organizing, an hour is earned.</Text>
        </View>
        {/* <View>
          <TextInput
            style={styles.input}
            placeholder={"Username"}
            placeholderTextColor={"#36096d"}
            place
          />
        </View> */}
        <TouchableOpacity>
          <Text style={styles.btnRegister}>Get Started</Text>
        </TouchableOpacity>
        
        <TouchableOpacity>
          <Text style={styles.btnLogin}>Login</Text>
        </TouchableOpacity>
      </ImageBackground>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    color: "white",

    // backgroundImage: linear-gradient("315deg", "#36096d", "#37d5d6"),
  },
  backgroundContainer: {
    flex: 1,
    width: null,
    height: null,
    alignItems: "center",
    justifyContent: "center",
  },
  icon: {
    width: 350,
    height: 250,
    marginLeft: 15
    // marginBottom: 200,
  
  },
  iconText: {
    color: "white",
    fontWeight:'bold',
    fontSize: 30,
    // marginBottom: 300,
    opacity: 0.5,
    marginLeft:3
  },
  subIconText:{
    color:'#6c757d',
    marginLeft: 15,
    marginBottom:100

  },
  textStyles: {
    fontSize: 25,
    fontFamily: "Ariel",
    alignItems: 'flex-end'
  },
  input: {
     width: WIDTH - 210,
    height:55,
    borderRadius:25 , 
    fontSize :22,
    fontWeight:'bold',
    textAlign:'center',
    // paddingLeft: 45,
    backgroundColor: '#0AC195CC',
    // marginHorizontal: 70,
    marginBottom:40
  },
  btnLogin: {
    width: WIDTH - 75,
    color:'white',
    textAlign:'center',
    backgroundColor:'#669bbc',
    fontWeight:'bold',
    borderRadius:205 , 
    width: WIDTH - 250,
    height:45,
    fontSize :22,
    paddingTop:7

  }, 
  btnRegister: {
    width: WIDTH - 75,
    color:'#003049',
    textAlign:'center',
    backgroundColor: '#0AC195CC',
    fontWeight:'bold',
    borderRadius:205 , 
    width: WIDTH - 250,
    height:45,
    fontSize :22,
    marginBottom: 50,
    paddingTop:7
  }
});
