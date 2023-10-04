from googleapiclient.discovery import build
import os
import json
class Channel:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.json_: dict = self.convert_youtube_json()
        self.json_item: dict = self.json_['items'][0]

        self.title: str = self.json_item['snippet'] ['title']
        self.description: str = self.json_item['snippet'] ['description']
        self.url: str = f'https://www.youtube.com/{self.json_item["snippet"]["customUrl"]}'
        self.subscribers_count = int(self.json_item['statistics']['subscriberCount'])
        self.video_count = int(self.json_item['statistics']['videoCount'])
        self.view_count = int(self.json_item['statistics']['viewCount'])

    def print_info(self):
        dict_to_print = self.get_service().channels().list(id=self.channel_id, part='snippet, statistics').execute()
        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)

    def convert_youtube_json(self):
        converting = json.dumps(self.get_service().channels().list(id=self.channel_id, part='snippet, statistics').execute())
        return json.loads(converting)

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, filename):
        dictionary = {
            'id_канала': self.channel_id,
            'название_канала': self.title,
            'описание_канала': self.description,
            'ссылка_на_канал': self.url,
            'количество_подписчиков': self.subscribers_count,
            'количество_видео': self.video_count,
            'общее_количество_просмотров': self.view_count
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dictionary, f, indent=2, ensure_ascii=False)



