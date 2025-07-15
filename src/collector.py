from telethon.sync import TelegramClient
from pathlib import Path
from datetime import datetime
import json

# Replace these with your actual credentials
api_id = 23969142
api_hash = "63cfef12e419c6f4a413724fccd8dda9"

client = TelegramClient('session', api_id, api_hash)

async def collect_From_channes(channel_username):
    await client.start()
    print(f"📥 Scraping messages from {channel_username}...")

    all_data = []

    try:
        async for msg in client.iter_messages(channel_username):
            if msg.text:
                all_data.append({
                    "id": msg.id,
                    "date": msg.date.strftime("%Y-%m-%d %H:%M:%S"),
                    "text": msg.text
                })

        print(f"✅ Scraped {len(all_data)} messages.")

        if not all_data:
            print("⚠️ No messages found — nothing to save.")
            return

        folder = Path("/home/samrawit/telegram-data-pipeline/data/raw") / datetime.now().strftime("%Y-%m-%d")
        folder.mkdir(parents=True, exist_ok=True)
        out_file = folder / f"{channel_username}.json"

        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved to {out_file}")

    except Exception as e:
        print(f"❌ Error while scraping or saving: {e}")

    finally:
        await client.disconnect()