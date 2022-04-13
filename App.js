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
import Homepage from "./Screens/Homepage"
import Calendar from "./Screens/Calendar"
import SmartSchedulingSystem from './Screens/SmartSchedulingSystem';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Events from './Screens/Events';
import addEventCalc from './Screens/addEventCalc';
import daysPage from './Screens/daysPage';


const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

export default function StackNavigator() {
 return(
  <NavigationContainer>
  <Stack.Navigator>
  <Stack.Screen name = "start up" component={SmartSchedulingSystem}/>
  <Stack.Screen name = "Login" component={Login}/>
  <Stack.Screen name = "SignUp" component={SignUp}/>
  <Stack.Screen name='daysPage' component={daysPage}/> 
  <Stack.Screen name='addEventCalc' component={addEventCalc}/>
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
      height:69,
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
       Home
      </Text>
          </View>
        ),
      }}      
      />
      <Tab.Screen name = "Events" component={Events}
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
      <Tab.Screen name = "Calendar" component={Calendar}
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
        style={{color: focused? 'red':'black', fontSize:10,right:7}}>
       Schedule
      </Text>
          </View>
        ),
      }}      
      />

    </Tab.Navigator>
  )
}