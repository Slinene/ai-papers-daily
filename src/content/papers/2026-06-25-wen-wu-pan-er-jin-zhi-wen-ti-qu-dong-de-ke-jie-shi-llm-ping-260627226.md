---
title: 'Ask, Don''t Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement'
title_zh: 问，勿判：二进制问题驱动的可解释 LLM 评估与自改进
authors:
- Sangwoo Cho
- Kushal Chawla
- Pengshan Cai
- Zefang Liu
- Chenyang Zhu
- Shi-Xiong Zhang
- Sambit Sahu
affiliations:
- Capital One, AI Foundations
arxiv_id: '2606.27226'
url: https://arxiv.org/abs/2606.27226
pdf_url: https://arxiv.org/pdf/2606.27226
published: '2026-06-25'
collected: '2026-06-27'
category: Eval
direction: 可解释 LLM 评估 · 二进制问题分解
tags:
- LLM Evaluation
- Binary Decomposition
- Interpretability
- Prompt Optimization
- Factuality
one_liner: 将评估准则分解为原子化二进制问题，实现可解释、可诊断且支持迭代提示优化的 LLM 评估框架
practical_value: '- **可解释的离线评估体系**：在推荐/搜索场景中，生成式模型输出（如商品推荐理由、搜索摘要、对话式回应）的评估常依赖人类，或使用单一分数（如
  BERTScore）难以定位问题。BINEVAL 的思路可直接复用：将业务评估维度（相关性、信息量、品牌安全、时效性）分解为一组原子化 yes/no 问题，由
  LLM 逐一回答并聚合得分，每个 badcase 都能追溯到具体问题，让离线评估从黑盒变为可诊断的诊断工具。

  - **自动化 Badcase 分类与监控**：线上实验通常只能看到整体指标下跌，不知道哪类问题在增多。可以借鉴 BINEVAL 的二进制问题设计，构建一套自动化质检
  pipeline，对线上采样结果用 yes/no 问题检测是否违背特定规则（如“是否包含虚假价格”“是否推荐已下架商品”），再聚合为各类问题发生率，快速定位系统退化点。

  - **迭代式 Prompt 优化**：在 Agent 或生成式推荐场景，prompt 版本迭代缺乏客观反馈信号。可用 BINEVAL 的“自我更新”或“跨模型更新”模式，对失败样例提取教训并自动改写
  prompt。该 trick 尤其适用：当模型已有能力但未被正确引导时（如格式化输出、关键词包含），通过少量失败样本的二进制反馈即可稳定提升；但对需要精确计数或复杂推理的能力瓶颈，则应避免过度优化，以免
  prompt 膨胀损害其他维度。

  - **评估者模型迁移的对齐**：当从一个大模型（如 GPT-4）迁到较小开源模型作为评估器时，BINEVAL 的跨模型 prompt 更新能利用强大模型的二进制问答结果作为参考，通过找出不一致的二进制问题并提取教训来对齐新模型的评估行为，降低迁移成本并保持评估一致性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
LLM 输出评估仍是 NLP 的瓶颈：人工评估慢且贵，词汇重叠指标不支持开放生成，而整体式 LLM-as-Judge 给出的单一分数难以解释和调试。对于需要快速迭代的推荐/搜索/对话系统，单一标量评分无法指出错误来源，无法驱动针对性的 prompt 优化。

## 方法关键点
- **二进制问题分解**：通过 meta-prompt 将任务提示（如“生成摘要”）自动拆解为一组原子化 yes/no 问题，每个问题对应一个细粒度评估标准（如“所有实体名是否准确？”“是否包含不在原文中的 URL？”），问题附有违反示例以明确定义。
- **可解释打分**：对每个输出，LLM 独立回答所有问题并给出解释，按维度（一致性、连贯性等）聚合 yes 比例得到 [0,1] 分数，可线性缩放到任意区间。分数可追溯到具体问题的 verdict 与 explanation，实现白盒诊断。
- **迭代式 Prompt 优化**：利用二进制问题反馈进行两类更新——① 自我更新：用评估者发现失败问题→提取教训→自动改写生成器 prompt；② 跨模型更新：用强参考评估器的二进制答案对齐弱评估器，通过不一致的问题提取教训并修改目标评估器的 prompt。

## 关键结果
- **SummEval 数据集**：BINEVAL (Claude) 平均 Spearman ρ=0.563，超越 UniEval (T5) 的 0.474 和 G-Eval (GPT-4) 的 0.514，尤其在一致性维度取得 0.655，比 G-Eval 提高近 15 个百分点。二进制分解能捕捉表面合理的文本中的事实错误（如误归属、虚构 URL）。
- **Topical-Chat 对话评估**：BINEVAL 取得最佳平均 Spearman 0.632，表明分解方法对主观性强的对话质量同样有效。
- **QAGS 事实一致性**：BINEVAL 平均 Spearman 0.620，远超 G-Eval (gpt-oss) 的 0.436，证明多问题分解对幻觉检测的鲁棒性。
- **提示优化**：SummEval 评估器自我更新后连贯性 ρ 从 0.521 升至 0.610；跨模型更新将一致性 ρ 从 0.501 升至 0.637。IFBench 生成优化中，格式与句型约束准确率提升 17pp，但计数/比率约束无效，说明优化适用于模型已有能力但缺乏引导的场景，对底层能力边界无效。

## 核心 insight
将宏大的评估任务切成多个可核查的小问题，不仅能获得更贴近人类判断的分数，还能让评价信号变得可解释、可操作，直接服务于 prompt 调试和系统迭代。
