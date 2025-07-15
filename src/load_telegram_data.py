import psycopg2
import json
from pathlib import Path
from datetime import datetime

# PostgreSQL connection parameters
conn_params = {
    "host": "localhost",
    "port": 5432,
    "dbname": "telegram_db",
    "user": "samrawit",
    "password": "Sam123"
}

def load_json_to_db(json_path):
    # Load JSON file
    with open(json_path, "r", encoding="utf-8") as f:
        messages = json.load(f)

    # Connect to DB
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO raw.telegram_messages (id, channel_username, text, date, media_path)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """

    for msg in messages:
        try:
            msg_id = msg.get("id")
            channel = msg.get("channel_username") or "unknown"
            text = msg.get("text") or ""
            date_str = msg.get("date")
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S") if date_str else None
            media = msg.get("media_path")

            cur.execute(insert_query, (msg_id, channel, text, date, media))

        except Exception as e:
            print(f"Error inserting message {msg.get('id')}: {e}")

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Loaded {len(messages)} messages from {json_path}")

def load_all_json_in_folder(folder_path):
    folder = Path(folder_path)
    for json_file in folder.glob("*.json"):
        load_json_to_db(json_file)

if __name__ == "__main__":
    load_all_json_in_folder("/home/samrawit/telegram-data-pipeline/data/raw/2025-07-15")
