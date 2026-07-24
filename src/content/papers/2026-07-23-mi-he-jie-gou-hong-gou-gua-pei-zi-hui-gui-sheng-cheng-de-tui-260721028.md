---
title: 'Bridging the Structural Gap: Adapting Autoregressive Generation for Recommendation'
title_zh: 弥合结构鸿沟：适配自回归生成的推荐系统
authors:
- Junchao Zeng
- Junzhang Zhu
- Junyang Chen
- Yudong Li
- Wei Liu
- Chengxiang Zhuo
- Zang Li
affiliations:
- Tencent
- Shenzhen University
- Sun Yat-sen University
arxiv_id: '2607.21028'
url: https://arxiv.org/abs/2607.21028
pdf_url: https://arxiv.org/pdf/2607.21028
published: '2026-07-23'
collected: '2026-07-24'
category: GenRec
direction: 生成式推荐 · 语义ID结构优化
tags:
- Generative Recommendation
- Semantic ID
- Hierarchical Decoding
- Item Context-Aware Attention
- Path Reranking
- Dual-Path Decoding
one_liner: 通过恢复 item 边界、路径重排与双路解码，缓解生成式推荐中的语义漂移
practical_value: '- ICA 模块可直接插入现有 Transformer 编码器前，通过可学习 query 做跨注意力得到 item 上下文，再用可训练门控融合回
  token 序列，几乎无额外参数开销，能有效恢复被扁平化破坏的 item 边界信号。

  - HPR 是一种轻量级、无需标签的路径重排方案：用解码器初始隐状态作为用户意图锚点，与累积路径嵌入做对比学习，训练后仅在 beam search 每层重排 top-N
  候选，不增大 beam width，可直接迁移到任何基于分层 codebook 的自回归生成管线。

  - DPD 的 OSQ‑VAE 通过可学习正交旋转将嵌入空间拆成两个互补子空间，形成双通道语义 ID；配合双解码器 + OR 融合，在 recall 阶段以极低成本获得显著互补增益，尤其适合大规模
  item 库中长尾与冷启 item 的召回增强。

  - 代码本采用「前大后小」的递减配置 (512,256,128,64) 且全部可学习，省去随机碰撞 ID，既保证粗粒度分类的容量，又控制总参数，适合工业级部署；推理时双路
  beam search 并行，延迟与单路基本持平。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐将 item 量化为多层语义 ID 逐 token 预测，但存在两个结构缺陷：1) 将 item 的多 token ID 压平为无差别序列，使得编码器丢失 item 边界信息；2) 分层 codebook 的解码存在语义漂移——浅层错误会使正确叶子节点无法到达。TIGER 等现有方法仅靠位置编码隐式恢复结构，且标准 beam search 无法感知跨层一致性。  

**方法**  
提出 BARGE，由三个正交模块解决：  
- **ICA**：在编码前用可学习 query 对每个 item 的 token 做跨注意力池化得到 item 上下文，再通过门控残差注入各 token，恢复 item 级粒度。  
- **HPR**：在每层 beam search 后，用解码器初始隐状态（用户意图）与累积路径嵌入做双塔对比打分（训练用对称 InfoNCE），重排 top‑N 候选，纠正路径级漂移而不扩展 beam。  
- **DPD**：用 OSQ‑VAE 通过可学习正交旋转将 item 嵌入拆分为两个互补子空间，产生两套语义 ID；共享编码器后接两个独立解码器与 HPR，推理时对两路结果做 soft‑OR 融合。  

**实验**  
在 Amazon Beauty、Sports 及腾讯媒体平台离线/在线评测。  
- 公开数据集上全面超越 SOTA 生成式基线（TIGER、COBRA、ActionPiece 等），Beauty R@10 提升 19.6%，Sports N@10 提升 16.7%。  
- 工业离线测试 Hit@5 达 0.6015，显著优于部署的 NANN 等模型。  
- 在线 A/B：CTR +0.60%，点击 UV +1.34%，总阅读时长 +1.70%。  
- 消融证实三模块增益独立可加，路径重排权重 λ 呈倒 U 型影响，两通道 top‑K 集合 Jaccard 仅 0.17‑0.18，互补性强。
