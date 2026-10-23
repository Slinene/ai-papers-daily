---
title: Deep Search in Real-World Web Environments
title_zh: 真实 Web 深度搜索基准 OpenDS-World
authors:
- Xiaomin Yu
- Hongliang Chen
- Zhe Huang
- Shilin Yan
- Shao-Rong Su
- Xuqiao Ma
- Feiyang Wang
- Jiayu Chen
- Jiwei Fang
- Yu Yan
affiliations:
- HKUST(GZ)
- Fudan University
- University of Washington
- Imperial College London
- Nanyang Technological University
arxiv_id: '2610.30181'
url: https://arxiv.org/abs/2610.30181
pdf_url: https://arxiv.org/pdf/2610.30181
published: '2026-10-18'
collected: '2026-10-23'
category: Eval
direction: 真实 Web 深度搜索 Agent 基准评测
tags:
- Deep Search
- Web Agents
- Benchmark
- Multimodal
- Tool Use
- OpenDS-World
one_liner: 提出 OpenDS 任务与 200 题基准，12 个前沿模型最好仅 39.0% 准确率，人类 21.1%
practical_value: '- 评估搜索/Agent 时把成本维度纳入主指标：同时记录 tool calls、wall-clock、tool failure
  占比与 budget exhaustion，能发现“高消耗低收益”的执行模式；可在电商搜索 Agent 评测中复刻这套成本与终止分析。

  - 业务证据获取往往跨格式（HTML/PDF/视频/结构化数据）和交互操作，不应只测最终答案；可把“证据获取路径”作为任务设计的一部分，考察 agent 能否完成筛选、时间索引、API
  查询等子步骤。

  - 更多调用和更长耗时不一定带来更高准确率，线上 Agent 应设置预算与早停，并监控低产出轨迹；例如限制搜索步数、对连续失败切换 tool 或终止当前链路。

  - LLM-as-judge 可用较小模型做语义等价判定，但难以暴露中间证据链错误；建议在关键步骤加入 intermediate verification 或
  checkpoints。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 Deep Search 评测主要覆盖静态检索、可控语料或单站导航，没有系统考察真实 Web 的证据获取复杂度：信息分散在多模态（文本/图像/音频/视频）、异构格式（HTML/PDF/WebP/MP3/Parquet）与交互访问（筛选、时间索引、API 查询、虚拟导览）之间。因此需要统一 benchmark，衡量 Agent 在开放 Web 上做端到端研究的能力。

**方法关键点**：
- 定义 OpenDS 任务：从一段真实视频锚点出发，Agent 必须自主搜索、访问、处理并连接多个独立来源的证据，最终给出唯一事实答案；证据位置和访问方式事先不提供。
- OpenDS-World：200 个任务，覆盖文化、日常生活、科学、经济、历史、自然、社会、技术 8 个领域；证据链平均 3.94 个节点，注释覆盖 4 种模态、42 种格式、7 种访问类型。任务由人工构建并经 10 名独立审阅者验证证据有效性与答案唯一性。
- 统一评估：12 个前沿模型在相同工具环境（Search/GUI/Other）与执行预算下运行，每个样本限 3600 秒、100 次工具调用；答案正确性由 Qwen3.8-27B 作为 LLM judge 判定。

**关键结果**：
- 最好模型 GPT-6 Astra 总体准确率 39.0%，Claude Opus 5.5 为 38.0%，Gemini 3.8 Flash 为 36.5%；人类独立解题 1000 次尝试准确率仅 21.1%，且有 42.5% 的任务无人解出。
- 难度分层后，12 个模型平均准确率从 Low 的 39.66% 降至 Medium 23.50%、High 16.76%；最强模型在 High 也只有 24.71%。
- 资源消耗与准确率不线性相关：Gemini 3.8 Flash 的 token 消耗约为 GPT-6 Astra 的 5.22 倍，准确率却更低；tool failure 只占调用次数的 2.83%–9.42%，但消耗了 19.27%–61.90% 的工具执行时间。

**最值得记住的一句话**：真实 Web 深度搜索的主要瓶颈不仅是“搜到”，而是证据获取与长程执行管理；当前最强 Agent 成功率不足 40%，更多 tool calls 和更长耗时并不直接换来准确率。
