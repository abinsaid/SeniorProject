import React, { Component, useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  StatusBar
} from 'react-native';
// import DatePicker from 'react-native-date-picker'
// const [date, setDate] = useState(new Date())
//   const [open, setOpen] = useState(false)

export default class DaysPage extends Component {
 
  constructor(props) {
     super(props);
     this.state ={
       bookingDate: this.props.navigation.bookingDate
     }
     
     var t = new Date(props.route.params.bookingDate.timestamp)
     var now = new Date().toLocaleTimeString()

     var hours = t.getHours();
     var minutes = t.getMinutes();
     var newformat = t.getHours() >= 12 ? 'PM' : 'AM';  
     
     // Find current hour in AM-PM Format 
     hours = hours % 12;  
 
     var formatted = 
    (t.toString().split(' ')[0]) 
    + ', ' +('0' + t.getDate()).slice(-2) 
    + '/' + ('0' + (t.getMonth() + 1) ).slice(-2)
    + '/' + (t.getFullYear())
    + ' - ' + ('0' + t.getHours()).slice(-2)
    + ':' + ('0' + t.getMinutes()).slice(-2)
    + ' ' + newformat;
     console.log('time',formatted)
     console.log('timestamp',props.route.params.bookingDate.timestamp)
     console.log('now time',now)
}


render() {

    return (
      <View style={styles.container}>
         <Text style={{}}>day: {this.state.bookingDate}</Text>
         <DatePicker
  mode="time"
/>
         {/* <Text>time: {formatted}</Text> */}
         <TouchableOpacity 
          style={styles.btnEvent}
          onPress={() => {
           this.props.navigation.navigate("AddEventCalc");
          } }
        >
          <Text style={{color: "white",
    textAlign: "center",
    bottom:12,
    fontSize:50,
    }}>+</Text>
        </TouchableOpacity>

      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  btnEvent: {
    color: "white",
    backgroundColor: "#003049",
    width:50,
    borderRadius:70,
    top:130, 
    left:320,
    height:50,
    fontSize: 20,}
});