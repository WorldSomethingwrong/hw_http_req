from pprint import pp, pprint
import requests

token = ''

class YaUploader:
    host = 'https://cloud-api.yandex.net:443'
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {"path": path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json().get('href')

    def upload(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    uploader = YaUploader(token)
    uploader.upload('/test.txt', 'test.txt')
