---
title: 'Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms'
title_zh: RLVR 多域能力融合范式深度对比
authors:
- Siye Wu
- Kai Yang
- Yuchen Cai
- Xin Xu
- Peng-Yuan Wang
- Jiaxuan Wang
- Jiashun Liu
- Jiafei Lyu
- Yangkun Chen
- Saiyong Yang
affiliations:
- Fudan University
- Tencent
arxiv_id: '2608.27409'
url: https://arxiv.org/abs/2608.27409
pdf_url: https://arxiv.org/pdf/2608.27409
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: RLVR 多域融合范式对比
tags:
- RLVR
- Model Merging
- Multi-domain
- On-policy Distillation
- Task Vector
- LoRA
one_liner: 系统对比 Merge、Mix RL、MOPD，发现跨域关系决定性能，融合仅重排已有解不扩覆盖
practical_value: '- 多能力 LLM 后训练融合选型：如果线上已有 query 改写、商品文案、Agent 工具调用等分别 RLVR 产出的 LoRA/全参
  expert，优先试 Merge/Task Arithmetic，融合成本几乎为 0；但下单前先算 task-vector cosine，IF/Agent 类能力通常与其他域近乎正交，merge
  后会掉点，需单独评估或提高权重。

  - 如果没有现成 expert 且要训练统一模型，用 Mix RL 成本约为单域 RL 的 0.58-0.67x；数据混合比例不能简单按自然数据量，推理型任务（数学/代码/科学）可以互相增强并适度降低配比，指令遵循/Agent
  类缺少正向迁移，必须保证足够的采样占比，否则对应 benchmark 会明显塌陷。

  - MOPD 适合已有 domain experts 且要求各域精度不掉、可以接受端到端成本更高的场景；它的收敛快但被 teacher 上限约束，不适合期望超越单专家的场景。

  - 融合只提升 pass@1、不扩大解覆盖，对搜索/推荐里首屏 top-1 质量优化有效；若目标是长尾多样性或生成式 item ID 覆盖，需要额外做采样、多样性约束，而不是靠单模型融合。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：RLVR 在单一能力上有效，但要覆盖数学、代码、科学、指令遵循、Agent 等多能力，通常需要每域训练一个 expert 并单独部署；Merge、Mix RL、多教师 on-policy distillation（MOPD）三种融合范式过去分别研究，缺少同框架对比和选型依据。

**方法关键点**：
- 统一按可复用产物划分：Merge 只组合专家任务向量 τ_i=θ_i−θ_0（Task Arithmetic，λ=0.6）；Mix RL 丢弃专家、只用各域数据集 D_i 做一次联合 GRPO；MOPD 同时用专家和混合数据，在 student 自采样轨迹上按域匹配 teacher log-prob，目标为逐 token reverse KL。
- 5 个域：Math 38,131、Science 50,000、Code 19,169、Instruction Following 16,575、Agent 10,229；混合比例 25/22/22/19/12，共 87,699 条。
- 骨干 Qwen3-4B-Instruct-2507 与 Qwen3-8B，专家同时有 full-parameter 和 LoRA（rank=32）。评估用 AIME25/26、GPQA、LiveCodeBench v5/v6、IFEval、IFBench、BFCL v3，mean@16。

**关键结果**：
- 三范式平均分差距≤1.4 点，但单项最大 8.6 点：4B 上 Merge 63.7 / Mix RL 62.3 / MOPD 63.3（Per-domain RL 63.9，Base 57.0）；8B 上 Mix RL 54.6 / Merge 53.7 / MOPD 53.2（Base 42.0，Per-domain RL 53.8）。
- 跨域关系主导差异：math/science/code 相互正向迁移，IF 与 Agent 几乎正交且 IF→Agent 有负迁移（4B BFCL 掉 9.8 点）；task-vector cosine 同样显示 math-science 0.0217/0.0507，IF/Agent 对多数 <0.0023。Mix RL 在 8B AIME 超过数学专家 6.5/7.3 点，但 IFBench 掉 4.9-9.2 点；MOPD 永远不超过 teacher。
- pass@k 显示三种融合只提升 pass@1，到 pass@32 与 base 无显著差异；SimpleQA-Verified 和 AA-LCR 两个 held-out 能力没有退化。
- 成本：Merge 几乎 0 GPU-h；Mix RL 为单域 RL 的 0.58x/0.67x；MOPD fusion 阶段<0.2x，但端到端 1.14x/1.19x。

**最值得记住**：融合不扩展解空间，只是在 base model 已能生成的解上重新分配概率；选择 Merge/Mix RL/MOPD，取决于跨域迁移结构、是否已有专家、以及可接受的端到端成本。
