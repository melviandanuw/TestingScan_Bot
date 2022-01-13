import os
import telebot
import requests


#nama bot nya @TestingScanner_Bot

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['start'])
def start(message):
  new_user_name = message.from_user.username
  bot.send_message(message.chat.id, "Welcome, {0}! \n\nPlease enter the address you want to check..".format(new_user_name))

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

@bot.message_handler(commands=['help'])
def help(message):
  bot.reply_to(message, "All Commands: \n\n1. /start\nReboot bot from the beginning\n2. /bsc\nBSC Scan website address.")
  
@bot.message_handler(commands=['bsc'])
def bsc_website(message):
  bot.reply_to(message, "https://bscscan.com/")

@bot.message_handler(func=lambda message: True)
def address_finder(message):
  try: 
    cid = message.chat.id
    mid = message.message_id 
    message_text = message.text 
    user_id = message.from_user.id 
    user_name = message.from_user.first_name
  
    URL = "https://api.pancakeswap.info/api/v2/tokens/" + message_text
    r = requests.get(url = URL)
    data = r.json()
    coin = data["data"]["name"]
    price = data["data"]["price"]
    price_bnb = data["data"]["price_BNB"]
    print_message = "Name: " +  coin  + "\nPrice Per USD: " + price + "\nPrice Per BNB: "+ price_bnb
    bot.reply_to(message, text = print_message)
  except:
    bot.reply_to(message, "Address not found, please enter correct address.")

bot.polling()