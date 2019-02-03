from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as Ureq
import urllib.parse as Uparse
import sys
import io
import os
sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = Uparse.quote_plus("사자");
url = base + quote;
# print(url)
res = Ureq.urlopen(url);
savePath = "C:\\imagedown\\" #C:/imagedown (window)
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath));
        #os.mkdir(savePath); same operation
except OSError as e:
    if(e.errno != errno.EEXIST):
        print("make folder FAIL")
        raise
soup = BeautifulSoup(res,"html.parser");
img_list = soup.select("div.photowall._photoGridWrapper > div.photo_grid._box > div > a.thumb._thumb > img");
for i, img_lists  in enumerate(img_list,1):
    if(i==1):
        print(type(img_lists));
        #print(img_lists);
        print(img_lists['class']);
        print(img_lists['data-source']);
    full_file_name = os.path.join(savePath,savePath+str(i)+".jpg")
    Ureq.urlretrieve(img_lists['data-source'],full_file_name)

print("END");
