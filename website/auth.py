import flask_login
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import session as session2

import models
import server_funcs
from models import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_login import login_user, login_required, logout_user, current_user
from random import randrange
import email_funcs
import bricker
auth = Blueprint('auth', __name__)
email = ''
password1 = ''
password2 = ''
six_digit_code = ''


def lower(st:str):
    try:
        return st.lower()
    except:
        return False
    return False




@auth.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['submit-both'] == 'login':
            email = request.form.get('email')
            password = request.form.get('password')
            user = models.User(email=email, password=bricker.hashBrick(password))
            print(f"ATTEMPTING FRONT END LOGIN WITH {email}")
            if server_funcs.user_exists(email):
                print(f"ENTERED PASSWORD {password} and got {bricker.hashBrick(password)} to compare to {server_funcs.get_platypus(email)}")
                if bricker.hashBrick(password) == server_funcs.get_platypus(email):

                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    session2["CurrentUser"] = user
                    if "music-naming-tool" in request.query_string.decode(encoding="utf-8"):
                        print(f"ATTEMPTING TO REDIRECT TO MAIN APP FOR MUSIC NAMING TOOL")
                        print(f"CURRENT USER: {session2['CurrentUser']}")
                        return redirect(url_for('views.MusicNameGen', user=email))
                    return redirect(url_for('views.home'))
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Email does not exist.', category='error')
        elif request.form['submit-both'] == 'forgot':
            return redirect(url_for('auth.forgot'))
        elif request.form['submit-both'] == 'Sign Up':
            return redirect(url_for('auth.sign_up'))
    return render_template("login.html", user=current_user)


@auth.route('/Recover', methods=['GET', 'POST'])
def forgot():
    global email
    global password1
    global password2
    global six_digit_code
    if request.method == 'POST':
        if request.form['submit-both'] == 'submit-email':
            six_digit_code = []
            email = lower(request.form.get('email'))
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            if not server_funcs.user_exists(email):
                flash('Email does not exist on our system.', category='error')
            elif "@" in email and email.split("@")[1] in server_funcs.txt_file_to_listv2('/static/bad_emails.txt'):
                flash('Sneaky! We worked too hard on this project to allow disposable emails. Try a safer email provider.')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                for i in range(6):
                    six_digit_code.append(str(randrange(9)))
                six_digit_code = str(six_digit_code).replace("'", '')
                six_digit_code = six_digit_code.replace("]", '')
                six_digit_code = six_digit_code.replace("[", '')
                six_digit_code = six_digit_code.replace(" ", '')
                six_digit_code = six_digit_code.replace(",", "")
                print(six_digit_code)
                try:
                    email_funcs.itoven_send_html_verification(email,'Your code is here!',
                                                      six_digit_code)
                except:
                    flash("Try again. Server either didn't approve your email or is unresponsive.")
                flash(message='Great work! Please check your email for the confirmation code to continue. Please allow up to 3-5 minutes before requesting a new code.')
        if request.form['submit-both'] == 'submit-verification':
            print(f"test?{six_digit_code}")
            code_user = request.form.get('verification')
            if code_user == six_digit_code:
                server_funcs.changePlatypus(username=lower(flask_login.current_user.email), platypus=bricker.hashBrick(password1))
                flash('Password Updated!', category='success')
                return redirect(url_for('auth.login'))
            else:
                flash(
                    "Error. Invalid code. If you would, just refresh this page. We can start this process over no problem!")
    return render_template("recovery.html", user=current_user)


@auth.route('/Logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/Register', methods=['GET', 'POST'])
def sign_up():
    global email
    global password1
    global password2
    global six_digit_code
    if request.method == 'POST':
        if request.form['submit-both'] == 'submit-email':
            six_digit_code = []
            email = lower(request.form.get('email'))
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            user = User(email=email, password=password1)
            if user:
                flash('Email already exists.', category='error')
            elif "@" in email and email.split("@")[1] in server_funcs.txt_file_to_listv2('/static/bad_emails.txt'):
                flash('Sneaky! We worked too hard on this project to allow disposable emails. Try a safer email provider.')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                for i in range(6):
                    six_digit_code.append(str(randrange(9)))
                six_digit_code = str(six_digit_code).replace("'", '')
                six_digit_code = six_digit_code.replace("]", '')
                six_digit_code = six_digit_code.replace("[", '')
                six_digit_code = six_digit_code.replace(" ", '')
                six_digit_code = six_digit_code.replace(",", "")
                print(six_digit_code)
                try:
                    email_funcs.itoven_send_html_verification(email,'Your code is here!',
                                                      six_digit_code)
                except:
                    flash("Try again. Server either didn't approve your email or is unresponsive.")
                flash(message='Great work! Please check your email for the confirmation code to continue. Please allow up to 3-5 minutes before requesting a new code.')
        if request.form['submit-both'] == 'submit-verification':
            print(f"test?{six_digit_code}")
            code_user = request.form.get('verification')
            if code_user == six_digit_code:
                new_user = User(email=lower(email), password=bricker.hashBrick(password1))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                server_funcs.create_dyno_acct(username=lower(flask_login.current_user.email), platypus=bricker.hashBrick(password1))
                flash('Account created!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash(
                    "Error. Invalid code. If you would, just refresh this page. We can start this process over no problem!")
    return render_template("sign_up.html", user=current_user)
