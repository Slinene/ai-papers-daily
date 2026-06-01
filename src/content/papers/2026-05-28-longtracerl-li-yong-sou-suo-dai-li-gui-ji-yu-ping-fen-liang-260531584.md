---
title: 'LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories
  with Rubric Rewards'
title_zh: LongTraceRL：利用搜索代理轨迹与评分量规奖励学习长上下文推理
authors:
- Nianyi Lin
- Jiajie Zhang
- Lei Hou
- Juanzi Li
affiliations:
- Tsinghua University
arxiv_id: '2605.31584'
url: https://arxiv.org/abs/2605.31584
pdf_url: https://arxiv.org/pdf/2605.31584
published: '2026-05-28'
collected: '2026-06-01'
category: Reasoning
direction: 长上下文强化学习 · Rubric 奖励
tags:
- Long-Context Reasoning
- RLVR
- Rubric Reward
- Distractor Construction
- Agent Trajectories
one_liner: 通过搜索代理轨迹构建分层干扰项与实体级评分量规奖励，大幅提升长上下文 RL 的训练效果
practical_value: '- **训练数据构造**：借鉴搜索代理的打开/引用行为生成高混淆度（打开但未引用）与低混淆度（检索到但未打开）干扰项，比随机采样或单次搜索更贴近真实检索场景，可迁移到电商长文档推荐解释、多跳问答数据增强。

  - **过程奖励设计**：实体级 Rubric 奖励只施加于最终答案正确的样本（positive-only），有效防止模型通过枚举实体而不做真实推理来刷分。在
  Agent 工具调用或多步推理任务中，可对中间关键信息（如商品属性、状态变迁）设计类似逐项检查的奖励，避免 reward hacking。

  - **组内归一化**：对不同难度的样本，在 rollout 组内归一化 Rubric 分数，使过程信号与难度解耦，让不同任务的奖励尺度可比较，利于通用训练。

  - **适中权重**：超参 α=0.3 时效果最佳，过大（0.5）会稀释结果奖励；经验上可在多目标 RL 中保持 outcome reward 主导地位。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有长上下文强化学习（RLVR）方法面临两大瓶颈：训练数据中的干扰文档多由随机采样产生，与查询语义无关，易混淆度低；奖励仅基于最终答案正确性，信号稀疏，可能让模型通过错误推理链碰巧得到正确答案。这导致模型难以在长文本中准确定位和整合关键信息。

**方法关键点**
- **数据构造**：基于 Wikipedia 知识图谱随机游走生成 8 跳复杂问题，然后部署搜索代理（搜索→打开→引用）求解问题，收集轨迹。将代理打开但未引用的文档作为 Tier-1 高混淆干扰项，将出现在搜索结果但未打开的文档作为 Tier-2 低混淆干扰项，按优先级填充至 128K 上下文。
- **评分量规奖励（Rubric Reward）**：定义黄金推理链的实体集合，计算模型响应中出现的实体召回率作为原始量规分数，并在 GRPO 组内归一化。采用 positive-only 策略：仅当最终答案正确时才加入量规奖励（与 outcome reward 加权组合），防止模型直接枚举上下文实体骗取高分。
- **训练**：使用 GRPO 算法，组大小 8，学习率 2e-6，在 32 张 H800 上训练 200 步，α=0.3。

**关键结果**
在 AA-LCR、MRCR、FRAMES、LongBench v2、LongReason 五个基准上，Qwen3-4B-Thinking-2507 经 LONGTRACERL 训练后平均分从 53.3 提升至 59.0（+5.7），超出最强基线 LongRLVR 2.5 点；DeepSeek-R1-0528-Qwen3-8B 和 Qwen3-30B-A3B 同样取得一致提升。消融显示，去除量规奖励（变成 outcome-only GRPO）后平均分回落至 53.7，证明过程监督是关键驱动力；替换随机或单次搜索干扰项后，性能明显下降，验证了搜索轨迹分层干扰项的必要性。
