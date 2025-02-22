import firebase_admin.auth
from flask import Flask, request, render_template, jsonify, redirect, session
import firebase_admin
from firebase_admin import credentials, firestore, auth
from flask_session import Session
#from flask_admin import Admin

cred = credentials.Certificate("firebase-auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()




app = Flask(__name__)

app.secret_key = 'KEY'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/', methods = ['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        data = request.json
        uid = str(data.get("uid"))
        session['uid'] = uid
        print(uid)
        return jsonify({})
    if "uid" not in session:
        print("uid not in session")
        return redirect('login')
    print(session['uid'])
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loggedin')
def loggedin():
    return redirect("/")

@app.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect('login')

@app.context_processor
def uid():
    if "uid" in session:
        print(session["uid"])
        return {"uid" : session["uid"]}
    else:
        print("none")
        return {"uid" : None}
    



if __name__ == "__main__":
    app.run(debug=True)
