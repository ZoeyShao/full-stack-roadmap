# Full-Stack Roadmap 2026 学习工作区

这个目录把图片里的路线图扩展成一个可持续学习的教程工作区。

## 怎么开始

1. 打开 [Lecture Trace 课程站](/home/ubuntu/learning/full-stack-roadmap/lectures/index.html?trace=lecture_01)。
2. 从第 0001 课开始，每节课控制在 20-40 分钟。
3. 每学完一节，先做页面里的回忆题，再去读推荐的官方资料。
4. 遇到陌生术语，查 [全栈术语表](/home/ubuntu/learning/full-stack-roadmap/reference/0002-glossary.html)。
5. 每完成一个季度模块，都做对应的项目验收。

## 发布 edtrace viewer

如果要把交互式 lecture trace 一起发布到 GitHub Pages，先运行：

```bash
./build-edtrace-frontend.sh
```

这会生成 `trace/` 静态目录。GitHub Pages 从 `full-stack-roadmap/` 根目录发布时，trace viewer 的访问路径类似：

```text
https://<owner>.github.io/<repo>/trace/?trace=var/traces/edtrace_lectures.lecture_01.json
```

如果要生成完整 GitHub Pages 发布目录，运行：

```bash
./build-github-pages-site.sh
```

详细步骤见 [GITHUB_PAGES.md](/home/ubuntu/learning/full-stack-roadmap/GITHUB_PAGES.md)。

## 目录结构

- `MISSION.md`: 这套学习的目标。
- `RESOURCES.md`: 官方文档和高信任资源。
- `NOTES.md`: 教学偏好和工作记录。
- `edtrace.md`: edtrace 课件生成和查看说明。
- `build-edtrace-frontend.sh`: 生成 GitHub Pages 可发布的 edtrace viewer。
- `build-github-pages-site.sh`: 生成完整 `published-site/` 静态发布目录。
- `GITHUB_PAGES.md`: GitHub Pages 发布步骤。
- `lectures/`: 仿 `./cs336` 的 lecture trace 入口，用 `?trace=lecture_01` 这种方式导航。
- `lessons/`: 16 节短课，按路线图推进。
- `reference/`: 长期复习卡和速查表。
- `trace/`: edtrace viewer 的 production build，可随 GitHub Pages 发布。
- `learning-records/`: 之后用于记录你已经真正掌握的关键理解。

## 学习节奏

这套教程按图片的季度路线组织：

- Q1: 前端基础，React + TypeScript，Git。
- Q2: 后端基础，API，数据库，认证。
- Q3: 云服务，DevOps，IaC，CI/CD，观测。
- Q4: 系统设计，项目，作品集，面试。

重点不是“看完”，而是每一节都能拿出可运行、可解释、可复盘的产物。
