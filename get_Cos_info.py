import requests
import MongoDB
import AES
import json
import time
import random
import pymongo
from http.cookiejar import LWPCookieJar
import threading

client = MongoDB.MongoClient('mongodb://localhost:27017/')
db = client['test']
user = db['data_show']

head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

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

    '''data = {
        'params':AES.params ,
        'encSecKey':AES.encSecKey
    }'''

    data1 = {
        'params': 'NTeLq+UCeGKl6NzOQgNAzollDYv/60QCYsOdAaGlqWzKHbQKtU1fBrtRdxb46B2mViuKPO6KDGPh9f/tPgtXXjQ9GN1n53pZTxm5Z0dWVBYV8xk9kYrCisxYo03+Lj6MGEOD1T7shBf3CIphovvqvaSV7RAredzkRLofNManQts5V6PGgiDXvTnfGNGKPkmF8dStW0uD3O+6i5O3z2hg4/KUbpCWRPwAM+k5Njt5/Xk=',
        'encSecKey': '434a59ec5d55ad042edda11c07b3ba2464a49e3bc59a2f4216eda9caa38b5abfa3cc61b76b7ed6f1aa359d3e44ad666b14a72f8b44eea801c1039db99fff5acd0348d806e43380fc039bb8cf37fbeea7e788b7d6061a686de3e7cd5382d5089558e063d9812cf46e6ecc1dc9c0877f35e809200f9d59baded268acfd231ba5fb'
    }

    # proxies = {'http': '211.167.112.14:80'}

    '''def get_list(self, user_id, flag):
        self.headers['Referer'] = 'http://music.163.com/#/user/home?id='+ str(user_id)

        if flag:
            r = requests.post('http://music.163.com/weapi/v1/play/record?csrf_token=',
                              headers=self.headers, params=self.params, data=self.data)
            print(r.content)
            return r

        else:
            r = requests.post('http://music.163.com/weapi/v1/play/record?'+ str(user_id),
                              headers=self.headers, params=self.params, data=self.data1)
            return r.json()'''

    def get_list(self, uid, flag):
        self.headers['Referer'] = 'http://music.163.com/'
        action = 'http://music.163.com/weapi/v1/play/record?csrf_token='  # NOQA
        csrf = '92ae0a52166c681854c10164ad8901a4'
        action += csrf
        data = {"uid": uid, "type": flag, "limit": 1000, "offset": 0, "total": True}  # 0是week  1是all
        connection = requests.post(action,
                                   # data = self.data1,
                                   data=AES.encrypted_request(data),
                                   headers=self.headers)
        s = requests.session()
        s.keep_alive = False
        return connection.json()

    def get_info(self, list, user_id, flag):
        song = {'user_id': user_id}
        if flag == 0:
            dict1 = list.get('allData')
            try:
                length = len(dict1)
            except TypeError:
                print('There is no allData')
                length = 0
        # print(length)
        i = 0
        if length != 0:
            while i < length:
                score = dict1[i].get('score')
                dict2 = dict1[i].get('song')  # 获取第i首歌的歌曲信息
                dict3 = dict2.get('ar')  # 获取第i首歌的演唱者信息
                song_name = dict2.get('name')
                # print(song_name,score)
                song['song_name' + str(i)] = song_name
                song['score' + str(i)] = score
                i = i + 1
            user.insert_one(song)


def get_user_id():
    a = 1
    try:
        for raw_data in db.user.find({}):
            user_id = raw_data['user_id']
            print(a)
            # if a >= 9534:
            try:
                total_list = List()
                # print('1')
                list_all = total_list.get_list(user_id, 0)  # 248958316梦泽   278487128我   33759252仓
                # print(list_all)
                total_list.get_info(list_all, user_id, 0)
                a = a + 1
                # time.sleep(random.randint(0, 10))
            except Exception as e:
                print('error 000:', end=' ')
                print(e)
                # else:
                # a = a + 1
                # MongoDB.MongoClient.close_cursor()
    except Exception as e:
        print('error 001:', end=' ')
        print(e)


if __name__ == '__main__':
    get_user_id()
    '''total_list = List()
    list_all = total_list.get_list(278487128, 0)  # 248958316梦泽   278487128我   33759252仓
    print(list_all)
    list_week = total_list.get_list(278487128, 1)
    print(list_week)
    for i in range(0,2):
        if i == 0:
            total_list.get_info(list_all, 278487128,i)
        else:
            total_list.get_info(list_week, 278487128,i)'''

    # print(type(lists))
    # songs = lists.get('allData')
    # print(type(songs))
    # print(songs[1])
    # print(type(songs[1]))
    # song = songs[1].get('song')
    # print(song)
    # print(type(song))
    # song1 = song.get('ar')
    # song2 = song.get('al')
    # print(song1[0])
    # print(type(song1[0]))
    # singer = song1[0].get('name')
    # print(singer)

    # print(type(songs))


    # print(songs2)
