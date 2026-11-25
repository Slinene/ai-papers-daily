---
title: 'LARF: Learning-aligned Reasoning Framework for Search Relevance'
title_zh: LARF：面向搜索相关性的学习对齐推理框架
authors:
- Tian Tang
- Guo Chen
- Reed Li
- Hao Wang
- Yu Lu
- Haijin Liang
- Haibo Shi
affiliations:
- Yuanbao Team, Tencent
- Southwest University
arxiv_id: '2611.32125'
url: https://arxiv.org/abs/2611.32125
pdf_url: https://arxiv.org/pdf/2611.32125
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: LLM 搜索相关性排序 · 推理蒸馏
tags:
- LLM
- Search Relevance
- GRPO
- Knowledge Distillation
- CoT
- NDCG
one_liner: 三阶段框架——引导式CoT SFT、判别式GRPO+margin、双头蒸馏——提升相关性分级并降延迟
practical_value: '- 在电商搜索相关性、广告质量分等多档排序任务中，可借鉴对 terminal relevance token 加 hinge margin
  loss：显式拉开正确档位与最强竞争档位的 logits 差，解决相邻档位易混问题，比单纯轨迹级 reward 更直接。

  - 冷启动数据选择值得复用：主题分层覆盖 + 各档位密度保留 + 错误样本/高熵样本挖掘，只用 1/3 数据即可超过全量 SFT，显著降低标注成本；配合 multi-agent
  生成维度化 rationale 后再用一致性 checker 筛掉低质样本，能提升训练信号质量。

  - 双头蒸馏适合在线精排：保留生成头只在训练期提供推理监督，上线路只走多维分类头。文中 8B 教师蒸馏到 1.7B 学生后，延迟从 5.68s/pair 降到
  0.97s/pair，精度还略高于原 8B 非推理 backbone，可迁移到电商/广告的轻量 reranker 或精排模型。

  - GRPO 奖励分解可参考：attribute-wise 用 exp(-|label diff|) 平滑监督各子维度，list-wise 用 query 组内
  PNR 零中心化并按组大小加权，rule-consistency 对推理与标注原则冲突给予 -1 惩罚，三者组合能改善推理一致性和排序质量。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM 用于搜索相关性估计面临三个矛盾：SFT 只学标签映射、缺少对判断依据的监督；轨迹级 GRPO 奖励对最终档位 token 的监督过于稀疏，难以区分相邻相关性档位；CoT 推理在线延迟过高，无法直接部署。因此需要把推理作为训练期信号，同时显式优化终端决策，并蒸馏出高效分类模型。

**方法关键点**  
- **Cold-Start SFT with Guided CoT**：通过分层主题覆盖、相关性类别密度、错误样本与高熵样本挖掘构建约 1/3 训练数据的精选子集；用 multi-agent 生成语义相关性、内容质量、来源权威、时效四维 rationale，并经过 hallucination checker 筛选。只使用 1/3 数据即可超过全量 SFT。
- **Discriminative GRPO with Margin Alignment**：奖励分解为 attribute-wise（子维度指数衰减差）、list-wise（query 组内 PNR 零中心化，按组大小加权）、rule-consistency（推理与标注规则一致性 ±1）三部分；同时对终端 relevance token 的 logits 加 hinge margin loss，显式扩大正确档位与最强竞争档位的边界。
- **Dual-head Knowledge Distillation**：共享 backbone 上同时保留多维分类头和辅助生成头；训练时用 GRPO 教师生成的 rationale 做生成蒸馏，推理时丢弃生成头，仅用分类头做单次非自回归前向。

**关键实验**  
在约 300K 训练、16K 测试的 6 档 web search relevance 基准上，LARF-8B 将 fine-grained accuracy 从 45.20% 提升到 50.98%，NDCG 从 74.51 提升到 79.56，超过 30 倍参数量的 Qwen3-235B-A22B-Instruct。部署的 LARF-1.7B 学生在 Yuanbao AI Search A/B 测试中高满意度率 +1.77%，低满意度率 -3.22%。分类-only 服务路径延迟从 5.68s/pair 降至 0.97s/pair，降幅 82.9%。

**最值得记住的一句话**  
把 CoT 作为训练期表征增强和决策边界监督的信号，最终用分类头在线服务，并用 margin loss 直接拉开相邻档位，是搜索相关性建模中兼顾效果与延迟的关键思路。
