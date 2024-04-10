import playlist 
from pytube import YouTube
import pandas as pd
from pytube.exceptions import AgeRestrictedError
import dotenv
import os

# API KEY
dotenv.load_dotenv(dotenv.find_dotenv())
api_key = os.getenv("API_KEY")

# Playlist -> Music for Download
playlist_id = 'PLqlojiaFQyHHp6mtsK_-0oEbvw52-oDrY'


videos = playlist.get_playlist_videos(api_key, playlist_id)
print("videos IDs:", videos)

df_previous = pd.read_excel('videos_history.xlsx')
df = pd.DataFrame(videos, columns=['Video_ID'])

# Download musics 
new_videos = videos[len(df_previous):]

for i in new_videos:
    print(f"Downloaded {i}")
    try:
        YouTube(f'https://www.youtube.com/watch?v={i}').streams.first().download(output_path = "D:\Musicas\Music_for_download")
    except AgeRestrictedError:
        print(i)
        pass

df.to_excel('videos_history.xlsx', index=False)

print("Completed")




