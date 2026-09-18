---
title: 'Confidence Comes from Experience: Experiential Confidence Estimation from
  Reasoning to Agents'
title_zh: 置信源于经验：LLM 与 Agent 的体验式置信度估计
authors:
- Caiqi Zhang
- Xiaochen Zhu
- Chengzu Li
- Yulong Chen
- Dharshan Kumaran
- Nigel Collier
affiliations:
- University of Cambridge
- Google DeepMind
arxiv_id: '2609.17708'
url: https://arxiv.org/abs/2609.17708
pdf_url: https://arxiv.org/pdf/2609.17708
published: '2026-09-14'
collected: '2026-09-18'
category: LLM
direction: 经验驱动 LLM 置信度校准
tags:
- confidence estimation
- calibration
- experience bank
- self-consistency
- LLM agent
- selective prediction
one_liner: 用模型自己的历史验证样本构建经验库，检索相似任务与置信度，校准 LLM 输出置信度，以 1/10 成本匹敌 10 次采样一致性
practical_value: '- 在 LLM 生成商品标题/广告文案/搜索改写等任务中，收集每次生成时的模型自评、置信度和最终效果（点击、转化或人工审核），构建经验库；上线时检索相似任务与相似置信度的历史，看实际成功率，用于决定自动发布还是人工审核。

  - 用 task embedding + 模型自报置信度作为检索键，代替仅靠语义相似度；用历史结果标签微调度量空间（如重加权）可以让检索到“失败原因相似”的案例，而不仅是主题相似。

  - 反思阶段把历史失败教训读给模型，让模型先说出自己的 recurring failure mode 再重估置信度，比单纯让其内省更校准；最终将统计成功率与反思置信度做
  0.5/0.5 等权平均。

  - 经验库需要独立于模型自身判断的结果标签（如用户反馈、人工审核、真实转化），不能用模型自己判断的 label，否则会在模型自信但错误的地方失效；且 lesson
  要隔离，避免后见之明。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 LLM 置信度估计只读当前推理过程（口头置信度、token 概率、自采样一致性），但人类元认知研究表明人会从相似历史事件的结果判断自信。模型常常过度自信，而历史经验可以机械地纠正这种习惯性误判。本文将置信度估计从“读当前推理”转向“读自身经验”。

**方法关键点**：
- **经验库**：存储模型过去 episodes，每个记录包含 task、solution 前的 self-reflection、stated confidence、graded outcome、以及事后由模型自己写下的 lesson；lesson 与当前未评分推理隔离，避免后见之明。
- **Recall**：用 task embedding（frozen off-the-shelf embedder）与 stated confidence 组成 key，在 correctness-supervised 重缩放的空间中检索 top-k=50 最近邻，直接计算历史成功率作为校准估计。
- **Reflect**：将检索到的历史记录（含 lesson）展示给模型，让模型说出 recurring failure mode 并重新给出校准置信度。
- 最终置信度 = (Recall + Reflect) / 2；无需 logit、无需权重更新、仅一次答案生成，格式通用（选择题、代码、多模态与 agent rollout）。

**关键结果**：在 9 个 benchmarks（MMLU-Pro、SuperGPQA、BBEH、OlympiadBench、LiveCodeBench、MMMU-Pro、ScienceWorld、AppWorld、SWE-bench Verified）和 4 个模型（Gemini 2.5/3.5 Flash、Qwen3.5-397B、Claude Sonnet 4.6）上，XConf 在 24 个模型-数据集比较中 23 个 beat or match 10 次采样自一致性，ECE 显著更低（MMLU-Pro 低 3-8 倍），生成成本仅 1/10。在 Agent 任务上，丢弃 10% 最低置信度，成功率最高提升 8.7 点（AppWorld Gemini 3.5 Flash 0.805→0.892）。经验库可跨数据集/模型迁移但跨模型有损失；经验越多校准越好，且训练-free 方法在某些 agent 任务上超过 trained verifier。

最值得记住：**模型的 track record 是强校准信号，用历史成功率 + 反思阅读可以低成本获得高校准置信度。**
