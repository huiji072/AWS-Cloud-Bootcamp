from http import client
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
 
# ID of the channel you want to send the message to
channel_id = "C04LDTQP6BT"
 
try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text="Hello world"
    )
 
except SlackApiError as e:
    print(f"Error posting message: {e}")