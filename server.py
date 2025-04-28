from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')  # Telegram bot token from BotFather
CHAT_ID = os.getenv('CHAT_ID')  # Your Telegram chat ID
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received data: {data}")
    
    message = f"📈 Trading Signal:

{data}"
    
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    requests.post(TELEGRAM_API_URL, data=payload)
    
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)