---
title: 'Causal Memory Policy: Making Memory Utility Identifiable by Intervening on
  Retrieval'
title_zh: 因果记忆策略：通过干预检索使记忆效用可识别
authors:
- Arman Behnam
- Binghui Wang
affiliations:
- Illinois Institute of Technology
arxiv_id: '2610.02070'
url: https://arxiv.org/abs/2610.02070
pdf_url: https://arxiv.org/pdf/2610.02070
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent 记忆管理 · 因果识别
tags:
- Causal Inference
- Memory Augmentation
- LLM Agent
- Retrieval
- Identification
- Inverse Propensity Weighting
one_liner: 提出 CMP，用随机化检索暴露恢复记忆效用的可识别性，解决确定性检索下的 positivity violation
practical_value: '- 在 RAG / 生成式推荐或用户画像记忆系统中，离线估计某个 item 或 memory 的增量价值时，必须警惕召回/检索阶段的
  positivity 问题：未被召回的 item 其效用不可识别，导致基于效用的 eviction 或降权策略退化为随机。可借鉴 CMP：保留固定比例曝光槽位，对候选
  item/memory 以已知 propensity 随机采样，强制产生 support。

  - 采用平衡分配（balanced assignment）替代独立随机：固定每个 item 的曝光次数，propensity 精确已知，方差可解析计算；估计器用
  self-normalized IPW（等价于 arm 均值差），便于工程实现。

  - 对不可逆操作（如删除记忆、商品永久下架、从长期候选池剔除）采用单边弃权（one-sided abstention）：Bayes 最优规则要求只有当估计效用显著低于负阈值时才执行不可逆操作，避免误删高价值
  item。

  - 识别出 utility 不等于能做出 retention 决策：per-query utility 在特定 query 上 AUC 很高，但跨 query
  聚合困难，无法用单个标量代表长期价值。这提示在推荐/搜索中，item 价值随上下文变化，需要 query-conditioned 模型而非全局打分，且保留/淘汰决策需考虑未来查询分布的不确定性。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
Memory-augmented LLM 需要估计每个记忆的效用以决定保留还是遗忘。现有方法依赖日志中已被检索的记忆，但正是因为检索是确定性的，许多记忆从未被放进上下文，其效用无法识别（positivity violation）。这种不可识别与真实低效用不可区分，导致基于效用的策略可能误删重要记忆。

**方法关键点**  
- 将 memory-augmented LLM 建模为 SCM，指出 retrieval 是 mediator：记忆效用分解为检索概率 × 条件效用；当检索概率为零时，效用恒为零，无法识别。
- 提出 CMP：随机化检索暴露设计。预留 k 个 context slot，从候选池中以已知 propensity 采样记忆填入；使用平衡分配保证每个记忆获得固定曝光次数，从而 propensity 精确已知。
- 估计：用 self-normalized inverse propensity weighting（Hájek 估计器），在均衡下退化为曝光组与未曝光组的均值差，方差精确。
- 决策：针对不可逆操作（如 forget）推导 Bayes 最优弃权规则，单边弃权优于双边，避免误删。

**关键实验**  
在 LongMemEval、LoCoMo、Mem0 等数据集上，发现 54%（LongMemEval）和 67%（LoCoMo）的必需记忆从未被检索；store-level randomization 在 52.2% 的干预下不改变 retrieved set，效用估计近似随机（lift 0.97）。CMP 将必需记忆 vs 非必需记忆的判别 AUC 从 0.54 提高到 0.66，gold loss 从 10.9 降至 5.2。per-query 估计 AUC 达到 0.78，但跨 query 聚合困难，无法形成可靠的 retention 策略。

**最值得记住的一句话**  
确定性检索导致未检索记忆的效用不可识别，随机化检索暴露是恢复识别性的关键，但识别出的效用本身不足以指导保留决策。
