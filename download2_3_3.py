import sys
import io
import urllib.request as u_req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8');
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8');

url1 = "http://www.encar.com";

API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

value ={
    'ctxCd': '1012'
}
print('before',value);
params = urlencode(value);
print('after',params);

url = API + "?" + params
print("URL: "+ url);

reqData  = u_req.urlopen(url).read().decode('utf-8');
print("출력 ",reqData);
