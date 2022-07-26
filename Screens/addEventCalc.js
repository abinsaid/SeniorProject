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
const windowWidth = Dimensions.get("window").width;
const windowHeight = Dimensions.get("window").height;
const onClickListener = () => {
  
};
export default function Addevent() {
  return (
    
    <ImageBackground
      source={require("../images/background.png")}
      style={styles.backgroundContainer}
    >
      <View style={styles.PageStyle}>
        <Text style={styles.h1}>Add Event Manually</Text>
        {/* for new lines: */}
        <Text></Text>
          
          <TextInput
            placeholder="Topic"
            style={styles.InputStyle}
          ></TextInput>

          <TextInput
            placeholder="Day"
            style={styles.InputStyle}
          ></TextInput>

          <TextInput
            placeholder="Date"
            style={styles.InputStyle}
          ></TextInput> 

          <TextInput
          placeholder="Starting time"
          style={styles.InputStyle}
        ></TextInput>

         <TextInput
            placeholder="Ending time"
            style={styles.InputStyle}
          ></TextInput>
          <TouchableOpacity
          onPress={onClickListener}
        >
          <Text style={styles.btnConfirm}>Confirm</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
    )
}
const styles = StyleSheet.create({
  PageStyle: {
    flex: 0.85,
    width: windowWidth,
    // justifyContent: "space-between",
    backgroundColor: "#ffffff",
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

  h1: {
    fontSize: 30,
    fontWeight: "bold",
    alignSelf: "center",
  },
  btnConfirm: {
    fontWeight: "bold",
    fontSize: 22,
    color: "#003049",
    backgroundColor: "#48cae4",
    width: 100,
    top:30,
    left:10,
    textAlign: "center",
    borderRadius: 170,
    marginLeft: 20,
  },
});