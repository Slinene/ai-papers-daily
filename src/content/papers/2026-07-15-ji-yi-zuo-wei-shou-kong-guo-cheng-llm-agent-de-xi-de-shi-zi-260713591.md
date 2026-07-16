---
title: 'Memory as a Controlled Process: Learned Adaptive Memory Management for LLM
  Agents'
title_zh: 记忆作为受控过程：LLM Agent 的习得式自适应记忆管理
authors:
- Eric Hanchen Jiang
- Zhi Zhang
- Yuchen Wu
- Levina Li
- Dong Liu
- Xiao Liang
- Rui Sun
- Yubei Li
- Edward Sun
- Haozheng Luo
affiliations:
- University of California Los Angeles
- University of Washington
- Northwestern University
arxiv_id: '2607.13591'
url: https://arxiv.org/abs/2607.13591
pdf_url: https://arxiv.org/pdf/2607.13591
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 自适应记忆控制 · Contextual Bandit
tags:
- Agentic Memory
- Contextual Bandit
- Adaptive Retrieval
- Backend-Agnostic
- UCB
one_liner: 将 Agent 记忆访问建模为 MDP，用在线 contextual bandit 学习自适应策略，零额外 LLM 调用且后端无关
practical_value: '- **轻量级记忆控制器**：可将 Agent 检索深度、是否注入过往成功策略、何时遗忘陈旧信息的决策，接管为一个表格式上下文
  Bandit，在线学习 Q 表，收敛只需几十个任务，无需额外 LLM 推理，适合电商对话 Agent、智能客服等对延迟和成本敏感的场景。

  - **后端解耦**：记忆控制策略与底层存储（向量库、图记忆、潜 Token 记忆等）分离，现有系统只需暴露检索/存储接口即可无缝装配，便于在推荐商品问答、多轮导购等场景中，渐进式将固定
  retriever 升级为自适应 retriever。

  - **令牌节省机制**：通过抑制无效检索、复用成功计划模板，MEMCON 实现 5–20% 的 token 消耗下降同时提升成功率，对计费严格的 LLM 应用有直接成本收益。

  - **状态设计思路**：在电商推荐 Agent 中，可按“目标商品类别”“步骤阶段”“是否卡壳”“记忆库规模”等构建紧凑状态，配合少量离散动作空间，即可部署类似
  UCB 策略，让 Agent 学会何时更多检索历史对话、何时直接复用成功推荐链路。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现有 LLM Agent 记忆系统（向量检索、图记忆、反思库等）几乎全部用固定超参数（top‑k、跳数、查询模板）访问记忆，无法适应不同任务阶段：初期记忆稀疏，盲目检索反而稀释提示；相同目标类型重复出现时，应直接复用过往成功计划，而非每次做近邻检索；卡壳时需更换查询重新检索；长期任务流中需要合并与遗忘。单一静态启发式无法同时满足这四种需求。虽然 MemGPT 等用 LLM 本身做记忆控制器可达成自适应，但每次记忆操作增加一次 LLM 调用，开销过大。

**方法关键点**  
- **记忆 MDP**：将记忆操作建模为马尔可夫决策过程，状态融合任务进度（目标类型、步骤阶段、是否卡壳、位置等）与记忆状态（库大小、是否有可用计划、学习阶段），离散化为少量哈希键，动作空间包含检索（不同 top‑k / insight‑k / 跳数）、计划注入、重新检索、合并、遗忘、无操作。
- **在线 Contextual Bandit**：用表格 Q‑learning + UCB 探索，无预训练、零额外 LLM 调用。Q 值初始化带有人类可读先验（检索和计划注入正先验，遗忘负先验），每任务结束后用反向折扣 Monte‑Carlo 回报更新整条轨迹上各状态的 Q 值。
- **后端无关包装器**：在任意记忆后端的检索/存储接口上包裹一层控制器，策略输出参数后透传给后端，不修改底层实现即可将此自适应控制赋予任何现有记忆系统。
- **增强操作**：计划注入从成功轨迹中提取泛化模板并注入提示；目标分解处理复合任务。两者均为可选，但主要收益来自学习到的控制器。

**关键结果**  
在 ALFWorld、PDDL、ScienceWorld、TriviaQA、WebWalkerQA、GAIA 六个基准上，结合 Lobster、LangGraph、Microsoft Agent‑Framework 三种 agent 框架，使用 GPT‑4.1‑mini、Claude Sonnet‑4、DeepSeek‑V3.2 三个 LLM 主干，MEMCON 与 9 个记忆基线比较：
- 在 GPT‑4.1‑mini 下，ALFWorld 任务成功率从最好固定回顾基线 59.7% 提升至 67.9%，同时每任务 token 从 45K 降至 39K（‑13%）。
- 在 Sonnet‑4 下，18 个评测单元中 15 个取得最佳，且 token 节省 5–20%。
- DeepSeek‑V3.2 下所有交互决策单元全部最佳。
- 消融实验表明，学习到的 UCB 控制器独自贡献最大（ALFWorld 上 +5.2 百分点），计划注入和目标分解各额外贡献约 1.5 点。

**一句话记忆**  
“不要设计记忆怎么用，让 Agent 在线学会在什么状态下、做哪种记忆操作能带来成功，且这个学习过程不增加任何 LLM 推理成本。”
