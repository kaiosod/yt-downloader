from googleapiclient.discovery import build

def get_playlist_videos(api_key, playlist_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    playlist_items = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        playlist_items.extend(response['items'])
        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    video_ids = [item['snippet']['resourceId']['videoId'] for item in playlist_items]
    return video_ids

