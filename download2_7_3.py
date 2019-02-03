from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as Ureq
import urllib.parse as Uparse
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'utf-8')
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/"
quote = Uparse.quote_plus("추첨결과");
res = Ureq.urlopen(url).read();
#res = Ureq.urlopen(url).read().decode('cp949', 'ignore');
#res =  res1.decode('utf-8') ;

#web_driver = webdriver.Chrome();
#web_driver.implicitly_wait(2)
#web_driver.get(url)
#res = web_driver.page_source;
#web_driver.close();
soup = BeautifulSoup(res, "html.parser")
#top10 = soup.select("#siselist_tab_0");
#print("top9",top10);
#\37 08 > div > ul > li:nth-child(19) > div > div.block_content > h4 > a
#global > div.pusher > section:nth-child(8) > div > div > div > div.vibe_grid > ul > li:nth-child(6) > div > div.block_content > h4 > a
#global > div.pusher > section:nth-child(8) > div > div > div > div.vibe_grid > ul > li:nth-child(5) > div > div.block_content > h4 > a
top10 = soup.select("ul > li");
#print(top10)
Cnt = 0;
for e in top10:
    #if e.find("") is not None:
    #    print(e.select_one("h4.block_title").string);
    Cnt= Cnt+1;
    if e.find("h4") is not None:
        print(Cnt,e.select_one(".block_title").string);


print("END");
