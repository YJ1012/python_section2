import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8');
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8');

print('hi');
print("하이");

imgUrl="https://ssl.pstatic.net/tveta/libs/1220/1220273/fbad517f3a3bcf975f80_20190109115650663.png"
videoUrl="https://tvetamovie.pstatic.net/libs/1224/1224339/1ab2d911cd59a312c329_20190110155122392.mp4-pBASE-v0-f71833-20190110155240101.mp4"
savePath1 = "./homework_img.jpg";
savePath2 = "./homework_vide.mp4";

dw.urlretrieve(imgUrl,savePath1);
dw.urlretrieve(videoUrl,savePath2);

print("다운로드완료");
