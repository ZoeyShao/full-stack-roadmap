# GitHub Pages 发布说明

目标：把 `full-stack-roadmap` 发布成一个稳定可访问的网站，包含普通课程页面和 edtrace 交互式 trace viewer。

## 1. 构建发布目录

在 `full-stack-roadmap/` 目录运行：

```bash
./build-github-pages-site.sh
```

它会生成：

```text
published-site/
  index.html
  lectures/
  lessons/
  reference/
  trace/
```

`trace/` 里已经包含 edtrace viewer 和 `var/traces/*.json`。

默认构建假设 GitHub Pages URL 是：

```text
https://<owner>.github.io/full-stack-roadmap/
```

如果你的仓库名不是 `full-stack-roadmap`，构建时设置：

```bash
EDTRACE_BASE_DIR="/<repo>/trace/" ./build-github-pages-site.sh
```

## 2. 发布方式 A：单独建一个 GitHub Pages 仓库

如果你想让这个课程独立成站点，建一个新仓库，例如：

```text
full-stack-roadmap
```

把 `published-site/` 里的内容 push 到仓库根目录，然后在 GitHub 仓库设置里：

```text
Settings -> Pages -> Build and deployment -> Source: Deploy from a branch
Branch: main / root
```

访问地址通常是：

```text
https://<owner>.github.io/full-stack-roadmap/
```

edtrace 第一讲地址是：

```text
https://<owner>.github.io/full-stack-roadmap/trace/?trace=var/traces/edtrace_lectures.lecture_01.json
```

## 3. 发布方式 B：放进已有仓库的 docs 目录

如果你已经有一个仓库，可以把 `published-site/` 内容复制到仓库的 `docs/` 目录，然后在 Pages 设置里选择：

```text
Branch: main / docs
```

访问地址通常是：

```text
https://<owner>.github.io/<repo>/
```

## 4. 本地预览

```bash
python3 -m http.server 8000 -b 127.0.0.1 -d published-site
```

打开：

```text
http://127.0.0.1:8000/
```

edtrace 第一讲：

```text
http://127.0.0.1:8000/trace/?trace=var/traces/edtrace_lectures.lecture_01.json
```

## 5. 重新生成

修改课程或 trace 后，重新运行：

```bash
./build-github-pages-site.sh
```

然后重新提交 `published-site/` 对应的发布内容。
