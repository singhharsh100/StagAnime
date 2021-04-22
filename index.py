from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')


@app.route('/latest.html')
def latest():
    return render_template('latest.html')


@app.route('/contactus.html')
def contactus():
    return render_template('contactus.html')


@app.route('/1pep.html')
def peps():
    return render_template('1pep.html')


@app.route('/dbsep1.html')
def dbsep():
    return render_template('dbsep1.html')


@app.route('/haep1.html')
def haep():
    return render_template('haep1.html')


@app.route('/narutoep1.html')
def narutoep():
    return render_template('narutoep1.html')


@app.route('/tgep1.html')
def tgep():
    return render_template('tgep1.html')


@app.route('/dnep1.html')
def dnep():
    return render_template('dnep1.html')


@app.route('/login.html')
def logings():
    return render_template('login.html')


@app.route('/submit_frm', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin@gmail.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('homepage.html')
    return render_template('login.html')