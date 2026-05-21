---
title: 'LamPO: A Lambda Style Policy Optimization for Reasoning Language Models'
title_zh: LamPO：一种 Lambda 风格的推理语言模型策略优化
authors:
- Zhe Yuan
- Yipeng Zhou
- Jinghan Li
- Xinyuan Chen
- Bowen Deng
- Zhiqian Chen
- Liang Zhao
affiliations:
- Pinterest
- Facebook
- University of Michigan - Ann Arbor
- Mississippi State University
- Carnegie Mellon University
arxiv_id: '2605.21235'
url: https://arxiv.org/abs/2605.21235
pdf_url: https://arxiv.org/pdf/2605.21235
published: '2026-05-20'
collected: '2026-05-21'
category: Training
direction: 推理语言模型 · RLHF/RLVR 优化
tags:
- RLVR
- GRPO
- pairwise advantage
- lambda policy optimization
- reasoning
- ROUGE-L
one_liner: 用成对分解优势替代标量组优势，保留组内排序关系，提升RLVR样本效率与稳定性
practical_value: '- 如果在训练对话/生成式推荐策略时使用 GRPO 等组相对训练，可借鉴成对优势分解：将组内每个样本与所有其他样本的奖励差用策略
  log 概率差加权求和，保留细粒度排序信息，改善信用分配。

  - 置信度权重 σ(Δs/τ) 简单实用：直接使用策略自身对样本对的偏好程度调节学习强度，可扩展到其他需要组内比较的场景。

  - 对于有参考答案/轨迹的 RL 训练，可加入基于 ROUGE-L 的稠密辅助奖励，缓解稀疏正确性奖励下的学习困难，微小代价换取样本效率提升。

  - 训练稳定性提升在小型模型的实验中表现明显，对资源受限下的快速迭代有帮助。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
在 RLVR（基于可验证奖励的强化学习）中，GRPO 等主流方法将每个采样组内的回应压缩为均值和标准差，丢弃了回应之间的成对排序信息。当奖励稀疏（如只有 0/1 正确性）且回应的推理质量差异细微时，这种标量基线难以分辨“接近正确”和“完全错误”的样本，影响信用分配效率。  

**方法关键点**  
- **成对分解优势 (PDA)**：对于组内每个回应 \( o_i \)，计算其与所有其他回应 \( o_j \) 的奖励差 \( R(o_i)-R(o_j) \)，并用 \( \sigma( (\log \pi(o_i) - \log \pi(o_j)) / \tau ) \) 作为置信度权重进行加权平均，得到 \( A_\lambda(o_i) \)。这保留了组内的相对排序关系，而不仅是偏离均值的程度。  
- **PPO 式裁剪更新**：直接替换 GRPO 中的标量优势，保持 critic-free 和 clipped surrogate objective。  
- **稠密辅助奖励**：当有参考答案时，加入生成回应与参考答案的 ROUGE-L F1 分数作为额外信号，缓解稀疏奖励，系数 \( \lambda_{sem} \) 控制强度。  
- **计算开销**：成对比较带来 \( O(G^2) \) 开销，但组大小 G 通常很小，可接受。  

**关键实验结果**  
在 AIME24、AIME25、MATH-500、GPQA-Diamond 上使用 Qwen3-1.7B/4B 和 Phi-4-mini 训练。  
- Qwen3-1.7B 上 LamPO 平均分 53.60，相比 GRPO (51.42) 提升 2.18，其中 AIME24 由 42.08 提高到 46.67。  
- Qwen3-4B 上 LamPO 平均分 77.09 vs GRPO 75.40，AIME24 由 71.67 升至 74.66。  
- Phi-4-mini 上 LamPO 平均 56.88 vs GRPO 55.35。  
- 训练曲线显示 LamPO 的奖励增长更平稳，生成长度更稳定。  

**最值得记住的一句话**  
用策略自身的 log 概率差对成对奖励差距进行加权，保留组内细粒度排序，使 RLVR 在稀疏奖励时获得更丰富的学习信号。
