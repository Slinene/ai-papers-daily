---
title: 'GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time
  Latent Reasoning'
title_zh: GradCuit：通过信用分配梯度流实现鲁棒可解释的测试时潜在推理
authors:
- Zhaoxin Yu
- Qi Shen
- Hengli Li
- Zhaowei Zhang
- Song-Chun Zhu
- Chi Zhang
- Zilong Zheng
affiliations:
- NLCo Lab, Beijing Institute for General Artificial Intelligence
- Institute of Automation, Chinese Academy of Sciences
- School of Artificial Intelligence, Beijing University of Posts and Telecommunications
- School of Artificial Intelligence for Science, Peking University
arxiv_id: '2608.02585'
url: https://arxiv.org/abs/2608.02585
pdf_url: https://arxiv.org/pdf/2608.02585
published: '2026-08-02'
collected: '2026-08-05'
category: Reasoning
direction: LLM 测试时潜在推理优化
tags:
- test-time optimization
- latent reasoning
- credit assignment
- gradient attribution
- interpretability
- LLM
one_liner: 在 Transformer 层插入可优化隐状态，利用因果注意力将奖励梯度直接赋予隐状态，提升推理精度与鲁棒性
practical_value: '- **测试时在线优化机制**：在 Agent 多步推理或推荐流程中，可以在不更新模型参数的前提下，为每个样本动态优化一组中间隐状态，类似于为当前上下文“微调”表示。这对搜索推荐中实时适应用户意图、处理长对话状态有参考价值。

  - **信用分配直接化**：GradCuit 的奖励加权梯度直接回传至隐状态，无需通过序列解码展开。在电商多轮对话或步骤反馈奖励（如用户点击）的场景下，可借鉴这种直接对中间表示做梯度更新的思路，替代复杂的强化学习估计。

  - **工程实现简单且超参数鲁棒**：该方法只需在某一层插入可训练向量，训练过程稳定，对学习率不敏感，甚至随机游走变体也有效。对于需要低延迟在线优化的系统，这种低超参敏感性的方法易于工程落地。

  - **可解释性可视化**：通过梯度归因可以分析哪个 token 或哪一层对最终决策影响最大，这可用于调试策略、排查推荐解释或优化 prompt 设计，在需要强可解释性的业务场景中有潜在应用价值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：传统测试时潜在推理方法通过解码 token 间接影响后续推理，导致信用分配模糊，难以解释隐状态更新的作用机理。

**方法**：GradCuit 在选定 Transformer 层的前向过程中，将一组可优化的潜在变量拼接在 prompt 的隐藏表示之后、生成续写之前。由于因果自注意力机制赋予每个续写 token 的对数概率对之前的所有潜在变量一条可微路径，因此可以直接用整个生成序列的奖励加权对数概率作为损失，通过梯度下降优化这些隐状态。该方法无需额外策略网络，只需在冻结的 LLM 内进行少量步数的在线优化。

**结果**：在 5 个指令微调主干、3 个推理基准（数学与逻辑）及两种答案格式上，GradCuit 平均准确率达 64.5%，比 chain-of-thought 提示高 6.6 个百分点，比最强竞争方法 LatentSeek 高 2.4 个百分点。在 7 种学习率设置下，GradCuit 的标准差仅 0.82（LatentSeek 为 1.53），且随机游走变体也能与 LatentSeek 持平。梯度归因显示隐状态的影响集中在推理连接词（如“因此”），层分析表明早期到中层 Transformers 是最优优化空间。
