import urequests as requests

class CloudFlare:
    def __init__(self, API_KEY, ACCOUNT_EMAIL):
        self.CLOUDCLARE_API_ENDPOINT='https://api.cloudflare.com/client/v4/'
        self.API_KEY = API_KEY
        self.ACCOUNT_EMAIL = ACCOUNT_EMAIL

    def send_request(self, method, path, data):
        headers = {
            'X-Auth-Email': self.ACCOUNT_EMAIL,
            'X-Auth-Key': self.API_KEY
        }
        res = requests.request(
            method,
            self.CLOUDCLARE_API_ENDPOINT + path,
            None,
            data,
            headers,
            None
        )
        return res if res is None else res.json()

    def get_zone_identifier(self, domain):
        res = self.send_request('GET', 'zones?name=' + domain, {})
        return res if res is None else res['result'][0]['id']

    def get_record_identifier(self, zone_identifier, record_name):
        response = self.send_request('GET', 'zones/' + zone_identifier + '/dns_records?name=' + record_name, {})
        if response is None:
            return None
        return {
           'id': response['result'][0]['id'],
           'ip': response['result'][0]['content']
        }

    def update_dns_record(self, zone_identifier, record_identifier, record_name, ip):
        data = {
            'type': 'A',
            'name': record_name,
            'content': ip
        }
        res = self.send_request('PUT', 'zones/' + zone_identifier + '/dns_records/' + record_identifier, data)
        return False if res is None else res['success']
