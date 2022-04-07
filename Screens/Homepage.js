import {
  Text,
  StyleSheet,
  View,
  Button,
  TouchableOpacity,
  TextInput,
  ImageBackground,
  Dimensions,
  SafeAreaView,
  ScrollView,
} from "react-native";


const { width: WIDTH } = Dimensions.get("window");
const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;
export default function Login({ navigation }) {
  return (
    <ImageBackground source={require('../images/background.png')} style={styles.backgroundContainer}>

     
     {/* upper label */}
     <View>
     <View style= {styles.upperView}><Text style= {styles.upperText}>This is the Homepage screen!</Text></View>
      <View style={styles.lowerView}>
        {/* <Text style={styles.homeText}>This is the Homepage screen!</Text> */}
       
        <TouchableOpacity style = {styles.btnEvent}
          onPress={() => {
            navigation.navigate("Events");
          }}
        >
          <Text style= {styles.btnEvent}>Events Page</Text>
        </TouchableOpacity>
     
      </View>
      </View>
    </ImageBackground>
  );
}

export const styles = StyleSheet.create({
  upperView: {
    // flex: 1,
    // alignItems: "center",
    // justifyContent: "center",
    // backgroundColor: "#bde0fe",
    // paddingBottom:50,
    fontWeight:'bold',
    fontSize: 50,
    paddingTop:220,
    alignItems: 'center',
    //  marginBottom: 10,
     width:windowWidth *1,
     height: 280,
     color:'#bde0fe'
    //  borderRadius:100 ,
   
  },
  upperText: {
    
    fontWeight:'bold',
    fontSize: 30,
     color:'#bde0fe'
   
  },
  lowerView: {
    backgroundColor: "#fe6d73",
    // marginTop: 10,
    alignItems: "center",
    paddingTop: 50,
    // paddingBottom: 50,
    height: 650,
    borderRadius:105 ,
    width:windowWidth *1
  },
  homeText: {
      marginTop: -150,
      fontSize: 25,
      fontWeight: "bold",
    },
      backgroundContainer: {
        flex: 1,
        width: null,
        height: null,
        alignItems: "center",
        justifyContent: "center",
      },
  
  btnLogin: {
    width: WIDTH - 75,
    color: "#003049",
    textAlign: "center",
    backgroundColor: "#0AC195CC",
    fontWeight: "bold",
    borderRadius: 205,
    width: WIDTH - 250,
    height: 45,
    fontSize: 22,
    marginBottom: 50,
    // paddingTop: 7,
  },
  btnEvent: {
    color: "white",
    textAlign: "center",
    backgroundColor: "#003049",
    borderRadius:5 , 
    fontSize: 20,
    // paddingBottom: 100

 }
<<<<<<< HEAD
});
=======
});
>>>>>>> db3a336f8d73156e0a36c6b1db32ab62604d5895
