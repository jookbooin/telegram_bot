import pytz
import telegram
import asyncio
import schedule
from datetime import datetime


token = "6674460309:AAHk4cAmNaQK2zaqRzqmp58kQntILUJTCzs"

bot = telegram.Bot(token=token)
public_chat_name = '@jookbooinch'


def job():
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return  

    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    id_channel = asyncio.get_event_loop().run_until_complete(bot.sendMessage(chat_id = public_chat_name ,
                        text=formatted_time))
    print(id_channel)
    print()

schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()