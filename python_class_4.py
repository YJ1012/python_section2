# from bs4 import BeautifulSoup
# from selenium import webdriver
# import urllib.request as Ureq
#import urllib.parse as Uparse
import sys
import io
import os
sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class NameTest:
    total = 0;

print(dir())
print("before ",NameTest.__dict__);
NameTest.total=1;
print("before ",NameTest.__dict__);


n1 = NameTest();
n2 = NameTest();
print(id(n1), id(n2))
print(dir())

print(n1.__dict__);
print(n2.__dict__);

n1.total = 77

print(n1.__dict__);
print(n2.__dict__);

print(n1.total)
print(n2.total)

print(n1.__dict__['total']);
#print(n2.__dict__['total']);
