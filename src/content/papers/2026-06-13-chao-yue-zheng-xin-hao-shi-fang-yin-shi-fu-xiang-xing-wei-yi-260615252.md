---
title: 'Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced
  Sequential User Modeling'
title_zh: 超越正信号：释放隐式负向行为以增强序列用户建模
authors:
- Zexuan Cheng
- Yue Liu
- Jun Zhang
- Jie Jiang
affiliations:
- Tencent Inc.
arxiv_id: '2606.15252'
url: https://arxiv.org/abs/2606.15252
pdf_url: https://arxiv.org/pdf/2606.15252
published: '2026-06-13'
collected: '2026-06-16'
category: RecSys
direction: 隐式负反馈融入行为序列建模
tags:
- Implicit Negative Feedback
- Sequential Modeling
- CTR Prediction
- Target-Aware Polarity Fusion
- Behavior Sequence
- Attention Rebalancing
one_liner: 在CTR行为序列中按时间交错正负行为，用极轻量的极性感知校准即可让多种架构一致提升1.9%–9.6% AUC
practical_value: '- **序列构建零成本升级**：将用户曝光但未点击/快速划过/低完播的隐式负向行为直接作为普通token，与正向行为按时间戳交错，保持序列长度不变，推理成本零增加，即可在现有模型上获得明显收益。适用于广告、电商、信息流等场景。

  - **极性编码即可获得大部分增益**：最简单的极性偏置嵌入（PBE）已能解锁混合序列的主要价值，只需为每条行为增加一个可学习的极性embedding，适合快速上线验证。

  - **TAPF作为轻量级增强**：若资源允许，可进一步使用目标感知极性融合（TAPF），通过在注意力前增加目标相关的门控残差，重平衡正负token的注意力分配（如从75%:25%调整到59%:41%），带来额外0.3%–0.8%
  AUC提升，且仅增加线性层和元素级运算，对在线时延影响小。

  - **数据质量管理**：负向行为必须是真实且近期的，随机采样或错误极性标签会严重退化效果；建议按实效性排序采样，避免远历史负信号。在低活跃用户或冷启动商品上，混合序列的增益更大，可重点在此类群体应用。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现代CTR预估中的行为序列建模几乎完全依赖点击、购买等正向行为，而大量隐式负向行为（跳过、快速划过、低完播）被舍弃。随着正向序列扩展收益递减，这一设计留下巨大信息真空：隐式负向数据是正向的数十倍，且能刻画用户“拒绝什么”，增强对候选物品的判别力。

**方法关键点**  
- **混合极性序列构建**：在固定长度预算内，按时间戳交错采样最近的正向与负向行为，负向token取代部分正向token，序列总长不变，推理成本与纯正向序列相同。  
- **极性语义校准**：提出极性偏置嵌入（PBE）作为基础方案，为每个token添加可学习的极性embedding；进而设计目标感知极性融合（TAPF），利用目标物品与序列token的逐元素交互生成门控信号，通过带符号残差自适应调整token表征，让正向token靠近目标、负向token远离。  
- **模型无关性**：上述方法可插入任意两阶段或统一块式CTR架构（DIN、Transformer、OneTrans、HyFormer、MixFormer），无需改动主干网络。

**关键结果**  
在KuaiRec、KuaiRand和TAAC三个公开数据集上，混合极性序列+PB/TAPF相较纯正向序列在各架构均取得一致提升：相对AUC提升范围+1.9%～+9.6%（如KuaiRec上MixFormer +5.5%，Transformer +4.2%）。序列长度缩放实验显示混合序列的斜率约为纯正向的2倍，有效缓解了纯正向序列因用户正向历史有限而早熟停滞的问题。正负比例在r=0.2–0.7时性能稳定，r=0.5即可覆盖大部分收益。冷启动物品在KuaiRand上获得1.5–2倍增益；低活跃用户（0–1条正向行为）在TAAC上AUC提升达+0.041～+0.050。消融实验证实，真实近期负向行为而非随机采样是性能核心，错误极性标签会严重破坏模型。模型自发习得极性区分性注意力，TAPF能将负向token的注意力权重从25.5%提升至41.3%，使得用户表征更充分利用负反馈信息。

**一句话核心**  
“将隐式负向行为作为一等序列token按时序交错注入，配合极轻量极性校准，即可用零额外推理成本显著提升多架构CTR模型。”
