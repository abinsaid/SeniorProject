// import { json, response } from "express";
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
  ActivityIndicator,
} from "react-native";
import { FlatList } from "react-native-gesture-handler";

export default function Events() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://192.168.1.100:3000/getEvent")
      .then((response) => response.json())
      .then((json) => {
        setData(json);

        console.log("========================");
        console.log(data);
        console.log("========================");
      })
      .catch((error) => alert(error))
  },[]);

  return (
    <SafeAreaView>
        <View style={{}}>
          <FlatList
            //data of Event object
            data={data}
            keyExtractor={({ id }, index) => id}
            renderItem={({ item }) => (
              <View
                style={{
                  paddingBottom: 10,
                  borderBottomWidth: 1,
                  marginBottom: 12,
                }}
              >
                <Text style={styles.eventText}>
                  {item.instructor} , {item.topic}
                </Text>
              </View>
            )}
          />
        </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 48,
    textAlign: "center",
  },
  eventText: {
    fontSize: 22,
    fontWeight: "200",

    textAlign: "center",
    // borderWidth: 1,
    // borderColor: "thistle",
    borderRadius: 50,
  },
  topic: {
    fontSize: 32,
    fontWeight: "bold",
  },
  instructor: {
    textAlign: "center",
    marginBottom: 18,
    fontWeight: "200",
    color: "green",
  },
});