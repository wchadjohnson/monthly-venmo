
from dotenv import load_dotenv
from utils import get_env, env_vars


load_dotenv()

from venmo_api import Client
# Initialize api client using an access-token
client = Client(access_token=get_env('VENMO_ACCESS_TOKEN'))

payment_methods = client.payment.get_payment_methods()
for payment_method in payment_methods:
    print(payment_method.to_json())
