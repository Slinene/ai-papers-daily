---
title: Diffusion Language Model for Recommendation
title_zh: 面向推荐的离散扩散语言模型
authors:
- Chengyi Liu
- Yongqi Zhou
- Junwei Pan
- Zhixiang Feng
- Chengguo Yin
- Haijie Gu
- Jie Jiang
- Yinghao Liu
- Yujuan Ding
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
- Tencent Inc.
arxiv_id: '2607.21519'
url: https://arxiv.org/abs/2607.21519
pdf_url: https://arxiv.org/pdf/2607.21519
published: '2026-07-23'
collected: '2026-07-24'
category: GenRec
direction: 生成式推荐 · 离散扩散语言模型
tags:
- Diffusion Language Model
- Discrete Diffusion
- Generative Recommendation
- Iterative Refinement
- Stochastic Tokenizer
- Curriculum Learning
one_liner: 提出离散扩散替代自回归生成，通过迭代去噪和协同感知 token 化实现更优推荐
practical_value: '- **推荐生成范式转换**：在需要生成商品集合或预测下一个交互对象的场景中，考虑用离散扩散替代自回归。扩散的迭代去噪可纠正早期错误，且双向建模更能捕捉
  item 间的全局依赖，尤其适用于行为顺序含有噪声的电商推荐。

  - **协同感知 tokenization 设计**：借鉴 CAST 的多跳随机量化思路，用 GNN 提取用户/商品的协同信号，通过温度调控的多码本随机映射生成离散
  token，可保留协同相似性，与 LLM 集成时比单纯 ID 或文本摘要更有效。

  - **课程式微调策略**：在 LLM 推荐微调中，可先采用 item 级掩蔽对齐（同时掩蔽 token 和文本描述）来建立离散 token 与语义的对应，再过渡到
  token 级掩蔽并引入偏好对比损失，逐步从语义理解迁移到推荐任务。

  - **投票式推理稳定化**：在扩散推理阶段，不丢弃中间预测，而是累积各步 log-prob 进行投票，对稳定位置早停，在不确定性高的位置融合更多信息，可提升推荐生成的鲁棒性和一致性，也可用于
  interpretable 推荐或多轮交互式推荐。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 LLM 推荐普遍采用自回归方式逐 token 生成 item，但推荐场景中用户行为序列的顺序关系远弱于语言，自回归易导致错误累积，且只能利用前缀信息。离散扩散语言模型通过双向建模和迭代去噪，天然契合从稀疏、噪声交互中恢复偏好结构的需求。初步实验表明扩散模型在推荐上训练更稳定且效果更优，但直接应用面临挑战：离散 token 需保留协同语义并兼容扩散过程；标准随机掩蔽忽略了推荐任务对偏好建模的要求；推理中的重掩蔽解码会丢弃有价值的中间预测。

**方法要点**
- **协同感知随机量化器 (CAST)**：用 LightGCN 提取用户/商品的多跳协同嵌入，每个 hop 对应一个子码本，通过 Top-S 相似度随机采样（温度随 hop 增加而升高）生成离散 token，无序列依赖且保留多粒度协同信号。训练时联合重建、码本对齐和对比损失，确保 token 的可区分性。
- **课程驱动训练**：阶段一采用 item 级掩蔽，同时掩蔽离散 token 和文本描述，难度逐步增加，迫使模型从残缺上下文建立 token-语义对齐；阶段二转为 token 级掩蔽，并引入偏好损失，通过软量化得到预测表示，与正样本拉近、与硬负样本推开，强化推荐判别力。
- **稳定性投票迭代精炼**：推理时进行多步去噪，对预测置信度稳定的目标 token 位置提前锁定，不稳定位置以用户条件先验和当前预测混合输入继续更新；最后对所有中间步的 log-prob 求和投票，得到最终 token 序列，用 CAST 解码后通过向量检索生成推荐列表。

**关键实验**
在 LastFM、MovieLens-1M 和 Amazon-Beauty 三个数据集上，与 GNN（LightGCN、SGL 等）、序列（SASRec、BERT4Rec）、扩散推荐（DiffRec、CDRec、LLaDaRec）和 LLM 推荐（TIGER、LLaRa、CoLLM、TokenRec）等基线对比。**主要结果**：在 MovieLens-1M 上，DLMRec 的 Recall@20 达到 0.2693，NDCG@20 达到 0.1875，比最先进的扩散推荐模型 LLaDaRec 分别提升 18.2% 和 16.3%，在所有数据集上一致最优，验证了离散扩散在推荐中的优势。

**一句话记住**：离散扩散语言模型将推荐重构为从被掩蔽的交互序列中逐步去噪恢复 item 的过程，用双向建模和投票精炼实现比自回归更准确、更稳定的生成式推荐。
