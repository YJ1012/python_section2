import sys
import io
import urllib.request as dw
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8');
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8');

print('hi');
print("하이");

imgUrl="http://cafefiles.naver.net/20150404_41/onehodang2_1428121325007MWF8c_JPEG/10.jpg";
htmlURL="http://google.com";
savePath1 = "./test1_img.jpg";
savePath2 = "./index.html";

# dw.urlretrieve(imgUrl,savePath1);
# dw.urlretrieve(htmlURL,savePath2);

f1 = dw.urlopen(imgUrl);
f2 = dw.urlopen(htmlURL);

saveFile1 = open(savePath1,'wb');
saveFile1.write(f1.read());
saveFile1.close();

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2.read());

print("다운로드완료");

# urlopen 과 urlretrieve 의 차이
# urlretrieve 는 parsing 없이 바로 download 용
# urlopen 은 open 된  url data를 parsing 등 작업을 할때 유용


print(urlparse("http://www.encar.com"));
