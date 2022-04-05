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
import Events from "./Screens/Events"
import Homepage from "./Screens/Homepage"
import Schedule from "./Screens/Schedule"
import SmartSchedulingSystem from './Screens/SmartSchedulingSystem';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';


const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

export default function StackNavigator() {
 return(
  <NavigationContainer>
  <Stack.Navigator>
  <Stack.Screen name = "start up" component={SmartSchedulingSystem}/>
  <Stack.Screen name = "Login" component={Login}/>
  <Stack.Screen name = "SignUp" component={SignUp}/>
  {/* <Stack.Screen name = "Events" component={Events}/> */}
  {/* <Stack.Screen name = "Homepage" component={Homepage}/> */}
  <Stack.Screen name = "Home" component={Tabs} options={{ headerShown: false }}/>
  </Stack.Navigator>
</NavigationContainer>
 );
}
function Tabs(){
  return(
    <Tab.Navigator>
      <Tab.Screen name = "HomePage" component={Homepage}/>
      <Tab.Screen name = "Events" component={Events}/>
      <Tab.Screen name = "Schedule" component={Schedule}/>
    </Tab.Navigator>
  )
}