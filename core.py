from json import loads
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import ReadTimeout, ConnectTimeout

request_url = "http://w.nuaa.edu.cn/iPortal/action/doLogin.do"

login_info = {
    'username': '',
    'password': '',
    'saved': '1',
    "from": '003cc944be32e25365428f2dd2adbbe2',
    'domain': '1'
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'w.nuaa.edu.cn',
    'Origin': 'http://w.nuaa.edu.cn',
    'Referer': 'http://w.nuaa.edu.cn/iPortal/index.htm?'
               'from=003cc944be32e25365428f2dd2adbbe2&wlanuserfirsturl=http://www.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/38.0.2125.104 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'

}


s = Session()
s.mount('http://', HTTPAdapter(max_retries=0))


def connect_portal(username, password, domain='1'):
    if username and password:
        login_info['username'] = username
        login_info['password'] = password
        login_info['domain'] = domain

        if s.get('http://202.119.65.214', timeout=0.5).status_code != 200:
            return 'No Network'
        else:
            try:
                login_resp = s.post(request_url, data=login_info, headers=headers, timeout=0.5)
                return loads(login_resp.json()['data'])['status'].capitalize()
            except ReadTimeout:
                return 'Timeout'
            except ConnectTimeout:
                return 'Timeout'
            except:
                return 'Unknown Err'

    return 'Need Information'


def test_public():
    if s.get('http://baidu.com', timeout=0.5).status_code == 200:
        return "Accessible"

    else:
        return "Not Accessible"
