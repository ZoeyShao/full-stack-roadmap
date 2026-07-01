# Edtrace Courseware

这层是仿 CS336 的可执行课件源。

## 生成 trace

在 `full-stack-roadmap/` 目录下运行：

```bash
uv run python -m edtrace.execute -m edtrace_lectures.lecture_01
```

这会生成 `var/traces/edtrace_lectures.lecture_01.json`。

也可以一次生成多讲：

```bash
uv run python -m edtrace.execute \
  -m edtrace_lectures.lecture_01 \
     edtrace_lectures.lecture_02 \
     edtrace_lectures.lecture_03
```

## 查看 trace

最省事的方式是运行本项目提供的启动脚本：

```bash
./start-edtrace-viewer.sh
```

脚本会：

1. clone 官方 edtrace viewer 到 `.edtrace-viewer/`。
2. 安装 viewer 的 npm 依赖。
3. 把本项目的 `var/` 软链接到 viewer 里。
4. 在本地启动 Vite dev server。

启动后打开：

```text
http://127.0.0.1:5173/?trace=var/traces/edtrace_lectures.lecture_01.json
```

要看其他讲，把末尾改成对应文件：

```text
var/traces/edtrace_lectures.lecture_02.json
var/traces/edtrace_lectures.lecture_03.json
...
var/traces/edtrace_lectures.lecture_16.json
```

也可以打开 `http://127.0.0.1:5173/`，在输入框里填：

```text
var/traces/edtrace_lectures.lecture_01.json
```

## 手动方式

edtrace 官方查看方式需要 frontend。等价的手动命令是：

```bash
git clone https://github.com/percyliang/edtrace
ln -s "$PWD/var" edtrace/frontend/var
npm --prefix=edtrace/frontend run dev
```

然后打开 `http://127.0.0.1:5173/`，并加载生成的 trace 文件。CS336 lecture repo 使用的也是这个思路：Python lecture 生成 `var/traces/*.json`，再由 edtrace frontend 读取。

## 构建 GitHub Pages 版 viewer

如果要把 edtrace viewer 一起发布到 GitHub Pages，运行：

```bash
./build-edtrace-frontend.sh
```

这会生成 `trace/` 目录，里面包含：

- edtrace viewer 的 production build。
- `var/traces/*.json` trace 文件。

如果你的 GitHub Pages 从 `full-stack-roadmap/` 根目录发布，访问地址会类似：

```text
https://<owner>.github.io/<repo>/trace/?trace=var/traces/edtrace_lectures.lecture_01.json
```

如果你用自定义域名或其他发布路径，也仍然可以用同样的相对 trace 路径：

```text
trace/?trace=var/traces/edtrace_lectures.lecture_01.json
```

## 为什么还保留 HTML

`edtrace_lectures/` 更像课堂演示源；`lessons/` 和 `reference/` 更像课后讲义、练习和复习卡。两者服务不同学习场景。
