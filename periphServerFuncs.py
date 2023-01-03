import random
import time
import boto3
from boto3.dynamodb.conditions import Key
import flask
import os
import bricker
import cred
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import flask_login
from flask import Blueprint, render_template, request, flash, redirect, url_for
import server_funcs
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_login import login_user, login_required, logout_user, current_user
from random import randrange
import email_funcs
import UIFuncs

from flask import (Blueprint, current_app, flash, jsonify, redirect, request,
                   url_for)

from flask import current_app, flash, jsonify, make_response, redirect, request, url_for, render_template, \
    render_template_string
import json
session = boto3.Session(
    aws_access_key_id=cred.AWSAccessKeyId,
    aws_secret_access_key=cred.AWSSecretKey,
    region_name="us-east-2")
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=cred.AWSAccessKeyId,
                          aws_secret_access_key=cred.AWSSecretKey,
                          region_name="us-east-2")
table = dynamodb.Table("LotteryAIBased")
response = table.scan()
data = response['Items']
frontNotBack = True
streamlined = []
views = Blueprint('views', __name__)
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=cred.AWSAccessKeyId,
                          aws_secret_access_key=cred.AWSSecretKey,
                          region_name="us-east-2")
orderedTicketArray = []
email = ''
password1 = ''
password2 = ''
six_digit_code = ''
iTovenUserTable = "itoven_nottauserbase"
iTovenTableUsers = iTovenUserTable
iTovenNamingTable = "tableOfMusicNamingIdeas"
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=cred.AWSAccessKeyId,
                          aws_secret_access_key=cred.AWSSecretKey,
                          region_name="us-east-2")
views = Blueprint('views', __name__)
auth = Blueprint('auth', __name__)

