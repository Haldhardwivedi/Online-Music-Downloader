import sys
from  pytube import YouTube

SAVE_PATH ="/home/"

vid_link=str(sys.argv[1])
yt =YouTube(vid_link)
video = yt.streams.filter(only_audio=True).first()
try:
    video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
#ytmd.Downloader(sys.argv[1]);
#print(sys.argv[1]); 
