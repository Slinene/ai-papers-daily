---
title: 'DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs'
title_zh: 暗森林：通过受控通信提升多智能体大模型推理精度
authors:
- Yi Li
- Songtao Wei
- Dongming Jiang
- Zhichun Guo
- Qiannan Li
- Bingzhe Li
affiliations:
- University of Texas at Dallas
- Independent Researcher
- University of California, Davis
arxiv_id: '2605.25188'
url: https://arxiv.org/abs/2605.25188
pdf_url: https://arxiv.org/pdf/2605.25188
published: '2026-05-23'
collected: '2026-05-28'
category: MultiAgent
direction: 多智能体LLM协作 · 受控通信与证据校准
tags:
- Multi-Agent
- LLM
- Calibrated Belief
- Controlled Communication
- Reasoning
- Token Efficiency
one_liner: 提出受控通信框架 DarkForest，通过独立生成、校准信念和紧凑证据披露，在六个推理基准上取得领先精度，通信量降低高达 6.5 倍。
practical_value: '- 在多智能体投票/决策中，用校准信念代替简单多数投票：引入代理历史可靠性（α）、联合模式可靠性（R）、置信度重加权（ϕ）、解析质量折扣（ρ）和独立性校正（δ），生成后验分布指导最终选择，可减少电商推荐中多模型融合的误判。

  - 限制代理间通信：只向协调者暴露紧凑的候选摘要、支持模式和后验边距，不传递完整推理链，直接降低 token 消耗和延迟，适合高吞吐的在线 Agent 系统。

  - 采用“独立生成 + 协调者 + 确定性守卫”架构：协调者基于证据做出决策，只有当信念状态强烈支持某一候选且与协调者输出冲突时才触发守卫，防止强证据被大模型输出的随机性覆盖，可借鉴到客服/推荐的多路召回后融合。

  - 离线校准参数（可靠性、折扣因子等）无运行时额外开销：对电商 Agent 的历史行为日志进行离线统计即可建立代理可信度表，部署时不增加模型调用成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
多智能体 LLM 系统常通过交互提升推理，但无限制通信容易导致错误传播和推理成本激增：一旦错误理由被共享，后续代理可能采纳并放大错误，且多轮对话大幅增加 token 消耗、延迟和推理成本。本文受不完全信息博弈启发，认为关键不在“多交流”，而在“保留独立证据并控制跨越边界的消息”。

**方法关键点**  
- **独立生成**：各代理 (Qwen2.5-7B, Mathstral, Coder 等) 不互看输出，独立产生候选答案。  
- **解析与聚类**：将原始输出解析为结构化观察（规范候选、置信度、解析合法性），规范化等价答案并聚类成候选假设。  
- **校准信念**：为每个候选簇计算证据得分 `s(z) = Rπ * Σ(α_i * ρ_i * δ_i * ϕ(c_i))`，其中 `α_i` 代理可靠性、`Rπ` 支撑模式可靠性、`ρ_i` 解析质量折扣、`δ_i` 相关性惩罚、`ϕ(c_i)` 置信度乘子，归一化为后验分布。  
- **受控披露**：仅向协调者传递候选标识、后验质量、边距、不确定指示等紧凑证据，不暴露完整推理链。  
- **最终决策**：协调者基于输入和证据给出答案；确定型守卫仅当信念状态强烈支持一候选且与协调者输出冲突时替换结果。

**关键结果**  
在 MATH、HumanEval、MMLU-Pro、GPQA、FinQA、LegalBench 六个基准上评估，对比 Debate、Self-Consistency、Refine、ReConcile、Mixture-of-Agent、Graph-of-Agent 等方法。DarkForest 在 MATH 上准确率达 **76.8%**，比最强基线 Self-Consistency（71.8%）绝对提升 **5 个点（30.7% 相对提升）**，同时 token 消耗从 13.8k 降至 **4.7k（约 2.9 倍减少，与其他基准相比最高 6.5 倍）**。消融表明，协调者与守卫在专业领域（LegalBench）可互补：去掉守卫后准确率从 68.0% 跌至 65.6%，且守卫无额外模型调用。

**核心洞察**  
多智能体推理的关键不是增加通信，而是保留独立证据并控制哪些信息穿越代理边界。
