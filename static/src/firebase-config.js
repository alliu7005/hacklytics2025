import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyDwMMuWrvfHcS0bhQ_VV0PyKf6dcfl7Tr0",  
    authDomain: "hacklytics25.firebaseapp.com", 
    projectId: "hacklytics25",
    storageBucket: "hacklytics25.firebasestorage.app",
    messagingSenderId: "103017309341",
    appId: "1:103017309341:web:a0cc62422cd8fc08116074",
    measurementId: "G-7WGZN3C31Y"  
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

window.onload =  function() {
    
    var signUpButton = document.getElementById("signUpButton");
    var signInButton = document.getElementById("signInButton");

    signUpButton.addEventListener("click", function() {
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
        
        createUserWithEmailAndPassword(auth, email, password).then((userCredential) => {
                var user = userCredential.user;
                console.log("User Created:", userCredential.user);
                alert("Success");
            })
            .catch((error) => {
                console.error("Error:", error.message);
            });
    });

    signInButton.addEventListener("click", function() {
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
        
        signInWithEmailAndPassword(auth, email, password).then((userCredential) => {
                var user = userCredential.user;
                
                console.log("heeeeees")
                const userId = { "uid": user.uid };
                var d = JSON.stringify(userId);
                console.log(JSON.parse(d))
                fetch("/", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(userId)
                    
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                })
                .catch(error => console.error('Error:', error));
            
            })
            .catch((error) => {
                console.error("error:", error.message);
            })
        window.location.href = "/";
    });

    onAuthStateChanged(auth, (user) => {
        if (user) {
            const uid = user.uid;
        }
        else {
            
        }
    })

}


