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


class SelfTest:
    def function1():
        print("call function 1")
    def function2(self):
        print(id(self))
        print("call function 2")

f = SelfTest();
print(id(f))
#f.function1()
f.function2()
print(f.__dict__)
SelfTest.function1();
