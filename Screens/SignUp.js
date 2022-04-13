import React, { input, Label, useState, useEffect, useContext } from "react";
import {
  Text,
  Alert,
  StyleSheet,
  View,
  Button,
  Element,
  TouchableOpacity,
  TextInput,
  Input,
  ImageBackground,
  Dimensions,
  Form,
  SafeAreaView,
} from "react-native";
import CheckBox from "expo-checkbox";
import { ScrollView } from "react-native-gesture-handler";
import { LogBox } from 'react-native';


// handling a warning message when opening signUp page
LogBox.ignoreLogs([
  "[react-native-gesture-handler] Seems like you\'re using an old API with gesture components, check out new Gestures system!",
]);


const windowWidth = Dimensions.get("window").width;
const windowHeight = Dimensions.get("window").height;

export default function SignUp(navigation) {
  const [studName, setName] = useState("");

  const [email, setEmail] = useState("");

  const [pass, setPassword] = useState("");
  
  const [intrest1, setIntrest1] = useState(false);
  const [intrest2, setIntrest2] = useState(false);
  const [intrest3, setIntrest3] = useState(false);
  const [intrest4, setIntrest4] = useState(false);
  const [intrest5, setIntrest5] = useState(false);
  const [intrest6, setIntrest6] = useState(false);

  const onClickListener = () => {
    if (studName) {
      if (email) {
        if (pass) {
          if(email.includes('@stu.kau.edu.sa')){
            console.log('student email has been registered')
            handleSubmit();
           } else { console.log("wrong email: only student emails allowed!")}
          // console.log({ student });
          
        } else {
          console.log("pls enter password");
        }
      } else {
        console.log("pls enter email");
      }
    } else {
      console.log("pls enter student name");
    }
  };
  const handleSubmit = () => {
    // setIsPending(true);
    if(intrest1==false && intrest2 == false && intrest3 == false
    && intrest4==false && intrest5 == false && intrest6 == false){
      console.log('you must choose atleast one intrest')
    } else {

    
    try {
      fetch("http://192.168.1.100:3000/signup", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          studName,
          email,
          pass,
          intrest1,
          intrest2,
          intrest3,
          intrest4,
          intrest5,
          intrest6,
        }),
      })
        .then((response) => response.json())
        .then((json) => console.log(json)
        );
    } catch (err) {
      console.log("Connection is wrong!");
    }
    
  };
}
  return (
    <>
    <ImageBackground
      source={require('../FrontEndImages/background.png')}
      style={styles.backgroundContainer}
    >
      <View style={styles.PageStyle}>
        <Text style={styles.h1}>Register your info</Text>
        {/* for new lines: */}
        <Text></Text>
        <ScrollView>
          <TextInput
            placeholder="name"
            onChangeText={(value) => setName(value)}
            value={studName}
            style={styles.InputStyle}
          ></TextInput>

          <TextInput
            placeholder="email"
            onChangeText={(value) => {setEmail(value)}}
            value={email}
            style={styles.InputStyle}
          ></TextInput>

          <TextInput
            placeholder="password"
            secureTextEntry
            // everytime text changes will set the password
            onChangeText={(value) => setPassword(value)}
            value={pass}
            style={styles.InputStyle}
          ></TextInput>

          <Text></Text>
          <View style={styles.checkboxContainer}>
            <CheckBox
              style={styles.checkbox}
              disabled={false}
              placeholder="IT"
              value={intrest1}
              onValueChange={(newValue) => setIntrest1(newValue)}
            />
            <Text style={styles.label}> IT related</Text>
          </View>
          {/* ////////////////////////// */}

          <View style={styles.checkboxContainer}>
            <CheckBox
              style={styles.checkbox}
              disabled={false}
              placeholder="cyber"
              value={intrest2}
              onValueChange={(newValue) => setIntrest2(newValue)}
            />
            <Text style={styles.label}> Cyber Security </Text>
          </View>
          {/* ////////////////////////// */}

          <View style={styles.checkboxContainer}>
            <CheckBox
              style={styles.checkbox}
              disabled={false}
              placeholder="AI"
              value={intrest3}
              onValueChange={(newValue) => setIntrest3(newValue)}
            />
            <Text style={styles.label}> AI related</Text>
          </View>
          {/* ////////////////////////// */}

          <View style={styles.checkboxContainer}>
            <CheckBox
              style={styles.checkbox}
              disabled={false}
              placeholder="game"
              value={intrest4}
              onValueChange={(newValue) => setIntrest4(newValue)}
            />
            <Text style={styles.label}> Game development </Text>
          </View>
          {/* ////////////////////////// */}
          <View style={styles.checkboxContainer}>
            <CheckBox
              style={styles.checkbox}
              disabled={false}
              placeholder="Web"
              value={intrest5}
              onValueChange={(newValue) => setIntrest5(newValue)}
            />
            <Text style={styles.label}> Web development </Text>
          </View>
          {/* ////////////////////////// */}
          <View style={styles.checkboxContainer}>
            <CheckBox
              style={styles.checkbox}
              disabled={false}
              placeholder="other"
              value={intrest6}
              onValueChange={(newValue) => setIntrest6(newValue)}
            />
       
            <Text style={styles.label}> other </Text>
          </View>
        </ScrollView>
        {/* for new lines: */}
        <Text>
          {"\n"}
          {"\n"}
          {"\n"}
        </Text>

        <TouchableOpacity
          onPress={onClickListener}
        >
          <Text style={styles.btnConfirm}>Confirm</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
    </>
  );
}

const styles = StyleSheet.create({
  PageStyle: {
    flex: 0.75,
    width: windowWidth,
    // justifyContent: "space-between",
    backgroundColor: "#ffffff",
    opacity:0.8
  },
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  checkboxContainer: {
    flexDirection: "row",
    alignItems: "",
    // marginBottom: 20,
  },
  checkbox: {
    alignSelf: "center",
    margin: "center",
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
    marginRight: 40,
    alignSelf: "center",
    paddingLeft: 5,
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
    marginLeft: 70,
    width: windowWidth - 100,
   
  },
  label: {
    fontSize: 22,
    marginBottom: 5,
    // paddingTop:2
  },
  btnConfirm: {
    fontWeight: "bold",
    fontSize: 22,
    color: "#003049",
    backgroundColor: "#48cae4",
    width: windowWidth - 300,
    textAlign: "center",
    borderRadius: 170,
    marginLeft: 20,
  },
  h1: {
    fontSize: 30,
    fontWeight: "bold",
    alignSelf: "center",
  },
  errorMessage: {
    fontSize: 16,
    color: "red",
    marginLeft: 15,
    marginTop: 15,
  },
});
