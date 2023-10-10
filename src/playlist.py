from src.APIMixin import APIMixin
from googleapiclient.discovery import build
import os
import json
from datetime import timedelta
import isodate

class PlayList(APIMixin):
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        title = self.get_service().playlists().list(id=playlist_id, part='snippet').execute()
        self.title = title['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"


    @property
    def total_duration(self) -> timedelta:
        playlist_video = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                           part='contentDetails',
                                                           maxResults=50,
                                                           ).execute()
        video_id = []
        for video in playlist_video['items']:
            videos = video['contentDetails']['videoId']
            video_id.append(videos)

        video_response = self.get_service().videos().list(id=','.join(video_id), part='contentDetails, statistics').execute()

        total_time = timedelta()
        for video in video_response['items']:
            iso = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso)
            total_time += duration

        return total_time

    def show_best_video(self):
        playlist_video = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                           part='contentDetails, snippet',
                                                           maxResults=50,
                                                           ).execute()
        video_id = []
        for video in playlist_video['items']:
            video_id.append(video['contentDetails']['videoId'])

        video_response = self.get_service().videos().list(id=','.join(video_id),
                                                    part='statistics',
                                                    ).execute()
        video_likes = [(video['id'], int(video['statistics']['likeCount'])) for video in video_response['items']]
        best_video, _ = max(video_likes, key=lambda x: x[1])
        return f'https://youtu.be/{best_video}'
