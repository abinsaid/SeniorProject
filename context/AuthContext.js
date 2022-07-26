import createDataContext from './createDataContext';
import trackerApi from '../api/tracker'

const authReducer = (state, action) => {
  switch (action.type) {
    default:
      return state;
  }
};

const signup = dispatch =>{
return async({studName,email,pass,intrest1,intrest2,intrest3,intrest4,intrest5,intrest6})=>{

  try{
    const response = await trackerApi.post('/signup',{studName,email,pass,intrest1,intrest2,intrest3,intrest4,intrest5,intrest6})
    console.log(response.data)
  } catch(err){
  console.log(err.message)
  }
 
// make api request to sign up with user info's

// if we sign up, modify our state, and say that we are authenticated

// if signing in fails we probably need to reflecr an error 
}
}


const signin = (dispatch)=>{
  return({email,pass}) =>{
    // Try to signin
    //handle success by updating state
    // handle failure by showing error message 
  }
}

const signout = (dispatch) => {
return () =>{
// sign out

}

}
export const { Provider, Context } = createDataContext(
  authReducer,
  {signup,signin,signout},
  { isSignedIn: false }
);
