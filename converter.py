import os
from moviepy.editor import VideoFileClip

path_folder = "D:\Musicas\Music_for_download"
mp3_path = "D:\Musicas\Music_for_download\Spotify_Local"

def make_conversions():

    for file in os.listdir(path_folder):
        if file.endswith('.mp4'):
            complete_path = os.path.join(path_folder,file)

            video_clip = VideoFileClip(complete_path)

            mp3_file = os.path.splitext(file)[0] + '.mp3'
            output_path = os.path.join(mp3_path, mp3_file)

            video_clip.audio.write_audiofile(output_path)
            
            video_clip.close()
            print("--Complete file conversion--")

