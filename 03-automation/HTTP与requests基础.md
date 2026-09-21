# HTTP 与 requests 基础

> 接口自动化的地基：搞清"一个请求由什么组成"，以及它在 Apifox 和 requests 里分别怎么写。

## 一、一个请求，就 4 个部分

```text
① Method（方法）    →  GET / POST / PUT / DELETE
② URL               →  Path（路径）+ Query（问号后的参数）
③ Header（请求头）   →  Token 等附加信息
④ Body（正文）       →  POST 提交的数据
```

## 二、这 4 部分，在 Apifox 和 requests 里分别怎么写

| HTTP 部分 | Apifox 里 | requests 里 |
|---|---|---|
| **Method** | 左上角下拉选 | `requests.get()` / `requests.post()` |
| **Path** | URL 框 | `requests.get("https://...")` |
| **Query** | **Params** 标签 | `params={...}` |
| **Header** | **Headers** 标签 | `headers={...}` |
| **Body** | **Body** 标签 | `json={...}` |

> Apifox 的"标签名"和 requests 的"参数名"一一对应。

## 三、响应，就 2 个部分

| 响应部分 | Apifox 里 | requests 里 |
|---|---|---|
| **Status Code** | 右上角 `200` | `response.status_code` |
| **Body** | 下方 Body | `response.json()` |

## 四、同一个请求，两种写法

**任务**：GET 请求，带 Query 参数 `platform=wechat`，带 Header `token=abc123`

**Apifox 里：**
```text
Method：GET
URL：   https://httpbin.org/get
Params 标签：platform = wechat
Headers 标签：token = abc123
```

**requests 里：**
```python
import requests

response = requests.get(
    "https://httpbin.org/get",              # Path
    params={"platform": "wechat"},          # Query（Params 标签）
    headers={"token": "abc123"}             # Header（Headers 标签）
)
print(response.status_code)                 # 状态码
print(response.json())                      # Body
```

**Apifox 点"发送" = `requests.get(...)`。**

## 五、记忆口诀

```text
方法      →  requests.get / post
URL       →  第一个参数
Query     →  params={...}      （Params 标签）
Header    →  headers={...}     （Headers 标签）
Body      →  json={...}        （Body 标签）

三个都是字典 {"key": "value"}
```

## 六、用 httpbin 验证参数放哪

httpbin 会把你的请求拆开返回，用来验证参数位置：

| 你传的位置 | 响应的哪个字段 |
|---|---|
| Query 参数 | `args` |
| Header | `headers` |
| Body | `json`（POST） |

## 七、重要认知

- **HTTP 200 ≠ 业务成功**：很多接口业务失败也返回 200，错误码在 Body 里（如 `{"code": 500, "msg": "积分不足"}`）。
- 所以接口测试要**同时看三层**：HTTP 状态码 + 业务 code + 数据。
