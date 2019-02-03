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


base = "https://www.inflearn.com/"
#quote = Uparse.quote_plus("업무-효율성");
quote = "";
url = base + quote;
#print(url)
res = Ureq.urlopen(url);
savePath = "C:\\imagedown2\\" #C:/imagedown (window)
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath));
        #os.mkdir(savePath); same operation
except OSError as e:
    if(e.errno != errno.EEXIST):
        print("make folder FAIL")
        raise
soup = BeautifulSoup(res,"html.parser");
# img_list = soup.select("div > ul > li > div > div.block_media > a > img");
# txt_list = soup.select("div > ul > li > div > div > h4 > a");
total_list = soup.select("div > ul > li > div");
##\34 78 > div > ul > li:nth-child(7) > div > div.block_content > h4 > a
#print(total_list)

for i, e  in enumerate(total_list,1):
    tmp_txt = e.select_one("h4.block_title > a");
    tmp_img = e.select_one("div.block_media > a > img");
    if(tmp_txt != None):
        with open(savePath+"text_"+str(i)+".txt","wt") as F:
            F.write(tmp_txt.string);
    if(tmp_img != None):
        full_file_name = os.path.join(savePath, savePath+str(i)+".jpg")
        print(tmp_img)
        Ureq.urlretrieve(tmp_img['src'],full_file_name);
    ##\34 78 > div > ul > li:nth-child(7) > div >
#     if(i==1):
#         print(type(img_lists));
#         #print(img_lists);
#         print(img_lists['class']);
#         print(img_lists['data-source']);
#     full_file_name = os.path.join(savePath,savePath+str(i)+".jpg")
#     Ureq.urlretrieve(img_lists['data-source'],full_file_name)
#
# print("END");
