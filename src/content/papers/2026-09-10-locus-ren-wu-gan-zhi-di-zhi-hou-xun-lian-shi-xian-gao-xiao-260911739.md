---
title: 'LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation'
title_zh: LOCUS：任务感知低秩后训练实现高效 token 语言生成
authors:
- Dongfang Zhao
affiliations:
- University of Washington
arxiv_id: '2609.11739'
url: https://arxiv.org/abs/2609.11739
pdf_url: https://arxiv.org/pdf/2609.11739
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 低秩后训练控制 LLM 输出 token 成本
tags:
- token efficiency
- DPO
- low-rank adaptation
- verbosity bias
- LLM serving
one_liner: 冻结主干，在任务相关低秩子空间内做偏好优化，仅更新0.24-0.28%参数即可显著降低输出长度
practical_value: '- 在电商/广告/Agent 场景中，LLM 生成商品文案、推荐解释、客服回复或搜索词时，输出长度直接决定推理成本与首字延迟。LOCUS
  提示可以不在全参上做偏好对齐，而是冻结基座，用低秩适配器训练“简洁但保持有用”的偏好，参数更新量极小，便于线上灰度、热切换和快速回滚。

  - 将输出 token 成本显式建模为约束优化：在 utility 约束下最小化长度。业务上可借鉴为“在转化率/相关性不显著下降的前提下，最小化生成 token
  数”，用带长度惩罚或约束的 DPO 目标训练，避免模型学到“长回复=高偏好”的 verbosity bias。

  - 任务感知的低秩子空间选择可以迁移为场景化适配器：不同业务（广告标题、搜索建议、Agent 任务规划）用不同低秩 subspace，分别控制生成长度，既保持各场景特有偏好，又避免冗长输出。

  - 工程收益：论文显示仅更新约 0.25% 参数即可获得长度显著下降，这对需要频繁迭代偏好模型的多租户推荐/广告系统尤其有价值，可以大幅降低存储、训练和部署成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 服务成本随输出 token 数线性增长，但标准偏好对齐（如 DPO）常导致模型生成更冗长而实用价值未提升的响应，增加 KV cache 与延迟开销。

方法：LOCUS 研究后训练参数化对生成长度的影响，不修改对齐损失本身，而是选择一个任务相关的低秩适应子空间，冻结主干网络，仅在该子空间内进行原生偏好优化。目标形式化为在 utility 约束下最小化输出 token 成本，从而抑制 verbosity bias。

结果：在 Anthropic HH-RLHF 对话偏好数据上，对 Pythia-2.8B 与 Qwen2.5-3B 两个约 3B 解码器模型进行评估，对比协议匹配的全参 DPO、DrDPO 以及已发布 SamPO checkpoint。LOCUS 在 Pythia-2.8B 上将续写长度最高降低 39.84%，在 Qwen2.5-3B 上降低 14.87–17.58%，而只更新 0.24–0.28% 的模型参数，同时内部偏好诊断无显著变化，表明在保持偏好质量的同时有效降低生成 token 成本。
