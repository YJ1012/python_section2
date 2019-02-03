import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8');
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8');
import pytube
import os
import subprocess

#from pytube import YouTube
urlAddr  = input("URL addr:");
yt = pytube.YouTube(urlAddr);
# yt = YouTube('https://www.youtube.com/watch?v=g12T0_OzLLs&t=75s')
videos = yt.streams.all();

for i in range(len(videos)) :
    print(i,' , ',videos[i])

cNum  = int(input("Download format:"));
downloadPath = "./youtube";

videos[cNum].download(downloadPath);

newFilename =input("MP3 file name :");
orgFilename =videos[cNum].default_filename;

subprocess.call(['./youtube/ffmpeg','-i',
    os.path.join(downloadPath,orgFilename),
    os.path.join(downloadPath,newFilename)]
)

print("File changed fomr ORG to NEW");
