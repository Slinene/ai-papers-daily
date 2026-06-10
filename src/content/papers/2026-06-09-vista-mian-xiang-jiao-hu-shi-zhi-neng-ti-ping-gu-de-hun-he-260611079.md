---
title: 'VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation'
title_zh: VISTA：面向交互式智能体评估的混合用户仿真工具包
authors:
- Yunan Lu
- Ryan Shea
- Yusen Zhang
- Zhou Yu
affiliations:
- Columbia University
- Arklex.ai
arxiv_id: '2606.11079'
url: https://arxiv.org/abs/2606.11079
pdf_url: https://arxiv.org/pdf/2606.11079
published: '2026-06-09'
collected: '2026-06-10'
category: Eval
direction: 交互式智能体评估 · 混合用户仿真
tags:
- User Simulation
- Agent Evaluation
- Hybrid Simulation
- Metrics
- E-commerce
one_liner: 结合 UI 与 API 混合仿真并引入覆盖率、真实感等六项指标，更全面地暴露智能体故障
practical_value: '- **混合仿真架构**：在电商客服或对话式推荐 Agent 评估中，可借鉴 UI 交互与 Mock API 相结合的方式，用
  API 可靠提供用户订单、账户等结构化信息，避免纯 UI 导航的噪声与误操作，同时更全面地触发 Agent 故障。

  - **覆盖率指标用作自动质量信号**：工具转移熵、工具分布熵、轨迹距离等指标无需人工标注就能衡量仿真多样性；实践中可用其持续监控仿真器是否能充分探索 Agent
  能力边界，作为评估有效性的代理指标。

  - **故障自动识别框架**：LLM-as-Judge 从 helpfulness/coherence/relevance 等五维度评分后合并故障理由，可自动化地归类
  `false information`、`repetition` 等典型错误，辅助 Agent 迭代优化。

  - **真实感一致性的自动评测**：用户画像、目标与领域知识一致性评测采用参考无的 LLM 判断，与人类评分正相关（ρ=0.60），可作为仿真质量快速反馈信号，无需昂贵人工评估即可调优仿真策略。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
交互式智能体（如电商客服、教育支持）在真实多轮场景下容易暴露静态基准无法捕获的故障模式。现有用户仿真评估方法常局限于纯 UI 或纯 API 交互，且缺乏对仿真质量本身的度量，难以判断仿真是否充分探索了智能体的能力边界和故障空间。

**方法关键点**
- **混合用户仿真器**：同时支持 UI 动作（点击、输入、滚动等）和 API 工具调用（如查询订单、账号信息、模拟考试调度等），通过观察-规划-动作循环动态路由，先用 API 获取结构化信息再执行 UI 交互，提高仿真可靠性与多样性。
- **六项评估指标**：
  - 覆盖率：工具转移熵（TE）、工具分布熵（TDE）、轨迹距离（TD），衡量智能体被导向的工具调用多样性和轨迹差异度。
  - 真实感：用 LLM 评测用户话语与画像、目标、知识的一致性，反映仿真行为的人类相似度。
  - 成本：每轮 token 与动作数，代理时间和金钱开销。
  - 故障识别：LLM-Judge 基于五维度（helpfulness, coherence, verbosity, relevance, faithfulness）评分后聚合为唯一故障数，评估暴露问题的广度。
- **场景构建**：为每次交互定义用户画像、目标及领域知识，生成有约束的仿真场景；任务专用工具通过 Mock API 实现多样化返回（成功/失败/边界情况）。

**关键实验**
在电商购物（Shopify 13 个工具）和教育客服（8 个 Mock 工具）两个领域，使用 gpt-5.4 和 Qwen3.5-27B 分别生成 100 条混合 vs UI-Only 交互。
- 混合仿真在覆盖率指标上最高提升 10%，识别出的唯一故障数比 UI-Only 多 42%。
- 人类评估中，混合仿真在类人性、连贯性、目标一致性上均优于 UI-Only，且被误判为人类的概率高 6%。
- 自动化真实感评分与人类评分 Spearman 相关系数 0.60，指标有效。
- 案例分析显示混合仿真能更精准地还原用户行为（如准确报出订单号），从而暴露 Agent 错误处理缺陷。

核心结论：通过 UI+API 混合交互和配套质量指标，VISTA 能以更贴近真实、更高覆盖度的方式评估交互式智能体，为电商客服等场景提供更可靠的自动化评估范式。
