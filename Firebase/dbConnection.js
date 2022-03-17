import * as firebase from "firebase"
import * as firebase from "firebase/app";
import { firebase } from "@react-native-firebase/auth";

// Import the functions you need from the SDKs you need

import {initializeApp} from "firebase/app";
import {getDatabase} from "firebase/database";
 import { getFirestore, collection, getDocs, query, where, doc, getDocFromCache } from 'firebase/firestore';

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC7B9U3AepmdWHtvV4bIoEuvbpd3IFKPjY",
  authDomain: "seniorproject-2f25b.firebaseapp.com",
  projectId: "seniorproject-2f25b",
  storageBucket: "seniorproject-2f25b.appspot.com",
  messagingSenderId: "591237912061",
  appId: "1:591237912061:web:8e908390dae4dd61193594",
  measurementId: "G-QP4GC2F97N"
};

// Initialize Firebase


const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
// export auth = getAuth(app)


// fetching the database

 export async function getUsr(email){
          // try to handle network errors
const usrReference = collection(db, 'users');
// const usrReference = doc(db,"users","Student1");
const usrSnapshot = await getDoc(usrReference);

const q = query(usrReference, where(email, "==","Abdullah@gmail.com"))
 
querySnapshot.forEach((doc) => {
  // doc.data() is never undefined for query doc snapshots
  console.log(doc.id, " => ", doc.data()); 
})
return usrList;
 }
 



  

