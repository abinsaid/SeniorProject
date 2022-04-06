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

// const EventData = [
//   {
//     topic: "Health care course",
//     instructor: "Abdullah Mohammed",
//     time1: "20:00",
//     time2: "22:00",
//   },
//   {
//     topic: "Network course",
//     instructor: "Zain Sami",
//     time1: "17:00",
//     time2: "19:00",
//   },
//   {
//     topic: "Wrestling course",
//     instructor: "Ahmed",
//     time1: "08:00",
//     time2: "10:00",
//   },
// ];

export default function Events(navigation) {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState();

  const [topic, setTopic] = useState([]);
  const [instructor, setInstructor] = useState([]);

  useEffect(() => {
      
   fetch('http://192.168.1.100:3000/getEvent')
   .then((response)=>response.json())
   .then((json) =>{
       console.log('========================')
    console.log(json)
    // const jsoon = JSON.parse(json)
    setData(data)
       setTopic(json[1].topic)
       setInstructor(json.instructor)
       console.log('========================')
       console.log({topic}
        )
    }
       )
   .catch((error) => alert(error))
   .finally(() => setLoading(false))
},[]);
  return (
    <SafeAreaView>
    {isLoading ? (
        <ActivityIndicator/>
    ): (
        <View>
        
      <Text>This is the Event screen and it is working!</Text>
      <Text>{data}</Text>
      <FlatList

      //data of Event object
      data ={data}
      keyExtractor={ ( { id } , index ) => id}
      renderItem={({item}) => (
          <View>
       <Text>
           {item.topic}
           {item.instructor}
       </Text>
       </View>
      )}
      
      />
      </View>
      )}
    </SafeAreaView>
  );
}
