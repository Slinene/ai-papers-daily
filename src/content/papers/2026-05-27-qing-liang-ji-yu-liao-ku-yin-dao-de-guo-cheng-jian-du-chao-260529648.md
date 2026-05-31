---
title: 'Verifiable Rewards Beyond Math and Code: Lightweight Corpus-Grounded Process
  Supervision for Factual Question Answering'
title_zh: 轻量级语料库引导的过程监督：超越数学与代码的事实问答可验证奖励
authors:
- Shicheng Fan
- Haochang Hao
- Dehai Min
- Weihao Liu
- Philip S. Yu
- Lu Cheng
affiliations:
- University of Illinois Chicago
arxiv_id: '2605.29648'
url: https://arxiv.org/abs/2605.29648
pdf_url: https://arxiv.org/pdf/2605.29648
published: '2026-05-27'
collected: '2026-05-31'
category: Training
direction: RL 过程奖励 · 事实性增强
tags:
- Process Reward
- Factual QA
- Reinforcement Learning
- Wikipedia Co-occurrence
- Lightweight Verifier
one_liner: 基于维基百科共现统计的轻量过程奖励，替代昂贵神经验证器，高效提升事实问答 RL 训练。
practical_value: '- 对电商知识问答、商品属性确认等事实敏感场景，可借鉴 Wikipedia 共现思路，用领域知识图谱或商品共现统计构建轻量过程奖励，低成本过滤幻觉。

  - 在推荐解释生成或 Agent 多步推理中，将最终奖励细化为句子/步骤级信用分配，结合简单对齐映射到 token 级优势，提升 RL 训练信号密度。

  - 当业务涉及长尾实体（冷门商品、小众品牌）时，统计共现信号比神经验证器更稳定可靠，可作为冷启动奖励的备选方案。

  - 奖励计算只需单次语料查找 + 0.5B 小模型抽取，比 LLM-as-a-judge 快 5 倍以上，适合在线 RL 或高频迭代场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：事实问答中，RL 训练常因奖励粗粒度（仅响应级）或验证器昂贵不可靠（神经模型对罕见实体误判）而失效。

**方法**：提出 CorVer，用 Wikipedia 共现统计替代神经验证器，为推理链中的每个句子分配信用，再通过简单对齐映射到 token 级优势，构成轻量过程奖励。仅需一个 0.5B 抽取器获取主体-客体对，然后查共现次数，以此判断事实支持度。

**结果**：在 3B-14B 的 6 个指令模型、5 个 QA 基准上，30 组实验全部优于原始基线，TriviaQA 平均提升 +4.1pp。与 4 种神经验证器比较，20 组中有 18 组表现更优，且训练速度快 4.8–8.4 倍。
