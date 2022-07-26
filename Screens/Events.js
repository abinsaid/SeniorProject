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
  SafeAreaView,Linking,
  ActivityIndicator,
} from "react-native";
import { FlatList } from "react-native-gesture-handler";
export default function Events() {
   const [data,setData] = useState([])
   const openUrl = async (url) =>{
     const isSupported = await Linking.canOpenURL(url)
     if(isSupported){
       await Linking.openURL(url)
     } else{
       Alert.alert('url is not working')
     }
   }
  // const [status,setStatus] = useState('other')
  useEffect(() => {
    fetch("http://172.20.10.2:3000/getEvent")
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
          
          // if(item.Technology == '0'){
          //   item.Technology = 'something'
          // }
          
          <View
            style={{
              textAlign:"left",
              paddingBottom: 10,
              borderBottomWidth: 1,
              marginBottom: 12,
            }}
          >
            <Text style={styles.eventText}>
    Instructor: {item.Instructor} 
    {"\n"} 
    Topic: {item.Topic}
    {"\n"}
    Date: {item.Date}
    {"\n"}
    Day: {item.Day}            <TouchableOpacity style={styles.LinkText} onPress={ ()=> 
  openUrl(item.Link) } ><Text style={styles.btnLink} >رابط التسجيل</Text></TouchableOpacity>
    {"\n"} 
    From {item.Starting} | to {item.Ending} 
    {"\n"}
    category:
    {item.Technology == '0' ?  
    
     <Text></Text>
     : <Text>Technology, </Text>} 
     {item.SoftSkills == '0' ?  
    
     <Text></Text>
     : <Text>SoftSkills, </Text>} 
     {item.Managment == '0' ?  
    
     <Text></Text>
     : <Text>Management</Text>}
     {"\n"}
    
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
    // flex: 1,
    paddingHorizontal:10,
    justifyContent: "center",
  },
  eventText: {
    fontSize: 20,
    fontWeight: "200",

    textAlign: "left",
    // borderWidth: 1,
    // borderColor: "thistle",
    borderRadius: 50,
  },
  topic: {
    fontSize: 15,
    fontWeight: "bold",
  },
  instructor: {
    textAlign: "center",
    marginBottom: 18,
    fontWeight: "200",
    color: "green",
  },
  LinkText: {
   color:'#4361ee',
   textDecorationLine: 'underline',
  },
  btnLink: {
    fontWeight: "bold",
    fontSize: 22,
    color: "#003049",
    backgroundColor: "#48cae4",
    // width: windowWidth - 300,
    alignItems:'center',
    textAlign: "center",
    borderRadius: 170,
    marginLeft: 20,
  },
  listTab:{
  flexDirection: 'row',
  alignSelf: 'center',
  marginBottom:20
  },

  btnTab:{
    // width: 68,
    // fontSize:20
    flexDirection: 'row',
    borderWidth: 0.9,
    borderColor: '#6c757d',
    padding: 10,
    justifyContent:'center'
  },
  textTab: {
  fontSize:10,
  fontWeight:'bold'
  } , 
  btnTabActive:{
    backgroundColor:'#E6838D'
  },
  textTabActivity:{
    color:"#001219"
  },
  itemContainer: {
    flexDirection: 'row',
    paddingVertical:15
  },
  itemBody:{
    flex:1,
    paddingHorizontal:'10'
  }

});
