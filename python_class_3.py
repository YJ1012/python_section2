from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as Ureq
#import urllib.parse as Uparse
import sys
import io
import os
sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class WareHouse():
    stock_num =0;
    def __init__(self,name):
        self.name =name;
        WareHouse.stock_num += 1;

    def __del__(self):
        print("del")
        WareHouse.stock_num -= 1;


user1= WareHouse("kim")
user2= WareHouse("Lee")

print(user1.name)
print(user2.name)

print(user1.__dict__)
print(user2.__dict__)
print(WareHouse.__dict__)

print(user1.stock_num)
print(user2.stock_num)
