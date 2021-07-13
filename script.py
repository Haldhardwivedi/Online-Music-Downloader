import sys
from  pytube import YouTube

SAVE_PATH ="/home/haldhar/Downloads/"

try:
    vid_link=str(sys.argv[1])
    yt =YouTube(vid_link)
    video = yt.streams.filter(only_audio=True).first()
    video.download() 
except: 
    print("Some Error!") 
#ytmd.Downloader(sys.argv[1]);
#print(sys.argv[1]); 
