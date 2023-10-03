from googleapiclient.discovery import build
import os
import json
class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def get_service(self):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def print_info(self):
        dict_to_print = self.get_service().channels().list(id=self.channel_id, part='snippet, statistics').execute()
        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)
