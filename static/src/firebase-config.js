import firebase from "firebase/compat/app";
import "firebase/compat/auth";

const firebaseConfig = {
    apiKey: "AIzaSyDwMMuWrvfHcS0bhQ_VV0PyKf6dcfl7Tr0",  
    authDomain: "hacklytics25.firebaseapp.com", 
    projectId: "hacklytics25",
    storageBucket: "hacklytics25.firebasestorage.app",
    messagingSenderId: "103017309341",
    appId: "1:103017309341:web:a0cc62422cd8fc08116074",
    measurementId: "G-7WGZN3C31Y"  
};

firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();

window.onload =  function() {
    console.log("HEEREE");
    var signUpButton = document.getElementById("signUpButton");
    var signInButton = document.getElementById("signInButton");

    signUpButton.addEventListener("click", function() {
        console.log("HEEREE");
        var email = document.getElementById("email");
        var password = document.getElementById("password");
        auth.createUserWithEmailAndPassword(email.value, password.value).then((userCredential) => {
                var user = userCredential.user;
                console.log("User Created:", userCredential.user);
                alert("Success");
            })
            .catch((error) => {
                console.error("Error:", error.message);
            });
    });

    signInButton.addEventListener("click", function() {
        console.log("EEEEEE")
        var email = document.getElementById("email");
        var password = document.getElementById("password");
        auth.signInWithEmailAndPassword(email.value, password.value).then(function() {
                var user = userCredential.user;
                console.log("heeeeees")
                window.location.href = "index.html";
            })
            .catch((error) => {
                console.error("error:", error.message);
            })
    });
}


