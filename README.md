# SDET Learning Lab

> 用一个真实测试项目，把测试能力、技术能力和工程能力持续串起来。

## 01｜项目定位

这个仓库不是单纯的 Python 学习笔记，而是我的 **SDET 实践实验室**。

核心思路：

**基础知识 → 真实测试 → 问题分析 → 实际产物 → Git 沉淀**

每天学到的知识，都尽量马上放进真实接口或业务场景中使用。

---

## 02｜核心实践项目

### Ruffwear 小程序 API

以实际 OpenAPI 接口作为主要练习对象，围绕：

**登录 · 用户 · 会员 · 订单 · 积分 · 优惠券 · 售后 · 退款 · 积分商城 · 地址 · 宠物 · 跨系统同步**

逐步完成从手工测试到自动化、工程化的完整过程。

---

## 03｜能力地图

| 能力 | 学习重点 | 最终产物 |
|---|---|---|
| 测试 | 需求、风险、场景、状态机、回归 | 用例 / 风险分析 |
| 管理 | 计划、排期、报告、发布判断 | 测试计划 / 报告 |
| 沟通 | 产品、开发、Bug、风险、进度 | 沟通记录 |
| API | HTTP、OpenAPI、Token、JSON | 接口分析 / API 用例 |
| 编程 | Python、数据处理、异常 | Python 代码 |
| 数据 | SQL、MySQL、数据校验 | SQL / 双断言 |
| 自动化 | Requests、Pytest、Fixture | 自动化测试 |
| 工程化 | Git、Linux、Docker | 工程实践 |
| CI/CD | Jenkins、Pipeline、报告 | Jenkins 项目 |
| 高级测试 | 幂等、并发、异步、一致性 | 专项测试案例 |

---

## 04｜完整测试闭环

```text
需求
 ↓
澄清问题
 ↓
风险分析
 ↓
测试计划
 ↓
测试排期
 ↓
测试设计
 ↓
环境 / 数据准备
 ↓
冒烟 → 功能 / API → 回归
 ↓
缺陷沟通
 ↓
测试报告
 ↓
发布风险判断
```

技术能力逐步嵌入这条链路：

```text
HTTP / API
   ↓
Python
   ↓
Requests
   ↓
Pytest
   ↓
SQL
   ↓
自动化框架
   ↓
Git / Linux / Docker
   ↓
Jenkins / CI/CD
```

---

## 05｜每天怎么学

每天只抓一个主要知识点。

例如：

> 今天学习 HTTP Header

马上进入实际测试：

```text
理解 Header
 ↓
分析真实接口
 ↓
设计正常 / 异常场景
 ↓
执行测试
 ↓
记录问题
 ↓
模拟一次产品 / 开发沟通
 ↓
留下一个测试产物
```

所以沟通、测试计划、排期、报告从一开始就会出现，只是复杂度逐渐增加。

---

## 06｜Jenkins

Jenkins 是后期工程化的重点。

最终目标：

```text
Git
 ↓
Jenkins
 ↓
安装依赖
 ↓
执行 Pytest
 ↓
生成报告
 ↓
保存结果
 ↓
失败定位
```

学习范围：

**Job → Pipeline → Jenkinsfile → 参数化 → 环境变量 → 定时执行 → 报告 → 失败排查**

---

## 07｜仓库结构

```text
sdet-learning-lab/
├── README.md
├── ROADMAP.md
├── DAILY_PROTOCOL.md
│
├── 01-testing/
├── 02-api/
├── 03-python/
├── 04-automation/
├── 05-sql/
├── 06-debugging/
├── 07-advanced/
├── 08-ci/
├── 09-communication/
├── 10-interview/
└── learning-log/
```

每个目录只保存真正产生的成果，不为了“看起来完整”提前堆内容。

---

## 08｜最终目标

最终希望能够独立完成：

**拿需求 → 找风险 → 做计划 → 设计测试 → 测 API → 查数据库 → 写自动化 → 定位问题 → 沟通风险 → 输出报告 → 用 Jenkins 自动执行。**

这就是这个仓库最终要证明的能力。
