---
title: 'Studying Without a Syllabus: Task-Agnostic Environment Preprocessing'
title_zh: 无大纲学习：任务无关的环境预处理
authors:
- Vinay Samuel
- Varun Ursekar
- Vijay S. Kalmath
- Apaar Shanker
- Veronica Chatrath
- Yuan Xue
affiliations:
- Scale AI
- University of Maryland, College Park
arxiv_id: '2609.10824'
url: https://arxiv.org/abs/2609.10824
pdf_url: https://arxiv.org/pdf/2609.10824
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: Agent 任务无关环境预处理
tags:
- Task-Agnostic Preprocessing
- LLM Agent
- Environment Adaptation
- Meta-Agent
- Study Budget
- Frozen Solver
one_liner: 提出任务无关环境预处理框架，meta-agent 在无下游任务信息下探索环境生成可复用工件，5/6 基准优于固定流程
practical_value: '- 面对新业务环境（新商品库、新 API 工具、新文档系统）时，可在离线 stage 用 meta-agent 做环境探索与预处理，生成索引、技能手册或
  playbook，而不必等具体任务/用户 query 分布确定；把线上多次采样成本转移到一次性研究阶段。

  - 对异构工具/语料不必固守单一预处理策略：维护一个 workflow archive（包含索引构建、合成实践、技能抽取等），让 meta-agent 根据环境特征自行组合；例如大语料检索用固定
  CORPUS2SKILL 管线，工具环境用 PREPING 类合成实践。

  - 不要迷信研究预算或探索广度：预算增加不总能提升下游 reward，更广泛文件探索未必有效；应监控 artifacts 对下游任务的边际收益，并注意工件可能误导
  solver（如引导到不完整索引），需要验证与回滚机制。

  - 在推荐/搜索冷启动场景下可借鉴 task-agnostic 预处理：无历史行为或标注时，先对环境/语料/工具生成通用辅助（如商品知识图谱、导航树、脚本），待有反馈后再做
  task-informed 微调，形成两级适应。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM agent 在新环境中的表现高度依赖环境预处理（索引、工具、提示等），但现有自动化适应方法需要任务示例、轨迹或反馈来指导构建，冷启动时这些信号不可用。固定 task-agnostic 方法（PREPING 合成实践、CORPUS2SKILL 语料建技能层次）虽无需任务信息，却各自只适配特定环境类型。论文提出开放式“无大纲学习”：agent 在测试前、无下游任务分布知识下，自主探索环境并决定如何准备，生成可复用工件。

## 方法关键点
- 形式化任务无关环境预处理：研究系统 S 接收环境 E 和学习预算 Bstudy，输出修改后的环境 Estudied，包含原环境所有 artifact 及新增的 file-based artifacts（目录、索引、知识库、脚本、工具或 harness 上下文）。
- 冻结 solver：下游 agent 使用 Claude Code harness + Claude Haiku 4.5，权重和 harness 固定，仅通过挂载的研究工件影响其行为。
- Meta-Agent 两个变体：无 archive 的 META-AGENT w/o archive 自主探索并决策；有 archive 的 META-AGENT w/ archive 额外挂载包含 PREPING、CORPUS2SKILL 和通用探索工作流的技能库，可调用、组合或忽略。
- 基线：PREPING（合成实践蒸馏 playbook）和 CORPUS2SKILL（文档聚类为技能层次），分别代表固定策略的两个极端。
- 成本计量：研究成本和测试推理成本分别按 API 美元计，支持预算缩放分析。

## 关键实验
- 六基准：BCP-G（约 10 万文档）、OfficeQA（697 文档）、Harvey LAB（9,288 文档 + 1 工具）、DABStep（7 文件+Python 处理）、Apex Agents（31 个世界）、AppWorld（105+ 工具）。
- 结果：Meta-Agent 变体在 5/6 基准上取得最高 Avg@3 和 Best@3；带 archive 的版本在所有基准排名第一或第二；CORPUS2SKILL 仅在 BCP-G 最优；PREPING 相对 NOSTUDY 在全部 6 个基准均有提升但从未第一。
- 预算缩放：增加研究预算在 OfficeQA、Apex Agents 上不带来持续提升，仅 Harvey LAB 上 meta-agent 随预算上升；说明现有模型缺乏预算跟踪和规划能力。
- 测试时计算：带研究工件的一 rollout（Best@1）通常达到 NOSTUDY 需要 2–8 个 rollouts 才能达到的分数，可节省 1.6–5.5 倍任务时推理成本，但前期研究成本需足够多任务摊薄。
- 可解释性：更广泛探索不总是更好；工件可能误导 solver，例如不完整索引将 agent 引向一般文档而忽略特定输入文件。

## 最值得记住的一句话
任务无关的环境预处理能有效将测试期试错成本转移到研究期，但更贵的准备不一定更好，且工件可能误导——应通过策略选择/归档与验证提升可靠性。
