#!/usr/bin/env python3
import json

# 新天气数据 (5/1 - 5/5)
new_weather = {
    "五台山大朝台": [  # 五台县
        {"d": "5/1", "icon": "☁️", "text": "阴/多云", "low": 4, "high": 23, "wind": "东南风1-3级"},
        {"d": "5/2", "icon": "⛅", "text": "多云/多云", "low": 5, "high": 22, "wind": "西南风1-3级"},
        {"d": "5/3", "icon": "⛅", "text": "多云/多云", "low": 8, "high": 26, "wind": "西北风1-3级"},
        {"d": "5/4", "icon": "☁️", "text": "多云/阴", "low": 9, "high": 23, "wind": "西南风1-3级"},
        {"d": "5/5", "icon": "☁️", "text": "阴/阴", "low": 8, "high": 25, "wind": "西南风1-3级"},
    ],
    "大理鸟吊山": [  # 洱源
        {"d": "5/1", "icon": "⛅", "text": "多云/多云", "low": 10, "high": 22, "wind": "北风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 8, "high": 20, "wind": "西南风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/小雨", "low": 9, "high": 20, "wind": "西南风1-3级"},
        {"d": "5/4", "icon": "🌧️", "text": "小雨/小雨", "low": 9, "high": 20, "wind": "东南风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "小雨/多云", "low": 10, "high": 20, "wind": "西南风1-3级"},
    ],
    "阿西里西韭菜坪": [  # 赫章
        {"d": "5/1", "icon": "🌧️", "text": "小雨/多云", "low": 11, "high": 23, "wind": "北风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 10, "high": 16, "wind": "北风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/小雨", "low": 11, "high": 19, "wind": "西北风1-3级"},
        {"d": "5/4", "icon": "☁️", "text": "阴/阴", "low": 11, "high": 19, "wind": "东北风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "小雨/小雨", "low": 13, "high": 22, "wind": "南风1-3级"},
    ],
    "乌蒙东坡": [  # 水城
        {"d": "5/1", "icon": "🌧️", "text": "小雨/多云", "low": 11, "high": 22, "wind": "北风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 11, "high": 20, "wind": "西风1-3级"},
        {"d": "5/3", "icon": "⛅", "text": "多云/小雨", "low": 11, "high": 20, "wind": "北风1-3级"},
        {"d": "5/4", "icon": "☁️", "text": "阴/阴", "low": 11, "high": 19, "wind": "南风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "小雨/小雨", "low": 13, "high": 20, "wind": "东南风1-3级"},
    ],
    "龙脊天路": [  # 六枝
        {"d": "5/1", "icon": "🌧️", "text": "小雨/小雨", "low": 15, "high": 22, "wind": "东南风1-3级"},
        {"d": "5/2", "icon": "⛅", "text": "多云/小雨", "low": 13, "high": 20, "wind": "北风1-3级"},
        {"d": "5/3", "icon": "⛅", "text": "多云/小雨", "low": 14, "high": 22, "wind": "西北风1-3级"},
        {"d": "5/4", "icon": "☁️", "text": "阴/阴", "low": 15, "high": 23, "wind": "东北风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "小雨/小雨", "low": 17, "high": 23, "wind": "东南风1-3级"},
    ],
    "老王山": [  # 六枝 (同龙脊天路)
        {"d": "5/1", "icon": "🌧️", "text": "小雨/小雨", "low": 15, "high": 22, "wind": "东南风1-3级"},
        {"d": "5/2", "icon": "⛅", "text": "多云/小雨", "low": 13, "high": 20, "wind": "北风1-3级"},
        {"d": "5/3", "icon": "⛅", "text": "多云/小雨", "low": 14, "high": 22, "wind": "西北风1-3级"},
        {"d": "5/4", "icon": "☁️", "text": "阴/阴", "low": 15, "high": 23, "wind": "东北风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "小雨/小雨", "low": 17, "high": 23, "wind": "东南风1-3级"},
    ],
    "子花山": [  # 全州
        {"d": "5/1", "icon": "⛅", "text": "多云/小雨", "low": 14, "high": 24, "wind": "南风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 18, "high": 24, "wind": "西南风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/小雨", "low": 17, "high": 21, "wind": "东北风1-3级"},
        {"d": "5/4", "icon": "☁️", "text": "阴/阴", "low": 16, "high": 26, "wind": "东北风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "阴/小雨", "low": 20, "high": 28, "wind": "南风1-3级"},
    ],
    "真穿南": [  # 资源
        {"d": "5/1", "icon": "⛅", "text": "多云/小雨", "low": 13, "high": 23, "wind": "南风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 17, "high": 22, "wind": "西南风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/小雨", "low": 16, "high": 22, "wind": "东北风1-3级"},
        {"d": "5/4", "icon": "⛅", "text": "小雨/多云", "low": 15, "high": 25, "wind": "东风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "阴/小雨", "low": 18, "high": 27, "wind": "南风1-3级"},
    ],
    "南风面": [  # 炎陵
        {"d": "5/1", "icon": "⛅", "text": "多云/多云", "low": 15, "high": 25, "wind": "西北风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 17, "high": 24, "wind": "北风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/小雨", "low": 16, "high": 21, "wind": "西风1-3级"},
        {"d": "5/4", "icon": "🌧️", "text": "小雨/阴", "low": 15, "high": 26, "wind": "西南风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "多云/小雨", "low": 18, "high": 28, "wind": "西北风1-3级"},
    ],
    "瑶峰": [  # 宜章
        {"d": "5/1", "icon": "⛅", "text": "多云/多云", "low": 17, "high": 27, "wind": "西南风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 19, "high": 25, "wind": "南风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/小雨", "low": 18, "high": 24, "wind": "西风1-3级"},
        {"d": "5/4", "icon": "🌧️", "text": "小雨/阴", "low": 15, "high": 27, "wind": "西南风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "阴/小雨", "low": 20, "high": 29, "wind": "南风1-3级"},
    ],
    "黄梅雪后穿越": [  # 曲江
        {"d": "5/1", "icon": "⛅", "text": "多云/晴", "low": 20, "high": 28, "wind": "北风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 19, "high": 27, "wind": "西南风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/阴", "low": 21, "high": 27, "wind": "西南风1-3级"},
        {"d": "5/4", "icon": "⛅", "text": "阴/多云", "low": 19, "high": 29, "wind": "西南风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "小雨/小雨", "low": 22, "high": 30, "wind": "南风1-3级"},
    ],
    "梅子岭古道": [  # 英德
        {"d": "5/1", "icon": "☀️", "text": "晴/多云", "low": 20, "high": 26, "wind": "北风1-3级"},
        {"d": "5/2", "icon": "🌧️", "text": "小雨/小雨", "low": 19, "high": 27, "wind": "西南风1-3级"},
        {"d": "5/3", "icon": "🌧️", "text": "小雨/小雨", "low": 21, "high": 27, "wind": "西南风1-3级"},
        {"d": "5/4", "icon": "⛅", "text": "小雨/多云", "low": 20, "high": 30, "wind": "西风1-3级"},
        {"d": "5/5", "icon": "🌧️", "text": "小雨/小雨", "low": 22, "high": 31, "wind": "南风1-3级"},
    ],
}

# 读取文件
with open('/home/xiaobai/storage/footprint/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 更新天气
for dest in data['destinations']:
    name = dest['name']
    if name in new_weather:
        dest['weather'] = new_weather[name]
        print(f"Updated: {name}")

# 更新 meta
data['meta']['updated'] = '2026年4月25日'

# 保存
with open('/home/xiaobai/storage/footprint/data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")
