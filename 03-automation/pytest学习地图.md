# pytest 完整学习地图

> 先看全貌，再逐个练。每条 = 讲一点 → 写 → 跑 → 提交。

## 一、基础 ✅

| # | 知识点 | 状态 |
|---|---|---|
| 1 | 命名规则：文件 `test_*.py`、函数 `test_*` | ✅ |
| 2 | 断言 `assert` | ✅ |
| 3 | 运行方式：`pytest` / `pytest 文件` / `-v` | ✅ |
| 4 | 读输出：passed / failed / 失败定位 | ✅ |

## 二、参数化 ✅

| # | 知识点 | 状态 |
|---|---|---|
| 5 | `@pytest.mark.parametrize` 单参数 | ✅ |
| 6 | 多参数 | ⬜ |
| 7 | 从文件读数据（YAML/CSV）做参数化 | ⬜ |

## 三、Fixture

| # | 知识点 | 状态 |
|---|---|---|
| 8 | `@pytest.fixture` 基础 | ✅ |
| 9 | `yield`（前置 + 后置清理） | ⬜ |
| 10 | 作用域 scope（function/class/module/session） | ⬜ |
| 11 | `conftest.py`（跨文件共享 fixture） | ⬜ |
| 12 | `autouse=True`（自动使用） | ⬜ |

## 四、标记 Mark

| # | 知识点 | 状态 |
|---|---|---|
| 13 | `@pytest.mark.skip` / `skipif`（跳过） | ⬜ |
| 14 | `@pytest.mark.xfail`（预期失败） | ⬜ |
| 15 | 自定义标记（`@pytest.mark.smoke`） | ⬜ |
| 16 | `-m` 按标记选择运行 | ⬜ |

## 五、组织与配置

| # | 知识点 | 状态 |
|---|---|---|
| 17 | 目录结构：`api/` + `testcases/` 分层 | ⬜ |
| 18 | 配置管理：`config.py` / 环境切换 | ⬜ |
| 19 | `pytest.ini` / `pyproject.toml` 配置 | ⬜ |
| 20 | 测试数据与代码分离 | ⬜ |

## 六、报告

| # | 知识点 | 状态 |
|---|---|---|
| 21 | `pytest-html` 生成 HTML 报告 | ⬜ |
| 22 | `allure` 报告 | ⬜ |
| 23 | 失败时输出日志 / 请求响应 | ⬜ |

## 七、进阶

| # | 知识点 | 状态 |
|---|---|---|
| 24 | 失败重试 `pytest-rerunfailures` | ⬜ |
| 25 | 并发执行 `pytest-xdist` | ⬜ |
| 26 | 数据驱动（数据文件 → 用例） | ⬜ |

## 八、CI 集成

| # | 知识点 | 状态 |
|---|---|---|
| 27 | Jenkins 跑 pytest + 出报告 | ⬜ |

---

## 学习顺序

```
基础 ✅ → 参数化 ✅ → Fixture → Mark → 组织与配置
   → 报告 → 进阶 → CI 集成
```
