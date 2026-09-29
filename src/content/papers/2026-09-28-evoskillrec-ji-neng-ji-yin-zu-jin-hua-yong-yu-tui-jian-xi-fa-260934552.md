---
title: 'EvoSkillRec: Skill-Genome Evolution for Recommender Architecture Discovery'
title_zh: EvoSkillRec：技能基因组进化用于推荐系统架构发现
authors:
- Xiaopeng Li
- Kuo Cai
- Bo Chen
- Wenlin Zhang
- Mengyang Ma
- Yingyi Zhang
- Zichuan Fu
- Yu Yang
- Qidong Liu
- Yiyu Wang
affiliations:
- City University of Hong Kong
- Kuaishou Technology
- Xi'an Jiaotong University
arxiv_id: '2609.34552'
url: https://arxiv.org/abs/2609.34552
pdf_url: https://arxiv.org/pdf/2609.34552
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: 推荐架构自动进化 · Skill 库与 LLM 代码合成
tags:
- recommender systems
- architecture search
- LLM-driven evolution
- skill library
- AutoML
- multi-objective
one_liner: 将推荐模型拆解为可复用技能卡，通过技能空间重组与LLM代码空间发明双空间进化，并沉淀有效创新
practical_value: '- 将现有线上模型拆成结构化 skill card：声明输入输出 key、inductive bias、失败签名、验证 suite
  与历史收益，形成可检索库；新架构组合时靠类型检查和规则匹配过滤不可行候选，避免浪费训练资源。

  - 双空间进化策略：先用低成本 skill 空间做 add/replace/hybridize/specialize 重组，性能平台期再动态增加 code 空间预算，让
  LLM 规划器与合成器发明新模块；验证有效后将其沉淀为 Tier-2 技能，供后续 skill 空间复用，形成持续积累。

  - 生成式排序模型上可联合优化 AUC 与训练 MFU：设置 eligibility 门槛（AUC 损失 ≤1e-3、MFU ≥ 种子模型 95%）选择候选，实验显示同一批进化结构可同时提升精度与硬件利用率，避免两目标对立。

  - LLM backbone 对发现结果影响显著：CTR 任务闭源模型更稳，MTL/MDL 任务开放权重 GLM-5.2 性价比高；可针对业务任务类型预选 backbone，降低
  API 探索成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
推荐系统长期依赖人工设计的架构 inductive bias，AutoML/NAS 搜索空间固定，LLM 开放代码进化虽能突破空间限制，但常生成无效低质修改，且有效创新无法跨代积累。论文提出把架构进化视为可积累知识的过程，而非一次性突变。

**方法关键点**  
- 将已有推荐模型（DeepFM、DIN、MMoE、PLE 等）自动拆解为原子可执行 skill，每个 skill 带类型化输入输出、语义标注、失败签名、验证用例与历史记忆，存为两库：Tier-1 人工 curated，Tier-2 进化过程中自动发现并验证有效的新模块。  
- 双空间搜索：skill 空间在 skill 图上做 add/replace/hybridize/specialize 遗传算子，利用库内已验证知识；code 空间由 LLM planner 生成架构草图、synthesizer 生成可执行模块，仅在 skill 空间难解时加大投入。  
- AutoResearch 循环负责 diagnose 失败模式、检索相关 skill、筛选候选、训练验证、选 survivor，并把 survivor 携带的新 skill 沉淀回 Tier-2，使搜索空间随代数单调扩张。  
- 自适应预算：默认 6:2 偏向 skill 空间，性能平台期自动向 code 空间倾斜。

**关键实验与结果**  
在 CTR（MovieLens、Amazon Books/Beauty）、MTL（Census-Income）、MDL（Amazon/MovieLens）上，EvoSkillRec 测试 AUC 均超过最强手工模型、NASRec 与 OpenEvolve，提升幅度 0.0001–0.0085，虽多数微小但一致。消融显示 skill 空间与 code 空间贡献互补：MDL 任务 skill 空间更强，CTR 任务 code 空间更强。多目标实验在工业级 QK-Video 生成式排序模型上，以 RankMixer 为种子，联合优化 AUC 与 MFU，发现 Pareto 前沿，其中 P1 在测试 AUC 提升 1.7e-4 的同时 MFU 从 1.433% 升至 1.477%。LLM backbone 对比中 GLM-5.2 在 MTL/MDL 表现最佳且成本低，Claude Opus 4.8 在 CTR 最好。实验总 API 成本约 $7,000，且单次进化运行统计分辨率有限。

**最值得记住的一句话**  
推荐架构进化不应只是突变，更应记忆：把验证有效的模块沉淀为可复用 skill，让搜索空间随进化单调扩张。
