from flask import Flask, request, render_template, jsonify, redirect
import firebase_admin
from firebase_admin import credentials, firestore, auth


cred = credentials.Certificate("firebase-auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    if not user_logged_in():
        return redirect('login')
    return render_template('index.html')


def user_logged_in():
    try:
        user = auth.get_user()
        return user is not None
    except:
        return False

if __name__ == "__main__":
    app.run(debug=True)
