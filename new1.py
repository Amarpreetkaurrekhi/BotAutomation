import requests
from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')
raw_TS =datetime.now(IST)
curr_date = raw_TS.strftime("%d-%m-%Y")
curr_time=raw_TS.strftime("%H:%M:%S")
telegram_auth_token ="6142801697:AAGPPJfoOeVFEuHDF2ntw3F2uvTQ4Co8Nqc"
telegram_group_id = "MySunshine12345"
msg = f" Message received on {curr_date} at {curr_time}"
def send_msg_on_telegram(message):
    telegram_api_url = f"http://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    tel_resp = requests.get(telegram_api_url)
    if tel_resp.status_code ==200:
        print("INFO :Notification has been sent on Telegram")
    else:
        print("ERROR: Could not send Message")
send_msg_on_telegram(msg)

