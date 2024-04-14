
from dotenv import load_dotenv
from utils import get_env, env_vars


load_dotenv()

from venmo_api import Client
# Initialize api client using an access-token
client = Client(access_token=get_env('VENMO_ACCESS_TOKEN'))
# Search for users. You get a maximum of 50 results per request.
user = client.user.get_user_by_username(username=get_env('K_USER_NAME'))

print(user.id)
