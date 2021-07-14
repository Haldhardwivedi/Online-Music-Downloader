import sys
from  pytube import YouTube
import os

try:
    vid_link=str(sys.argv[1])
    yt =YouTube(vid_link)
    video = yt.streams.filter(only_audio=True).first()
    out_file=video.download()
    os.rename(out_file,"new.mp4") 
except: 
    print("Some Error!") 
#ytmd.Downloader(sys.argv[1]);
#print(sys.argv[1]); 
