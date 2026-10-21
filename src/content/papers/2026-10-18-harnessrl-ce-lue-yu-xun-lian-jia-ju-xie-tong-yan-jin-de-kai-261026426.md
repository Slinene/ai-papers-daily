---
title: 'HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended
  RL'
title_zh: HarnessRL：策略与训练夹具协同演进的开放式强化学习
authors:
- Xiaoqiang Wang
- Ting-En Lin
- Yuchuan Wu
- Pinyi Zhang
- Caixin Kang
- Ling Li
- Bingxue Qiu
- Jieping Ye
- Yongbin Li
- Bang Liu
affiliations:
- Alibaba Token Hub, Alibaba Group
- Université de Montréal Mila - Quebec AI Institute
arxiv_id: '2610.26426'
url: https://arxiv.org/abs/2610.26426
pdf_url: https://arxiv.org/pdf/2610.26426
published: '2026-10-18'
collected: '2026-10-21'
category: Training
direction: LLM 后训练 · 自适应奖励与训练接口
tags:
- rubric-based RL
- training harness
- JIT critic
- reward hacking
- GRPO
- open-ended generation
one_liner: 提出 HarnessRL，通过任务采样、rollout 引导与 rubric 标准三接口协同进化，并在冻结策略上实测更新效果，显著减少奖励失效。
practical_value: '- 在基于 LLM judge 的奖励训练中（如商品文案、对话策略、Agent 行为生成），把 rubric 视为可训练配置而非固定标准：按每条标准诊断
  blind/saturated/spurious，饱和任务降采样、达不到的标准注入 few-shot 引导、刷分标准拆分或重写，能直接缓解 reward hacking。

  - 借鉴 JIT critic 机制：所有 reward/rubric/采样权重/引导变更，先冻结当前策略，在小批量上测 reward 变化，仅当变化落在校准接受带内才生效；这比直接应用规则或生成式更新更稳，能显著降低训练后期反复横跳。

  - 建立 training-time memory 和语义检索：把历史 rollout、评分矩阵、rubric 变更按任务和 criterion 存下来，检索跨任务相似标准与正负样本，作为引导
  reference 或标准修改证据；在电商多任务 RL 中可复用，降低人工调 reward 成本。

  - 如果做生成式推荐/Semantic ID 等开放生成，奖励函数退化问题同样会出现；可借鉴该框架让采样分布、生成约束和评判标准与策略协同演化，而不是等到刷分后再修复。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：Rubric-based RL 用自然语言标准做奖励训练开放式生成，但固定 rubric 会随着策略进化而失效。作者识别出三类奖励失败：blind（标准一直达不到）、saturated（所有 rollout 都满足，失去区分度）、spurious（能区分但排序不反映真实质量）。在 Rubric-Mix-10k 上，GRPO 训练中 61.6% 的响应对存在这类问题，其中 34.0% 提供误导性对比信号。原因是任务采样、探索与评估标准在训练中固定不变，需要与策略协同演化。

方法关键点：
- HarnessRL 定义三个训练接口：任务采样 p_t、rollout 引导 g_t、rubric 标准 c_t，形成训练时 harness H_t。
- 维护 training-time memory M_t，记录每次 rollout、rubric 历史与训练动态；通过时间索引和语义索引检索证据，区分持续性失败和单步噪声，并提供跨任务参考样本。
- harness evolver 包含 attributor、proposer、JIT critic：attributor 将每个 criterion 标记为 blind/saturated/spurious/agree 并路由到相应接口；proposer 生成重采样、添加/撤回引导、改写/拆分/合并 rubric 等候选更新；JIT critic 在冻结策略上测量候选更新效果，只有落在接受带内才采纳，否则退回修改或 noop。
- RL 目标扩展 GRPO：按 p_t 采样任务，带引导生成 rollout，按动态 rubric 计算奖励，并用重要性采样修正重加权带来的分布偏移。

关键实验：构建 Rubric-Mix-10k，覆盖医学、科学、写作、角色扮演、指令遵循五个领域，共 8600 个训练任务、每域 250 个 held-out 任务及 OOD benchmark。对比 GRPO、RuscaRL、SkillRL、EvoRubric、AMARIS、AMARIS++。在 Qwen3.5-4B 上，HarnessRL 达到 in-domain 64.5、OOD 49.8，分别比最强基线 AMARIS++ 高 3.0 和 2.8 分；在 Qwen3.5-9B 上，差距为 2.9 和 3.1 分。训练到最佳 checkpoint 所需的步数比 GRPO 减少约一半，reward-oracle agreement 从 38.4% 提升到 48.9%。消融显示 critic 和 memory 是主要增益来源，反转率从 AMARIS++ 的 18.2% 降至 1.6%。

最值得记住的一句话：固定奖励会随策略进化而失效，应把任务采样、探索引导和奖励标准视为可协同进化的训练接口，并且在采纳任何更新前用当前策略实测其效果。
