from venmo_api import Client
from dotenv import load_dotenv
from utils import get_env, env_vars

load_dotenv()

# Get your access token. You will need to complete the 2FA process
# Please store it somewhere safe and use it next time
# Never commit your credentials or token to a git repository
access_token = Client.get_access_token(username=get_env('TOKEN_USER'),
                                        password=get_env('TOKEN_PWD'))
print("My token:", access_token)

