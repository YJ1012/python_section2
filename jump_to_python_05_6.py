import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8');
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8');
print(sys.argv)
print(sys.path)

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()


import os
print(os.environ['PATH'])
os.system("dir")

import shutil
shutil.copy("test.txt", "test2.txt")
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()

import glob
glob.glob("./*.py");
print(glob.glob("./*.py"));

import time
print(time.asctime(time.localtime(time.time())))
print( time.ctime())

import calendar
calendar.prcal(2019)
calendar.prmonth(2019,1)


import threading

def long_task(num):
    for i in range(5):
        print("%d working:%d\n" %(num,i));
        time.sleep(0.1);

def sum(idx,cnt):
    for i in range(5):
        print("%d %d Subthread %d" %(idx,cnt,i));
        time.sleep(0.1)

print("Start")

threads = []
for k in range(5):
    t = threading.Thread(target=sum,args=(k,k))  # 스레드를 생성한다.
    threads.append(t)
print(len(threads))

for t1 in threads:
    t1.start()  # 스레드를 실행한다.
for t2 in threads:
    t2.join()  # 스레드를 실행한다.
print("END")
