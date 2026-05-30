---
title: 'UniNote: A Unified Embedding Model for Multimodal Representation and Ranking'
title_zh: UniNote：面向多模态 I2I 检索的统一嵌入与排序模型
authors:
- Jinghan Zhao
- Wenwei Jin
- Anqi Li
- Jintao Tong
- Luya Mo
- Jiawei Li
- Bin Li
- Yao Hu
affiliations:
- Xiaohongshu Inc.
- Shanghai Jiao Tong University
- Huazhong University of Science and Technology
- Beijing Institute of Technology
arxiv_id: '2605.29287'
url: https://arxiv.org/abs/2605.29287
pdf_url: https://arxiv.org/pdf/2605.29287
published: '2026-05-28'
collected: '2026-05-30'
category: RecSys
direction: 多模态嵌入 · 统一检索排序框架
tags:
- Multimodal Embedding
- I2I Retrieval
- Reinforcement Learning
- GRPO
- Matryoshka Representation
- Hard Negative Mining
one_liner: 提出两阶段训练范式，将对比 SFT 与 GRPO 强化学习结合，实现多模态 I2I 检索与相关性排序一体化
practical_value: '- **多任务统一嵌入构建**：将 I2I 检索细化为 10 种具体任务（原子对齐、局部检索、OCR 感知等），通过模态替换与描述生成构造训练对，可直接借鉴用于电商商品多模态检索的统一
  embedding 模型。

  - **两阶段训练解锁检索-排序一体化**：第一阶段用对比 SFT + 多粒度硬负样本挖掘（相似度区间设置 + 规则负样本）训练基础嵌入，第二阶段用 GRPO
  多维度奖励（无关惩罚、基础奖励、绝对/相对位置奖励）直接在嵌入空间优化排序，省去额外重排序模型，适合对延迟敏感的线上召回。

  - **MRL 实现灵活部署**：训练时融入 Matryoshka Loss，可输出 64/512/1024/4096 维嵌入，512 维已接近全维性能，为不同存储与算力约束的工业场景提供按需降维的选择。

  - **在线/离线双模式架构**：高并发小库验证 + 低请求大库检索的部署设计，用一次嵌入同时支持多种下游匹配，大幅降低资源开销，可直接参考用于 Agent 或推荐系统中的实时物品检索。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现代内容平台的物品间检索（I2I）需要同时处理多模态输入、全局语义与局部细节检索、相关性排序和大规模延迟约束。现有 CLIP 双塔模型只支持单模态且缺乏细粒度对齐，MLLM embedding 忽略局部-全局关系，分阶段重排序又带来推理瓶颈。为此，UniNote 旨在用一个统一模型解决检索与排序的融合问题。

**方法关键点**：
- 定义 5 类 10 种 I2I 检索任务（原子对齐、局部检索、语义提取、OCR 感知、内容相关性），并通过数据增强（模态替换、描述生成）和规则硬负样本构建高质量训练集。
- 两阶段训练：阶段一采用对比 SFT，将 Qwen3VL-8B 作为骨干，取 last token 作为嵌入，使用多粒度硬负样本挖掘（相似度区间 0.5-0.7 筛选 + 规则负样本）和 JS 散度对齐 soft 标签；同时融入 Matryoshka Representation Learning 支持多维度输出。
- 阶段二引入基于 GRPO 的相对重排序强化学习，针对 note2note 任务构造重叠度递减的候选序列，设计包含无关惩罚、基础相关性奖励、绝对位置奖励和相对顺序奖励的四维奖励函数，直接在嵌入空间优化排序质量。
- 在线部署采用双模式：高并发流量实时匹配小库进行安全验证，离线人工触发从大库检索 Top-K 相关内容。

**关键实验结果**：
- 在 6.6 万笔记、50 万+ 项目的大规模评测集上，UniNote 在 9 个任务中取得 SOTA，I2Note 的 R@1 从 41.2% 提升至 93.7%，Note2I 的 R@1 从 64.3% 提升至 90.2%。
- 消融显示，规则硬负样本使 R@1 在四个元任务上平均提升 10.7 个百分点；RL 阶段使 note2note 的 P@5 提升 3.4%。
- MRL 实验中 512 维已接近全维 4096 的性能，降维后仍保留 70% 以上能力。
- 在线 A/B 测试：单次嵌入提取实现 85.6% 召回，基线方法需 9.2 倍存储；离线大库检索召回提升 23.5%。
