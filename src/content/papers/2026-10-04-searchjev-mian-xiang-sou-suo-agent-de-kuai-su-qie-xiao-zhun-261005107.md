---
title: 'SearchJev: A Fast and Calibrated System-1 Model for Search Agents'
title_zh: SearchJev：面向搜索 Agent 的快速且校准良好的 System-1 决策模型
authors:
- Congfeng Cao
- Lipeng Zuo
- Konstantinos Papakostas
- Qiwei Xu
- Songwei Xu
- Lun Zhou
- Zhaochun Ren
- Yougang Lyu
- Xiaohui Yan
affiliations:
- Huawei Technologies Co., Ltd.
- Leiden University
arxiv_id: '2610.05107'
url: https://arxiv.org/abs/2610.05107
pdf_url: https://arxiv.org/pdf/2610.05107
published: '2026-10-04'
collected: '2026-10-06'
category: Agent
direction: Agent 双系统搜索决策加速与校准
tags:
- Search Agent
- System-1
- Calibration
- Dual-System
- Decision Model
- LoRA
one_liner: 将搜索 Agent 中的短决策与 System-2 生成分离，用 schema-conditioned logits 直接输出校准概率，实现
  5.2-5.3 倍决策加速并提升端到端答案准确率
practical_value: '- 把搜索/推荐链路中频繁的短判断（相关性、query 改写是否等价、意图分类、证据充分性、next action）从 LLM
  自回归生成中拆出来，用同一个轻量模型基于 schema-conditioned first-token logits 直接做分类/打分，避免 JSON 解码，可显著降低线上延迟。

  - 借鉴 SLCD：对不确定标注用 soft-label，训练时混合 cross-entropy + Brier loss，并按输出类型（Choice/Score/Noul）做
  temperature calibration；这能提供更可靠的置信度，适合做置信度 gate、拒识或降级。

  - 双系统架构值得迁移：System 1 出低延迟决策 + 置信度阈值，不置信时回退到 System 2（大模型）处理；在电商/广告的召回粗排、query 改写、相关性过滤等场景可以平衡成本与效果。

  - 将异构标注数据统一成 state-schema 格式训练一个多任务决策模型，用 LoRA 微调小模型即可覆盖多种决策类型，降低多模型维护成本；对 unordered
  options 做 permute 可减少位置偏差。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM-based search agents 在轨迹中反复做短决策：文档是否相关、证据是否充分、下一步该搜索还是打开页面。这些判断决定证据的输入与搜索走向，但用生成式 LLM 统一处理会带来顺序解码延迟，且 verbalized 或 token-probability 置信度常常校准不佳。任务特定 reranker/分类器虽快但每种决策都要单独模型和监督，维护成本高。因此需要一个统一、高效且置信度可靠的短决策模型。

## 方法关键点
- **Schema-conditioned 决策读头**：给定 search state 和决策 schema，SEARCHJEV 将每个 legal option 映射到单 token label，读取因果 LM 第一个输出位置的 logits，仅在这些 legal label 上做 softmax，直接得到决策分布，完全避免自回归生成和 JSON 解析。
- **SLCD 训练**：用 soft-label 表示监督不确定性；损失为加权 cross-entropy + Brier loss（两个 proper scoring rules）；对无序选项做 permutation 减少位置偏差；中英文 schema 改写增强；训练后按输出类型拟合 temperature 做置信度校准。
- **双系统 Agent**：System 2 保留 planning、query generation、answer composition；System 1 SEARCHJEV 处理 routing/rewriting/relevance/sufficiency/navigation/verification 六类决策。置信度 gate 用 max prob 与阈值 δ 比较，不置信时交给 System 2，再由 search controller 映射为动作。
- **SearchDecision-Bench**：将多源数据统一为 state-schema 格式，覆盖六类决策和 Choice/Score/Noul 三种输出类型，并划分 ID/OOD 测试集。

## 关键结果
在 SearchDecision-Bench ID 测试上，SEARCHJEV-0.8B/4B 全面优于同尺寸 Qwen3.5 AR (JSON)：relevance NDCG 98.6/99.0 vs 85.7/96.7；sufficiency acc 89.4/96.0 vs 49.9/57.7；routing acc 83.2/86.6 vs 24.7/53.3。平均 ECE 相对同尺寸 AR 模型降低 74.4%/40.7%，决策延迟为 27.6/37.1ms，加速 5.2-5.3×。端到端 BrowseComp-Plus 上，SEARCHJEV-4B 双系统 agent 将答案准确率从 System-2-only 的 45% 提升到 54%，System-2 调用从 90.3 降到 84.6，输出 token 从 73.7k 降到 22.1k，active search time 从 4080s 降到 1102s，加速 3.7×。

**最值得记住的一句话**：把频繁、低延迟的搜索短决策从生成式推理中剥离，用 schema-conditioned logits + soft-label 校准，是同时提升 Agent 效率与置信度可靠性的关键。
