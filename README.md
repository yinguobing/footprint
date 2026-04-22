# Footprint · 足迹

> 简洁直观的出行计划展示界面，数据驱动，智能体友好。

前后端分离的数据驱动模板。页面渲染与数据完全解耦，更新内容只需修改 `data.json`。

从出行计划的展示与比较，到行程安排、旅途照片、GPS 轨迹——`footprint` 为每一段旅程留下清晰的足迹。

## 文件结构

```
51-hiking/
├── index.html    # 前端模板（CSS + JS 渲染引擎）
├── data.json     # 全部数据（目的地、天气、装备、待办）
└── README.md     # 本文件
```

## 快速开始

```bash
# 本地预览
python3 -m http.server 8000
# 打开 http://localhost:8000
```

## 在线演示

```
https://<your-github-username>.github.io/footprint/
```

## 数据更新指南

### 智能体（AI Agent）更新

直接读写 `data.json`，**无需修改 `index.html`**。

**更新天气示例：**
```javascript
// 读取数据
const data = JSON.parse(fs.readFileSync('data.json', 'utf8'));

// 修改五台山 5/1 天气
dest = data.destinations.find(d => d.id === 1);
dest.weather[0] = {
  "d": "5/1", "icon": "☀️", "text": "晴/晴",
  "low": 5, "high": 18, "wind": "北风1-3级"
};

// 保存
data.meta.updated = new Date().toISOString().slice(0,10).replace(/-/g,'年') + '日';
fs.writeFileSync('data.json', JSON.stringify(data, null, 2));
```

### 人工手动更新

用任何文本编辑器打开 `data.json`，编辑后保存即可。

> ⚠️ JSON 格式严格，注意：
> - 字符串用双引号 `"`
> - 最后一个元素后面不能加逗号
> - 可用 [JSONLint](https://jsonlint.com/) 在线校验

## 数据格式说明

### `meta` — 行程元信息
```json
{
  "updated": "2026-04-21",
  "dates": "5.1 — 5.5",
  "people": 2,
  "title": "五一假期 · 徒步露营计划",
  "subtitle": "12个候选目的地 · 5天行程"
}
```

### `recommendation` — 首选推荐
```json
{
  "id": 1,
  "label": "首选推荐",
  "badge": "全程晴好"
}
```
- `id` 对应 `destinations` 中的目的地 ID

### `destinations` — 目的地数组

每个目的地对象：
```json
{
  "id": 1,
  "name": "五台山大朝台",
  "location": "山西忻州 · 五台连穿50km",
  "province": "shanxi",
  "provinceName": "山西",
  "tags": ["⭐天气最佳"],
  "lat": "113.666",
  "lng": "39.043",
  "weather": [
    { "d": "5/1", "icon": "🌧️", "text": "小雨/多云", "low": -2, "high": 11, "wind": "北风1-3级" }
  ],
  "transport": [
    { "type": "✈️", "text": "广州→太原武宿：海航HU7249 ¥760 2h40m" }
  ],
  "transportMeta": {
    "fastest": "约5h",
    "cheapest": "¥580起",
    "bestRoute": "广州✈️五台山机场 → 台怀镇包车",
    "highlight": "九元航空直飞最省"
  }
}
```

**字段说明：**
| 字段 | 说明 |
|------|------|
| `province` | 英文标识：`shanxi`/`yunnan`/`guizhou`/`guangxi`/`hunan`/`guangdong` |
| `icon` | 天气 emoji：`☀️` `🌤️` `⛅` `☁️` `🌧️` `🌦️` `⛈️` |
| `type` | 交通方式 emoji：`✈️` `🚄` `🚗` `🚌` |

### `gear` — 装备清单

```json
{
  "clothing": [{ "name": "UTO羊毛速干衣上衣与裤子", "price": 498 }],
  "hiking": [{ "name": "挪客登山包氦70L", "price": 998 }]
}
```
- `price` 为 `null` 表示价格未确定

### `todos` — 待办事项

```json
[
  { "text": "天气预报（行政区划15天）", "done": true },
  { "text": "装备清单确认", "done": false }
]
```

## 部署

纯静态文件，可部署到任意 Web 服务器：

```bash
# Nginx
sudo cp -r 51-hiking /var/www/html/

# Python 临时服务
python3 -m http.server 80

# 上传至对象存储 / CDN
```

## 技术栈

- **前端**：原生 HTML5 + Tailwind CSS (CDN) + Lucide Icons (CDN)
- **数据**：JSON 文件，fetch API 加载
- **无构建步骤**：无需 npm/webpack，保存即生效
