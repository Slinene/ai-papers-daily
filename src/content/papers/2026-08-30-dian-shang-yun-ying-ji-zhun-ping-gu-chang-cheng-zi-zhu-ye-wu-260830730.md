---
title: 'E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business
  Operation'
title_zh: 电商运营基准：评估长程自主业务运营的 LLM Agent
authors:
- Wei Fan
- Xinjie Shen
- Xudong Guo
- Jianhong Tu
- Yang Su
- Yinger Zhang
- Lianghao Deng
- Fengyu Wang
- Baohua Dong
- Yangqiu Song
affiliations:
- Qwen Team, Alibaba Group
- Taobao & Tmall Group, Alibaba Group
- HKUST
arxiv_id: '2608.30730'
url: https://arxiv.org/abs/2608.30730
pdf_url: https://arxiv.org/pdf/2608.30730
published: '2026-08-30'
collected: '2026-09-02'
category: Eval
direction: Agent 长程运营评测基准
tags:
- LLM Agents
- Benchmark
- E-commerce
- Negotiation
- Long-Horizon
- Deterministic Simulation
one_liner: 首个开源电商运营基准，融合确定性谈判、动态事件与真实数据，评估 LLM Agent 全年自主经营的多维能力
practical_value: '- 确定性对手内核：在评估谈判/交互 Agent 时，将对手定价、让步、接受/拒绝逻辑做成确定性规则内核，LLM 只负责语言渲染，避免对手模型随机性污染评估；业务中训练电商谈判机器人的奖励函数也可用此分离增强可复现性。

  - 现金流延迟与破产约束：采用银行/托管/钱包三账户和 9 天结算延迟，能暴露 Agent 只追求 GMV 而忽视流动性的问题；在电商运营 Agent 或推荐系统收益模拟中，加入类似延迟结算和破产惩罚可避免短视策略。

  - 信息不对称工具设计：让查询返回标签（如高/中/低利润潜力）而非具体参数，迫使 Agent 通过探索和结果推断学习，而不是直接读取底层数据；在构建智能运营助手时，可有意隐藏部分系统参数，训练模型做因果推断和试错。

  - 多维评估雷达图：不要只用利润/GMV 作为唯一指标，应同时评估欺诈损失、现金流回撤、运营效率（每工具调用产出）、学习能力（重复采购降价趋势）；在选型推荐/运营
  Agent 时建立类似能力画像，否则可能选到高利润但高风险模型。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：现有长程 agentic benchmark 要么依赖 LLM 模拟对手导致随机性不可复现，要么缺少谈判、对抗动态或真实数据，难以评估 Agent 在持续业务运营中的学习与适应能力。

方法关键点：
- 环境：365 天模拟，初始资金 ¥100,000，最多经营 4 个网店；数据来自淘宝天猫，含 6,886 个商品、576 个供应商（其中 152 个欺诈）。
- 确定性双市场：客户购买/退货由固定多因素需求模型决定（价格弹性、周末、季节、促销、事件、声誉、容量限制）；供应商谈判由确定性谈判内核控制，LLM 仅渲染对话。
- 三账户延迟结算：银行、托管、钱包，现金流延迟 9 天，连续 10 天负余额破产。
- 信息不对称：隐藏成本底线、需求参数、供应商类型；市场查询只返回粗略标签。
- 上下文管理：128k token 预算，120k 触发驱逐，保留系统提示、首轮和最新两组；持久记忆最多 20 条笔记。
- 18 个工具调用消耗模拟分钟，一天 600 分钟。

关键结果数字：评估 18 个模型 ×5 episodes。GPT-5.6 Sol 年末资产最高 ¥1,431,425（14.31x），但欺诈避免排第 16；Fable5 运营效率最高（¥479/tool call）；Claude Opus 4.7 谈判和欺诈避免最佳但利润中等；开源最佳 Qwen3.8-Max-Preview ¥416,252（4.16x）且学习能力最强；4/18 模型部分跑破产；在 8,647 次重复采购中，16 个模型未显示逐年压低采购价的明确趋势。

最值得记住的一句话：年末资产第一的模型欺诈避免排第 16，单一利润指标掩盖能力短板，必须用多维能力画像评估 LLM Agent。
