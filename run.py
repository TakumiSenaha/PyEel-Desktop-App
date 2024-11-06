#!/usr/bin/env python3
# coding: utf8

import os
import random

import eel
from pymongo import MongoClient

# MongoDBに接続
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client: MongoClient = MongoClient(mongo_uri)
db = client["bus_schedule_db"]


@eel.expose
def log_message(message):
    print(f"JavaScript Log: {message}")


# サービスタイプをランダムに返す関数
@eel.expose
def get_random_service_type():
    service_types = ["2-bus-day", "3-bus-day-full", "holiday"]
    return random.choice(service_types)


# 日付に応じたバス時刻表を取得
@eel.expose
def get_timetable(date_str, stop):
    service_type_key = get_random_service_type()  # ランダムでサービスタイプを取得
    service_types = db["service_types"].find_one({"_id": "service_types"})
    service_type_schedule = service_types["service_types"].get(service_type_key, [])

    for entry in service_type_schedule:
        if entry["stop"] == stop:
            return entry["departure_times"]
    return "該当するデータがありません"


# 全ての時刻表データを取得
@eel.expose
def get_all_timetables():
    service_types = db["service_types"].find_one({"_id": "service_types"})
    print(service_types["service_types"])
    return service_types["service_types"] if service_types else {}


# Webディレクトリの初期化
eel.init(os.path.join(os.path.dirname(__file__), "web"))

# アプリケーションを起動
eel.start("index.html", size=(1000, 800), mode="chrome")
