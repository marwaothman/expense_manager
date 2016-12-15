from flask import Flask, redirect, render_template, request, url_for, flash, session
from db import db

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/logina', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        value = db.authenticate(
            request.form['username'],
            request.form['password'])
        if (value == 1):
            print "login Succesfully"
            session['name'] = request.form['username']
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password \
            Please try again!'
            return render_template('login.html', error=error, session=session)
    return render_template('login.html')


@app.route('/reg?is%2')
def registration():
    return render_template('registration.html')


@app.route("/registform", methods=['POST'])
def register():
    data = db.user_alreadyexits(request.form['field3'],
                                request.form['field1'],
                                request.form['field2'],
                                request.form['field4'])
    if (data == 1):
        flash('ERROR! PLEASE ENTER SOMETHING OR CHECK YOUR USER')
        return redirect(url_for('registration'))
    print data
    flash('You were successfull')
    return redirect(url_for('registration'))


@app.route('/login')
def index():
    return render_template('index.html', session=session)


@app.route('/future')
def future():
    return render_template('upcoming.html')


@app.route('/logina')
def logina():
    return render_template('login.html')


@app.route('/add')
def add():
    return render_template('add_catagories.html')


@app.route('/clearsession')
def clearsession():
    session.clear()
    return redirect(url_for('logina'))


@app.route("/catagory", methods=['POST'])
def catagory():
    data_catagory = db.catagory_alreadyexits(session['name'],
                                             request.form['field7'],
                                             request.form['field8'],
                                             request.form['field9'])
    if (data_catagory == 1):
        flash('ERROR! CATAGORY ALREADY SATISFIED OR SOMETHING WENT WRONG PLEASE CHECK NEXT MESSAGE TO CONFIRM')
    else:
        flash(data_catagory)
        return redirect(url_for('add'))
    flash('REQUEST PERFORMED!')
    return redirect('add')


if __name__ == '__main__':
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=int("80")
    )