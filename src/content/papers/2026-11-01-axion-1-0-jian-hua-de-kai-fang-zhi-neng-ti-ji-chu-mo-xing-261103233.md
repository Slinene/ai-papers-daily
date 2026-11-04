---
title: 'Axion 1.0: Open Agent Foundation Models, Simplified'
title_zh: Axion 1.0：简化的开放智能体基础模型
authors:
- Yuqi Jia
- Yunjie Tian
- Jiayu Zheng
- Yijun Liang
- Jingchen Sun
- Mengyu Zhao
- Di Fu
affiliations:
- Duke University
- ByteDance
- University of Maryland, College Park
- University at Buffalo
arxiv_id: '2611.03233'
url: https://arxiv.org/abs/2611.03233
pdf_url: https://arxiv.org/pdf/2611.03233
published: '2026-11-01'
collected: '2026-11-04'
category: Agent
direction: Agent 基础模型 · 三阶段极简训练
tags:
- Agent
- RL
- SFT
- Synthetic Data
- Tool Use
- GRPO
one_liner: 用两阶段 SFT 加 RL 的极简 recipe，构建可复现的开放 Agent 基础模型，在多项 agentic 基准上达到前沿水平
practical_value: '- **模型感知的数据增强**：Stage I 用基座模型能否解出作为难度筛选器，只对能解出的题目做组合、参数化、范围移位、分情况讨论等对抗式改写，让数据难度贴合模型能力边界。电商场景中构造训练数据时，可以先用线上模型筛选出“太简单”的样本，再做变体改写，从而提升训练集的信息密度。

  - **可验证工具任务生成**：Stage II 的 filter-select-compute-verbalize 流水线把结构化商品/内容库转化为需要检索+计算的问答，答案由确定性程序预计算，支持自动验证。对于电商搜索、比价、选品等
  agent 任务，可以类似地从商品数据库抽取属性，设计需要多步工具调用和计算的题，自动获得带 ground-truth 的服务数据。

  - **RL 奖励设计**：对未解出的轨迹给部分信用，公式 `max(0, 0.3P - 0.1(1-A))` 鼓励中间步骤正确但最终未提交的探索，同时惩罚无终态的输出。在业务
  RL 中，长链路 agent 任务（如导购对话）往往最终转化稀疏，引入可验证中间目标（如识别的实体、检索到的属性）能有效缓解奖励稀疏。

  - **训练-推理一致性工程**：TITO 直接传递 token ID 避免 message re-tokenize 导致的数据漂移；R3 重放 MoE expert
  routing 降低 rollout 与训练 logprob 偏差。电商推荐系统若使用 MoE 大模型做 agent 微调，可参考这两项工程实践，减少离线-在线性能
  gap。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

现代 Agent 基础模型的训练管线越来越复杂，集成了 mid-training、多个 SFT 阶段、DPO、OPD 等组件，不仅难以复现，也难以定位能力来源。论文追问：构建强泛化 Agent 基础模型到底需要多少复杂度？

**方法关键点**

- **三阶段极简 recipe**：只做两个 lightweight SFT 阶段（Stage I 自包含推理 + Stage II 工具依赖推理）加一个 GRPO 强化学习阶段，无 mid-training、DPO、OPD。
- **Stage I 模型感知数据构造**：以公开课程/竞赛题做种子，先做组合增强；再用基座模型验证，能解出的题目继续用 Composition、Parameterization、Range Shift、Case Analysis 四种操作对抗式增强；每个新题用 GPT-5.5 独立解三次验证答案，最终保留约 10.8K 条正确轨迹。
- **Stage II 可验证工具任务生成**：从真实数据库触发，用 filter-select-compute-verbalize 四步构造需要搜索、网页访问和计算的题；建设期数据库被屏蔽，剔除闭卷即可回答的题，确保题目必须依赖外部工具；保留 7.5K 条正确轨迹，并附带中间验证目标。
- **RL 奖励设计**：最终答案正确得 1，否则通过验证中间目标给部分信用，公式 `max(0, 0.3P - 0.1(1-A))`，并过滤掉全不正确或奖励无方差的题。
- **工程加强**：SFT 用 FSDP + expert parallelism + context parallelism 支持 128K 长轨迹；RL 用异步 GRPO + TITO（Token-In-Token-Out）保持 token 一致性 + R3（Rollout Routing Replay）回放 MoE 路由。

**关键实验**

在 HLE、BioMysteryBench、SEAL-0、HiPhO、FrontierScience Olympiad/Research 六个基准上评估，对比 Agents-A1、Kimi-K2.6、GPT-5.5、GPT-5.6 Sol、Gemini 3.1 Pro、Claude Opus 5 等。Axion 1.0-35B 在 HLE 达 52.2%、SEAL-0 达 62.2%、FrontierScience Olympiad 达 86.0%；122B 在 FrontierScience Research 达 66.7%，超过 GPT-5.6 Sol 的 63.3%。训练阶段消融显示 Stage I 主要提升科学推理，Stage II 主要提升 BMB、SEAL-0 等信息获取任务，RL 进一步提升 HLE-130 和 SEAL-0，对科学推理涨幅不稳定。SFT 成本仅 7.5h（122B，240 GPU-hours）。

**最值得记住的一句话**

强 Agent 能力不必依赖堆叠专用的训练阶段；用模型自身的能力边界做对抗式数据构造，配合确定性的可验证工具任务生成，再叠加一层 RL，就能以极简管线逼近前沿水平。
