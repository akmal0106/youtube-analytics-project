from src.APIMixin import APIMixin
from googleapiclient.discovery import build
import os
import json
class Channel(APIMixin):
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

    def __str__(self):
        return f"'{self.title} ({self.url})'"

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscribers_count + other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count + other
        raise NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscribers_count - other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count - other
        raise NotImplemented

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        if isinstance(other, Channel):
            return self.subscribers_count * other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count * other
        raise NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Channel):
            return self.subscribers_count / other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count / other
        raise NotImplemented

    def __rtruediv__(self, other):
        return self / other

    def __gt__(self, other):
        if isinstance(other, Channel):
                return self.subscribers_count > other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count > other
        raise NotImplemented

    def __ge__(self, other):
        if isinstance(other, Channel):
                return self.subscribers_count >= other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count >= other
        raise NotImplemented

    def __lt__(self, other):
        if isinstance(other, Channel):
                return self.subscribers_count < other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count < other
        raise NotImplemented

    def __le__(self, other):
        if isinstance(other, Channel):
                return self.subscribers_count <= other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count <= other
        raise NotImplemented

    def __eq__(self, other):
        if isinstance(other, Channel):
                return self.subscribers_count == other.subscribers_count
        if isinstance(other, (int, float)):
            return self.subscribers_count == other
        raise NotImplemented
    def print_info(self):
        dict_to_print = self.get_service().channels().list(id=self.channel_id, part='snippet, statistics').execute()
        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)

    def convert_youtube_json(self):
        converting = json.dumps(self.get_service().channels().list(id=self.channel_id, part='snippet, statistics').execute())
        return json.loads(converting)

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