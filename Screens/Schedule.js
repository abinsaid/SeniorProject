import React, {useState} from 'react';
import {View, TouchableOpacity, Text, StyleSheet,SafeAreaView} from 'react-native';
import {Agenda} from 'react-native-calendars';
import {Card, Avatar} from 'react-native-paper';


function Schedule() {
      return (
        <SafeAreaView style={styles.safe}>
          <Agenda  />
        </SafeAreaView>
      );
    };
    
    
    const styles = StyleSheet.create({
      safe: {
        flex: 1,
      },
      itemContainer: {
        backgroundColor: 'white',
        margin: 5,
        borderRadius: 15,
        justifyContent: 'center',
        alignItems: 'center',
        flex: 1,
      },
    });
    
export default Schedule;