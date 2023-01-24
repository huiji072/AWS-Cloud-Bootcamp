from slacker import Slacker
from datetime import datetime

token = 'xoxb-4577538761255-4666924670823-P9gcxT45qFeM97r3vA4WSivp'



def send_slack_message(msg, error=''):
    full_msg = msg
    if error:
        full_msg = msg + '\n에러 내용:\n' + str(error)
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
    slack = Slacker(token)
    slack.chat.post_message('#seek', today + full_msg, as_user=True)

if __name__ == "__main__":
    # 일부러 에러가 발생하도록 함.
    try:
        a = 1/0
    except Exception as e:
        send_slack_message('테스트', e)