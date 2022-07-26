import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  StatusBar
} from 'react-native';

export default class Dayspage extends Component {
 
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

      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1
  }
});