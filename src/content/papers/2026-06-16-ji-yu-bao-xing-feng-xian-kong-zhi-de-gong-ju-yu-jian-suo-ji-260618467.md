---
title: 'ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use
  Drift'
title_zh: 基于保形风险控制的工具与检索增强Agent轨迹级风险校准
authors:
- Jeffery Opoku
- David Banahene
affiliations:
- The University of Texas Rio Grande Valley
- Florida International University
arxiv_id: '2606.18467'
url: https://arxiv.org/abs/2606.18467
pdf_url: https://arxiv.org/pdf/2606.18467
published: '2026-06-16'
collected: '2026-06-18'
category: Agent
direction: Agent 轨迹风险控制·保形预测
tags:
- Conformal Risk Control
- Agent Trajectory
- Drift Detection
- Tool-Use
- Retrieval-Augmented Generation
- Anytime Alarm
one_liner: 将Agent完整轨迹作为校准对象，控制检索与工具使用漂移下的上游风险，避免仅依赖最终答案的风险盲区。
practical_value: '- **推荐链路的全轨迹风险校准**：在电商搜索/推荐的多级漏斗（召回→粗排→精排→重排→生成文案）中，可借鉴轨迹风险评分思想，对每一步（如召回是否覆盖、精排是否过度依赖某些特征、生成式推荐是否支持证据）赋予风险分数，整体校准一个接受/干预阈值，而非仅校验最终排序的指标。

  - **漂移检测与有效样本量监控**：引入基于轨迹相似度的漂移分数和有效样本量，用于线上监测推荐系统输入分布、用户行为、商品池变化。当有效样本量过低或漂移分数变大时，可自动触发更保守的策略（如提高重排门槛、回退到规则兜底）。

  - **随时报警与提前止损**：利用超鞅构造的anytime alarm，在推荐请求处理途中（如召回结果异常、工具调用失败、生成置信度过低）即停止，避免浪费后续计算资源并防止上线高风险结果。

  - **风险来源分解定位**：将总风险分解为检索贡献、工具使用贡献、合成贡献等，对应推荐中召回不相关、模型偏差、融合失误等问题，帮助快速定位系统薄弱环节并指导改进。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：现代AI Agent在生成最终答案前会进行检索、调用工具、核查中间信息，仅依靠最终答案的校准会忽略上游检索错误、工具输出不可靠等隐藏风险。论文指出，最终答案看起来可接受时，上游失败仍可能被接受，导致总体轨迹风险不受控。因此，需将整个Agent轨迹作为校准的统计对象。

**方法关键点**
- **轨迹风险建模**：将Agent运行完整记录为轨迹 τ = (请求, 动作, 观察, …, 最终答案)，对每一步定义原始风险分数 S_{i,j}（如检索不支持度、工具错误标志）和审计标签 Y_{i,j}。
- **轨迹级风险合成**：采用 noisy-or 或加权和将步骤风险聚合成轨迹风险分数 S^{traj}，形成单调接受阈值策略：若 S^{traj} ≤ λ 则接受，否则干预。
- **保形风险控制**：在交换假设下，对校准轨迹集用保形风险控制挑选最大可行阈值 λ̂，保证未来轨迹接受风险 E[R^{traj}(λ̂)] ≤ α，并提供有限样本保证。
- **漂移应对**：引入轨迹表示 φ(τ) 和基于核的权重，给出有效样本量与 Wasserstein 漂移边界，将漂移环境下的控制转化为近似保证，并提供可审计的漂移代理量 bD_t 和 Lipschitz 常数估计。
- **随时报警与诊断**：构造超鞅提前报警规则，在运行中途即可停止高风险轨迹；并输出检索、工具、合成等分项风险贡献、干预率、有效样本量等诊断信息。

**关键实验结果**
- 在合成工具链漂移、RAG/工具压力测试、SQuAD 衍生的检索支持实验、Agent QA 案例、20 种子鲁棒测试、漂移边界审计、线上 Agent 基准等多项实验中，仅校准最终答案的风险控制方法在漂移后风险显著超标（例如线上基准中风险达 0.355），而 ToolChain-CRC 维持在接受风险目标 0.08 以下，同时干预率合理。
- 漂移审计验证了方法在实际部署中可报告漂移幅度与校准支持度，防止在远离校准域时过度自信。

**核心启示**：Agent 安全必须监控整条行动链，而非仅校验最终输出。
