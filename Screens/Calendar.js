import React, { Component } from 'react';
import {
  StyleSheet,
  View,
  TouchableOpacity,
  Text
} from 'react-native';
import {Calendar} from 'react-native-calendars';
export default class Schedule extends Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.onDayPress = this.onDayPress.bind(this);
  }
  onDayPress(day) {
    this.setState({
      selected: day.dateString
    });
    this.props.navigation.navigate('daysPage', { bookingDate : day })
  } 
  render() {
    return (
      <View style={styles.container}>      
        <Calendar
          onDayPress={this.onDayPress}
          theme={{
            selectedDayBackgroundColor: '#003049',
            todayTextColor: '#003049',
            arrowColor: '#003049',
          }}
        />
        <TouchableOpacity 
          style={styles.btnEvent}
          onPress={() => {
           this.props.navigation.navigate("Addevent");
          } }
        >
          <Text style={{color: "white",
    textAlign: "center",
    bottom:7,
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
  calendar: {
    paddingTop: 10,
    borderBottomWidth: 5,
    borderColor: '#003049',
    height: 350
  },
  btnEvent: {
    color: "white",
    backgroundColor: "#003049",
    width:50,
    borderRadius:70,
    top:230, 
    left:320,
    height:50,
    fontSize: 20,}
});