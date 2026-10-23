---
title: 'Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic
  Compression and Balanced Discrete Generation'
title_zh: Cola2：连续语义压缩与平衡离散生成的协同自适应层次语言建模
authors:
- Hongcan Guo
- Yian Zhao
- Feng Wang
- Shen Nie
- Guoqiang Wei
- Yan Zeng
- Hengshuang Zhao
affiliations:
- The University of Hong Kong
- ByteDance Seed
- Peking University
- Renmin University of China
arxiv_id: '2610.31305'
url: https://arxiv.org/abs/2610.31305
pdf_url: https://arxiv.org/pdf/2610.31305
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: 层次语言建模 · 连续压缩离散扩散生成
tags:
- Hierarchical LM
- Continuous Latent
- Masked Diffusion
- Flow Matching
- Semantic Compression
- LLM
one_liner: 提出Cola2，通过连续语义压缩、离散重建-生成平衡与连续-离散协同适应，346B tokens训练8任务平均60.10超越Llama-3-8B部分任务
practical_value: '- 对生成式推荐/Semantic ID：将物品语义压缩为连续 latent，再离散生成语义 ID；负反馈控制压缩率可省去辅助
  loss 调参，适合对商品描述或用户行为序列做自适应语义摘要，减少 token 预算。

  - 对搜索/广告文案生成：block-causal masked diffusion 解码器在 clean/noisy/dropped latent 条件下训练，能提高对
  query/商品属性缺失或噪声输入的鲁棒性；Classifier-free guidance 可显式调节文案对约束的重建忠诚度和自主创意之间的平衡。

  - 对 Agent 多轮交互：推理时 re-encode under fixed span layout 保持隐历史与实际文本一致，可缓解多轮生成中 latent
  history 漂移；stop-gradient 分离 Flow Matching 先验与表示学习，适合多任务/多阶段训练，避免先验目标干扰主任务表示。

  - 对工程实现：continuous latent 压缩+离散解码可减少长序列 token 数，提升长文本/长行为序列建模效率；训练用 clean/noisy/dropped
  latent 条件成本低，可作为增强 decoder 鲁棒性的通用 trick。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
层次语言生成将连续语义建模与离散文本生成分离，但效果取决于潜在空间压缩什么信息、离散生成器如何利用。现有方法常面临压缩率与预测性不平衡、连续-离散表示不匹配。

**方法关键点**
Cola2 动态将文本切分为 semantic spans，使用无辅助损失的负反馈机制控制压缩率；结合重建与生成监督学习紧凑且预测性的 latent。解码器采用 block-causal masked diffusion，训练时输入 clean/noisy/dropped latent 条件，用 classifier-free guidance 调节语义重建与自主生成。token 预测梯度通过 latents 更新 encoder，实现连续表示与离散生成协同适应；Flow Matching 先验学习通过 stop-gradient 与表示学习解耦。推理时按固定 span layout 重新编码生成文本，保持 latent history 与真实文本上下文一致。

**关键结果**
在约 210B tokens、五个下游任务上验证设计有效，呈现竞争性且未饱和的 scaling。346.03B source tokens 的未收敛 checkpoint 在八任务平均 60.10，在 HellaSwag 和 StoryCloze 上超过 Llama-3-8B，而后者预训练预算大 43 倍以上。结果表明其可有效迁移 Qwen 初始化解码器的生成能力，并有较大扩展余量。
