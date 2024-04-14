from venmo_api import Client

# Get your access token. You will need to complete the 2FA process
# Please store it somewhere safe and use it next time
# Never commit your credentials or token to a git repository
access_token = Client.get_access_token(username='wchadjohnson@gmail.com',
                                        password='meqzyk-xiprom-rugbU7')
print("My token:", access_token)

