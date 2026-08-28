---
title: Preference Flow Matching with Spectral Factorization for Micro-video Recommendation
title_zh: 面向微视频推荐的谱分解偏好流匹配框架
authors:
- Xinxin Dong
- Haokai Ma
- Fei Hu
- YuZe Zheng
- Bin Wu
- Yonghui Yang
- Xiaodong Wang
affiliations:
- National University of Defense Technology
- National University of Singapore
- Zhengzhou University
arxiv_id: '2608.26579'
url: https://arxiv.org/abs/2608.26579
pdf_url: https://arxiv.org/pdf/2608.26579
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 多模态微视频推荐 · Flow Matching
tags:
- Flow Matching
- Micro-video Recommendation
- Spectral Factorization
- Multimodal
- Sequential Recommendation
one_liner: 用频谱分解将帧级视频表示解耦为静态与动态因子，并以条件流匹配建模偏好转移
practical_value: '- 视频/短视频推荐中，不要只对帧级特征做整体平均池化；可借鉴 SSF 把帧序列经 rFFT 后在频域用可学习软掩码分离静态语义与动态因子，避免两类信号互相干扰。

  - 若业务已用扩散或 Flow Matching 做序列建模，可参考 x1-parameterization 直接预测目标 item 表示，推理时用少量 Euler
  步（文中 10 步）即可，训练目标只用 L_rec + L_CFM，计算和显存显著低于扩散模型。

  - 用户对内容静态/动态成分的偏好存在异质性；可引入一个基于用户行为序列的 intent gate 动态加权静态与动态上下文，作为条件注入生成过程，提升个性化。

  - 在物品侧交互稀疏的场景下，把多模态内容因子作为生成式过程的结构化条件，比单纯作为附加特征更有效；尤其适合冷启动或长尾内容推荐。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
微视频推荐需要从用户历史交互和多模态视频内容中推断偏好。现有方法通常将帧序列压缩为单一整体表示，混淆了稳定视觉语义与帧间动态变化；而扩散/流匹配推荐模型仅以粗粒度行为上下文为条件，忽略了视频内部时间结构。作者发现视频的高频能量比分布极不均匀，且用户对静态与动态内容的敏感度存在明显分化，因此需要显式分解并分别建模这两类信号。

**方法关键点**
- **Spectral Semantic Factorization (SSF)**：对帧级视觉表示沿时间维做 rFFT 得到幅度谱；用先验引导的可学习频率掩码生成软掩码 M_s 和 M_d，得到静态谱 H_i^s 与动态谱 H_i^d；再通过分支特有的通道残差门控、多尺度 depthwise 卷积和频域平均池化，得到静态表示 r_i^s 与动态表示 r_i^d。
- **Context-Calibrated Preference Matching (CPM)**：将下一视频预测建模为内容条件化的流匹配过程。先聚合历史视频的静态/动态因子，用用户行为序列生成的 intent gate 加权得到校准视频上下文 c_u^v；再结合文本上下文和时间间隔，在 rectified flow 路径上以 x1-parameterization 直接预测目标 item 表示。最终表示融合生成结果与序列偏好状态。
- **优化目标**：联合 L_rec（全 softmax 推荐损失）与 L_CPM（endpoint 回归损失）。

**关键实验**
在 MicroLens-Small/Big 和 Shortvideo-Small/Big 四个数据集上对比 14 个 baseline。PrismRec 在所有 16 个指标上均取得最优，相对最强 baseline 最高提升 22.65%（Shortvideo-Small H@20）。消融显示 SSF 与 CPM 均有稳定贡献；同时 PrismRec 取得最低的推理时间与峰值 GPU 显存。

**最值得记住的一句话**
把视频内容的静态/动态因子作为流匹配轨迹的结构化条件，能让内容成为偏好形成的内生驱动力，而不是辅助侧信息。
