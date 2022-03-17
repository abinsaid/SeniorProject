import * as React from 'react';
import {
  StyleSheet,
  Button,
  Dimensions,
} from "react-native";
import { TextInput } from "react-native-gesture-handler";
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import SignUp from "./Screens/SignUp";
import Login from "./Screens/Login";
import EventsScreen from "./Screens/EventsScreen"
import Homepage from "./Screens/Homepage"
import SmartSchedulingSystem from './Screens/SmartSchedulingSystem';

const Stack = createNativeStackNavigator();


function StackNavigator() {
 return(
  <NavigationContainer>
  <Stack.Navigator>
  <Stack.Screen name = "start up" component={SmartSchedulingSystem}/>
  <Stack.Screen name = "Login" component={Login}/>
  <Stack.Screen name = "SignUp" component={SignUp}/>
  <Stack.Screen name = "EventsScreen" component={EventsScreen}/>
  <Stack.Screen name = "Homepage" component={Homepage}/>
  </Stack.Navigator>
</NavigationContainer>
 );
}
export default StackNavigator;