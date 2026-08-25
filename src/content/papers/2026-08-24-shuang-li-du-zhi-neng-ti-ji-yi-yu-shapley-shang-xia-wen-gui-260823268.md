---
title: Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic
  Learner
title_zh: 双粒度智能体记忆与 Shapley 上下文归因的多模态学习框架
authors:
- Jieke Wang
- Tiancheng Shen
- Yibo Yang
- Ming-Hsuan Yang
affiliations:
- UC Merced
- Shanghai Jiao Tong University
arxiv_id: '2608.23268'
url: https://arxiv.org/abs/2608.23268
pdf_url: https://arxiv.org/pdf/2608.23268
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: 多模态 Agent 记忆与检索优化
tags:
- Agent Memory
- Multimodal
- Shapley
- Retrieval
- Frozen MLLM
- Credit Assignment
one_liner: 冻结多模态大模型配外部双粒度记忆，用 Shapley 归因优化规则检索，提升科学推理基准
practical_value: '- 检索增强场景中，把“相似度检索”升级为“相似度 + 历史效用”的组合排序：用 Shapley/边际贡献离线计算每个知识条目（规则、策略、案例）的效用，避免上下文里塞进相似但无效甚至误导的条目；推荐系统里可类比给召回
  item 或策略规则打分。

  - 双粒度记忆架构值得直接迁移：实例级 case 与类别级规则/策略分开存储，中间层只从抽象规则生成类别记忆，避免具体样本细节污染类别级归纳；电商/Agent
  中可将用户行为轨迹与商品属性规则、query 意图分存。

  - 概念类别空间无需预定义 taxonomy，用 LLM 在线增量生成类别并序列化更新，动态贴合语料分布；适合电商 query 意图聚类、商品概念动态归类，避免固定分类过粗或过细。

  - 工程上无需梯度更新，只依赖 gold answer 作为监督，可在闭源/端侧模型上快速构建外部记忆；训练时用 temperature 采样 rollouts
  构建记忆，测试时只读，适合低成本复用现有大模型能力。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

## 动机
前沿多模态大模型（MLLM）在科学和数学推理上仍有明显短板，而参数级微调对闭源或端侧模型不可行，纯 prompt 方法又无状态、无法从已解决问题中积累。现有智能体记忆系统往往走两个极端：要么保存原始轨迹/案例，实例绑定强但难以抽象；要么只提炼单层规则，失去具体 grounding。两个关键问题未被解决：类别空间未知时如何组织记忆；多个共同检索到的记忆如何公平分配功劳。

## 方法关键点
DG-Mem 采用双粒度外部记忆：
- **Exemplar memory** 存储实例级记录，包含可迁移的 reasoning_strategy 和 verification_check；
- **Schema memory** 存储类别级 IF-THEN 规则，由 transient reflection store 作为中间层合成，且 schema 合成不直接读取 exemplar 文本，避免实例细节污染类别抽象；
- **在线概念分类器** 增量建立类别空间，不依赖预定义 taxonomy；
- **Stage-2 Shapley 上下文归因**：把同一个问题下共同检索到的规则视为合作博弈玩家，采样规则子集 rollout，计算每条规则的 Shapley 边际贡献作为效用，测试时用“相似度 + 效用”组合排序；
- 全流程无梯度更新，冻结 backbone，仅用 gold answer 作为监督。

## 关键实验
在 MathVista、MMMU、MMMU-Pro 三个多模态推理基准上，用 Qwen3.5-27B、Qwen3.5-122B-A10B、GPT-5-Nano、Gemini-3-Flash 四个 backbone 评测。相比 No-memory 基线，平均提升：GPT-5-Nano +12.5、Gemini-3-Flash +5.2、Qwen3.5-122B-A10B +5.6、Qwen3.5-27B +2.3。消融显示 exemplar 和 schema 分别覆盖不同失败模式，去掉任一粒度都会掉点；去掉 Shapley 效用仅按 similarity 检索，在 MMMU-Pro 上会掉约 2 个百分点。

最值得记住的一句话：**用 Shapley 值把多规则检索的贡献拆开，让检索排序从“相似”变成“相似×历史效用”，同时用双粒度记忆分离实例 grounding 与跨实例抽象。**
