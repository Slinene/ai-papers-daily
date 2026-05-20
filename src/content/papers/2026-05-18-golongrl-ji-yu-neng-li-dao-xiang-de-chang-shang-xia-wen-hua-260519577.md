---
title: 'GoLongRL: Capability-Oriented Long Context Reinforcement Learning with Multitask
  Alignment'
title_zh: GoLongRL：基于能力导向的长上下文强化学习与多任务对齐
authors:
- Minxuan Lv
- Tiehua Mei
- Tanlong Du
- Junmin Chen
- Zhenpeng Su
- Ziyang Chen
- Ziqi Wang
- Zhennan Wu
- Ruotong Pan
- jian Liang
affiliations:
- Kuaishou Technology
- University of Chinese Academy of Sciences
arxiv_id: '2605.19577'
url: https://arxiv.org/abs/2605.19577
pdf_url: https://arxiv.org/pdf/2605.19577
published: '2026-05-18'
collected: '2026-05-20'
category: Training
direction: 长上下文RLVR多任务对齐训练
tags:
- RLVR
- Long Context
- Multitask
- GRPO
- Reward Normalization
- Capability Data
one_liner: 提出能力导向的长上下文RLVR数据集和TMN-Reweight多任务优化，使30B模型长上下文性能比肩大模型
practical_value: '- **能力导向的数据构建**：按细粒度长文本能力（如推理、检索、多跳聚合）设计多类型任务和自然评估指标，可直接用于电商搜索或Agent长上下文数据构造，提升生成式推荐对长会话、产品文档的理解。

  - **TMN-Reweight多任务训练技巧**：通过任务级均值归一化消除异构奖励尺度差异，再按难度自适应加权，可复用到多目标RL场景（如同时优化CTR、转化率、停留时长），避免某一目标主导优化。

  - **开源数据与代码**：23K长上下文RLVR样本及完整训练流程已开源，可直接作为基础数据集或框架，加速业务中基于GRPO的RLVR训练，节省数据设计成本。

  - **GRPO训练配置**：验证了在长上下文RLVR中，更大的任务多样性和奖励差异性能显著提升效果；业务中若需RL训练，应避免单一任务结构，追求覆盖多种真实场景的能力类型。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有长上下文RL方法倾向构造复杂检索路径，导致任务同质、奖励单一，难以覆盖实际需要的多种长文能力。

**方法**：
1. **能力导向数据**：定义9类长上下文能力（如多跳推理、对话理解），为每类设计自然评估指标，构造23K RLVR样本，混合开源数据和基于真实文档（书籍、论文、多轮对话）的合成QA。
2. **TMN-Reweight**：多任务训练时，先对每个任务的奖励做均值归一化（跨任务对齐尺度），再按样本难度进行加权，改进GRPO的优势估计。

**结果**：
- 相同GRPO设定下，本数据集效果超过闭源QwenLong-L1.5。
- Qwen3-30B-A3B用本数据训练后，长上下文基准平均分与DeepSeek-R1-0528、Qwen3-235B-A22B等大模型可比。
- TMN-Reweight进一步提平均性能，且通用能力保持或提升。
