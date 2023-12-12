import os
from dotenv import load_dotenv


load_dotenv()

ACCOUNT_ID = os.getenv('ACCOUNT_ID')
APPLICATION_NAME = os.getenv('APPLICATION_NAME')
ASSUME_ROLE = os.getenv('ASSUME_ROLE')
AWS_DEFAULT_PROFILE = os.getenv('AWS_DEFAULT_PROFILE')
AWS_EB_PROFILE = os.getenv('AWS_EB_PROFILE')
AWS_PROFILE = os.getenv('AWS_PROFILE')
AWS_REGION = os.getenv('AWS_REGION')
USE_ORG_FOR_ACCOUNT_LIST = os.getenv('USE_ORG_FOR_ACCOUNT_LIST')

def main():
    from .dependencyChecker import lambda_handler
    lambda_handler(None, None)
