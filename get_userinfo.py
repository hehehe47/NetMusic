import requests
import os
from bs4 import BeautifulSoup
import MongoDB
import city
import time
import AES
import random


def get_gender(Gender):
    if Gender == 0:
        gender = None
    elif Gender == 1:
        gender = '男'
    else:
        gender = '女'
    return gender


def get_birth(birthday):
    if birthday < 0:
        birth = None
    else:
        birthday = int(birthday / 1000)
        # print(birthday)
        timeArray = time.localtime(birthday)
        birth = time.strftime("%Y", timeArray)
        birth = int(birth)
        #print(type(birth))
        if birth >= 1930 and birth < 1935:
            birth = '30后'
        elif birth >= 1935 and birth < 1940:
            birth = '35后'
        elif birth >= 1940 and birth < 1945:
            birth = '40后'
        elif birth >= 1945 and birth < 1950:
            birth = '45后'
        elif birth >= 1950 and birth < 1955:
            birth = '50后'
        elif birth >= 1955 and birth < 1960:
            birth = '55后'
        elif birth >= 1960 and birth < 1965:
            birth = '60后'
        elif birth >= 1965 and birth < 1970:
            birth = '65后'
        elif birth >= 1970 and birth < 1975:
            birth = '70后'
        elif birth >= 1975 and birth < 1980:
            birth = '75后'
        elif birth >= 1980 and birth < 1985:
            birth = '80后'
        elif birth >= 1985 and birth < 1990:
            birth = '85后'
        elif birth >= 1990 and birth < 1995:
            birth = '90后'
        elif birth >= 1995 and birth < 2000:
            birth = '95后'
        elif birth >= 2000 and birth < 2005:
            birth = '00后'
        elif birth >= 2005 and birth < 2010:
            birth = '05后'
        elif birth >= 2010 and birth < 2015:
            birth = '10后'
        elif birth >= 2015 and birth < 2020:
            birth = '15后'
        else:
            birth = 'WHAT?'
            ######
    return birth


class List(object):
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
        'Cookie': '_ntes_nnid=2ad449218b232a8b606eb5a5e5c412ad,1484892581656; _ntes_nuid=2ad449218b232a8b606eb5a5e5c412ad; NTES_PASSPORT=Qf1XyC1Ma2dDdiDNEVhQaWzzRswYe2rqhKskchaa9Fm4izPRd18o7g4xvCaVvH.6OdUkn1pKp0aybp6QABRBpBevRLQmyXdCMdYVS0tjqW0qh; P_INFO=yhuichun47@163.com|1484970325|1|mail163|00&99|anh&1484970309&mail163#anh&341100#10#0#0|153797&0|g37_client_check&cloudmusic&mailsettings&mail163|yhuichun47@163.com; mail_psc_fingerprint=638d991b872ead11c5ffdc4211c118ce; playlist=382744742; Province=021; City=021; vjuids=666bc2e5f.159caa454fb.0.0c36c65706762; vjlast=1485163484.1485163484.30; ne_analysis_trace_id=1485163484427; NTES_SESS=DOi62OSN0VH2x7wqQjutir7YskkptzI8aTso4HAMUMb2waIbZfUYeviR3.cO3pj0oVAFmOPjogz6VYH3kLgn1Ic45QWQyDSQF6wuSE52PWtzyS6fyaMx3YxlsnnXyF85seTDk2b4wM.3G67_ME2qolq7sSWBm1TW3.OVwqsMbpuadNwh77JBi1rvc; S_INFO=1485163486|1|0&80##|yhuichun47; ANTICSRF=a3ae126394a66dcbedc115b2a71dbd81; NTES_REPLY_NICKNAME=yhuichun47%40163.com%7Cyhuichun47%7C%7C%7C%7CQf1XyC1Ma2dDdiDNEVhQaWzzRswYe2rqhKskchaa9Fm4izPRd18o7g4xvCaVvH.6OdUkn1pKp0aybp6QABRBpBevRLQmyXdCMdYVS0tjqW0qh%7C1%7C-1; vinfo_n_f_l_n3=31086c3ff9fa6b5c.1.0.1485163484439.0.1485163495443; s_n_f_l_n3=31086c3ff9fa6b5c1485163484440; JSESSIONID-WYYY=oeAkaheMikdiC1Fffh%2FzB5gv6sFrh6MW%2FD%2BetPNCgy9bQW9JuwAZcbUxRSHSKP7h%2Fy%2BKDkfBA3bK7CknKr63YtmRRy4EIgfHHwtb%2BCofGQoor6PDEnmGZMBIGIXoKQ4jgghkx46n9xMb%2F1s%2B9tOFgjepZ92Mgno5YRfiBT9wXuGe03a1%3A1485168649976; _iuqxldmzr_=32; MUSIC_U=8310f4148f98de4e91c373ab0401213e20df35b3e4b78fe14bec0982693efaf6f24d835b7fd9da0e2eb1804c805373b4b3af56c2e35dceeaa70b41177f9edcea; __csrf=a2a57d13824107fbf01a068e90d219f5; __remember_me=true; __utma=94650624.218650173.1484892585.1485153862.1485163389.13; __utmb=94650624.20.10.1485163389; __utmc=94650624; __utmz=94650624.1484975575.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
    }

    params = {
        'csrf_token': ''
    }

    data = {
        'params': 'zUIpiQ1LC8wkGb0c5HvPT2on9BkyrlkjdSaRSwAnyquwmepdDpCr2MKa8HQyMkdFLUgFBUAIG6OymuZoZNCwkkIwEuVIzs9DJ76TxRpb18NSL1Lc4Z9gEXkVzpcUEhkNM8+abNdvlC6dFR4d8bhN31ykIM/sS+tqLiBtzkLyehZhJcpSVSkDnndx1ukMU6QNbhe+lMml8YsvwiQ2N2fwr/GeIzBhyHRX1uX6G4iRA5q6ZDvuDWzOlg/QV3U1okAOLUHwdp1jJEhVQTVUK3qpTv29hxeBzmBxtef0bGaKuOJGBGhWq+eyi6ahGbayHpsZ',
        'encSecKey': '33c9894e7f22244fcb175500aa29c45a81b22380319dbae7f4777f71e680201a87c02d18955080657174b09bf3e09f97c4dea370030cd719d5ee46db5f90cc3f2d18caa378463c37e55d4eeabb9a7bf97e16a2423cdd94f38d7235cf57e4a7d9cd2094c2e4ff20ea52137a789a644b6fc4edce3bdcc205dbdbbb09c672c518af'}

    data1 = {
        'params': 'sCMIUZfPB7GklrG1SJmp0kTT90E5cV46xHLotAK4rTmAEE7qVKb398jCnuhM6ZzlOEmmAMtVTDeE8n40NgZegexpa2PAD403L9NcsDkDu3Y5MZtQI9HhLLjR7EUbcIxLlXE3G4VS/81V3Tj3SfOoTszC0283PFvWmvsQCYTs7QL3oAelFumdCYpjBnm5eGAyf8sx0gIqN4NSwsbaoiJ/Eq1dyWA8MgYtnl/BW1K7g+m5PdlX0/gdhTFELyWUHBv0m809YBI+C2S9IghUlHD+e4UU1JLg2k7JWYkLOxickn2rkxf0Z1VRIafwirIhX8CpDi2VItsmfZ0y2xUfv4X9d37hVvQQkbG5PUZGlGUXX5YrC4Z9r5eFdNvYE/hIoJlX',
        'encSecKey': 'b6e44f526219fdac8dc6d2d9b0ee4d1c375b777b32100451cab1af14af1e9ad8205d35a26b72db90bf8d19acc19ad85e2de303e40051b0a51539b8c2fa585cf941ef8240688e82f96440fc7047a5caff419e1b7e3c9310fce4d296547cb641c8a3f2a8b665d6535645dc6c4ba393dc1f7eec798cc61fbb37767caa4b6a8c6bd1'}
    # proxies = {'http': '211.167.112.14:80'}
    # hehehe47


    '''def get_list(self, str, flag):
        self.headers['Referer'] = 'http://music.163.com/#/search/m/?s=' + str + '&type=1002'

        if flag:
            r = requests.post('http://music.163.com/weapi/cloudsearch/get/web?',
                              headers=self.headers, params=self.params, data=self.data)
            return r.json()

        else:
            r = requests.post('http://music.163.com/weapi/cloudsearch/get/web?',
                              headers=self.headers, params=self.params, data=self.data)
            return r.json()'''

    def get_list(self, str, flag):
        self.headers['Referer'] = 'http://music.163.com/search/'
        action = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='  # NOQA
        csrf = '92ae0a52166c681854c10164ad8901a4'
        action += csrf

        data = {"s": str, "limit": 30, "offset": (flag * 30), "type": 1002}
        connection = requests.post(action,
                                   # data = self.data1,
                                   data=AES.encrypted_request(data),
                                   headers=self.headers)
        return connection.json()

    def get_user_info(self, list):
        list1 = list.get('result')
        list2 = list1.get('userprofiles')
        for user in list2:
            city_id = user.get('city')
            # city_id = 1000100
            if city_id < 1000100:
                pro_id = int(city_id / 10000) * 10000
            else:
                pro_id = city_id
            # print(city_id)
            pro_name = city.get_city(pro_id)
            city_name = city.get_city(city_id)
            # print(city_name)
            gender = user.get('gender')
            gender = get_gender(gender)
            birthday = user.get('birthday')
            # get_birth(birthday)
            birth = get_birth(birthday)
            MongoDB.insert_user_show(user.get('nickname'), user.get('userId'), gender, birth, city_name, pro_name)

            # def get_all(list):
            # for i in range(1, 10):
            # try:
            # list.get_user_info(i, list)
            # time.sleep(random.randint(0, 60))
            # except Exception as e:
            # print(e)


if __name__ == '__main__':
    list = List()
    # list1 = List()
    for a in range(120, 123):  # a 98b 99c 100d
        print(chr(a))
        for i in range(0, 25):
            print(i)
            try:
                user_list = list.get_list(chr(a), i)
                list.get_user_info(user_list)
                time.sleep(random.randint(0, 10))
            except Exception as e:
                print(e)
