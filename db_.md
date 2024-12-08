
### JSONファイル一覧

1. **timetable_data.json**
```json
[
  {
    "_id": "service_types",
    "service_types": {
      "2-bus-day": [
        {
          "start": "南大沢キャンパス東",
          "departure_times": ["07:45", "08:40", "09:10", "09:50", "10:35", "12:10", "13:00", "13:50", "14:40", "15:25", "15:55", "17:10", "17:30", "18:45"]
        },
        {
          "start": "南大沢キャンパス西",
          "departure_times": ["07:47", "08:42", "09:12", "09:52", "10:37", "12:12", "13:02", "13:52", "14:42", "15:27", "15:57", "17:12", "17:32", "18:47"]
        },
        {
          "start": "日野キャンパス",
          "departure_times": ["07:50", "08:35", "09:10", "09:50", "10:30", "12:20", "13:00", "13:50", "14:50", "15:20", "16:20", "16:30", "18:00", "18:30"]
        }
      ],
      "3-bus-day-full": [
        {
          "start": "南大沢キャンパス東",
          "departure_times": ["07:40", "07:45", "08:40", "09:10", "09:15", "09:50", "10:30", "10:35", "12:10", "12:20", "13:00", "13:45", "13:50", "14:40", "15:25", "15:30", "15:55", "17:00", "17:10", "17:30", "18:45"]
        },
        {
          "start": "南大沢キャンパス西",
          "departure_times": ["07:42", "07:47", "08:42", "09:12", "09:17", "09:52", "10:32", "10:37", "12:12", "12:22", "13:02", "13:47", "13:52", "14:42", "15:27", "15:32", "15:57", "17:02", "17:12", "17:32", "18:47"]
        },
        {
          "start": "日野キャンパス",
          "departure_times": ["07:50", "08:35", "08:40", "09:10", "08:45", "09:50", "10:30", "11:00", "12:20", "12:50", "13:00", "13:50", "14:40", "14:45", "15:20", "16:20", "16:30", "18:00", "18:05", "18:30"]
        }
      ],
      "3-bus-day-afternoon": [
        {
          "start": "南大沢キャンパス東",
          "departure_times": ["12:10", "12:20", "13:00", "13:45", "13:50", "14:40", "15:25", "15:30", "15:55", "17:00", "17:10", "17:30", "18:45"]
        },
        {
          "start": "南大沢キャンパス西",
          "departure_times": ["12:12", "12:22", "13:02", "13:47", "13:52", "14:42", "15:27", "15:32", "15:57", "17:02", "17:12", "17:32", "18:47"]
        },
        {
          "start": "日野キャンパス",
          "departure_times": ["12:20", "12:50", "13:00", "13:50", "14:40", "14:45", "15:20", "16:20", "16:30", "18:00", "18:05", "18:30"]
        }
      ],
      "1-bus-day": [
        {
          "start": "南大沢キャンパス東",
          "departure_times": ["07:45", "09:10", "10:35", "13:00", "14:40", "15:55", "17:30"]
        },
        {
          "start": "南大沢キャンパス西",
          "departure_times": ["07:47", "09:12", "10:37", "13:02", "14:42", "15:57", "17:32"]
        },
        {
          "start": "日野キャンパス",
          "departure_times": ["08:35", "09:50", "12:20", "13:50", "15:20", "16:30", "18:30"]
        }
      ]
    }
  }
]


```
2. **dates.json**（日付とサービスタイプの関連を管理）

```json
[
  {
    "_id": "dates",
    "dates": {
      "2024-10-01": "2-bus-day",
      "2024-10-02": "3-bus-day-full",
      "2024-10-03": "holiday",
      "2024-10-04": "3-bus-day-afternoon",
      "2024-10-05": "holiday",
      "2024-10-06": "holiday",
      "2024-10-07": "2-bus-day",
      "2024-10-08": "2-bus-day",
      "2024-10-09": "3-bus-day-full",
      "2024-10-10": "3-bus-day-afternoon",
      "2024-10-11": "2-bus-day",
      "2024-10-12": "holiday",
      "2024-10-13": "holiday",
      "2024-10-14": "2-bus-day",
      "2024-10-15": "2-bus-day",
      "2024-10-16": "3-bus-day-full",
      "2024-10-17": "3-bus-day-afternoon",
      "2024-10-18": "2-bus-day",
      "2024-10-19": "holiday",
      "2024-10-20": "holiday",
      "2024-10-21": "2-bus-day",
      "2024-10-22": "2-bus-day",
      "2024-10-23": "3-bus-day-full",
      "2024-10-24": "3-bus-day-afternoon",
      "2024-10-25": "2-bus-day",
      "2024-10-26": "holiday",
      "2024-10-27": "holiday",
      "2024-10-28": "2-bus-day",
      "2024-10-29": "2-bus-day",
      "2024-10-30": "3-bus-day-full",
      "2024-10-31": "3-bus-day-afternoon",
      "2024-11-01": "2-bus-day",
      "2024-11-02": "holiday",
      "2024-11-03": "holiday",
      "2024-11-04": "2-bus-day",
      "2024-11-05": "2-bus-day",
      "2024-11-06": "3-bus-day-full",
      "2024-11-07": "3-bus-day-afternoon",
      "2024-11-08": "2-bus-day",
      "2024-11-09": "holiday",
      "2024-11-10": "holiday",
      "2024-11-11": "2-bus-day",
      "2024-11-12": "2-bus-day",
      "2024-11-13": "3-bus-day-full",
      "2024-11-14": "3-bus-day-afternoon",
      "2024-11-15": "2-bus-day",
      "2024-11-16": "holiday",
      "2024-11-17": "holiday",
      "2024-11-18": "2-bus-day",
      "2024-11-19": "2-bus-day",
      "2024-11-20": "3-bus-day-full",
      "2024-11-21": "3-bus-day-afternoon",
      "2024-11-22": "2-bus-day",
      "2024-11-23": "holiday",
      "2024-11-24": "holiday",
      "2024-11-25": "2-bus-day",
      "2024-11-26": "2-bus-day",
      "2024-11-27": "3-bus-day-full",
      "2024-11-28": "3-bus-day-afternoon",
      "2024-11-29": "2-bus-day",
      "2024-11-30": "holiday",
      "2024-12-01": "holiday",
      "2024-12-02": "2-bus-day",
      "2024-12-03": "2-bus-day",
      "2024-12-04": "3-bus-day-full",
      "2024-12-05": "3-bus-day-afternoon",
      "2024-12-06": "2-bus-day",
      "2024-12-07": "holiday",
      "2024-12-08": "holiday",
      "2024-12-09": "2-bus-day",
      "2024-12-10": "2-bus-day",
      "2024-12-11": "3-bus-day-full",
      "2024-12-12": "3-bus-day-afternoon",
      "2024-12-13": "2-bus-day",
      "2024-12-14": "holiday",
      "2024-12-15": "holiday",
      "2024-12-16": "2-bus-day",
      "2024-12-17": "2-bus-day",
      "2024-12-18": "3-bus-day-full",
      "2024-12-19": "3-bus-day-afternoon",
      "2024-12-20": "2-bus-day",
      "2024-12-21": "holiday",
      "2024-12-22": "holiday",
      "2024-12-23": "2-bus-day",
      "2024-12-24": "2-bus-day",
      "2024-12-25": "holiday",
      "2024-12-26": "holiday",
      "2024-12-27": "holiday",
      "2024-12-28": "holiday",
      "2024-12-29": "holiday",
      "2024-12-30": "holiday",
      "2024-12-31": "holiday",
      "2025-01-01": "holiday",
      "2025-01-02": "holiday",
      "2025-01-03": "holiday",
      "2025-01-04": "holiday",
      "2025-01-05": "holiday",
      "2025-01-06": "1-bus-day",
      "2025-01-07": "2-bus-day",
      "2025-01-08": "3-bus-day-full",
      "2025-01-09": "3-bus-day-afternoon",
      "2025-01-10": "2-bus-day",
      "2025-01-11": "holiday",
      "2025-01-12": "holiday",
      "2025-01-13": "2-bus-day",
      "2025-01-14": "2-bus-day",
      "2025-01-15": "3-bus-day-full",
      "2025-01-16": "3-bus-day-afternoon",
      "2025-01-17": "2-bus-day",
      "2025-01-18": "holiday",
      "2025-01-19": "holiday",
      "2025-01-20": "2-bus-day",
      "2025-01-21": "2-bus-day",
      "2025-01-22": "3-bus-day-full",
      "2025-01-23": "3-bus-day-afternoon",
      "2025-01-24": "2-bus-day",
      "2025-01-25": "holiday",
      "2025-01-26": "holiday",
      "2025-01-27": "2-bus-day",
      "2025-01-28": "2-bus-day",
      "2025-01-29": "3-bus-day-full",
      "2025-01-30": "3-bus-day-afternoon",
      "2025-01-31": "2-bus-day",
      "2025-02-01": "holiday",
      "2025-02-02": "holiday",
      "2025-02-03": "1-bus-day",
      "2025-02-04": "2-bus-day",
      "2025-02-05": "3-bus-day-full",
      "2025-02-06": "3-bus-day-afternoon",
      "2025-02-07": "2-bus-day",
      "2025-02-08": "holiday",
      "2025-02-09": "holiday",
      "2025-02-10": "2-bus-day",
      "2025-02-11": "2-bus-day",
      "2025-02-12": "3-bus-day-full",
      "2025-02-13": "3-bus-day-afternoon",
      "2025-02-14": "2-bus-day",
      "2025-02-15": "holiday",
      "2025-02-16": "holiday",
      "2025-02-17": "2-bus-day",
      "2025-02-18": "2-bus-day",
      "2025-02-19": "3-bus-day-full",
      "2025-02-20": "3-bus-day-afternoon",
      "2025-02-21": "2-bus-day",
      "2025-02-22": "holiday",
      "2025-02-23": "holiday",
      "2025-02-24": "2-bus-day",
      "2025-02-25": "2-bus-day",
      "2025-02-26": "3-bus-day-full",
      "2025-02-27": "3-bus-day-afternoon",
      "2025-02-28": "2-bus-day"
    }
  }
]

```

### 各JSONファイルの説明

- **timetable_data.json**:
  - 特定のサービスタイプの中には、時刻表が出発地点ごとに定義されています。
  - 例: `"2_bus_day"`には、そのサービスタイプの日の出発時刻が、出発地点ごとに格納されています。

- **dates.json**:
  - 日付ごとにその日のサービスタイプ（運行パターン）が指定されています。
  - このファイルを参照して、指定された日付のサービスタイプを決定できます。

### 使い方のイメージ

1. **日付と出発地点が指定されたとき**:
   - `dates.json`を参照して、その日付に対応するサービスタイプを取得します。
   - 次に、該当する出発地点のサービスタイプの出発時刻を取得して表示します。

- 日付と出発地点を受け取って、時刻表を返却する関数
  - 日付を受け取ってサービスタイプを返却する関数

---

db関連コマンド
```
docker exec -i mongo_container mongoimport --db bus_timetable_db --collection service_types --drop --jsonArray --file /docker-entrypoint-initdb.d/timetable_data.json
```

```
docker exec -i mongo_container mongoimport --db bus_date_db --collection dates --drop --jsonArray --file /docker-entrypoint-initdb.d/date.json
```

```
# 指定された日付と出発地点に基づいてバスの時刻表を取得する関数
function get_timetable(date_str, start_location):
    # ステップ 1: bus_date_db データベースから指定日付に対応するサービスタイプを取得
    date_entry = bus_date_db.dates.find_one({ "_id": "dates", "dates." + date_str: { "$exists": True } })
    
    if date_entry is None:
        return "指定した日付に対応するサービスはありません。"
    
    service_type = date_entry["dates"][date_str]  # 例: "2-bus-day"
    
    # ステップ 2: bus_timetable_db データベースからサービスタイプに対応する時刻表を取得
    service_types_data = bus_timetable_db.service_types.find_one({ "_id": "service_types" })
    
    if service_types_data is None:
        return "該当するデータがありません"
    
    # サービスタイプに対応する出発地点の時刻表を取得
    service_schedule = service_types_data["service_types"].get(service_type, [])
    
    # ステップ 3: 指定された出発地点の出発時刻を検索
    for entry in service_schedule:
        if entry["start"] == start_location:
            return entry["departure_times"]  # 出発時刻リストを返す
    
    return "該当するデータがありません"

```

