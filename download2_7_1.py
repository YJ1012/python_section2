from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'utf-8')
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net/domestic/market_cap"

web_driver = webdriver.Chrome();
# web_driver.implicitly_wait(3)
web_driver.get(url)
res = web_driver.page_source;
web_driver.close();
# res = req.urlopen(url).read()


soup = BeautifulSoup(res, "html.parser")
top = soup.select("#boxMarketCap > div.box_contents > div > table > tbody > tr");
#print(top)
for i,e in enumerate(top,1):
    #print(i,e.find("a").string, "=", e.find("span").string)
    #print(type(e),i,e.find("a").string,e.find("span").string);
    print(i,e.find("a").string,end=' ');
    all_num = e.find_all("span",{"class":"num"});
    for k in all_num:
        tmp_txt1 = str(k.string);
        tmp_txt2 = (tmp_txt1.replace("\n",""))
        tmp_txt_arr =tmp_txt2.split()
        for jj in tmp_txt_arr:
            print(jj,end=' ')

    print("\n");

# f = open("272_test.html","wt");
# tmp_txt=soup.prettify();
# print(tmp_txt);
# f.write(tmp_txt);
# f.close();
