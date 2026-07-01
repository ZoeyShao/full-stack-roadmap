from __future__ import annotations

from edtrace import link, note, text


LECTURES = {
    "lecture_01": {
        "quarter": "Q1 Frontend Fundamentals",
        "title": "Web 是怎样工作的",
        "lesson": "lessons/0001-how-the-web-works.html",
        "reference": "reference/0003-frontend-cheatsheet.html",
        "primary": ("MDN Learn web development", "https://developer.mozilla.org/en-US/docs/Learn_web_development"),
        "mission": "建立浏览器、URL、DNS、HTTP、HTML/CSS/JS 的整体地图。",
        "steps": [
            "从 URL 拆出 protocol、host、path 和 query。",
            "说明 DNS、TCP/TLS、HTTP request/response 的作用。",
            "解释 HTML、CSS、JS 分别进入 DOM、CSSOM 和交互逻辑。",
            "用 DevTools Network 验证一次页面加载。",
        ],
        "deliverable": "画出从输入 URL 到页面可交互的流程图。",
    },
    "lecture_02": {
        "quarter": "Q1 Frontend Fundamentals",
        "title": "HTML、CSS、JavaScript 基础闭环",
        "lesson": "lessons/0002-html-css-js-foundations.html",
        "reference": "reference/0003-frontend-cheatsheet.html",
        "primary": ("MDN Learn web development", "https://developer.mozilla.org/en-US/docs/Learn_web_development"),
        "mission": "用一个最小页面连通语义结构、样式和交互。",
        "steps": [
            "用语义 HTML 写内容结构。",
            "用 CSS 盒模型、层叠和选择器控制展示。",
            "用 JavaScript 监听表单提交。",
            "把 DOM 更新作为交互反馈。",
        ],
        "deliverable": "一个无框架 HTML/CSS/JS 小页面。",
    },
    "lecture_03": {
        "quarter": "Q1 Frontend Fundamentals",
        "title": "布局、响应式和可访问性",
        "lesson": "lessons/0003-layout-responsive-accessibility.html",
        "reference": "reference/0003-frontend-cheatsheet.html",
        "primary": ("W3C WAI Accessibility Intro", "https://www.w3.org/WAI/fundamentals/accessibility-intro/"),
        "mission": "做出能在移动端和桌面端使用，也能被键盘操作的页面。",
        "steps": [
            "一维排列优先考虑 Flexbox。",
            "二维页面骨架优先考虑 Grid。",
            "用 mobile-first media query 扩展布局。",
            "检查 label、focus、alt、错误提示和键盘路径。",
        ],
        "deliverable": "一个响应式且键盘可用的页面。",
    },
    "lecture_04": {
        "quarter": "Q1 Frontend Fundamentals",
        "title": "React + TypeScript 组件模型",
        "lesson": "lessons/0004-react-typescript-components.html",
        "reference": "reference/0004-react-typescript-cheatsheet.html",
        "primary": ("React Learn", "https://react.dev/learn"),
        "mission": "把静态 UI 拆成组件树，用类型表达组件边界。",
        "steps": [
            "用 Thinking in React 从设计稿提取组件。",
            "用 props 表达只读输入。",
            "用 state 表达会随交互变化的数据。",
            "用 TypeScript 给 props、事件和 API 数据建模。",
        ],
        "deliverable": "一个有类型的 React 组件树。",
    },
    "lecture_05": {
        "quarter": "Q1 Frontend Fundamentals",
        "title": "React 状态、表单、数据获取和测试",
        "lesson": "lessons/0005-react-state-forms-query-tests.html",
        "reference": "reference/0004-react-typescript-cheatsheet.html",
        "primary": ("TanStack Query React Docs", "https://tanstack.com/query/latest/docs/framework/react/overview"),
        "mission": "处理真实前端常见状态：表单、本地状态、服务端状态和测试。",
        "steps": [
            "区分 local state 和 server state。",
            "用 queryKey 定义缓存身份。",
            "mutation 成功后刷新相关 query。",
            "用测试覆盖用户关键流程。",
        ],
        "deliverable": "一个带数据获取和测试的 React 页面。",
    },
    "lecture_06": {
        "quarter": "Q1 Frontend Fundamentals",
        "title": "Git 分支、提交和协作",
        "lesson": "lessons/0006-git-branching-commits.html",
        "reference": "reference/0001-roadmap-master-plan.html",
        "primary": ("Pro Git Book", "https://git-scm.com/book/en/v2"),
        "mission": "让变更历史可理解、可回退、可 review。",
        "steps": [
            "为一个功能建立独立 branch。",
            "把修改拆成有意义的 commit。",
            "用 merge 或 rebase 整理历史。",
            "在 PR 描述中说明目的、变更和验证。",
        ],
        "deliverable": "一段可 review 的 Git 提交历史。",
    },
    "lecture_07": {
        "quarter": "Q2 Backend Fundamentals",
        "title": "后端运行时与 HTTP API",
        "lesson": "lessons/0007-backend-runtime-http-api.html",
        "reference": "reference/0005-backend-api-database-cheatsheet.html",
        "primary": ("Node.js Learn", "https://nodejs.org/learn"),
        "mission": "理解后端服务如何接收请求、执行业务逻辑并返回响应。",
        "steps": [
            "建立 request 和 response 的心智模型。",
            "把 URL 映射到 route handler。",
            "用 middleware 处理通用逻辑。",
            "统一错误响应和日志。",
        ],
        "deliverable": "一个最小 HTTP API 服务。",
    },
    "lecture_08": {
        "quarter": "Q2 Backend Fundamentals",
        "title": "CRUD API 设计",
        "lesson": "lessons/0008-crud-api-design.html",
        "reference": "reference/0005-backend-api-database-cheatsheet.html",
        "primary": ("MDN HTTP", "https://developer.mozilla.org/en-US/docs/Web/HTTP"),
        "mission": "把业务对象变成稳定 API 合约。",
        "steps": [
            "把业务名词映射成 REST resource。",
            "用 HTTP method 表达动作。",
            "为成功和失败设计状态码。",
            "补齐验证、分页、幂等和错误结构。",
        ],
        "deliverable": "一份 CRUD API 合约。",
    },
    "lecture_09": {
        "quarter": "Q2 Backend Fundamentals",
        "title": "SQL 数据建模与查询",
        "lesson": "lessons/0009-sql-database-modeling.html",
        "reference": "reference/0005-backend-api-database-cheatsheet.html",
        "primary": ("PostgreSQL Tutorial", "https://www.postgresql.org/docs/current/tutorial.html"),
        "mission": "从业务实体设计表、关系、约束和查询。",
        "steps": [
            "找实体，定义 primary key。",
            "找关系，定义 foreign key。",
            "用 join 读取跨表数据。",
            "用索引和事务保护性能与一致性。",
        ],
        "deliverable": "一份数据库 schema 和核心 SQL。",
    },
    "lecture_10": {
        "quarter": "Q2 Backend Fundamentals",
        "title": "认证、Session、JWT 与 OAuth",
        "lesson": "lessons/0010-auth-sessions-jwt-oauth.html",
        "reference": "reference/0006-auth-security-cheatsheet.html",
        "primary": ("RFC 7519 JSON Web Token", "https://datatracker.ietf.org/doc/html/rfc7519"),
        "mission": "分清认证、授权和会话，并知道常见安全风险。",
        "steps": [
            "认证回答你是谁。",
            "授权回答你能做什么。",
            "Session 更适合同域传统 Web。",
            "JWT 是签名 claims，不是加密存储。",
            "OAuth 用于授权第三方访问资源。",
        ],
        "deliverable": "一份认证授权流程图和安全检查清单。",
    },
    "lecture_11": {
        "quarter": "Q3 Cloud + DevOps",
        "title": "云服务积木",
        "lesson": "lessons/0011-cloud-building-blocks.html",
        "reference": "reference/0007-cloud-devops-cheatsheet.html",
        "primary": ("AWS S3 User Guide", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"),
        "mission": "理解 S3、CloudFront、Lambda、API Gateway 如何拼成云上应用。",
        "steps": [
            "S3 存对象和静态资源。",
            "CloudFront 在边缘分发内容。",
            "Lambda 执行事件驱动函数。",
            "API Gateway 暴露 HTTP 入口。",
            "IAM 控制谁能访问什么。",
        ],
        "deliverable": "一个云上全栈架构草图。",
    },
    "lecture_12": {
        "quarter": "Q3 Cloud + DevOps",
        "title": "Infrastructure as Code 与 Terraform",
        "lesson": "lessons/0012-infrastructure-as-code-terraform.html",
        "reference": "reference/0007-cloud-devops-cheatsheet.html",
        "primary": ("Terraform Docs", "https://developer.hashicorp.com/terraform/docs"),
        "mission": "用代码声明基础设施，使环境可审查、可复现。",
        "steps": [
            "provider 连接云平台 API。",
            "resource 声明要管理的资源。",
            "plan 显示将要变化什么。",
            "apply 执行变化。",
            "state 记录真实资源映射。",
        ],
        "deliverable": "一份 Terraform 计划说明。",
    },
    "lecture_13": {
        "quarter": "Q3 Cloud + DevOps",
        "title": "CI/CD 流水线",
        "lesson": "lessons/0013-ci-cd-pipelines.html",
        "reference": "reference/0007-cloud-devops-cheatsheet.html",
        "primary": ("GitHub Actions Docs", "https://docs.github.com/en/actions"),
        "mission": "把测试、构建和部署自动化成质量门禁。",
        "steps": [
            "PR 上运行 lint、typecheck、test、build。",
            "main 分支合并后部署 staging。",
            "用 secrets 管理敏感信息。",
            "部署后运行 smoke test。",
        ],
        "deliverable": "一份 GitHub Actions workflow 草稿。",
    },
    "lecture_14": {
        "quarter": "Q3 Cloud + DevOps",
        "title": "日志、指标和告警",
        "lesson": "lessons/0014-observability-logs-metrics-alerts.html",
        "reference": "reference/0007-cloud-devops-cheatsheet.html",
        "primary": ("Amazon CloudWatch User Guide", "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html"),
        "mission": "用日志、指标和告警定位线上问题。",
        "steps": [
            "日志回答一次请求发生了什么。",
            "指标回答整体趋势如何。",
            "告警只应该叫醒需要人处理的问题。",
            "SLO 把可靠性目标量化。",
        ],
        "deliverable": "一份最小观测方案。",
    },
    "lecture_15": {
        "quarter": "Q4 Systems, Projects, Interviews",
        "title": "系统设计基础",
        "lesson": "lessons/0015-system-design.html",
        "reference": "reference/0008-system-design-portfolio-interview.html",
        "primary": ("AWS Well-Architected Framework", "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html"),
        "mission": "用需求、数据、流量、组件和取舍组织系统设计回答。",
        "steps": [
            "澄清功能需求和非功能需求。",
            "定义 API 和核心流程。",
            "估算容量和流量。",
            "画高层架构并解释取舍。",
            "补充安全、可靠性和观测。",
        ],
        "deliverable": "一份系统设计答题稿。",
    },
    "lecture_16": {
        "quarter": "Q4 Systems, Projects, Interviews",
        "title": "项目、作品集和面试表达",
        "lesson": "lessons/0016-projects-portfolio-interviews.html",
        "reference": "reference/0008-system-design-portfolio-interview.html",
        "primary": ("GitHub Pages Docs", "https://docs.github.com/en/pages"),
        "mission": "把项目打磨成别人能理解、能信任、能追问的作品。",
        "steps": [
            "README 说明问题、功能、技术栈和运行方式。",
            "Demo 展示核心用户流程。",
            "作品集突出你的职责和取舍。",
            "简历 bullet 写结果，不只写技术名词。",
        ],
        "deliverable": "作品集项目页、Demo 脚本和简历 bullet。",
    },
}


def _bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render(trace: str) -> None:
    lecture = LECTURES[trace]
    title = lecture["title"]  # @inspect title
    quarter = lecture["quarter"]  # @inspect quarter
    deliverable = lecture["deliverable"]  # @inspect deliverable

    text(f"# {title}\n\n{quarter}")
    text(f"**本讲使命：** {lecture['mission']}")

    note("先尝试从记忆解释本讲概念，再打开短课和官方资料。这样会比直接阅读更能建立长期记忆。")

    text("## 学习路径\n\n" + _bullets(lecture["steps"]))
    text(f"## 交付物\n\n{deliverable}")

    text(
        "## 配套材料\n\n"
        f"- 短课：`{lecture['lesson']}`\n"
        f"- 速查：`{lecture['reference']}`"
    )

    label, url = lecture["primary"]
    text("## 主资料")
    link(title=label, url=url)

    text(
        "## 课后回忆\n\n"
        "1. 不看笔记，说出本讲最重要的三个概念。\n"
        "2. 解释本讲交付物为什么能证明你学会了。\n"
        "3. 把不确定的问题记下来，下一轮问 agent。"
    )
