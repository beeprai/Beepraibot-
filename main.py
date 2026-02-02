import os
from flask import Flask
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler

# Bot ko zinda rakhne ke liye chota server
app = Flask('')
@app.route('/')
def home(): return "Bot is Alive!"

def run(): app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    Thread(target=run).start()
    # Aapka token hum baad mein Render mein daalenge
    token = os.getenv("BOT_TOKEN")
    bot = ApplicationBuilder().token(token).build()
    bot.add_handler(CommandHandler('start', lambda u, c: u.message.reply_text("Bhai, main chalu ho gaya hoon!")))
    bot.run_polling()
  
