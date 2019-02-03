import threading
import time
import os

def sum(idx,cnt):
    for i in range(2):
        print("%d %d Subthread %d" %(idx,cnt,i));
        time.sleep(0.1)

t = threading.Thread(target=sum, args=(1, 100000))
t.start()

print("Main Thread")
for i in range(2):
    print("Main Thread %d" %i);
    time.sleep(0.1)


str_test ="abcdefgabcdefg   abcdefgabcdefg    acbdgfdhwefhklsdihjnf";
str_test2= str_test.replace("abc","AAA")
print(str_test);
print(str_test2);

dir_list= list(os.listdir("./"));
"""
for d in dir_list:
    if os.path.isdir(d):
        print("Directory : ",d);
    else:
        print("File : ",d);
"""
for (path, dir, files)  in os.walk("./"):
     for dd in files:
        if os.path.isdir(dd):
            print("Directory : ",dd);
        else:
            print("File : ",dd);
