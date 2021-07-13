import sys
from __main__ import YouTube

vid_link=str(sys.argv[1])
yt =YouTube(vid_link)
video = yt.streams.filter(only_audio=True).first()
video.download()
#ytmd.Downloader(sys.argv[1]);
#print(sys.argv[1]); 
