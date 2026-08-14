---
title: 'DTAMLP: Denoise Time-aware MLP for Session-based Recommendation'
title_zh: DTAMLP：面向会话推荐的去噪时间感知 MLP
authors:
- Jiamu Zheng
- Xiaojun Shan
affiliations:
- University of Electronic Sciences and Technology of China
arxiv_id: '2608.12975'
url: https://arxiv.org/abs/2608.12975
pdf_url: https://arxiv.org/pdf/2608.12975
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: 会话推荐 · 时间去噪 MLP
tags:
- session-based recommendation
- time-aware MLP
- denoising
- plug-and-play
- FFT
one_liner: 针对会话推荐中短 dwell time 的偶发噪声，提出可插拔时间权重融合与 FFT 滤波的全 MLP 模型 DTAMLP
practical_value: '- 将 dwell time 作为软权重而非等权特征：用阈值截断（超过一定秒数就 cap）并做对数/归一化，与 attention
  得分相乘，作为插件嵌入现有 session/序列模型，冷启动快、改动小，可优先在电商详情页点击序列上尝试。

  - 频域去噪可作为通用 embedding 侧模块：对用户行为序列 embedding 做 FFT，学习可训练滤波器（如实部/虚部权重或 mask），再逆变换，再送入
  MLP/Transformer，计算开销低，适合处理多意图混杂的浏览序列。

  - 消融设计提示：不同去噪机制可能互补，但需控制阈值和频域模块容量，避免过拟合；上线前先用离线数据验证单独模块增益。

  - 注意评估的诚实性：论文明确说不是 SOTA，主要是机制验证；迁移到业务时先做小流量 AB，关注浏览深度、误触率等指标，而不是只看点击率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：会话推荐中，现有时间感知和 GNN 模型将每次点击的时间间隔视为同等信息，忽略了极短 dwell time 往往来自误触/偶然点击（称为 sporadic noise），造成偏好信号污染；此外，频域滤波的增益缺乏机制解释。

**方法关键点**：工作提出两个互补去噪机制。其一是轻量 plugin 权重融合模块：将 backbone attention 权重与 threshold-capped 时间间隔权重融合，几乎不改变架构即可嵌入 TiSASRec、SR-GNN 等模型，对短 dwell time 降权。其二是基于 FFT 的可学习频域滤波（继承 FMLP-Rec），作者推测时域行为混合了多个纠缠心理偏好，频域视角便于分离并下加权噪声。两者统一为 all-MLP 架构 DTAMLP。

**结果**：在 Diginetica 和 RetailRocket 上验证，消融显示两机制贡献互补且不冗余，轻量融合模块带来一致的准确率提升；系统级设计定位为 2023 年水平而非新 SOTA。
