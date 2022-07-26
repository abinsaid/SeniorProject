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
export default function Homepage({ navigation }) {
  return (
    
    <ImageBackground source={require('../FrontEndImages/lll.jpg')} style={styles.backgroundContainer}>

     
     {/* upper label */}
     <View>
     <View style= {styles.upperView}><Text style= {styles.upperText}>Welcome!</Text></View>
      <View style={styles.lowerView}>
      
          

          <Text style={{textAlign:"center" , fontSize:30, color:'white'}}>
          Thank you for choosing our app
 Our app will provide you with a list of KAU events that you can view and chose the one that suits you 
          </Text>
        {/* <TouchableOpacity style = {styles.btnEvent}
          onPress={() => {
            navigation.navigate("Events");
          }}
        >
          <Text style= {styles.btnEvent}>Events Page</Text>
        </TouchableOpacity> */}
     
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
  upperText2: {
    
    fontWeight:'bold',
    fontSize: 20,
     color:'white'
   
  },
  lowerView: {
    backgroundColor: "#2f6c9d",
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
});
