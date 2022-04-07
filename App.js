import * as React from 'react';
import {
  StyleSheet,
  View,
  Image,
  Text
} from "react-native";
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import SignUp from "./Screens/SignUp";
import Login from "./Screens/Login";
import EventsScreen from "./Screens/EventsScreen"
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
  <Stack.Screen name = "Home" component={Tabs} options={{ headerShown: false}}/>
  </Stack.Navigator>
</NavigationContainer>
 
 );
}


function Tabs(){
  return(
    <Tab.Navigator
    screenOptions={{tabBarShowLabel:false,  
      tabBarLabelPosition: 'below-icon',
      tabBarStyle:{
      position: 'absolute',
      bottom: 20,
      left: 7,
      right:7,
      elevation:0,
      backgroundcolor: 'white',
      borderRadius: 15,
      height:90,
      ...styles.shadow
    }}}
    >
      <Tab.Screen name = "HomePage" component={Homepage}
      options={{
        tabBarIcon:({focused})=>(
          <View style={{alignitems:'center',JustifyContent:'center', top:9}}>
          <Image
          source={require('./FrontEndImages/home.png')}
          resizeMode="contain"
          style={{
            width:24,
            height:24,
            tintColor: focused? 'red':'black',
          }}/>
        <Text
        style={{color: focused? 'red':'black', fontSize:10,right:2}}>
       HOME
      </Text>
          </View>
        ),
      }}      
      />
      <Tab.Screen name = "Events" component={EventsScreen}
      options={{
        tabBarIcon:({focused})=>(
          <View style={{alignitems:'center',JustifyContent:'center', top:9}}>
          <Image
          source={require('./FrontEndImages/conference.png')}
          resizeMode="contain"
          style={{
            width:24,
            height:24,
            tintColor: focused? 'red':'black',
          }}/>
        <Text
        style={{color: focused? 'red':'black', fontSize:10,right:3}}>
       Events
      </Text>
          </View>
        ),
      }}      
      />
      <Tab.Screen name = "Schedule" component={Schedule}
      options={{
        tabBarIcon:({focused})=>(
          <View style={{alignitems:'center',JustifyContent:'center', top:9}}>
          <Image
          source={require('./FrontEndImages/calendar.png')}
          resizeMode="contain"
          style={{
            width:24,
            height:24,
            tintColor: focused? 'red':'black',
          }}/>
        <Text
        style={{color: focused? 'red':'black', fontSize:10,right:5}}>
       Schedule
      </Text>
          </View>
        ),
      }}      
      />
    </Tab.Navigator>
    
  )
}
const styles = StyleSheet.create({
  shadow:{
    shadowColor:'black',
    shadowOffset:{
      width: 0,
      height:10
    },
    shadowOpacity:0.35,
    shadowRadius:3.5,
    elevation:5
  }
})