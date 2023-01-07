import boto3
import cred
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask import (Blueprint, current_app, flash, jsonify, redirect, request,
                   url_for)

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

orderedTicketArray = []
email = ''
password1 = ''
password2 = ''
six_digit_code = ''
iTovenUserTable = "itoven_nottauserbase"
iTovenTableUsers = iTovenUserTable
iTovenNamingTable = "tableOfMusicNamingIdeas"

auth = Blueprint('auth', __name__)
