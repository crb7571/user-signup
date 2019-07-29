from flask import Flask, render_template, request, redirect, url_for
import re
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/signup')
def index():
    return render_template('signup.html')

def empty_chr(x):
    if x:
        return True
    else:
        return False

def chr_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

@app.route('/signup', methods=['POST'])

def is_valid():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    invalid_username = ''
    invalid_password = ''
    invalid_verify = ''
    invalid_email = ''

    if not chr_length(username):
        invalid_username = 'Invalid length. 3 - 20 characters please'
        username = ''
        password = ''
        verify = ''
    else:
        if " " in username:
            invalid_username = 'Invalid characters. No spaces please'
            username = ''
            password = ''
            verify = ''

    if not chr_length(password):
        invalid_password = 'Invalid length. 3 - 20 characters please'
        password = ''
        verify = ''
    else:
        if " " in password:
            invalid_password = 'Invalid characters. No spaces please'
            password = ''
            verify = ''


    if verify != password:
        invalid_verify = 'Passwords do not match'
        password = ''
        verify = ''
    
    match = re.search("[@.]", email)
    string = ""
    if empty_chr(email):
        if not chr_length(email):
            invalid_email = 'This is not a valid e-mail address'
            email = ''
            password = ''
            verify = ''
        else:
            if not match:
                invalid_email = 'This is not a valid e-mail address'
                email = ''
                password = ''
                verify = ''
            else:
                if not empty_chr(email):
                    invalid_email = 'This is not a valid e-mail address'
                    email = ''
                    password = ''
                    verify = ''
                else:
                    if " " in email:
                        invalid_email = 'This is not a valid e-mail address'
                        email = ''
                        password = ''
                        verify = ''

    if not invalid_username and not invalid_password and not invalid_verify and not invalid_email:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', invalid_username=invalid_username, 
            invalid_password=invalid_password, 
            invalid_verify=invalid_verify, 
            invalid_email=invalid_email)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()