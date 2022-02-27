import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import SignUp from './SignUp';
import Login from './Login';
import ForgetPassword from './ForgetPassword';
import SmartSchedulingSystem from './App';

const Stack = createNativeStackNavigator();

function StackNavigator() {
 return(
       <NavigationContainer>
       <Stack.Navigator>
       <Stack.Screen name = "start up" component={SmartSchedulingSystem}/>
       <Stack.Screen name = "Login" component={Login}/>
       <Stack.Screen name = "SignUp" component={SignUp}/>
       <Stack.Screen name = "Reset Password" component={ForgetPassword}/>
       </Stack.Navigator>
     </NavigationContainer>
 )
}
export default StackNavigator;