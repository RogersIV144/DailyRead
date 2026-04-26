# DailyRead 使用指南

English guide: [HOW_TO_USE_DAILYREAD.md](./HOW_TO_USE_DAILYREAD.md)

## 这个工作区能做什么

这个工作区是一套 workspace-first 的科研工作流，覆盖：

- topic workflow mapping
- paper discovery
- venue survey
- deep paper analysis
- idea generation
- report writing
- 本地 papers / ideas 检索
- 可选的附件与图片整理

所有核心内容都保存在当前仓库里。你不需要依赖外部 Obsidian vault 才能使用这套主工作流。

## 工作区结构

```text
papers/        论文精读笔记
ideas/         idea 笔记
reports/       调研报告、阶段总结、venue survey
inbox/         临时线索、候选论文、待处理 backlog
index/         自动生成的索引与 catalog
attachments/   可选的 PDF、figure、artifact 等附件
config/        工作流配置与 research track 预设
templates/     paper / idea / report 模板
.github/       Copilot instructions、prompts、skills
scripts/       校验与索引脚本
.conda/        工作区本地 Python 环境
```

## 推荐的第一次使用步骤

1. 打开 `config/dailyread.yaml`，先看一遍全局默认配置。
2. 打开 `config/tracks/` 下与你当前方向最相关的 track 文件，按你的兴趣调整 keywords。
3. 如果你希望 slash commands 立刻刷新出来，先重载一次 VS Code 窗口。
4. 然后从下面这些 phase-1 skills 中选一个开始。

## Phase-1 Skills

在聊天里输入 `/`，你应该能看到这些 skills：

- `topic-workflow-map`
- `daily-discovery`
- `venue-survey`
- `paper-analyze`
- `idea-synthesis`
- `report-writer`
- `paper-search`
- `extract-paper-images`

## 推荐工作流顺序

### 1. 先做 topic workflow mapping

当你对一个 topic 还没有整体认知，或者你还说不清它在完整应用链路里扮演什么角色时，用 `topic-workflow-map`。

示例：

- `topic-workflow-map ai systems agentic serving`
- `topic-workflow-map architecture LLM training workflow`

预期输出：

- 一份 workflow report，写入 `reports/`
- 一个相对稳定的 lifecycle / layered stack 梳理
- 一个明确的下游 handoff，告诉你下一步更适合接 `daily-discovery`、`venue-survey` 还是 `paper-analyze`

### 2. 先做近期论文发现

当你想快速扫描一个方向最近值得读的论文时，用 `daily-discovery`。

如果你已经跑过 `topic-workflow-map`，这里应尽量沿用它给出的 layer terminology、focus question 和目标子环节。

示例：

- `daily-discovery ai systems recent inference serving papers`
- `daily-discovery architecture memory hierarchy recent_90d`

预期输出：

- 一份 survey-style discovery report，写入 `reports/`
- 一个 follow-up backlog，告诉你哪些 paper 值得继续深读
- 必要时补充到 `inbox/` 的候选线索

### 3. 再做指定会议调研

当你想围绕某个 venue 或 conference family 做定向调研时，用 `venue-survey`。

如果你已经有 workflow report，就用它来决定该优先看哪些 venue、哪些年份、哪一段技术脉络。

示例：

- `venue-survey ASPLOS recent_5y LLM serving`
- `venue-survey OSDI cluster scheduling`

预期输出：

- 一份 venue survey report，写入 `reports/`
- 重点 paper 列表
- gap map 与后续阅读建议

### 4. 深读单篇论文

当你已经挑出一篇值得认真看的 paper 时，用 `paper-analyze`。

如果同一 topic 已经有 workflow report，深读时要顺手回答：这篇 paper 处在哪一层，解决的是哪一段 lifecycle 的问题。

示例：

- `paper-analyze 2024 OSDI paper about inference serving`
- `paper-analyze arXiv:2401.12345`
- `paper-analyze https://doi.org/...`

预期输出：

- 一篇结构化的 paper note，写入 `papers/<year>/<venue>/`

### 5. 从阅读结果生成 ideas

当你已经有若干 paper notes 或 survey notes，希望把阅读转成 research ideas 时，用 `idea-synthesis`。

workflow report 也可以作为 source note 输入，尤其适合把 idea 锚定到某个明确的 stage / layer / intervention point 上。

示例：

- `idea-synthesis compare these three paper notes for unsolved bottlenecks`
- `idea-synthesis from this venue survey generate candidate ideas`

预期输出：

- 一个或多个 idea notes，写入 `ideas/`

### 6. 把阶段结果写成报告

当你想把 papers、ideas、surveys 收束成阶段总结时，用 `report-writer`。

示例：

- `report-writer weekly report from last week's papers and ideas`
- `report-writer progress review for ai systems reading this month`

预期输出：

- 一篇 report，写入 `reports/`

### 7. 搜索已有笔记

当你想根据 title、topic、venue、paper key 或 tag 找回已有内容时，用 `paper-search`。

示例：

- `paper-search topic memory disaggregation`
- `paper-search OSDI inference serving`

### 8. 收集 figures 或附件

当某篇 paper 有值得保存的 figures、PDF、project page 或 artifact 时，用 `extract-paper-images`。

预期输出：

- 文件或附件引用写入 `attachments/`

## 可复用 Prompts

workspace 里的 prompts 放在 `.github/prompts/`。

当前已经有：

- `Compare Papers`
- `Reading To Report`
- `Survey To Ideas`
- `Group Meeting Brief`

你可以直接在聊天里运行，也可以通过 `Chat: Run Prompt...` 调用。

## Notes 与 Metadata 约定

### Paper Notes

以 `templates/deep_paper_note.md` 为基准。

重点字段：

- `paper_key`
- `year`
- `venue`
- `topics`
- `related_ideas`
- `read_priority`

### Idea Notes

以 `templates/idea_note.md` 为基准。

重点字段：

- `origin_papers`
- `confidence`
- `maturity`
- `next_action`
- `blocking_questions`

### Reports

使用 `templates/workflow_report.md`、`templates/hybrid_report.md` 或 `templates/survey_report.md`。

重点字段：

- `report_kind`
- `trigger`
- `input_notes`
- `takeaways`
- `action_items`

## Python 环境

这个工作区使用本地 `.conda` 环境。

在 PowerShell 中使用：

```powershell
.\.conda\python.exe .\scripts\validate_dailyread.py
.\.conda\python.exe .\scripts\build_indexes.py
```

后续如果你再写 helper scripts，也应该优先复用这套本地 Python 环境，而不是直接用全局 base。

## 校验与索引

### 校验整个工作区

运行：

```powershell
.\.conda\python.exe .\scripts\validate_dailyread.py
```

它会检查：

- 必需目录和文件是否存在
- root config 结构是否齐全
- templates 的 frontmatter 是否完整
- skills 的命名与 description 是否合法
- prompts 和 instructions 的 frontmatter 是否可发现

### 重建索引

运行：

```powershell
.\.conda\python.exe .\scripts\build_indexes.py
```

它会更新 `index/` 下的这些文件：

- `catalog.json`
- `papers-by-topic.md`
- `papers-by-venue.md`
- `ideas-by-topic.md`
- `reports-by-kind.md`

## 如何扩展这套工作流

### 调整研究方向配置

- 编辑 `config/tracks/*.yaml`
- 修改 keywords、arXiv categories、preferred venues

### 增加或修改 prompts

- 在 `.github/prompts/` 下创建或编辑 `.prompt.md` 文件

### 增加或修改 skills

- 在 `.github/skills/` 下创建或编辑 skill 文件夹
- 每个 skill 文件夹里必须有 `SKILL.md`
- `SKILL.md` 里的 `name` 必须和文件夹名字完全一致

### 增加或修改 instructions

- 在 `.github/instructions/` 下创建或编辑 `.instructions.md`
- `description` 要写得足够具体，方便 Copilot 自动发现
- `applyTo` 只在真正适合的文件范围上使用，不要滥配

## 一个实际可执行的日常流程

1. 如果是陌生 topic，先跑一次 `topic-workflow-map`
2. 再对 workflow report 指向的子环节运行 `daily-discovery` 或 `venue-survey`
3. 从生成的 report 里挑 2 到 3 篇最值得读的 paper
4. 对其中最重要的一篇运行 `paper-analyze`
5. 基于新 paper note、workflow report 和 survey/discovery report 运行 `idea-synthesis`
6. 用 `report-writer` 写周报、月报或某个方向的小结
7. 如果你想更新目录视图，再运行一次 `build_indexes.py`

## 如果 slash commands 没有立刻显示出来

1. 重载 VS Code 窗口
2. 检查对应文件是否真的在 `.github/skills/` 或 `.github/prompts/` 下
3. 运行 `validate_dailyread.py`
4. 检查 YAML frontmatter 是否有效，以及 skill `name` 是否和文件夹名一致
