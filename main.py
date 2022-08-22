import googleapiclient.discovery

CHANNEL_NAME = 'myrusakov'
KEY = 'AIzaSyBs3Q8GXG7TzobVoZxpRrtHbizlY05A3zg'

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=KEY)


def get_video_ids_from_channel(channel_name):
    playlist_id = get_playlist_id(channel_name)
    response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=10
    ).execute()
    ids = []
    for video in response['items']:
        ids.append(video['snippet']['resourceId']['videoId'])
    return ids


def get_playlist_id(channel_name):
    response = youtube.channels().list(
        part="contentDetails",
        forUsername=channel_name
    ).execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


def print_videos_info(videos):
    response = youtube.videos().list(
        part="statistics, snippet",
        id=','.join(videos)
    ).execute()
    for video in response['items']:
        print('Название: {}'.format(video['snippet']['title']))
        print('Просмотров: {}'.format(video['statistics']['viewCount']))
        print('Лайков: {}'.format(video['statistics']['likeCount']))
        print('-------------------------------------------------------')


if __name__ == '__main__':
    videos = get_video_ids_from_channel(CHANNEL_NAME)
    print_videos_info(videos)
