# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

from flask import Flask, render_template, url_for
from flask import request
import models as dbHandler
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')
    
@app.route("/login")
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('./login.html', users=users)
    else:
        return render_template('./login.html')
    
@app.route('/order')
def order():
    return render_template('./order.html')
    
@app.route('/manager')
def manager():
    return render_template('./manager.html')
    
@app.route("/robots.txt")
def robots():
    return render_template('./robots.txt')
    
'''This has to be removed after fixes.'''
'''
@app.route("/dev/login")
def login_temp():
    return render_template('./dev/login.html')
'''
    
@app.route('/dev/login', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('./dev/login.html', users=users)
    else:
        return render_template('./dev/login.html')
    
@app.route("/dev/static/main.css")
def css():
    return render_template('./dev/static/main.css')

if __name__ == '__main__':
    app.run(debug=False, host= '0.0.0.0')