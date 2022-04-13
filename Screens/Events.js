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
const listTab =[
  {
    status: 'Discover more'
  },
  {
    status: 'Softskills'
  },
  {
    status: 'Sport'
  },
  {
    status: 'Economic'
  },
  {
    status: 'Management'
  },
  {
    status: 'Computer'
  },
]
// const updateEvent = () =>{

//   setInterval(setData( u()),  60 * 2000)
// }

export default function Events() {
  // const data =[
  //   {
  //     topic:'دورة الثقافة',
  //     status:'white'
  //   },
  //   {
  //     topic:'دورة السايبر',
  //     status:'Black'
  //   },
  //   {
  //     topic:'دورة العلم',
  //     status:'Green'
  //   }
  //   ]
  // const [data, setData] = useState([]);
   const [data,setData] = useState([])
  // const [status,setStatus] = useState('other')
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


  // useEffect(()=>{
  //   setInterval(()=>{
  //     fetch("http://192.168.1.100:3000/getEvent")
  //     .then((response) => response.json())
  //     .then((json) => {
  //       setData(json);
  
  //       console.log("========================");
  //       console.log(data);
  //       console.log("========================");
  //     })
  //     .catch((error) => alert(error))


  //   }, 60*2000)
  // },[])

  // const setStatusFilter = status =>{
  //   setStatus(status)
  // }
  //  const renderItem = ({item, index})=>{

  //      <View key={index} style ={styles.itemContainer}
       
  //     >
  //     <View style= {styles.itemBody}>
  //     <Text style={styles.topic}>{item.topic}</Text>
  //      </View>
       
  //     </View>
 
  // }
 
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
          {item.instructor} , {item.Topic}
    {"\n"}
    {item.Day} , From {item.Starting} | to {item.Ending} 
    {"\n"}
    {item.Date} 
    {"\n"}  
  
  
    <TouchableOpacity style={styles.LinkText} onPress={ ()=> 
  Linking.openURL(item.link) } ><Text style={styles.btnLink} >رابط التسجيل</Text></TouchableOpacity>
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

    textAlign: "center",
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
   textDecorationLine: 'underline'

  },
  btnLink: {
    fontWeight: "bold",
    fontSize: 22,
    color: "#003049",
    backgroundColor: "#48cae4",
    // width: windowWidth - 300,
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
