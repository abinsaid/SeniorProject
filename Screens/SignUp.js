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
  
  // const [intrest1, setIntrest1] = useState(false);
  // const [intrest2, setIntrest2] = useState(false);
  // const [intrest3, setIntrest3] = useState(false);
  // const [intrest4, setIntrest4] = useState(false);
  // const [intrest5, setIntrest5] = useState(false);
  // const [intrest6, setIntrest6] = useState(false);

  const onClickListener = () => {
    if (studName) {
      if (email) {
        if (pass) {
          if(email.includes('@stu.kau.edu.sa')){
            // Alert.alert('student has been registered')
            try {
              fetch("http://172.20.10.2:3000/signup", {
                method: "POST",
                headers: {
                  Accept: "application/json",
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  studName,
                  email,
                  pass
                }),
              })
                .then((response) => response.json())
                .then((json) => Alert.alert(json)
                );
            } catch (err) {
              Alert.alert("Connection is wrong!");
            }
            Alert.alert('student has been registered')
           } else { Alert.alert("wrong email: only student emails allowed!")}
          // Alert.alert({ student });
          
        } else {
          Alert.alert("pls enter password");
        }
      } else {
        Alert.alert("pls enter email");
      }
    } else {
      Alert.alert("pls enter student name");
    }
  // };
  // const handleSubmit = () => {
  //   // setIsPending(true);
  //   if(intrest1==false && intrest2 == false && intrest3 == false
  //   && intrest4==false && intrest5 == false && intrest6 == false){
  //     Alert.alert('you must choose atleast one intrest')
  //   } else {

  // };
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
