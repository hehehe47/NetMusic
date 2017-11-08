import MongoDB
import math
import datetime
import operator

client = MongoDB.MongoClient('mongodb://localhost:27017/')
db = client['test']
Song_list = []
Cos_list = []
upper = 10
user_upper = 5


def Song():  # 获取多维坐标（将所有歌曲放到一个列表中）
    for raw_data in db.data.find({}):  # 412226876
        for i in range(0, upper):  # 曲库上限
            try:
                song_name = raw_data["song_name" + str(i)]
                Song_list.append(song_name)
                # print(song_name)
            except Exception as e:
                break


def input_recom_list():
    recom = {}
    print('Please input listened musics!')
    for j in range(0, user_upper):  # 用户输入上限
        for i in range(0, 2):
            string = input()
            if string.isdigit():
                fre = string
            else:
                name = string
            if name not in Song_list:
                Song_list.append(name)
                print('Already appended!')
        recom[name] = int(fre)
    print(recom)
    return recom


def Cosine(user, recom):  # sum1 内积    sum2 user长  sum3 recom长
    sum1 = sum2 = sum3 = 0
    for key in recom:
        sum1 = user[key] * recom[key] + sum1
        sum2 = user[key] * user[key] + sum2
        sum3 = recom[key] * recom[key] + sum3
    if sum2 and sum3 != 0:
        cosine = sum1 / (math.sqrt(sum2) * math.sqrt(sum3))
    else:
        cosine = 0
    return cosine


def user_song_dic(recom):
    Song_dic = {}
    dic = {}
    for song_name in Song_list:
        Song_dic[song_name] = 0
    j = 1
    for user_data in db.data.find({}):  # 'song_name56': '我要你','song_name22': '天梯(Live) - live'
        process = (float)(j / 16000) * 100
        if process % 10 == 0:
            print(process, '%')
        for i in range(0, upper):  # 曲库上限
            try:
                Song_dic[user_data['song_name' + str(i)]] = user_data['score' + str(i)]
                # dic[user_data['song_name' + str(i)]] = user_data['score' + str(i)]
            except:
                break
        # print(user_data)
        # print(dic)
        j += 1
        cos = Cosine(Song_dic, recom)
        Cos_list.append(cos)
        dic = {}  # 需要清空字典
        for song_name in Song_list:
            Song_dic[song_name] = 0


def find_closest_user(Cos_list):
    i = 0
    j = i + 1
    for j in range(j, len(Cos_list)):
        if Cos_list[i] < Cos_list[j]:
            i = j
    print(Cos_list[i])
    a = 0
    for user in db.data.find({}):
        if a == i:
            return user
        a = a + 1


def find_recommond_song(user, recom):
    for i in range(0, 100):
        if user['song_name' + str(i)] not in recom:
            print('Maybe you would like "' + user['song_name' + str(i)] + '"this song!')
            break


starttime = datetime.datetime.now()

Song()
Song_list = list(set(Song_list))  # song_list 去重'''
recom = input_recom_list()
user_song_dic(recom)
print(Cos_list)
user = find_closest_user(Cos_list)
# sorted(user.items(), key=operator.itemgetter(1))
print(user)
find_recommond_song(user, recom)

endtime = datetime.datetime.now()
interval = (endtime - starttime).seconds
print(interval)
