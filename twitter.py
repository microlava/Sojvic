import tweepy
import requests
import time

# Twitter API credentials
API_KEY = 'MXhjPRahnl7GDcTXond86GwXs'
API_SECRET_KEY = 'NULAhzFA9heROMUTMfV8bktcttubbuX3Q5A5N1i0m1NOKQXm8D'
ACCESS_TOKEN = '1650520281763524609-d2zb3MxqNw4M17G05jhSqM1alPkxVC'
ACCESS_TOKEN_SECRET = 'SZWJm9rO6HbwaKAY1YIs21lxrwaErrumz412IzhUnhhCd'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPHHvgEAAAAASDZEPJXkhSRXLSSmvu4qlzX%2BSgA%3D6CMcceRf88dQXRXTpkGyrtOqwBNmK5Hp0BS0xXuVYGdLQ9bwkm'  # You need to generate a Bearer Token for this

# Pushover credentials
PUSHOVER_USER_KEY = 'uraihpd9h4q49e7ytjpykq1kxgi7rz'
PUSHOVER_API_TOKEN = 'ai9whb6t1eq2b4cd88mvzmzy151c43'

# Function to send a notification using Pushover
def notify(message):
    payload = {
        'token': PUSHOVER_API_TOKEN,
        'user': PUSHOVER_USER_KEY,
        'message': message
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification: {response.text}")

# Define a class to handle the streaming data
class MyStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if "bot developer" in tweet.text.lower():
            tweet_message = f"New tweet from @{tweet.author_id}: {tweet.text}"
            print(tweet_message)  # Optional: Print to console
            notify(tweet_message)  # Send notification

    def on_error(self, status_code):
        print(f"Error detected: {status_code}")
        return False  # Returning False disconnects the stream

# Initialize the streaming client
stream_listener = MyStreamListener(bearer_token=BEARER_TOKEN)

# Add rules to the stream
rule = tweepy.StreamRule(value="bot developer")
stream_listener.add_rules(rule)

# Start the stream
stream_listener.filter(expansions="author_id")

# Keep the script running
while True:
    time.sleep(1)