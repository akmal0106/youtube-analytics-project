import requests
import json


class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def get_channel_info(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?id={self.channel_id}&part=snippet,contentDetails,statistics&key=AIzaSyBNsbt4e1yy1uVY1GMZoUi31VSE3sSs108"
        response = requests.get(url)
        json_data = json.loads(response.text)
        return json.dumps(json_data, indent=2, ensure_ascii=False)

    def print_info(self):
        channel_info = self.get_channel_info()
        return channel_info
