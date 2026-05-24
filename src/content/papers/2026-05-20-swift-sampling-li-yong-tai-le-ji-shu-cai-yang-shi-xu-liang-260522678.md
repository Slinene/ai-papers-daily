---
title: 'Swift Sampling: Selecting Temporal Surprises via Taylor Series'
title_zh: Swift Sampling：利用泰勒级数采样时序惊喜帧
authors:
- Dahye Kim
- Bhuvan Sachdeva
- Karan Uppal
- Naman Gupta
- Vineeth N. Balasubramanian
- Deepti Ghadiyaram
affiliations:
- Boston University
- Microsoft Research India
arxiv_id: '2605.22678'
url: https://arxiv.org/abs/2605.22678
pdf_url: https://arxiv.org/pdf/2605.22678
published: '2026-05-20'
collected: '2026-05-24'
category: Multimodal
direction: 视频帧重要采样 · 时序惊喜检测
tags:
- Video Frame Sampling
- Temporal Surprise
- Taylor Series
- Training-Free
- Long-Form Video QA
one_liner: 用泰勒展开预测视频特征轨迹，选出偏离预测的时序惊喜帧，零训练、极低开销
practical_value: '- **轻量级无训练帧选择器**：仅需计算一阶/二阶特征差分的泰勒残差，无需辅助网络或调参，可直接插入现有多模态大模型的视频帧采样阶段，大幅降低
  token 开销。

  - **适用于电商视频理解**：在商品直播、产品解说等长视频中，可自动定位产品亮点或内容转折，提升视频问答、摘要生成的效率与准确性。

  - **通用时序惊喜检测**：泰勒残差思想可泛化至用户行为序列、对话流等，用于抽取信息量大的关键时刻，辅助构建更高效的 Agent 记忆或推荐特征提取。

  - **经济部署**：增加的计算量仅为基线的 0.02 倍，比同类方法便宜 30 倍，适合大规模视频处理或实时场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：长视频中大量帧是冗余的，关键信息集中于时序惊喜——即实际视觉特征偏离其预测演化的时刻。受大脑预测编码启发，提出一种训练无关的帧选择算法，自动发现高信息量片段。

**方法**：将视频看作视觉隐空间中的可微轨迹，计算特征的速度和加速度，利用泰勒展开预测后续帧的期望特征，实际特征与预测的残差作为“泰勒惊喜”度量。在局部时间窗口内应用非极大抑制，选择残差高的帧作为关键帧。整个过程无需任何训练或辅助网络，唯一超参数是窗口大小（作者固定为 5），计算开销仅为基线的 1.02 倍。

**结果**：在三个长视频问答基准（如 EgoSchema、NExT-QA）和 10 个下游任务上，Swift Sampling 一致超越均匀采样和先前查询无关方法。在帧预算紧张时（如 8 帧），准确率最大提升 +12.5 个百分点。
