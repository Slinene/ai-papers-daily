---
title: 'CRAMER: Control via Request-Aware Masking for Editing Recommenders'
title_zh: CRAMER：基于请求感知掩码的推荐模型编辑控制
authors:
- Zhiyuan Julian Su
- Naihe Feng
- Zhen Luther Qin
- Ga Wu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Faculty of Computer Science, Dalhousie University
arxiv_id: '2608.25370'
url: https://arxiv.org/abs/2608.25370
pdf_url: https://arxiv.org/pdf/2608.25370
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 请求感知序列推荐 · 参数掩码控制
tags:
- request-aware
- sequential recommendation
- masking
- parameter-efficient
- model control
- frozen backbone
one_liner: 用稀疏行-列参数掩码将自然语言请求即时作用于冻结的序列推荐骨干，避免重训与 LLM 推理开销
practical_value: '- **借鉴掩码控制冻结骨干的架构**：电商/推荐场景中，用户对推荐结果的即时反馈（如“不要太贵的”“更休闲”）可以用参数掩码在推理时快速调整模型，无需重新训练或部署多套模型；尤其适合已有大规模
  Transformer 排序/召回模型。

  - **用结构化行-列门控降低控制维度**：不要对每个参数单独 mask，而是对矩阵行/列做门控再外积得到 entrywise mask，参数量从 O(d²)
  降到 O(d)；配合 Gumbel-Top-k 实现 k-hot 稀疏，平衡表达力与开销。

  - **工程实现可复用**：请求文本经 PLM 编码 + mean pooling 得到语义向量 → 线性层投影到 gate logits → 离散采样得到 mask；训练只更新投影层和可选的部分
  PLM，推理只多一次轻量前向，适合集成到现有 serving 系统。

  - **超参数与模型选择**：drop ratio 在 0.10 左右最优；小数据集需要更稀疏（更大 drop ratio）防过拟合；请求编码器用 ModernBERT
  或 RoBERTa 比 MiniLM 效果好，可根据数据集规模选择。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：序列推荐模型只依赖历史行为，无法响应用户即时自然语言请求（如“想要更刺激的游戏”）。现有请求适应方法要么重训骨干、要么依赖 LLM 推理，开销大、延迟高，难以大规模部署。

**方法关键点**：
- 将用户请求视为控制信号，通过 request-to-mask 模块调制冻结的 Transformer 骨干（SASRec/BERT4Rec）。
- 请求编码：使用预训练语言模型（PLM）编码请求文本，对所有 token embedding 做 mean pooling 得到语义向量。
- 生成稀疏门控：线性投影到 gate logits，用 Gumbel-Top-k 采样 k-hot 二进制向量，drop ratio ρ 控制稀疏度；分解为每个矩阵的行门控和列门控，外积得到 entrywise mask，施加到骨干的 FFN 和/或 attention 输出投影矩阵 WO。
- 优化：仅训练投影层和可选部分 PLM，采用直通估计器（STE）处理离散采样，损失为预测损失 + 稀疏 KL 正则（除以维度归一化）。

**关键结果**：在 ReDial、KuaiSAR、Beauty、CDs&Vinyl 四个数据集上，CRAMER 在 SASRec 和 BERT4Rec 骨干下均显著优于 Query-SeqRec、BLaIR、LLM-ESR、REARANK 四个请求感知基线。例如 ReDial SASRec H@10 从 0.426 提升到 0.578，BERT4Rec H@10 从 0.421 提升到 0.580；KuaiSAR SASRec H@10 从 0.430 到 0.556。48 个成对 t 检验中 41 个显著（85.42%）。推理开销：SASRec 上额外 0.018 秒、1355.6 MiB GPU 内存，远低于 REARANK 的 9.256 秒、9824.7 MiB。掩码可解释性实验表明，请求能按语义方向调整推荐分布（如“避免浪漫电影”使浪漫电影占比从 0.286 降至 0.135）。

**最值得记住的一句话**：稀疏行-列掩码提供了一种对冻结推荐骨干的后验控制机制，以极低推理开销把自然语言请求即时转化为模型行为调整。
