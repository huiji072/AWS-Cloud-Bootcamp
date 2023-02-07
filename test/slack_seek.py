import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# slack_token = 'xoxb-4577538761255-4719521882436-rSb4mFoN9M2h5VbxsetSBCly' # Bot OAuth Token
# client = WebClient(token=slack_token)
client.chat_postMessage(
    channel="C04LDTQP6BT", # Channel ID

        
    text="Hello from your app! :tada:"
    )