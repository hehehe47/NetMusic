import AES
import json
import requests

headers = {
    'Host': 'music.163.com',
    'Connection': 'keep-alive',
    'Content-Length': '526',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Cookie': 'appver=1.5.0.75771;_ntes_nnid=2ad449218b232a8b606eb5a5e5c412ad,1484892581656; _ntes_nuid=2ad449218b232a8b606eb5a5e5c412ad; NTES_PASSPORT=Qf1XyC1Ma2dDdiDNEVhQaWzzRswYe2rqhKskchaa9Fm4izPRd18o7g4xvCaVvH.6OdUkn1pKp0aybp6QABRBpBevRLQmyXdCMdYVS0tjqW0qh; P_INFO=yhuichun47@163.com|1484970325|1|mail163|00&99|anh&1484970309&mail163#anh&341100#10#0#0|153797&0|g37_client_check&cloudmusic&mailsettings&mail163|yhuichun47@163.com; mail_psc_fingerprint=638d991b872ead11c5ffdc4211c118ce; playlist=382744742; Province=021; City=021; vjuids=666bc2e5f.159caa454fb.0.0c36c65706762; vjlast=1485163484.1485163484.30; ne_analysis_trace_id=1485163484427; NTES_SESS=DOi62OSN0VH2x7wqQjutir7YskkptzI8aTso4HAMUMb2waIbZfUYeviR3.cO3pj0oVAFmOPjogz6VYH3kLgn1Ic45QWQyDSQF6wuSE52PWtzyS6fyaMx3YxlsnnXyF85seTDk2b4wM.3G67_ME2qolq7sSWBm1TW3.OVwqsMbpuadNwh77JBi1rvc; S_INFO=1485163486|1|0&80##|yhuichun47; ANTICSRF=a3ae126394a66dcbedc115b2a71dbd81; NTES_REPLY_NICKNAME=yhuichun47%40163.com%7Cyhuichun47%7C%7C%7C%7CQf1XyC1Ma2dDdiDNEVhQaWzzRswYe2rqhKskchaa9Fm4izPRd18o7g4xvCaVvH.6OdUkn1pKp0aybp6QABRBpBevRLQmyXdCMdYVS0tjqW0qh%7C1%7C-1; vinfo_n_f_l_n3=31086c3ff9fa6b5c.1.0.1485163484439.0.1485163495443; s_n_f_l_n3=31086c3ff9fa6b5c1485163484440; JSESSIONID-WYYY=oeAkaheMikdiC1Fffh%2FzB5gv6sFrh6MW%2FD%2BetPNCgy9bQW9JuwAZcbUxRSHSKP7h%2Fy%2BKDkfBA3bK7CknKr63YtmRRy4EIgfHHwtb%2BCofGQoor6PDEnmGZMBIGIXoKQ4jgghkx46n9xMb%2F1s%2B9tOFgjepZ92Mgno5YRfiBT9wXuGe03a1%3A1485168649976; _iuqxldmzr_=32; MUSIC_U=8310f4148f98de4e91c373ab0401213e20df35b3e4b78fe14bec0982693efaf6f24d835b7fd9da0e2eb1804c805373b4b3af56c2e35dceeaa70b41177f9edcea; __csrf=a2a57d13824107fbf01a068e90d219f5; __remember_me=true; __utma=94650624.218650173.1484892585.1485153862.1485163389.13; __utmb=94650624.20.10.1485163389; __utmc=94650624; __utmz=94650624.1484975575.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
}
cookie = {'appver': '1.5.2'}

'''limit = 10

req = {
                "ids": id,
                "br": 320000,
                "csrf_token": csrf
            }

my_data = AES.encrypted_request(req)
params = my_data.get('params')
encSecKey = my_data.get('encSecKey')'''
s = 'Moon Without The Stars'
search_type = 'userprofileCount'
headers['Referer'] = 'http://music.163.com/'
id = 248958316
user_type = 0
csrf = '9f887d2b795f59867cf2be8724bbb23b'
action = 'http://music.163.com/weapi/v1/play/record?csrf_token='  # NOQA
action += csrf

req = {

    # "s":'a',"limit":20,"offset":1,"type":1002
    "uid": '248958316', "type": 0, "limit": 1000, "offset": 0, "total": True
}
connection = requests.post(action,
                           data=AES.encrypted_request(req),
                           headers=headers,
                           )
results = json.loads(connection.text)
print(results)
