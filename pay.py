from venmo_api import Client
from dotenv import load_dotenv
#from notifiers import get_notifier
from datetime import datetime

from utils import get_env, env_vars, Venmo, Telegram

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env.
#  actualVars = []
#  for var in env_vars:
#    actualVars.append(get_env(var))

  access_token=get_env('VENMO_ACCESS_TOKEN')
  k_friend_id=get_env('K_FRIEND_ID')
  venmo_fund_source=get_env('VENMO_FUND_SOURCE')
 
  #month = get_month(now)
  venmo = Client(access_token=access_token)
  #telegram = Telegram(bot_token, chat_id)

  venmo.payment.send_money(amount=1.00, note='Test', target_user_id=k_friend_id, funding_source_id=venmo_fund_source)

#  if success:
#    print("✅ Ran Vemo Pay script successfully")
#  else:
#    print("❌ Something in Venmo Pay script went wrong")

now = datetime.now()
main(now)
#telegram.send_message(message)