import os 

folder = "D:\Musicas\Music_for_download"

def delete():
    for file in os.listdir(folder):

        if file.endswith('.mp4'):
            full_path = os.path.join(folder,file)

            os.remove(full_path)