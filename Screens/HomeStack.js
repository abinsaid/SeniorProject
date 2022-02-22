import React from "react";
import { View, Text, StyleSheet, Button, FlatList } from "react-native";
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import LoginScreen from "./LoginScreen";
import MainScreen from "./MainScreen";
// import Navigation

// class HomeScreen extends React.Component {
//   render() {
//     return (
//     <ImageBackground source={bgImage} style={styles.backgroundContainer}>
//       <View>
//         <Image source={icon} style={styles.icon} />
//         <Text style={styles.iconText}>Smart Scheduling System</Text>
//         <Text style={styles.subIconText}>For every minute spent organizing, an hour is earned.</Text>
        
//       </View>
//       {/* <View>
//         <TextInput
//           style={styles.input}
//           placeholder={"Username"}
//           placeholderTextColor={"#36096d"}
//           place
//         />
//       </View> */}
//       <TouchableOpacity onPress={()=> this.props.nav}>
//         <Text style={styles.btnRegister}>Get Started</Text>
//       </TouchableOpacity>
      
//       <TouchableOpacity onPress={() => props.navigation.navigate('Login')}>
//         <Text style={styles.btnLogin}>Login</Text>
//       </TouchableOpacity>
//     </ImageBackground>
//   );
// }
// }
// render() {
//   return (
//     <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
//       <Text>Home Screen</Text>
//     </View>
//   );
// }
// }
// const screens = {
//   Home: {
//     screen: MainScreen
//   },
//   Login: {
//   Screen:LoginScreen}
// }
// const HomeStack = createStackNavigator(screens);
// export default HomeStack
