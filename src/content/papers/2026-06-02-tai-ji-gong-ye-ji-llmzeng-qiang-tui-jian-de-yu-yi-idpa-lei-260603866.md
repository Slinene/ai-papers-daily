---
title: 'Taiji: Pareto Optimal Policy Optimization with Semantics-IDs Trade-off for
  Industrial LLM-Enhanced Recommendation'
title_zh: 太极：工业级LLM增强推荐的语义-ID帕累托最优策略优化
authors:
- Yuecheng Li
- Zeyu Song
- Jing Yao
- Chi Lu
- Peng Jiang
- Kun Gai
affiliations:
- Kuaishou Technology
- Unaffiliated
arxiv_id: '2606.03866'
url: https://arxiv.org/abs/2606.03866
pdf_url: https://arxiv.org/pdf/2606.03866
published: '2026-06-02'
collected: '2026-06-03'
category: RecSys
direction: LLM增强推荐 · 帕累托最优RL对齐
tags:
- LLM4Rec
- GRPO
- Pareto Optimization
- Semantic-ID
- Industrial Recommender
- RLHF
one_liner: 通过逆推推理生成高质量CoT和帕累托最优策略优化实现LLM语义与推荐ID信号的动态平衡，提升广告收入
practical_value: '- **数据蒸馏与过滤**：利用逆推推理（RUPR）和基于PPL的拒绝采样（ORFT）生成高质量、领域相关的CoT数据，可借鉴到电商评论分析、用户意图理解等需要长文本推理的场景，尤其适合在缺少精确标注时自动筛选可靠推理路径。

  - **动态多奖励平衡**：POPO通过梯度对齐或奖励变异系数动态调整语义和ID奖励权重，避免手工固定权重，适用于多目标对齐的Agent训练或生成式推荐，能自动找到帕累托最优解，提升综合效果。

  - **轻量级实现**：POPO-light仅用rollout奖励的均值和标准差，零额外计算开销，适合工业级大规模RL训练；可直接嵌入现有GRPO流程，在算力受限时作为快速替代方案。

  - **特征工程与检索增强**：将LLM生成的语义表征量化为稀疏ID特征，并检索相似用户的行为序列作为排序模型输入，这种增强方式不改变主模型架构，可平滑迁移到推荐、广告等场景，对长尾用户效果显著提升。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM-as-Enhancer是工业界主流的推荐增强范式，但现有方法存在两个瓶颈：(1) SFT阶段缺乏对推荐领域CoT质量的可靠度量，导致微调数据噪音大；(2) RL阶段用固定权重组合LLM语义奖励和推荐ID奖励，忽略了二者之间的动态权衡，无法达到帕累托最优。

**方法关键点**：
- **逆推用户偏好推理（RUPR）**：利用用户的实际购买记录作为提示，让强大的教师模型（QwQ-32B）进行反向推理，生成可靠的CoT数据，保证答案的真实性。
- **开放式拒绝采样微调（ORFT）**：用目标物品的PPL作为CoT质量的代理指标，过滤掉低质量样本（PPL>中位数），然后对7B基座模型（DeepSeek-R1-7B）进行SFT，激活推理能力。
- **帕累托最优策略优化（POPO）**：在GRPO框架中，通过梯度对齐指标动态更新各奖励的权重，使得优化方向逼近帕累托前沿；同时提出轻量版POPO-light，仅用奖励的变异系数自适应调整权重，几乎零额外开销。
- **在线部署**：将RL优化后的LLM产生的CoT与答案编码、量化成稀疏特征，并检索相似用户的行为序列，共同输入广告排序模型，不改变主架构。

**关键结果**：
- 离线测试：Taiji (ORFT+POPO) 相比基座 DeepSeek-R1-7B，一级类目准确率提升55.96%，CTCVR提升11.68%，并全面超越32B教师模型。
- 在线A/B：在快手广告平台，整体广告主价值（ADVV）+2.83%，平台收入+3.30%；长尾用户增益更显著（ADVV +5.26%，收入+5.32%）。
- 已全量部署，服务超过4亿日活用户。

**核心洞见**：通过逆推推理保证CoT质量，再用动态帕累托优化平衡语义与协同信号，是实现工业级LLM增强推荐的有效路径。
