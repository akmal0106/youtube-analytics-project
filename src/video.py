from googleapiclient.discovery import build
import os
import json

class Video:
    YT_API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
    def __init__(self, video_id: str):
        self.video_id = video_id
        self.json_: dict = self.convert_youtube_json()
        self.json_item: dict = self.json_['items'][0]

        self.title = self.json_item['snippet']['title']
        self.view_count = self.json_item['statistics']['viewCount']
        self.like_count = self.json_item['statistics']['likeCount']

    def __str__(self):
        return self.title

    @classmethod
    def get_service(cls):
        return cls.youtube

    def print_info(self):
        video_response = self.youtube.videos().list(part='snippet, statistics, contentDetails, topicDetails', id=self.video_id).execute()
        return json.dumps(video_response, indent=2, ensure_ascii=False)

    def convert_youtube_json(self):
        return json.loads(self.print_info())

class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id: str = playlist_id
