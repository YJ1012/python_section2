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

class UserInfo:
    def __init__(self, name, phoneNum):
        self.Name = name
        self.phoneNum = phoneNum

    def setInfo(self, name, phoneNum):
        self.Name = name
        self.phoneNum = phoneNum

    def printInfo(self):
        print("----------------------");
        print("name : " + self.Name);
        print("Phone number : " + self.phoneNum);
        print("----------------------");

    def __del__(self):
        print("delete");

user1 = UserInfo("YJ","010-111")
user2 = UserInfo("SR","010-222")

user1.setInfo("YJ","010-111")
user2.setInfo("SR","010-222")

user1.printInfo()
user2.printInfo()


print(user1.__dict__)
print(user2.__dict__)
