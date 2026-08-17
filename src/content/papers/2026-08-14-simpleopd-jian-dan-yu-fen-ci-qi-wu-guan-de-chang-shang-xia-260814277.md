---
title: 'SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context
  Reasoning'
title_zh: SimpleOPD：简单与分词器无关的长上下文推理在线策略蒸馏
authors:
- Haonan He
- Haodi Lei
- Yun Luo
- Haoran Zhang
- Shunkai Zhang
- Yizhuo Li
- Shengji Tang
- Zhilin Wang
- Runzhe Zhan
- Lei Bai
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.14277'
url: https://arxiv.org/abs/2608.14277
pdf_url: https://arxiv.org/pdf/2608.14277
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: On-policy 蒸馏 · 跨 tokenizer 长上下文推理
tags:
- On-Policy Distillation
- Knowledge Distillation
- Cross-Tokenizer
- Long-Context Reasoning
- KL Regularization
- Training Stability
one_liner: 用共享文本空间跨 tokenizer 对齐并加入终止 token 掩码与参考 KL 稳定长上下文推理蒸馏
practical_value: '- **跨模型/跨 tokenizer 蒸馏工程**：业务中想把大推理模型蒸馏到小线上模型，不必做人工 token 映射，直接让
  teacher 用自己的 tokenizer 读 student 生成的文本，只对齐文本 span 完全相同的 token；实验中 lexical overlap
  始终 >90%，大部分监督信号可以保留，适合 Qwen/Llama/GLM/Gemma 等不同家族的在线蒸馏。

  - **长链推理蒸馏的稳定性 trick**：OPD 直接从长上下文老师搬推理能力，学生容易出现长度爆炸、截断、重复；可以照搬两个简单做法：① 掩盖 `</think>`、`<|im_end|>`
  等终止/结构 token 的 advantage，不强制学生模仿老师的终止倾向；② 加 student-reference KL，防止策略偏移。Intern-S2
  和 Qwen3.5-35B 上能有效把截断率降到接近 0。

  - **KL 系数是重要的超参**：师生差距越大，越需要更强的 reference KL；GLM-4.7 消融显示 0.5 不足、1.2 过度，1.0 最均衡。业务上做蒸馏可以优先按模型家族差异设
  0.5/1.0 两档。

  - **训练数据聚焦更利于能力迁移**：仅用 proof-only 数据蒸馏，目标证明能力提升最大；混入通用可验证数学数据反而削弱 ProofBench 迁移。类比到业务：要蒸馏商品知识、query
  改写或策略推理，训练集应保持任务纯净，不要混太多无关任务。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：On-policy distillation（OPD）能从强老师模型高效迁移推理能力，并缓解遗忘、提升泛化，但现有工作主要限定在同一模型家族和相同 vocab。将长上下文推理老师蒸馏到短上下文学生，既面临跨 tokenizer 无法直接对齐 token 分布，也容易出现长度爆炸、截断、训练不稳定。论文以数学证明推理为场景，尝试把 SU-01 的能力迁移到 Qwen3/3.5、Intern-S2、GLM-4.7、Gemma-4 等学生模型。

**方法关键点**：
- 在共享文本空间做 OPD：student 用自己 tokenizer 生成 response 并解码回文本；teacher 用自己 tokenizer 重新编码同一段文本；只有当 teacher token 和 student token 覆盖完全相同文本 span 时才对齐并继承 teacher log-prob，未对齐位置回退 student log-prob。
- 目标是 token-aligned reverse KL 的 PPO clipped loss；无需完整 tokenizer 映射，跨词表也能保留大部分监督信号。
- 两个稳定技巧：① 掩码 `</think>`、`<|im_end|>` 等终止 token 的 advantage，防止 teacher 抑制学生终止；② 加入 student-reference KL，限制学生偏离初始策略，减少长度爆炸和截断。
- 训练数据约 4500 道数学证明题：OPC 63、AoPS 2948、Books 900、Shuzhimi 617；使用 Slime/SGLang，100 rollout iterations，batch 64，每个 prompt 4 条 response，policy 每次 rollout 更新 4 次。

**关键结果**：
- 同家族：Qwen3-4B 在 ProofBench +12.30、AnswerBench +17.00、AIME25 +19.58；Qwen3-30B-A3B 在 ProofBench +22.67。
- 跨家族：Intern-S2-Preview 在 ProofBench 从 21.70 提升到 44.50；用 Gemini-2.5-Pro 做 judge 时从 34.0 提升到 55.2，超过 Gemini-2.5-Pro（52.9）。
- 跨词表模型：Qwen3.5-35B-A3B ProofBench 26.78→42.39；GLM-4.7-Flash 30.8→39.7；Gemma-4-26B-A4B 25.5→34.2，显示 tokenizer 差异越大迁移越有挑战。
- 领域外泛化：只在数学数据上训练，Intern-S2-OPD 在 HiPhO 从 38.6 提升到 41.1，表明能力迁移不限于数学领域。

**最值得记住的一句话**：跨 tokenizer 的 OPD 不必做完整 token 对齐，只在共享文本中匹配同一 span 的 token 并给 teacher 信号，再配合终止 token 掩码与 student-reference KL，就能把长上下文推理稳定地蒸馏给短上下文模型。
