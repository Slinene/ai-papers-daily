---
title: Latent On-Policy Self-Distillation
title_zh: 潜在在线策略自蒸馏
authors:
- Guibin Zhang
- Jiayang Lyu
- Ran Sun
- Xinlei Yu
- Haoyu Zhao
- Qibing Ren
- Shuicheng Yan
affiliations:
- National University of Singapore
- Beijing University of Posts and Telecommunications
- Shanghai Jiao Tong University
arxiv_id: '2608.13040'
url: https://arxiv.org/abs/2608.13040
pdf_url: https://arxiv.org/pdf/2608.13040
published: '2026-08-12'
collected: '2026-08-18'
category: Training
direction: LLM Agent 在线策略自蒸馏训练
tags:
- on-policy distillation
- self-distillation
- latent context
- agent training
- RLVR
one_liner: 让 OPSD 的特权上下文从手工设计变为可学习的潜在表示，联合蒸馏提升 agent 与代码策略，样本效率显著优于 GRPO/Skill-SD
practical_value: '- 在电商导购/客服 Agent 训练中，可将历史成功会话（用户目标+操作序列+结果）检索并压缩成 latent tokens
  条件化 teacher，让学生从自己的 rollout 中稠密学习，避免人工写死“成功策略/提示模板”；线上推理只保留学生，不增加延迟。

  - 使用 on-policy self-distillation 时必须加 privileged-margin 约束，否则 teacher 会退化到 student，联合训练效果反而比冻结
  composer 更差；可用结果奖励（如转化/点击）加权 per-token advantage，margin 建议设在 0.05 左右。

  - latent context 注入生产推理引擎不必改底层 embedding，用 placeholder sentinel + dummy token ids
  即可兼容 vLLM/SGLang；训练后 composer 和检索索引可以完全离线。

  - 在 RLVR 采样预算有限（如每天 1-2k 条 rollout）且需要快速策略迭代的推荐/广告 Agent 场景，latent-teacher 稠密监督比纯
  GRPO 样本效率高很多，可作为内部训练组件复用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：On-policy self-distillation (OPSD) 把经验学习转化为学生自身轨迹上的密集 token 级监督，但现有方法依赖人工指定的特权上下文（答案、反馈、技能、轨迹），信息格式固定，限制了自适应和扩展。核心问题：特权上下文本身能否端到端可学习？

**方法关键点**
- 学生从任务和交互历史 on-policy 采样轨迹；经验库只保存成功轨迹（任务+简化 action-result trace，去掉冗长 observation）。
- 用 dense retriever 检索 top-J（J=3）相关经验，composer 由冻结 backbone + LoRA encoder 和 QFormer compressor 组成，每条经验压缩为 K=32 个连续 latent tokens，共 96 个 token 作为 teacher 的特权上下文。
- Teacher 是冻结 backbone，接收 latent context 后重新评估学生访问过的每个前缀，用 reverse KL 蒸馏 student 和 teacher 的 top-M（M=20）+ tail 分布。
- 引入 privileged-margin 约束：用结果奖励 A(τ)=2r(τ)-1 加权每个 token 的 log-prob 优势，要求 teacher 优势保持 margin m=0.05 以上，双变量 β 动态更新；anchor 项防止 latent context 偏离初始化。冷启动用成功轨迹 NLL 初始化 composer。
- 训练后仅部署学生，推理无需检索器、composer 或 latent context。

**关键实验**：工具使用（EnvScaler、BFCL-v3、ACEBench）与代码生成（LiveCodeBench、HumanEval+、MBPP+），模型覆盖 Qwen3-4B/8B、OLMo3-7B。对比 Vanilla、GRPO、OPSD、SDPO、SDFT、Skill-SD，LOPD 在全部 10 个 backbone-benchmark 聚合中最佳；Qwen3-8B 上 EnvScaler 66.4 vs 最强 baseline 60.2，ACEBench 62.7 vs 58.0；OLMo3-7B 上 LiveCodeBench avg 50.98 vs 48.29。样本效率方面，LOPD 在 320 次 rollout 达到 0.61 mean reward，576 次到 0.637，超过 GRPO/Skill-SD 1600 次最终成绩，只需少于 30% 的 rollout 预算。消融：冻结 composer 0.573，无 margin 0.551，m=0.05 最佳 0.637，证明联合优化和 margin 约束必要。

最值得记住的一句话：经验表示本身应该被端到端优化，而不是设计成固定的人工制品；这样学生策略可以在更少采样下内化更好的行为。
