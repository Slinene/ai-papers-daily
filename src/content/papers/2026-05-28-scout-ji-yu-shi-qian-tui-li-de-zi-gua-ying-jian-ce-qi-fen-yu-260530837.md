---
title: 'Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in
  Prompt-Injection Defense'
title_zh: SCOUT：基于事前推理的自适应检测器分配防御提示注入
authors:
- Shuhao Zhang
- Jiarui Li
- Qi Cao
- Ruiyi Zhang
- Pengtao Xie
affiliations:
- UC San Diego
- University of Illinois Urbana-Champaign
arxiv_id: '2605.30837'
url: https://arxiv.org/abs/2605.30837
pdf_url: https://arxiv.org/pdf/2605.30837
published: '2026-05-28'
collected: '2026-06-10'
category: Other
direction: 提示注入防御 · 自适应检测器分配与路由
tags:
- Prompt Injection
- Detector Allocation
- Routing
- Safety–Utility Trade-off
- Pre-hoc Reasoning
- LLM Judge
one_liner: SCOUT 通过预测各检测器对每个请求的可靠性与延迟，动态分配轻量检测器并按需升级至 LLM 法官，实现可控的安全-效用权衡
practical_value: '- **多检测器动态分配架构**：可借鉴"指纹+预测器"的轻量路由思路，为电商推荐系统的多模型服务（如不同召回、排序模型组合）建立自适应调度，根据请求特征选择最优模型子集，避免昂贵的全模型调用。

  - **成本-质量可预测控制**：通过事前估计延迟和正确性并绑定单一阈值，可实现服务等级协议（SLA）管理，如限时延迟预算，自动选择满足延迟约束下最可靠的模型组合，适用于在线推理的时序控制。

  - **异质模型池的无缝扩展**：新检测器仅需在锚点集上记录行为即可加入路由，无需重训练路由策略，该模式可直接迁移到多模型服务中，降低新增模型的上线成本。

  - **风险分级与升级机制**：在 Agent 工作流中，可将不确定请求升级至更强大的模型（类 LLM 法官），平衡安全与成本，适用于高敏感对话、交易风控等场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：提示注入检测器存在明显的异质性——不同检测器擅长捕捉不同类别的攻击，但无单一检测器在所有场景下最优；而现有防御体系通常固定使用单个检测器或固定级联顺序，导致流量暴露于所选检测器的盲区。SCOUT 将防御问题重定义为**按请求的检测器分配**：依据输入特征动态决策激活哪些轻量检测器、何时升级至昂贵的 LLM 法官，从而在安全与效用（吞吐量、延迟）之间取得更优平衡。

**方法关键点**：
- **检测器指纹**：为每个检测器在预定义的锚点集上记录判决和延迟，形成结构化指纹，新检测器加入仅需一次指纹生成，无需重训练路由器。
- **检索增强预测**：针对每个请求，通过稠密检索相似锚点的指纹切片，输入小型预测模型（Qwen3-4B，经 SFT+GRPO 训练），预测每个检测器的**正确性**和**延迟**。
- **不确定性感知路由**：根据预测可靠性筛选轻量检测器并行运行，当它们加权投票的一致性低于可调阈值τ时，且预测显示 LLM 法官可靠，则升级至法官。τ 直接控制安全-延迟权衡，且通过预测延迟可预先满足延迟预算。
- **数据**：构建 SCOUT-450（450 条，严重攻击丰富）评估集，SCOUT-30K 训练集和 Anchor-400 锚点集。

**关键实验结果**：
- 在 SCOUT-450 上，操作点 τ=0.875 时，SCOUT 相比始终调用 GPT-4o 法官，**攻击成功率降低 46%（0.118→0.063）**，总墙钟时间减少 **40%**，良性效用仅从 0.979 降至 0.928。
- 在 BIPIA、IPI、IHEval 三个外部基准上无重训练迁移，均提升了安全-效用前沿；例如在 BIPIA 上准确率从 0.894 跃升至 0.971，延迟从 1654 秒降至 309 秒。
- 通过更换 LLM 法官或增减检测器，SCOUT 保持同一路由规则下的平滑可控变换，展示了对异质池的动态适应能力。
