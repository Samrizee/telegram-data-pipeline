from dotenv import load_dotenv
import os

load_dotenv()

print("Telegram Bot Starting...")
telegram_api_key = os.getenv("TELEGRAM_API_KEY")
print(f"Loaded API Key: {telegram_api_key}")