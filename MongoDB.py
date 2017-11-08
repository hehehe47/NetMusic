from pymongo import MongoClient


def insert_user(nickname, user_id, gender, birthday, city, pro):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    user = db['user']
    single_user = {
        'name': nickname,  # 用户名
        'user_id': user_id,  # id
        'gender': gender,
        'birthday': birthday,
        'city': city,
        'pro': pro
    }
    user.insert_one(single_user)


def insert_user_show(nickname, user_id, gender, birthday, city, pro):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    user = db['user_show']
    single_user = {
        'name': nickname,  # 用户名
        'user_id': user_id,  # id
        'gender': gender,
        'birthday': birthday,
        'city': city,
        'pro': pro
    }
    user.insert_one(single_user)


def insert_recent_list(user_id, sing_name, sing_id, song_name, song_id, album_name, album_id, score):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    user = db['recent_song']
    single_recent_list = {
        'user_id': user_id,
        'sing_name': sing_name,
        'sing_id': sing_id,
        'song_name': song_name,
        'song_id': song_id,
        'album_name': album_name,
        'album_id': album_id,
        'score': score
    }
    user.insert_one(single_recent_list)


def insert_recent_list_show(user_id, sing_name, sing_id, song_name, song_id, album_name, album_id, score):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    user = db['recent_song_show']
    single_recent_list = {
        'user_id': user_id,
        'sing_name': sing_name,
        'sing_id': sing_id,
        'song_name': song_name,
        'song_id': song_id,
        'album_name': album_name,
        'album_id': album_id,
        'score': score
    }
    user.insert_one(single_recent_list)


def insert_all_list(user_id, sing_name, sing_id, song_name, song_id, album_name, album_id, score):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    user = db['all_song']
    single_recent_list = {
        'user_id': user_id,
        'sing_name': sing_name,
        'sing_id': sing_id,
        'song_name': song_name,
        'song_id': song_id,
        'album_name': album_name,
        'album_id': album_id,
        'score': score
    }
    user.insert_one(single_recent_list)


def insert_all_list_show(user_id, sing_name, sing_id, song_name, song_id, album_name, album_id, score):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    user = db['all_song_show']
    single_recent_list = {
        'user_id': user_id,
        'sing_name': sing_name,
        'sing_id': sing_id,
        'song_name': song_name,
        'song_id': song_id,
        'album_name': album_name,
        'album_id': album_id,
        'score': score
    }
    user.insert_one(single_recent_list)

# def insert_city(city_num, city_name):
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['test']
#     city = db['city']
#     single_city_list = {
#         'city_num': city_num,
#         'city_name': city_name
#     }
#     city.insert_one(single_city_list)
