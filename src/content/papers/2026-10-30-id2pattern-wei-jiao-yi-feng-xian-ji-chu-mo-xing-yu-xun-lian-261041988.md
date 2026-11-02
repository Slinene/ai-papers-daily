---
title: 'ID2Pattern: Pretraining Generalizable Identity Behavior Patterns for Transaction
  Risk Foundation Models'
title_zh: ID2Pattern：为交易风险基础模型预训练可泛化身份行为模式
authors:
- Ze Zhao
- Haoyu Jiang
- Weiyu Han
- Ruobing Zuo
- Xiao Tan
- Shuai Chen
- Tianyi Zhang
affiliations:
- Ant International
- East China Normal University
arxiv_id: '2610.41988'
url: https://arxiv.org/abs/2610.41988
pdf_url: https://arxiv.org/pdf/2610.41988
published: '2026-10-30'
collected: '2026-11-02'
category: Other
direction: 身份行为模式预训练 · 交易风控/电商
tags:
- Identity Behavior Modeling
- Pretraining
- Transaction Risk
- High-Cardinality ID
- VQ-VAE
- Sequence Foundation Model
one_liner: 用 LAID 匿名 ID 编码与多尺度 VQ pattern codebook，从高基数身份序列中提取可泛化行为模式，提升风险/电商预测。
practical_value: '- **高基数 ID 不要用 hash/ID embedding，用 LAID 匿名编码**：将 user/device/card/item
  等 ID 映射为局部 ID、novelty、occurrence、recurrence 四通道；词表固定、不受 ID 新增影响，且对 ID 值置换不变。适合冷启动、跨域迁移以及线上推理速度（比
  hash 更快，参数不随 ID 增长）。

  - **用多尺度 VQ pattern codebook 做无监督预训练**：在 short/medium/long 三个时间窗口各自量化成离散 behavior
  pattern，通过 masked identity-state recovery 学共享码本；离散 pattern 比连续表示更稳，可跨数据集 transfer，甚至略优于
  in-domain 预训练。

  - **可迁移到电商/广告序列建模**：淘宝/RetailRocket/Synerise 上的结果表明，短期 window 捕捉 repeated revisit（转化意图），长期
  window 捕捉 novelty（风险/偏好变化）；可以把用户行为序列中 ID 的高基数问题与语义特征解耦，作为 plug-in 加到 GRU/LSTM/Transformer/Mamba
  骨干。

  - **工程实现上，LAID 计算只需 window 内等值比较，无需全局映射**：单次 pass O(#fields * sum L_s)；pattern token
  仅给 backbone 增加 3 个 token，复杂度可控。适合高 QPS 在线支付/推荐场景。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
在线支付/电商积累了大量高基数身份字段（card/device/account ID），但现有 vocab-based 和 semantics-based 编码不适配：ID 词表持续增长且无语义。真正可泛化的信号不在 ID 具体值，而在其在一段交易序列中的出现、重复、间隔等行为模式。现有 behavior foundation models 没有专门处理这类身份字段。

**方法关键点**
- LAID tokenizer：对每个身份字段独立计算 local ID（首次出现顺序）、novelty（是否首次）、occurrence（累计次数）、recurrence（距上次出现的间隔）；四通道由序列内等值关系导出，故对 ID 值置换不变，词表固定。
- 多尺度 pattern codebook：在 short/medium/long 三个窗口重算 LAID，共享 Transformer encoder 后，用 VQ-VAE 将行为表示量化为离散 pattern token；通过 masked identity-state recovery 预训练恢复被掩码的 novelty/occurrence/recurrence。
- 下游：将 [qS,qM,qL] 三个 pattern token 前置到 event token 序列，与语义/数值特征联合送入 backbone。

**关键结果**
- 工业支付风险 100M+ 序列：相对 semantic-only 基线，AUC +4.13%，T1 +22.64%，AddCB +19.67%；在线 shadow 评估逐日领先。
- 6 个公开数据集（3 风险 + 3 电商）：PR-AUC 平均优于最强 baseline +8.83%，R@0.5% 全部最优。
- 身份重标记实验：基线在 25% 新 ID 下 CCT 掉 53.4–87.9%，ID2Pattern 完全不变。
- 组件收益：LAID 贡献最大；替换为 hash 在 CCT 掉 44.3%；pattern branch 在风险任务更重要。
- 跨骨干 15/16 组合提升；跨数据集预训练持平或略优于 in-domain。

**一句话**
高基数 ID 的可泛化信号不在具体值，而在其行为模式：用匿名 LAID + 多尺度离散 pattern 预训练，可以让模型在新 ID、新场景下稳定迁移。
