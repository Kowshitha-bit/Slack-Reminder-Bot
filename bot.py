import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#general")

def send_reminder(message):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "channel": SLACK_CHANNEL,
        "text": message
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 and response.json().get("ok"):
        print("✅ Reminder sent successfully!")
    else:
        print("❌ Failed to send reminder:", response.text)

if __name__ == "__main__":
    send_reminder("🔔 This is your scheduled reminder!")
