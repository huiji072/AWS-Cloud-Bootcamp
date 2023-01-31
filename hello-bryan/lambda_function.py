import json

import requests


def lambda_handler(event, context):
    url = 'https://jsonplaceholder.typicode.com/albums'
    response = requests.get(url)
    status_code = response.status_code
    body = response.reason
    if status_code == 200:

        album_list = json.loads(response.content)
        body = f'album count = {len(album_list)}'

        if 'album_id' in event:
            album = next(filter(lambda x: x['id'] == event['album_id'], album_list), None)
            body = album if album else f'not found album id : {event["album_id"]}'

    return {
        'statusCode': status_code,
        'body': json.dumps(body)
    }
