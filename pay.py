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
  VENMO_PAY_USERNAME=get_env('VENMO_PAY_USERNAME')
  venmo_fund_source=get_env('VENMO_FUND_SOURCE')
  pay_amount=float(get_env('PAY_AMOUNT'))
  pay_note=get_env('PAY_NOTE')
 
  #month = get_month(now)
  venmo = Client(access_token=access_token)
  #telegram = Telegram(bot_token, chat_id)

  user = venmo.user.get_user_by_username(VENMO_PAY_USERNAME)
  venmo.payment.send_money(amount=pay_amount, note=pay_note, target_user=user, funding_source_id=venmo_fund_source)

#  if success:
#    print("✅ Ran Vemo Pay script successfully")
#  else:
#    print("❌ Something in Venmo Pay script went wrong")

now = datetime.now()
main(now)
