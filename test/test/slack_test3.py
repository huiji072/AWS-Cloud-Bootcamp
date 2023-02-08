import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = 'xoxb-4577538761255-4666924670823-P9gcxT45qFeM97r3vA4WSivp' # Bot OAuth Token
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="C04LDTQP6BT", # Channel ID
        text="Hello from your app! :tada:"
    )
except SlackApiError as e:
    assert e.response["error"]