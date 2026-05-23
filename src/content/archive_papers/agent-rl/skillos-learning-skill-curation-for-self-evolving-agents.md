---
title: 'SkillOS: Learning Skill Curation for Self-Evolving Agents'
authors: Siru Ouyang, Jun Yan, Yanfei Chen, Rujun Han, Chen-Yu Lee 等 (15 人)
affiliation: UIUC × Google Cloud AI Research × MIT
date: 2026-05
venue: arXiv
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: >-
  首篇把 "skill curation 本身" 升级为 RL 训练目标的 agent self-evolution 框架。冻结 executor + 训 8B
  skill curator，curator 通过 insert / update / delete 三个函数调用维护一个 Anthropic SKILL.md 风格的外部
  SkillRepo；用 grouped task streams 把延迟稀疏的下游 task outcome 转成密集监督，叠上 composite reward
  (task / function-call validity / content quality / compression) 进一步加密学习信号。ALFWorld /
  WebShop / 推理任务上稳超 ReasoningBank / MemP，且 8B 训练出的 curator 比直接拿 Gemini-2.5-Pro 当 curator 还强。
paperUrl: https://arxiv.org/abs/2605.06614
tags:
- Skill Curation
- GRPO
- Self-Evolving Agent
- Procedural Memory
- Composite Reward
unverified: false
detail:
  contribution: >-
    把 "skill curation policy 本身" 升级为 RL 训练目标，是 agent self-evolution 路线上第一篇专门优化
    curator（而非 executor 或 skill-using policy）的工作。三个具体贡献：① 模块化双 agent 范式 — 冻结
    executor + 训练 curator，curator 通过 insert / update / delete 三种函数调用维护外部 markdown
    SkillRepo，类似 OS 的 file I/O；② 训练数据按 skill 依赖分组 (grouped task streams)，让早期任务的
    curation 决策被同组后续任务的 executor 表现反向打分，把稀疏延迟信号转成密集监督；③ composite reward
    — 把 task outcome、函数调用合法性、外部 judge 评的 skill quality、SkillRepo 压缩率四项加权融合
    (λ_f=1.0 / λ_u=0.1 / λ_c=0.05)，稳定了 long-horizon curation 的训练动态。
  background: >-
    LLM agent 越来越多被部署在 streaming 任务流场景，但目前还是 "one-off problem solver"，不会从过去任务沉淀经验。把经验沉淀成
    reusable skills（Anthropic 风格的 SKILL.md）已被业界视为 agent self-evolution 的天然载体，**skill
    curation 才是真正瓶颈** — 以前要么靠人工写（Anthropic skills repo），要么用 prompt 启发式规则做 insert
    / delete（无下游反馈），要么做短时窗 skill adaptation（学不到 update / delete 这类 long-horizon
    决策）。本质问题：curation 决策的反馈是延迟、间接、稀疏的 — 只有当未来某个相关任务被 executor 解出来，才知道之前那次
    update 是否有用。
  method: >-
    多 agent 模块化 + RL 训练。**架构**：① **Agent Executor π_L** (冻结)：BM25 从 SkillRepo S_t
    检索相关 skill 子集，按 ReAct 流程在环境里执行任务，输出 trajectory ξ_t；② **Skill Curator π_S** (要训的)：接收
    trajectory、self-judged correctness、检索到的 skill 子集，输出结构化操作序列 c_t = (u_1, ..., u_M)，每个
    u 是 insert_skill / update_skill / delete_skill 之一，以函数调用形式执行；③ **SkillRepo**：外部
    markdown 文件集合，每个 skill = YAML frontmatter（name + 何时用）+ markdown body（工作流 / 约束 /
    启发式）。**RL 训练**：① **Grouped Task Streams** — 用 Gemini-2.5-Pro 给每个任务打 skill-relevant
    attribute tag（如 "algebra" / "Fourier transformation"），按属性相似度把数据集切成若干 group；同
    group 内任务按顺序处理，早期 trajectory 更新 SkillRepo、后期相关任务 evaluate 该 SkillRepo（首任务必从空
    repo 起步，task outcome reward = 后续 |G|-1 个任务的平均 success）。② **Composite Reward**：r
    = r_task + λ_f·r_fc + λ_u·r_cnt + λ_c·r_comp；其中 r_fc = 合法函数调用占比、r_cnt = Qwen3-32B
    judge 给的内容质量分、r_comp = 1 - |S_i| / |χ_i|（鼓励 repo 比 curator 上下文更紧凑、防 verbatim
    复刻 trajectory）。③ **优化器** GRPO（丢掉 KL 项鼓励探索），每个 group 采 N 个独立 rollout，组内相对
    advantage A_n = r_n - mean(r)。基模型 Qwen3-8B，lr=1e-6 / batch=32 / group size=8，16×H100
    训 2.5-5 天（ALFWorld 3 天 / 推理 2.5 天 / WebShop 5 天）。
  experiments: >-
    任务：ALFWorld（6 子集 140 题）/ WebShop / 推理三套（AIME24 / AIME25 / GPQA-Diamond）+ 训练集
    DeepMath-103k 抽 33k。三种 executor scale（Qwen3-8B / Qwen3-32B / Gemini-2.5-Pro），对比 No
    Memory、ReasoningBank、MemP、SkillOS-base（未训 curator）、SkillOS-gemini（直接拿 Gemini-2.5-Pro
    当 curator）。**ALFWorld** Qwen3-8B executor 平均 SR：47.9 → 55.7 (ReasoningBank) → **61.2
    (SkillOS, +5.5)**；Qwen3-32B 54.5 → 61.4 → **68.6**；Gemini-2.5-Pro 66.4 → 74.3 → **80.2**，平均步数从
    21 步降到 14-18 步。**WebShop** Gemini-2.5-Pro executor Score 48.6 → 51.3 → **56.0**。**推理**
    Gemini-2.5-Pro executor 平均准确率 81.8 → 83.5 → **88.6**。**关键观察**：① 8B trained curator
    > Gemini-2.5-Pro untrained curator（curator 不是 raw scale 越大越好，executor-grounded 训练更重要）；②
    curator 跨 executor 泛化（在 Qwen3-8B 上训，配 Gemini-2.5-Pro 仍涨）；③ agentic 收益 >> 单轮推理（程序化经验比抽象
    reasoning skill 更容易复用）；④ 推理上训的 curator 反过来用到 agentic 也涨，但反过来不成立（reasoning
    蒸出来的是更抽象的 decomposition / verification heuristic，更通用）。**消融 (Table 3)**：去 content-quality
    reward SR 61.2 掉到 58.6、去 compression reward 掉到 60.0、去 grouping 掉到 57.3（最大降幅，证
    grouping 是核心）。**curator 行为演化**：训练初期 insert 占 ~95%，到末期 update 上升到 50%+、delete
    缓增；skill 内容从一开始堆 "# Tips" / "# Optimization" 装饰段，到后期出现 "# Failure Handling" /
    "# Conditional Branches" 可执行段，全局上从 task-specific skill 主导演化到 verification / fallback
    / systematic search 这类 meta-strategy skill 占 30%+。
  pros: >-
    ① 把 "skill curation as RL objective" 从概念落地为可训练 + 可复现的完整 recipe（GRPO + 四项 composite
    reward + grouped task），方法论扎实；② 模块化解耦 executor / curator，可 plug-in 任何 frozen executor，工业适配性强（不动主模型权重）；③
    实验覆盖 3 种 executor scale × 3 类任务，generalization 验证完整；④ 8B curator 超 Gemini-2.5-Pro
    这点很有市场 — 说明小 curator 也能做出大效果，部署成本可控；⑤ skill 采 Anthropic SKILL.md 格式，跟 Claude
    Code skill 生态可互通；⑥ ablation 干净证明 grouping > 任何单项 reward 的贡献。
  cons: >-
    ① executor 完全冻结，curator 学到的 skill 终究受 executor 上限约束，不能解 executor 本来就做不了的题；②
    SkillRepo 用 BM25 检索 + markdown 文件，未来真有几千 skill 时检索 / 管理代价没讨论；③ task grouping
    依赖 Gemini-2.5-Pro 离线打 tag，数据预处理成本高、tag 质量本身没消融；④ 三个函数调用 insert / update
    / delete 是固定动作空间，没讨论更复杂操作（合并 / 拆分 / 引用 / 版本控制）；⑤ 绝对增益（如 ALFWorld +5.5）虽稳但不算
    dramatic，且对比的 ReasoningBank / MemP 都是相对早期 baseline，与更新的 long-context memory 方法没直接比；⑥
    截至 v1 没开源代码 / 训练数据，社区复现门槛较高。
  inspiration: >-
    ① "curator vs. executor 解耦 + 只训 curator" 是把 RL 用到 skill 管理上的最干净路径，比同时优化两个
    policy 更稳，可推广到任何 "agent + 外部 knowledge base" 系统（RAG knowledge 维护 / tool 库维护 /
    agent memory 维护）；② grouped task streams 本质是 "把延迟稀疏 reward 转成密集 reward" 的数据组织法，跟
    GRPO 组内相对优势天然契合，可借鉴到任何 long-horizon optimization；③ composite reward 里 "content
    quality (judge 打) + compression (token 比) + function call validity" 三项叠 task reward
    的设计，是个能 cap 住 reward hacking 的实用配方；④ 8B trained curator > Gemini-2.5-Pro 对工业落地极有意义：**meta-policy
    训练价值 > 推理能力 raw scale**；⑤ 用 markdown SKILL.md 沉淀 procedural memory 已是 Anthropic
    / Claude Code / 这篇 三方共识，可能正在成为 agent skill 的事实标准格式。
  takeaway: >-
    Agent self-evolution 路线上把 "skill curation 升级为 RL 训练目标" 的代表作；冻结 executor + 训
    8B curator + grouped task + composite reward 的配方，是当下 modular agent system 训练最干净的
    recipe。
---

首篇把 "skill curation 本身" 升级为 RL 训练目标的 agent self-evolution 框架。冻结 executor + 训 8B skill curator，curator 通过 insert / update / delete 三个函数调用维护一个 Anthropic SKILL.md 风格的外部 SkillRepo；用 grouped task streams 把延迟稀疏的下游 task outcome 转成密集监督，叠上 composite reward (task / function-call validity / content quality / compression) 进一步加密学习信号。ALFWorld / WebShop / 推理任务上稳超 ReasoningBank / MemP，且 8B 训练出的 curator 比直接拿 Gemini-2.5-Pro 当 curator 还强。

## 核心贡献

把 "skill curation policy 本身" 升级为 RL 训练目标，是 agent self-evolution 路线上第一篇专门优化 curator（而非 executor 或 skill-using policy）的工作。三个具体贡献：① 模块化双 agent 范式 — 冻结 executor + 训练 curator，curator 通过 insert / update / delete 三种函数调用维护外部 markdown SkillRepo，类似 OS 的 file I/O；② 训练数据按 skill 依赖分组 (grouped task streams)，让早期任务的 curation 决策被同组后续任务的 executor 表现反向打分，把稀疏延迟信号转成密集监督；③ composite reward — 把 task outcome、函数调用合法性、外部 judge 评的 skill quality、SkillRepo 压缩率四项加权融合 (λ_f=1.0 / λ_u=0.1 / λ_c=0.05)，稳定了 long-horizon curation 的训练动态。

## 背景

LLM agent 越来越多被部署在 streaming 任务流场景，但目前还是 "one-off problem solver"，不会从过去任务沉淀经验。把经验沉淀成 reusable skills（Anthropic 风格的 SKILL.md）已被业界视为 agent self-evolution 的天然载体，**skill curation 才是真正瓶颈** — 以前要么靠人工写（Anthropic skills repo），要么用 prompt 启发式规则做 insert / delete（无下游反馈），要么做短时窗 skill adaptation（学不到 update / delete 这类 long-horizon 决策）。本质问题：curation 决策的反馈是延迟、间接、稀疏的 — 只有当未来某个相关任务被 executor 解出来，才知道之前那次 update 是否有用。

## 方法

多 agent 模块化 + RL 训练。**架构**：① **Agent Executor π_L** (冻结)：BM25 从 SkillRepo S_t 检索相关 skill 子集，按 ReAct 流程在环境里执行任务，输出 trajectory ξ_t；② **Skill Curator π_S** (要训的)：接收 trajectory、self-judged correctness、检索到的 skill 子集，输出结构化操作序列 c_t = (u_1, ..., u_M)，每个 u 是 insert_skill / update_skill / delete_skill 之一，以函数调用形式执行；③ **SkillRepo**：外部 markdown 文件集合，每个 skill = YAML frontmatter（name + 何时用）+ markdown body（工作流 / 约束 / 启发式）。**RL 训练**：① **Grouped Task Streams** — 用 Gemini-2.5-Pro 给每个任务打 skill-relevant attribute tag（如 "algebra" / "Fourier transformation"），按属性相似度把数据集切成若干 group；同 group 内任务按顺序处理，早期 trajectory 更新 SkillRepo、后期相关任务 evaluate 该 SkillRepo（首任务必从空 repo 起步，task outcome reward = 后续 |G|-1 个任务的平均 success）。② **Composite Reward**：r = r_task + λ_f·r_fc + λ_u·r_cnt + λ_c·r_comp；其中 r_fc = 合法函数调用占比、r_cnt = Qwen3-32B judge 给的内容质量分、r_comp = 1 - |S_i| / |χ_i|（鼓励 repo 比 curator 上下文更紧凑、防 verbatim 复刻 trajectory）。③ **优化器** GRPO（丢掉 KL 项鼓励探索），每个 group 采 N 个独立 rollout，组内相对 advantage A_n = r_n - mean(r)。基模型 Qwen3-8B，lr=1e-6 / batch=32 / group size=8，16×H100 训 2.5-5 天（ALFWorld 3 天 / 推理 2.5 天 / WebShop 5 天）。

## 实验结果

任务：ALFWorld（6 子集 140 题）/ WebShop / 推理三套（AIME24 / AIME25 / GPQA-Diamond）+ 训练集 DeepMath-103k 抽 33k。三种 executor scale（Qwen3-8B / Qwen3-32B / Gemini-2.5-Pro），对比 No Memory、ReasoningBank、MemP、SkillOS-base（未训 curator）、SkillOS-gemini（直接拿 Gemini-2.5-Pro 当 curator）。**ALFWorld** Qwen3-8B executor 平均 SR：47.9 → 55.7 (ReasoningBank) → **61.2 (SkillOS, +5.5)**；Qwen3-32B 54.5 → 61.4 → **68.6**；Gemini-2.5-Pro 66.4 → 74.3 → **80.2**，平均步数从 21 步降到 14-18 步。**WebShop** Gemini-2.5-Pro executor Score 48.6 → 51.3 → **56.0**。**推理** Gemini-2.5-Pro executor 平均准确率 81.8 → 83.5 → **88.6**。**关键观察**：① 8B trained curator > Gemini-2.5-Pro untrained curator（curator 不是 raw scale 越大越好，executor-grounded 训练更重要）；② curator 跨 executor 泛化（在 Qwen3-8B 上训，配 Gemini-2.5-Pro 仍涨）；③ agentic 收益 >> 单轮推理（程序化经验比抽象 reasoning skill 更容易复用）；④ 推理上训的 curator 反过来用到 agentic 也涨，但反过来不成立（reasoning 蒸出来的是更抽象的 decomposition / verification heuristic，更通用）。**消融 (Table 3)**：去 content-quality reward SR 61.2 掉到 58.6、去 compression reward 掉到 60.0、去 grouping 掉到 57.3（最大降幅，证 grouping 是核心）。**curator 行为演化**：训练初期 insert 占 ~95%，到末期 update 上升到 50%+、delete 缓增；skill 内容从一开始堆 "# Tips" / "# Optimization" 装饰段，到后期出现 "# Failure Handling" / "# Conditional Branches" 可执行段，全局上从 task-specific skill 主导演化到 verification / fallback / systematic search 这类 meta-strategy skill 占 30%+。

## 优点

① 把 "skill curation as RL objective" 从概念落地为可训练 + 可复现的完整 recipe（GRPO + 四项 composite reward + grouped task），方法论扎实；② 模块化解耦 executor / curator，可 plug-in 任何 frozen executor，工业适配性强（不动主模型权重）；③ 实验覆盖 3 种 executor scale × 3 类任务，generalization 验证完整；④ 8B curator 超 Gemini-2.5-Pro 这点很有市场 — 说明小 curator 也能做出大效果，部署成本可控；⑤ skill 采 Anthropic SKILL.md 格式，跟 Claude Code skill 生态可互通；⑥ ablation 干净证明 grouping > 任何单项 reward 的贡献。

## 局限

① executor 完全冻结，curator 学到的 skill 终究受 executor 上限约束，不能解 executor 本来就做不了的题；② SkillRepo 用 BM25 检索 + markdown 文件，未来真有几千 skill 时检索 / 管理代价没讨论；③ task grouping 依赖 Gemini-2.5-Pro 离线打 tag，数据预处理成本高、tag 质量本身没消融；④ 三个函数调用 insert / update / delete 是固定动作空间，没讨论更复杂操作（合并 / 拆分 / 引用 / 版本控制）；⑤ 绝对增益（如 ALFWorld +5.5）虽稳但不算 dramatic，且对比的 ReasoningBank / MemP 都是相对早期 baseline，与更新的 long-context memory 方法没直接比；⑥ 截至 v1 没开源代码 / 训练数据，社区复现门槛较高。

## 对后续工作的启发

① "curator vs. executor 解耦 + 只训 curator" 是把 RL 用到 skill 管理上的最干净路径，比同时优化两个 policy 更稳，可推广到任何 "agent + 外部 knowledge base" 系统（RAG knowledge 维护 / tool 库维护 / agent memory 维护）；② grouped task streams 本质是 "把延迟稀疏 reward 转成密集 reward" 的数据组织法，跟 GRPO 组内相对优势天然契合，可借鉴到任何 long-horizon optimization；③ composite reward 里 "content quality (judge 打) + compression (token 比) + function call validity" 三项叠 task reward 的设计，是个能 cap 住 reward hacking 的实用配方；④ 8B trained curator > Gemini-2.5-Pro 对工业落地极有意义：**meta-policy 训练价值 > 推理能力 raw scale**；⑤ 用 markdown SKILL.md 沉淀 procedural memory 已是 Anthropic / Claude Code / 这篇 三方共识，可能正在成为 agent skill 的事实标准格式。

## 一句话总结

Agent self-evolution 路线上把 "skill curation 升级为 RL 训练目标" 的代表作；冻结 executor + 训 8B curator + grouped task + composite reward 的配方，是当下 modular agent system 训练最干净的 recipe。
