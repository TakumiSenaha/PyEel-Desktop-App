#!/usr/bin/env python3
# coding: utf8

import os

import eel
from pymongo import MongoClient

# MongoDBに接続
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client: MongoClient = MongoClient(mongo_uri)
timetable_db = client["bus_timetable_db"]
date_db = client["bus_date_db"]


@eel.expose
def log_message(message):
    print(f"JavaScript Log: {message}")


# 指定された日付に基づいてサービスタイプを取得
def get_service_type_by_date(date_str):
    print(date_str)

    # `dates` コレクションで指定された日付に対応するサービスを検索
    date_entry = date_db["dates"].find_one({"_id": "dates"})
    if date_entry and date_str in date_entry["dates"]:
        return date_entry["dates"][date_str]
    return None


# 日付と出発地点に応じたバス時刻表を取得
@eel.expose
def get_timetable(date_str, start_location):
    # 日付に対応するサービスタイプを取得
    service_type = get_service_type_by_date(date_str)
    if not service_type:
        return "指定した日付に対応するサービスはありません。"

    # サービスタイプに対応する時刻表データを取得
    service_types = timetable_db["service_types"].find_one({"_id": "service_types"})
    if service_types and service_type in service_types["service_types"]:
        for schedule in service_types["service_types"][service_type]:
            if schedule["start"] == start_location:
                return schedule["departure_times"]
    return "該当するデータがありません"


# 全ての時刻表データを取得
@eel.expose
def get_all_timetables():
    service_types = timetable_db["service_types"].find_one({"_id": "service_types"})
    if service_types and "service_types" in service_types:
        print(service_types["service_types"])
        return service_types["service_types"]
    return {}


# Webディレクトリの初期化
eel.init(os.path.join(os.path.dirname(__file__), "web"))

# アプリケーションを起動
eel.start("index.html", size=(1000, 800), mode="chrome")
