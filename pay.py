from venmo_api import Client
from dotenv import load_dotenv
#from notifiers import get_notifier
from datetime import datetime

from utils import get_env

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env.

  access_token=get_env('VENMO_ACCESS_TOKEN')
  k_friend_id=get_env('K_FRIEND_ID')
  venmo_fund_source=get_env('VENMO_FUND_SOURCE')
 
  #month = get_month(now)
  venmo = Client(access_token=access_token)
  #telegram = Telegram(bot_token, chat_id)

  venmo.payment.send_money(amount=160.00, note='Lawn Care Services - 4 cuts', target_user_id=k_friend_id, funding_source_id=venmo_fund_source)

#  if success:
#    print("✅ Ran Vemo Pay script successfully")
#  else:
#    print("❌ Something in Venmo Pay script went wrong")

now = datetime.now()
main(now)
