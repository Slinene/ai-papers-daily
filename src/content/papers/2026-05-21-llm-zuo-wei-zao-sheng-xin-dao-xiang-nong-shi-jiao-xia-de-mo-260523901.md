---
title: 'LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling
  Laws'
title_zh: LLM 作为噪声信道：香农视角下的模型容量与缩放定律
authors:
- Xu Ouyang
- Deyi Liu
- Yuhang Cai
- Jing Liu
- Yuan Yang
- Chen Zheng
- Thomas Hartvigsen
- Yiyuan Ma
affiliations:
- ByteDance Seed
- University of Virginia
- University of California, Berkeley
arxiv_id: '2605.23901'
url: https://arxiv.org/abs/2605.23901
pdf_url: https://arxiv.org/pdf/2605.23901
published: '2026-05-21'
collected: '2026-05-25'
category: Training
direction: LLM 训练缩放定律 · 香农信道理论
tags:
- Scaling Laws
- Noisy Channel
- Shannon Theory
- SNR
- LLM Training
- Non-monotonic Behavior
one_liner: 将 LLM 训练建模为噪声信道传输，提出香农缩放定律，解释非单调性能下降
practical_value: '- 在推荐模型或生成式推荐训练中，当数据量增加但信息增益不高时，应监控性能非单调下降，可借鉴信噪比思考合理的数据配比与早停策略。

  - 模型量化或压缩时，使用信噪比框架评估退化风险，避免 U 型性能崩塌，尤其适用于电商知识图谱 embedding 等场景。

  - 多任务训练中，不同任务的噪声可能相互干扰，可依据信噪比动态调整任务权重，类似于信号功率的分配。

  - 主要是理论贡献，可直接复用的工程 trick 较少，但为理解缩放瓶颈提供了新视角，有助于在模型升级决策时避免盲目扩展参数或数据。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**: 现有 LLM 的缩放定律多为单调幂律，无法解释灾难性过训练、量化退化等非单调现象，即计算增加反而性能下降。

**方法**: 受香农信道定理启发，将 LLM 训练视为信息在噪声信道中的传输：模型参数视为信道带宽，训练 token 视为信号功率，学习过程受固有噪声扰动。由此推导出统一框架——香农缩放定律，模型容量由信噪比（SNR）决定，当 SNR 不足时扩展带宽或信号将放大噪声，导致 U 型退化。

**结果**: 在 Pythia 和 OLMo2 模型上，加入高斯噪声、量化及数学、QA、代码等任务的监督微调实验，香农缩放定律拟合 R² 显著优于经典幂律和近期扰动感知定律，准确捕捉到先前方法漏掉的 loss 谷底。外推能力突出：在 ≤6.9B 参数、≤180B token 的 Pythia 模型上拟合，预测未见过的 12B 模型至 307B token 的 loss，pooled R²=0.847，而单调基线完全失效。
