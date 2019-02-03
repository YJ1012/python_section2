from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as Ureq
import sys
import io

#sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
res = Ureq.urlopen(url).read().decode('cp949', 'ignore');
#res =  res1.decode('utf-8') ;

#web_driver = webdriver.Chrome();
#web_driver.implicitly_wait(2)
#web_driver.get(url)
#res = web_driver.page_source;
#web_driver.close();
soup = BeautifulSoup(res, "html.parser")
#top10 = soup.select("#siselist_tab_0");
#print("top9",top10);
top10 = soup.select("#siselist_tab_0 > tr");
Cnt = 0;
for e in top10:

    if e.find("a") is not None:
        Cnt= Cnt+1;
        print(Cnt,e.select_one(".tltle").string);


print("END");
