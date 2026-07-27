---
title: 'DWT-Fusion: A Signal-Based Framework for Training-Free LLM-Generated Text
  Detection'
title_zh: DWT-Fusion：基于离散小波分析的免训练 LLM 文本检测框架
authors:
- Mehmet Batuhan Özdaş
- Murat Osmanoğlu
affiliations:
- Ankara University
arxiv_id: '2607.22026'
url: https://arxiv.org/abs/2607.22026
pdf_url: https://arxiv.org/pdf/2607.22026
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: LLM 生成文本检测 · 多分辨率信号分析
tags:
- LLM-generated text detection
- wavelet transform
- training-free
- voting ensemble
- token log-probability
one_liner: 用离散小波变换分析 token 级对数概率序列的多分辨率特征，结合校准融合投票，实现免训练零样本 LLM 文本检测
practical_value: '- **电商评论/搜索查询的 AI 生成内容检测**：可直接将 token 级 log-probability 序列送入小波变换，提取多尺度波动信号，无需训练即可判断文本是否为
  LLM 生成，用于过滤虚假评论或检测机器人搜索词。

  - **轻量级在线部署**：仅需一个代理语言模型（如 2.7B 参数量）计算 logits，推理开销可控，适合推荐系统旁路实时审核。

  - **校准加权投票融合**：组合不同小波基或分解层数的分数时，基于验证集校准的加权软投票可提升鲁棒性，该方法无需训练元模型，工程实现简单，可直接用于多信号融合场景（如内容安全、反欺诈）。

  - **多分辨率特征提取思路**：将一维序列（如 token 级困惑度、生成概率）通过小波变换分解为近似和细节系数，分离长期趋势与局部突变，可迁移到用户行为序列异常检测或会话质量评估。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有免训练 LLM 文本检测方法多依赖全局统计量（如平均困惑度），忽视了 token 级可预测性的局部波动与多尺度模式，导致跨领域、跨生成器泛化能力受限。

**方法**：提出 DWT-Fusion，先用代理因果语言模型获取文本的 token 级对数概率序列，再通过离散小波变换（DWT）将该序列分解为多分辨率近似与细节系数，从中提取检测信号（如细节系数的能量或方差）。为融合不同小波配置（基函数、分解层数）的检测分数，进一步设计四种无训练投票策略：等权硬投票、等权软投票、校准加权硬投票、校准加权软投票，其中校准权重由各配置在验证集上的 AUROC 线性变换得到，避免训练有监督元分类器。

**关键结果**：在 HC3、M4、MAGE 三个基准上，使用 GPT-Neo-2.7B、GPT-J-6B、Falcon-7B、LLaMA-3-8B 作代理模型。最佳单小波配置 AUROC 分别达 0.9872、0.8185、0.7138；校准加权软投票进一步将 AUROC 提升至 0.9919、0.8477、0.7471，尤其在 M4 上提升显著（+2.92%），验证了多分辨率信号与校准融合的有效性。
