---
title: 'From Search to Decision: How Post-Training Shapes Information-Seeking Capabilities
  in Large Language Models'
title_zh: 从搜索到决策：后训练如何塑造大模型的信息搜寻能力
authors:
- Haohang Huang
- Xuan Lu
- Mingjin Kuai
- Yuxuan Zhang
- Wei Ji
- Haiyang Zhang
affiliations:
- Xi'an Jiaotong-Liverpool University
- Shanghai Jiaotong University
- Nanjing University
- University of British Columbia
arxiv_id: '2611.14149'
url: https://arxiv.org/abs/2611.14149
pdf_url: https://arxiv.org/pdf/2611.14149
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: LLM 搜索决策的 post-training 综述
tags:
- Post-training
- Information Seeking
- RL
- RAG
- Search Agent
- Credit Assignment
one_liner: 以六项信息搜寻能力为中心，系统梳理后训练信号、优化器、更新位置与信用分配的证据与空白
practical_value: '- 把搜索型推荐/导购 agent 拆成六项可独立评估的能力：是否检索、查询表达、探索、证据评估、证据整合、自适应控制；不要只看端到端准确率，每项行为配对应指标，如
  retrieval routing 用 tool-use 决策、query 用 evidence coverage、budget 用搜索步数。

  - 长链路搜索/推荐 agent 不要只用最终答案 reward：借鉴 StepSearch 的信息增益/冗余惩罚、TRACE/CriticSearch 的回顾性
  turn-level value 估计，能提升长 horizon 训练稳定性，减少客服/导购场景的过早停止或重复搜索。

  - 检索决策要学“效用”而非“难度”：CoBRA 的 tool/no-tool counterfactual margin、AnySearch 的 budget-aware
  RL 值得复用；成本敏感业务可训练时采样不同 budget 做 unseen budget 泛化。但 query refiner 学到的偏好与特定 retriever
  耦合，跨搜索引擎部署需重新适配或做 environment-aware 训练。

  - 评估必须控制变量：用 fixed-history feedback intervention（固定历史/预算，只变最新 observation）判断是否真的
  feedback-conditioned；报告 generalization 改变的维度是 retriever/corpus/tool/budget，否则容易被端到端分数误导。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 越来越多地通过与外部信息环境交互完成知识密集型任务，检索不再是固定预处理步骤。现有综述多按系统架构、检索流程或优化技术组织，缺少以“能力”为中心的视角；不同 post-training 方法的信号、目标、更新单元差异大，仅看下游分数难以比较。因此需要把信息搜寻拆成可独立评估的能力，并连接学习机制与实证证据。

**方法关键点**
- 六项能力：epistemic awareness & retrieval utility（是否/值不值得检索）、information-need formulation（怎么表达 query）、information-space exploration（去哪找）、evidence evaluation（证据支持/充分/可靠）、evidence integration & belief revision（信念更新与忠实使用）、adaptive search control（观察后继续/改写/换源/停止）。
- 四个机制维度：learning signals（演示、交互轨迹、outcome reward、行为专用 reward、counterfactual preference）、policy optimization（SFT/DPO/RL/hybrid/teacher-guided）、update loci（整体策略 vs 专用组件如 query refiner/evidence verifier/memory）、credit assignment（中间 reward、retrospective critic、state-value TRACE、teacher-student SSPO）。
- 代表方法：CoBRA 用 tool/no-tool counterfactual margins 学检索边界；QREF 只训练 query refiner 不重训 reasoning agent；Search-R1 用最终正确性联合优化搜索与推理；AnySearch 做 budget-aware RL；TRACE 用 gold-conditioned state value 分配 turn-level credit。

**关键结果数字**
作为综述，没有新实验数字，但归纳已有工作的证据：检索路由与预算控制有直接动作级评测；query 改写用 retrieval gain/coverage；多工具探索用 recall/diversity；证据能力用 span support/sufficiency/grounded QA/counterfactual；自适应控制用 unseen budget 和 feedback-conditioned 干预。泛化方面，AnySearch 在 unseen budget 有效，CoBRA 在 OOD tool-use 有效，QREF 跨 agent backbone 有效；但 Environment-aware IR 发现学到的 query 模式可能依赖特定 retriever，跨 retriever 收益会下降。开放问题：prospective retrieval utility estimation、多能力协调、跨环境 adaptive control。

**最值得记住的一句话**：关键在于区分“是否需要检索”与“检索是否划算”，并用行为级指标和受控干预识别真正学到的能力，而不是只看端到端分数。
