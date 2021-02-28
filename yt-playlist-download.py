import os
import subprocess

from pytube import Playlist, YouTube

def downloadYTPlaylist():
    pl_url = input("Playlist URL: ")
    pl = Playlist(pl_url)
    
    for video_url in pl.video_urls:
        try:
            yt = YouTube(video_url)
            video = yt.streams.first()
            videoFileName = video.default_filename
            
            if not os.path.exists(videoFileName):
                print("Downloading " + videoFileName + "...")
                video.download("videos")
        except:
            print("Something went wrong with video " + videoFileName)
            continue
        
        print("Converting to mp3....")
        musicFileName = videoFileName[0:-3] + "mp3"
        subprocess.run(['./ffmpeg.exe', '-i',
            os.path.join("videos", videoFileName),
            os.path.join("music", musicFileName)
        ])
        
    print("Download finished.")

if __name__ == "__main__":
    downloadYTPlaylist()
