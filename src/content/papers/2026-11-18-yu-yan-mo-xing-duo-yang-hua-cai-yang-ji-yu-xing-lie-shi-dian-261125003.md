---
title: A Model of Diverse Sampling from Language Models
title_zh: 语言模型多样化采样：基于行列式点过程的 PoolDPP
authors:
- Manuel Prada-Corral
- Yahya Emara
- Timothy J. O'Donnell
- Ryan Cotterell
- Tim Vieira
affiliations:
- ETH Zürich
- MPI-IS
- ELLIS Institute Tübingen
- Cornell University
- McGill University
arxiv_id: '2611.25003'
url: https://arxiv.org/abs/2611.25003
pdf_url: https://arxiv.org/pdf/2611.25003
published: '2026-11-18'
collected: '2026-11-21'
category: LLM
direction: LLM 多样化采样 · DPP
tags:
- DPP
- Diverse Sampling
- LLM
- Importance Sampling
- Text Generation
one_liner: 将多样生成形式化为 DPP 子集采样，提出 PoolDPP 在候选池上做重要性加权与 DPP 采样
practical_value: '- 生成式推荐/搜索词推荐可直接复用「候选池 + DPP 子集选择」架构：先用 LLM 生成 N 个候选（如推荐理由、query
  变体、广告文案），再用质量分和语义 embedding 核做 K-DPP 重排，平衡业务指标与多样性。

  - 工程上用 greedy MAP 变体，按边际增益逐个选入 top-K，延迟低、可解释性好，适合线上排序后置层；embedding 相似度可复用离线双塔或 LLM
  embedding，无需额外训练。

  - importance weighting 技巧适用于从粗排/生成分布到目标分布不一致的场景：用 proposal 采样后按目标质量权重修正，不必直接采样复杂目标。

  - 结论「提升多样性不一定牺牲 pass@K」对模糊 query 推荐、多意图搜索建议有直接价值：可增加展示候选项的语义覆盖，而不损害头部质量。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机** 语言模型独立采样常得到高质量但高度重复的集合，样本聚集在相同语义模式周围；温度采样只改变词元分布，不建模输出之间相似性。

**方法** 将多样生成定义为从所有字符串上的 determinantal point process (DPP) 采样 size-K 子集：likelihood 编码质量，embedding 几何结构编码相似输出之间的排斥。精确推断不可行，因此提出 PoolDPP：从易处理的 proposal 分布采样有限候选池，对候选做 importance weighting 逼近目标质量，再在候选池诱导的核上运行 K-DPP 采样；同时提供 greedy MAP 变体用于确定性选择。

**理论** 证明有限样本界，输出与目标 K-DPP 的 KL 散度随池大小 N 以 O(1/N) 收敛。

**结果** PoolDPP 在开放文本生成上扩展质量-多样性前沿；在歧义 text-to-SQL（Ambrosia）上扩展 precision-recall 前沿；在数学推理 GSM8K 上，多样性提升且 pass@K 基本不变。
