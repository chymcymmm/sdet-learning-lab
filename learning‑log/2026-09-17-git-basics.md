# 2026-09-17｜Git 基础流程

## 一、核心心智模型：四个区

```text
工作区          暂存区          本地仓库         远程仓库
（改代码）  →  （挑选）      →  （存档）      →  （上传）
  E:\...        staging         .git            GitHub
```

## 二、三条命令 = 三跳

### 1. add —— 放进暂存区

```powershell
git add -A
```

| 部分 | 意思 |
|---|---|
| `git` | 执行 git 命令 |
| `-C 路径` | 在指定目录里执行（等于先 `cd` 过去） |
| `add` | 把改动加入**暂存区** |
| `-A` | **A**ll，所有改动（新增 + 修改 + 删除） |

> 暂存区 = **购物车**。先把要提交的东西挑进来。

### 2. commit —— 存成一个版本

```powershell
git commit -m "d01: python 环境 + 函数练习"
```

| 部分 | 意思 |
|---|---|
| `commit` | 把暂存区的内容**存成一个版本** |
| `-m "..."` | **m**essage，这个版本的说明文字 |

> commit = **结账存档**。以后随时能回到这个版本。

### 3. push —— 推到 GitHub

```powershell
git push origin main
```

| 部分 | 意思 |
|---|---|
| `push` | 推送（上传） |
| `origin` | **远程仓库的名字**（默认叫 origin，就是 GitHub 仓库） |
| `main` | **分支名**（主分支） |

> push = **把本地存档同步到云端**。

## 三、为什么分 add 和 commit 两步？

因为**可以挑**。改了 3 个文件，只想提交其中 2 个：

```powershell
git add 文件1 文件2      # 只挑这两个
git commit -m "..."
```

`add -A` 只是"全都要"的偷懒写法。

## 四、一句话总结

```text
add     → 把改动放进购物车
commit  → 结账，存成一个版本
push    → 把版本同步到 GitHub
```

**固定顺序：改代码 → add → commit → push。**
