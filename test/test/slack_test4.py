# import logging
# # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
 
# def execute():  # 슬랙 DM 보내기
#     logger = logging.getLogger()
#     # WebClient insantiates a client that can call API methods
#     # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
#     client = WebClient(token='xoxb-4577538761255-4666924670823-P9gcxT45qFeM97r3vA4WSivp')   # 봇 토큰, 개인에 맞게 설정
#     # ID of the channel you want to send the message to
#     channel_id = "C04LDTQP6BT"    #채널 ID 입력
 
#     # conversations.members (발송 대상 user id 가져오기)
#     try:
#         result_cvs = client.conversations_members(
#             channel=channel_id,  # USER ID 가져오기
#             limit=1000
#         )
#     except SlackApiError as e:
#         logger.error(f"Error getting channel members: {e}")
#         print("error---------------------------------------------")
 
#     cnt = len(result_cvs['members'])     # 발송 대상 수
#     # chat.postMessage
#     try:
#         # Call the chat.postMessage method using the WebClient
#         for i in range(cnt):
#             print(i, end = ' ')
#             result_chat = client.chat_postMessage(
#             channel=result_cvs['members'][i],   # USER ID를 이용하여 발송
#                 blocks = [
#                 {
#                     "type": "section",
#                     "text": {
#                         "type": "mrkdwn",
#                         "text": "메시지 작성"
#                     }
#                 },
#                 {
#                     "type": "actions",
#                     "block_id": "actionblock789",
#                     "elements": [
#                         {
#                             "type": "button",
#                             "text": {
#                                 "type": "plain_text",
#                                 "text": "링크1"
#                             },
#                             "url": "https://"
#                         },
#                         {
#                             "type": "button",
#                             "text": {
#                                 "type": "plain_text",
#                                 "text": "링크2"
#                             },
#                             "style": "primary",
#                             "value": "click_me_456",
#                             "url": "https"
#                         }
#                     ]
#                 }
#             ]
#             )
#             logger.info(result_chat)
 
#     except SlackApiError as e:
#         logger.error(f"Error posting message: {e}")
 
# if __name__ == '__main__':
#     execute()
