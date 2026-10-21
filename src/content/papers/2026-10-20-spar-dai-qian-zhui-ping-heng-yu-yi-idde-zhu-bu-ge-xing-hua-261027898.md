---
title: 'SPAR: Stepwise Personalized Autoregressive Recommendation with Prefix-Balanced
  Semantic IDs'
title_zh: SPAR：带前缀平衡语义ID的逐步个性化自回归推荐
authors:
- Chunrui Zhang
- Gaoyun Lin
- Chang Zhou
- Zheng Hu
- Qiran Song
- Shimin Cai
- Tao Zhou
affiliations:
- University of Electronic Science and Technology of China
- University of Science and Technology of China
- HUJING Digital Media & Entertainment Group
- Southwest Jiaotong University
arxiv_id: '2610.27898'
url: https://arxiv.org/abs/2610.27898
pdf_url: https://arxiv.org/pdf/2610.27898
published: '2026-10-20'
collected: '2026-10-21'
category: GenRec
direction: 生成式推荐 · Semantic ID
tags:
- Generative Recommendation
- Semantic ID
- Prefix Balancing
- Personalized Decoding
- DPO
- Industrial A-B Test
one_liner: 提出前缀平衡语义ID构建与逐步个性化解码，缓解生成式推荐分支不平衡和证据不匹配
practical_value: '- **Prefix-conditioned memory retrieval**：在生成式推荐或Agent决策中，可在每个解码步骤根据当前已生成前缀从长期记忆中动态检索相关证据，而非使用静态用户表示。用Q-Former压缩多粒度历史视图，再通过cross-attention按需读取，可灵活适配不同层级的分支决策。

  - **Prefix-balanced SID construction**：构建层级Semantic ID或类目树时，应在父节点下平衡子节点负载，而非全局平衡。通过设置负载上限并进行最小扭曲移动，可缓解流行路径主导，提升长尾物品可见性。适用于电商商品结构、广告创意圈选等场景。

  - **DPO preference alignment**：利用beam search生成候选集，由排序模型打分构造偏好对进行DPO训练，可进一步提升生成质量。工业级可行，可结合SFT和DPO联合优化，对推荐结果进行偏好对齐。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：SID-based生成式推荐将item选择分解为token序列决策，但每个前缀定义了不同候选集，需要逐步个性化。现有方法未充分考虑前缀相关的用户证据和候选分支间的交互负载不平衡，导致不可逆的分支选择错误和流行路径主导。

**方法关键点**：
- **RQ-PIB**：在残差语义聚类基础上，对每个父前缀下的子分支进行负载再平衡。通过设置有效负载上限（考虑平均负载和最大单item权重），以最小重建扭曲移动item来降低流行分支占比，保持语义结构。
- **PATH Decoder**：将长期历史按SID层级构建coarse-to-fine视图，用Q-Former压缩为memory banks。解码器backbone处理最近SID序列，在每一步通过前缀条件cross-attention动态检索相关长期证据，并融合User Token和Event Token，输出下一个token概率。
- **训练**：先用SFT训练，再结合DPO偏好对齐；beam search生成候选由排序模型打分构造偏好对。

**关键实验**：
- 数据集：优酷生产日志，90/5/5划分训练/验证/测试。
- 对比baselines：GRU4Rec、SASRec、TIGER、OneRec。
- 离线结果：相比最强基线OneRec，HR@10/20/50/100平均相对提升2.66%；目标前缀保留率平均提升5.79个百分点；最大子分支流量占比平均降低32.84%。
- 在线A/B：7天10%流量，平均观看时长/用户+3.95%，播放转化率+3.38%。

> 最值得记住的一句话：生成式推荐必须在分支层次上做前缀感知的个性化决策和负载平衡，才能有效缓解不可逆错误并抑制流行偏差。
