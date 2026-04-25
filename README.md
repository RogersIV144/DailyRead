# DailyRead

DailyRead 是一个 workspace-first 的科研工作流仓库，面向计算机系统、体系结构、分布式系统、网络、安全和 AI systems 方向的论文调研、精读、idea 生成与报告整理。

这个仓库的核心目标不是只存放笔记，而是把从 `paper discovery` 到 `report writing` 的日常研究流程稳定地落在同一个工作区里。

## What This Repository Provides

- 面向 research workflow 的目录骨架
- 可直接在 VS Code / Copilot 中使用的 prompts、instructions、skills
- 统一的 paper / idea / report templates
- 面向多个 research tracks 的配置文件
- 本地校验脚本与索引生成脚本
- 中英文双份使用指南

## Workspace Layout

```text
papers/        论文精读笔记
ideas/         idea 笔记
reports/       调研报告、阶段总结、venue survey
inbox/         临时线索与候选 backlog
index/         自动生成的索引与 catalog
attachments/   可选的 PDF、figure、artifact 等附件
config/        工作流配置与 track presets
templates/     paper / idea / report 模板
.github/       Copilot instructions、prompts、skills
scripts/       校验与索引脚本
.conda/        工作区本地 Python 环境（不纳入 git）
```

## Quick Start

1. 克隆仓库。
2. 用 VS Code 打开仓库根目录。
3. 阅读全局配置 `config/dailyread.yaml`。
4. 按你的研究方向调整 `config/tracks/` 下对应的 track preset。
5. 在 Copilot Chat 里输入 `/`，从现成 skills 开始。

如果 slash commands 没有立刻刷新，重载一次 VS Code 窗口即可。

## Built-in Skills

当前仓库已经提供这些 phase-1 skills：

- `daily-discovery`
- `venue-survey`
- `paper-analyze`
- `idea-synthesis`
- `report-writer`
- `paper-search`
- `extract-paper-images`

## Recommended Workflow

1. 用 `daily-discovery` 做近期论文发现。
2. 用 `venue-survey` 对重点会议做定向调研。
3. 用 `paper-analyze` 产出结构化 paper notes。
4. 用 `idea-synthesis` 从多篇阅读结果中提取 research ideas。
5. 用 `report-writer` 写周报、阶段总结或 topic review。
6. 用 `paper-search` 和 `index/` 回收已有积累，避免重复劳动。

## Templates and Metadata

仓库内置以下模板：

- `templates/deep_paper_note.md`
- `templates/idea_note.md`
- `templates/hybrid_report.md`
- `templates/survey_report.md`

元数据约定：

- 使用 YAML frontmatter
- enum 值统一使用 `snake_case`
- cross-note references 使用稳定 key，而不是文件路径
- 笔记正文采用 mixed-language 风格：中文为主，关键术语保留 English

## Validation and Indexing

仓库内置两个常用脚本：

```powershell
.\.conda\python.exe .\scripts\validate_dailyread.py
.\.conda\python.exe .\scripts\build_indexes.py
```

- `validate_dailyread.py` 用来检查配置、模板、skills、prompts、instructions 是否完整且可发现
- `build_indexes.py` 用来重建 `index/` 下的 catalog 与按 topic / venue / report kind 聚合的索引

## Documentation

- 中文详细指南：`HOW_TO_USE_DAILYREAD_ZH.md`
- English guide: `HOW_TO_USE_DAILYREAD.md`
- 持续执行计划：`IMPLEMENTATION_PLAN.md`

## Git Usage

这个仓库已经适配 SSH 推送。后续常用命令：

```powershell
git status
git add .
git commit -m "your message"
git push
```

如果你在新机器上使用本仓库，优先配置 GitHub SSH key，再绑定：

```powershell
git remote set-url origin git@github.com:RogersIV144/DailyRead.git
```

## Suggested First Session

如果你今天要真正开始用这套工作流，推荐这样启动：

1. 选择一个 track，例如 `ai_systems` 或 `systems`
2. 跑一次 `daily-discovery`
3. 从结果中挑 2 到 3 篇 paper
4. 对最重要的一篇运行 `paper-analyze`
5. 基于 paper note 再运行一次 `idea-synthesis`
6. 最后用 `report-writer` 输出你的阶段总结

这套流程的目标不是一次性做很多，而是把每天的阅读、判断、积累和输出稳定串起来。