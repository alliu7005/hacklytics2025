import firebase_admin.auth
from flask import Flask, request, render_template, jsonify, redirect, session
import firebase_admin
from firebase_admin import credentials, firestore, auth
from flask_session import Session

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
    
    if session["uid"] is None:
        return redirect('login')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
