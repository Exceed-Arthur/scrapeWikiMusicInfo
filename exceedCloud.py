import random
import boto3
import cred
from boto3.dynamodb.conditions import Key


def addTitleToMusicDB(category: str, title: str):
    if len(title) > 1:
        dynamodb = boto3.resource('dynamodb',
                                  aws_access_key_id=cred.AWSAccessKeyId,
                                  aws_secret_access_key=cred.AWSSecretKey,
                                  region_name="us-east-2")
        table = dynamodb.Table("tableOfMusicNamingIdeas")
        try:
            response = table.put_item(
                Item={
                    'id': random.randrange(1111111, 9999999),
                    'category': category,
                    'title': title
                }
            )
            return response
        except:
            print(f"Failed to add {title} to {category}")