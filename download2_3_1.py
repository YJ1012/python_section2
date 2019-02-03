import sys
import io
import urllib.request as u_req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8');
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8');

url1 = "http://www.encar.com";

mem = u_req.urlopen(url1);
# print(type(mem));
# print(type({}));
# print(type([]));
# print(type(()));


# print("geturl ",mem.geturl());
# print("status ",mem.status); # 200 : normal , 404 no page , 403 reject page , 500 server error
# print("headers ",mem.getheaders());


# print("info : ",mem.info());
# print("code : ",mem.getcode());

# print("read : ",mem.read(70).decode("utf-8"));
