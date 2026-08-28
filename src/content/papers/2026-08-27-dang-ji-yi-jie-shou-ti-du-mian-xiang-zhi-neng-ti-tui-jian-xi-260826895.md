---
title: 'When Memory Takes Gradients: Collaborative Vector Memory for Agentic Recommender
  Systems'
title_zh: 当记忆接受梯度：面向智能体推荐系统的协同向量记忆
authors:
- Hanchong Chen
- Xing Tang
- Lingjie Li
- Xiongfeng Shan
- Xiuqiang He
affiliations:
- Shenzhen Technology University
arxiv_id: '2608.26895'
url: https://arxiv.org/abs/2608.26895
pdf_url: https://arxiv.org/pdf/2608.26895
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent 记忆设计 · 协同向量记忆
tags:
- Agentic Recommender
- Vector Memory
- LightGCN
- LoRA
- Contrastive Alignment
- LLM Ranking
one_liner: 用 LightGCN 协同状态作为 LLM Agent 持久记忆，通过对比对齐和掩码 listwise 协同训练让模型学会读取向量记忆，在 4
  个指令推荐基准上超过文本记忆 Agent 且零额外维护调用
practical_value: '- 把 Agent 的用户记忆从“文本叙事”拆成“轻量文本画像 + 冻结协同向量记忆”。电商/推荐场景可复用已有的 LightGCN、SASRec、SVD++
  等用户与物品 embedding 作为记忆库，避免每次交互后调用 LLM 重写，省去大量 token 与串行延迟。

  - 采用 candidate-conditioned retrieval：用当前候选集 embedding 质心去用户历史里检索 top-K 最相关物品状态，而不是取最近
  K 个；这对排序/推荐 Agent 在线推理便宜且与当前决策相关。

  - 不要只把 embedding 塞进 prompt。需要 gated projector + 低秩 LoRA 构成可训练的 memory reader，并用“候选
  title 随机 mask + listwise margin loss”强制模型依赖协同 token；否则 LLM 会走文本捷径，向量 token 反而干扰。

  - 推理阶段用 pointwise yes/no logit 打分并并行请求，避免 listwise 生成排序的解析失败；指令位置可以用只基于训练集统计量的零样本规则卡选择，避免验证集泄漏。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有 Agentic 推荐系统中，LLM 的持久记忆几乎都是文本：交互历史通过串行 LLM 改写沉淀为叙事，决策时读回 prompt。这带来两个根本限制：一是每次吸收新交互都要额外 LLM 调用，维护昂贵，难以利用全量交互历史；二是协同结构被压缩进句子后丢失，只能命名少量邻居或 facet，无法保留整个商品目录上的分级相似性。更关键的是，排序梯度无法直接更新存储的文本记忆。因此需要一种记忆形式：保留 catalog 级协同几何、能从排序目标训练、且无需反复文本改写即可被 LLM 使用。

## 方法关键点
- **协同向量记忆库**：用 LightGCN 学习 d=64 的用户/物品状态并冻结，作为记忆库；同时保留一份一次性生成的轻量文本画像。
- **目标感知检索**：对当前候选集计算 embedding 质心，在用户的可用历史中检索与质心最相关的 top-K=5 个历史物品状态，无需 LLM 调用。
- **参数化记忆读取器**：gated projector 把状态向量映射为 LLM 输入空间的 soft token，配合 rank=4 的 LoRA adapter 调整注意力，总参数量约 6.8M，占模型不到 0.1%。
- **两阶段训练**：先做 semantic-anchor alignment，用物品 title/category embedding 作为锚点做对比学习，让投影后的状态落入语言空间；再做 masked listwise co-training，每个训练交互构成排序事件，候选 title 以 p=0.5 随机 mask，margin loss 只在 masked 竞争池上计算，迫使模型依赖协同 token 排序。
- **推理**：用 pointwise yes/no logit 对每个候选打分并行请求；指令位置由零样本 LLM 规则卡根据训练集统计量选择。

## 关键实验
在 4 个 InstructRec 指令推荐基准上评测：Books、Goodreads、MovieTV、Yelp。对比 LightGCN、SASRec、P5、Vanilla LLM，以及文本记忆 Agent iAgent、AgentCF、i2Agent、MemRec。结果显示 CoVeMem 在 20 个指标格中 19 个匹配或超过最强文本记忆 Agent MemRec：Goodreads H@1 从 0.3087 提升到 0.7730，MovieTV H@1 0.5799 vs 0.5371，Yelp H@1 0.5400 vs 0.5173；Books H@1 略低但 H@3/H@5 反超。消融显示去掉 LoRA 后模型掉到随机水平，说明必须通过学习读取器才能利用向量记忆。协同 backbone 可插拔，SVD++ 替换 LightGCN 后继续提升。内存维护方面，CoVeMem 需要零额外 LLM 调用。

最值得记住的一句话：记忆载体本身就是一个设计轴；一旦协同记忆变成可训练的向量状态并通过排序梯度学习读取方式，全量交互历史就能成为训练监督，无需再被压缩成文本。
