---
title: 'RAMP: Robust Ad Recommendation Under Limited Personalized-Feature Availability
  via Masking and Alignment Pathways'
title_zh: RAMP：掩码对齐路径实现有限个性化特征下的鲁棒广告推荐
authors:
- Dairui Liu
- Zhongyi Lu
- Roger Zhe Li
- Changhong Jin
- Jitao Lu
- Xinyang Shao
- Bichen Shi
- Mete Sertkan
- Aghiles Salah
- Aonghus Lawlor
affiliations:
- University College Dublin
- Huawei Ireland Research Center
arxiv_id: '2607.17473'
url: https://arxiv.org/abs/2607.17473
pdf_url: https://arxiv.org/pdf/2607.17473
published: '2026-07-20'
collected: '2026-07-21'
category: RecSys
direction: 隐私受限 · 蒸馏对齐
tags:
- CTR Prediction
- CVR Prediction
- Privacy Preserving
- Knowledge Distillation
- Dual-tower
- Output Masking
one_liner: 用双塔输出掩码分离个性/非个性化监督，配合蒸馏对齐路径，在隐私受限下提升 CTR/CVR 预测
practical_value: '- **双塔掩码策略可直接复用**：用一个共享嵌入层 + 两个独立塔，输出时依流量类型（个性化/非个性化）掩码，使两塔分别专精不同特征域，减少负迁移。在现有
  CTR/CVR 模型中容易嫁接，无需改变输入结构。

  - **蒸馏对齐实现“特权特征”训练**：训练时利用额外完整特征通路（个性化通路）指导仅用非个性化特征的通路，推理时只用轻量通路。在电商/广告中，可类似地将高权限特征（如用户历史）作为教师，引导受限特征模型，不增加线上耗时。

  - **非个性化路径训练即丢弃**：对齐模块仅在训练期激活，线上推理只保留已对齐的双塔组件，零额外推理成本。适合在线广告系统对延迟敏感的场景。

  - **距离损失权重需细粒度搜索**：实验中损失权重与性能呈倒U关系，建议用粗到细网格搜索确定最优值，避免过度对齐拖累主任务。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
在线广告的 CTR/CVR 预测高度依赖年龄、设备等个性化特征，但 GDPR 等法规使这类特征在部分流量中不可用，导致模型性能大幅下降（图1）。现有方案多关注隐私保护而非特征缺失下的预测精度，且单网络混合训练易出现负迁移。急需一种在不增加推理开销的前提下，同时适配个性化与非个性化流量的鲁棒预测架构。

**方法**  
RAMP 由三部分构成（图2）：  
1. **个性化路径（双塔）**：两个共享嵌入层但独立参数的前馈塔，根据流量类型用掩码分配监督——塔A仅对个性化样本计算损失，塔B仅对非个性化样本计算损失，消除跨域干扰。  
2. **非个性化路径**：额外使用仅含非个性化特征的前馈网络，在所有样本上训练，但输入严格去除了个性化字段，为纯非个性化场景提供专门表示。  
3. **蒸馏启发预测对齐**：最小化两路径在非个性化样本上的预测 logits 的 L1 距离，通过交叉熵风格损失对齐行为，使非个性化路径吸收来自个性化路径的暗知识。训练时两路径联合优化，推理时仅启用双塔组件，不增加线上开销。

**关键结果**  
在 Avazu、TaobaoAd（CTR）、CriteoPrivateAd、IndustryAd（CVR）四个数据集上，以 PNN、FCN 等为骨干，RAMP 在非个性化子集上显著优于所有基线：  
- CriteoPrivateAd：AUC 提升 0.87%（78.65%→79.52%）  
- TaobaoAd：AUC 提升 0.22%（59.17%→59.39%）  
- 工业 A/B 测试：总广告主价值提升超 3%。  
消融表明双塔掩码和蒸馏对齐各自带来增益，且模型对个性化特征数量减少具有韧性（移除前 10 重要特征后 AUC 仅降 0.17%）。  

**一句话总结**  
通过输出掩码让双塔各司其职、再用预测对齐将完整特征知识蒸馏到非个性化通路，RAMP 在不增加推理成本的前提下，大幅弥补了个性化特征缺失造成的精度损失。
