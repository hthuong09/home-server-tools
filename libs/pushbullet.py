import urequests as requests

class PushBullet:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.API_ENDPOINT = 'https://api.pushbullet.com/v2/'

    def send_request(self, method, path, json=None):
        headers = {
            'Access-Token': self.API_KEY,
            'Content-Type': 'application/json'
        }
        res = requests.request(
            method,
            self.API_ENDPOINT + path,
            None,
            json,
            headers,
            None
        )
        return res

    def push(self, type, title, body, channel_tag=None):
        data = {
            'type': type,
            'title': title,
            'body': body,
            'channel_tag': channel_tag
        }
        self.send_request('POST', 'pushes', data)

