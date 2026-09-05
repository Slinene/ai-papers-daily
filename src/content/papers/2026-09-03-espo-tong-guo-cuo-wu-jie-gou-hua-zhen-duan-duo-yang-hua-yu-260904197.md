---
title: 'ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize'
title_zh: ESPO：通过错误结构化诊断、多样化与稳定化优化提示
authors:
- Lihao Liu
- Peng Tang
- Kunwar Yashraj Singh
- Shabnam Ghadar
affiliations:
- AWS Agentic AI
arxiv_id: '2609.04197'
url: https://arxiv.org/abs/2609.04197
pdf_url: https://arxiv.org/pdf/2609.04197
published: '2026-09-03'
collected: '2026-09-05'
category: LLM
direction: 自动提示优化 · 错误结构化搜索
tags:
- prompt optimization
- error clustering
- bootstrap stability
- prompt bloat
- evolutionary search
- LLM
one_liner: 将提示优化分解为诊断错误模式、多样化候选、自举稳定性选择，平均准确率超 GEPA 3.76pp且提示缩短47%
practical_value: '- 避免 prompt bloat：在自动迭代优化 prompt 时引入长度惩罚或硬约束，防止规则不断追加导致线上推理变慢、成本升高；短
  prompt 在电商文案/推荐理由生成等高频场景可显著节省 token。

  - 利用错误聚类替代逐轮反思：先对 bad case 做结构化聚类（如意图混淆、属性抽取错误、价格理解等），再针对每个 cluster 生成候选修复策略，比每轮追加零散规则更高效，适合推荐系统
  query 改写和 Agent 指令调优。

  - 候选生成需要互补策略与 bootstrap stability selection 结合：不要只追求多样性；用 bootstrap 重采样评估稳定性来筛选候选，可防止过拟合训练集，在
  AB 测试中挑选更鲁棒的 prompt/策略。

  - 跨模型迁移验证：ESPO 的优化结果在不同学生模型上均保持最佳平均准确率，说明在电商多模型路由或模型升级时，针对弱模型的 prompt 优化可以更稳定地迁移。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：进化式提示优化（如 GEPA）存在 prompt bloat：每次迭代追加规则与告诫，提示长度最多增至 3 倍但准确率没有提升。归因于三个缺陷——不完整的错误观察、有限的搜索多样性、不可靠的选择。

方法关键点：ESPO 分解为三阶段。Diagnose 一次性将全部训练错误聚类为结构化模式；Propose 通过四种互补策略生成候选，各策略带有独立偏差；Select 应用 bootstrap stability selection 筛选稳定提示。

结果：在七个公开 NLP 基准（Tweet、MMLU、GSM8K、HotpotQA、ScoNe、HoVer、PUPA）上，平均准确率 74.67%，比 GEPA 的 70.91% 高 +3.76 pp，每个数据集都匹配或超过 GEPA，同时提示平均长度短 47%（1,004 vs 1,878 字符），推理更快。跨模型实验在 Gemma 3 12B、Mistral 14B、Qwen3 32B、Claude Haiku 4.5 上均取得最佳平均准确率，最大差距为 Qwen3 GSM8K 从 15.00% 提升至 91.40%。消融证实：只增加多样性而缺少 bootstrap selection 反而损害性能（-1.20%）。
