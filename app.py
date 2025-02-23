import firebase_admin.auth
from flask import Flask, request, render_template, jsonify, redirect, session
import firebase_admin
from firebase_admin import credentials, firestore, auth, db
from flask_session import Session
from find_bank import find_best_bank

cred = credentials.Certificate("firebase-auth.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hacklytics25-default-rtdb.firebaseio.com'
})
ref = db.reference()


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
    uid = session['uid']
    users_ref = ref.child("users")
    snapshot = users_ref.order_by_key().equal_to(uid).get()
    print(snapshot)
    if len(snapshot.keys()) != 0:
        session['results'] = [snapshot[uid]["best_bank"], snapshot[uid]["prob"]]
        print(session["results"])
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
    session.pop('results', None)
    return redirect('login')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == "GET":
        best_bank = session["results"][0]
        prob = session["results"][1]
    if request.method == "POST":
        employment_sector = "N/A"
        loan_amt = float(request.form.get("loan_amount"))
        fico = float(request.form.get("fico"))
        employment = int(request.form.get("employment"))
        if employment != 3:
            employment_sector = str(request.form.get("employment_sec"))
        monthly_gross_income = float(request.form.get("monthly_gross_income"))
        monthly_housing_payment = float(request.form.get("monthly_housing_payment"))
        bankrupt_foreclosed = int(request.form.get("bankrupt_foreclosed"))
        user_dict = {
            'loan': loan_amt,
            'income': monthly_gross_income,
            'housing': monthly_housing_payment,
            'fico': fico
        }
        best_bank, prob = find_best_bank(user_dict, employment)
        uid = session['uid']
        users_ref = ref.child('users')
        employment_statuses = ["Full Time", "Part Time", "Unemployed"]
        bankrupcy_statuses = ["No", "Yes"]
        snapshot = users_ref.order_by_key().equal_to(uid).get()
        session['results'] = [best_bank, prob]
        if len(snapshot.keys()) != 0:
            users_ref.child(uid).update({ "best_bank" : best_bank, "prob" : prob, "loan_amt": loan_amt, "fico": fico, "employment": employment_statuses[employment - 1], "employment_sector": employment_sector, "monthly_gross_income": monthly_gross_income, "monthly_housing_payment": monthly_housing_payment, "bankrupt_foreclosed": bankrupcy_statuses[bankrupt_foreclosed]})
        else:
            users_ref.child(uid).set({ "best_bank" : best_bank, "prob" : prob, "loan_amt": loan_amt, "fico": fico, "employment": employment_statuses[employment - 1], "employment_sector": employment_sector, "monthly_gross_income": monthly_gross_income, "monthly_housing_payment": monthly_housing_payment, "bankrupt_foreclosed": bankrupcy_statuses[bankrupt_foreclosed]})
    return render_template('results.html', best_bank = best_bank, prob = prob)

@app.context_processor
def uid():
    if "uid" in session:
        
        return {"uid" : session["uid"]}
    else:
        return {"uid" : None}
    
@app.context_processor
def resultsget():
    if "results" in session:
        print("results", session["results"])
        return {"resultsget" : session["results"]}
    else:
        print("none")
        return {"resultsget" : None}


if __name__ == "__main__":
    app.run(debug=True)
