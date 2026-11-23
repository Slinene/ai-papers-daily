---
title: 'Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training'
title_zh: 可组合软提示蒸馏 RL 专家：迈向持续后训练
authors:
- Zhen Zhang
- Changyi Yang
- Xuehai He
- Chengzhi Liu
- Yutong Yin
- Ziyue Liu
- Zhuoran Yin
- Yangmin Li
- Zhihan Liu
- Jisen Li
affiliations:
- University of California, Santa Barbara
- Carnegie Mellon University
- University of California, Santa Cruz
- Northwestern University
- NVIDIA
arxiv_id: '2611.27376'
url: https://arxiv.org/abs/2611.27376
pdf_url: https://arxiv.org/pdf/2611.27376
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: LLM 持续后训练 · soft prompt 蒸馏
tags:
- soft prompt distillation
- RL post-training
- continual learning
- multi-expert composition
- parameter-efficient adaptation
one_liner: 冻结基座并独立蒸馏各 RL 专家为 soft prompt，拼接即可组合，无需联合训练
practical_value: '- 在电商/广告多领域大模型后训练中，可把每个业务域 RL 专家独立蒸馏为 soft prompt，新增或下线业务域时只增删 prompt，保持基座冻结，降低持续训练成本与跨域遗忘风险。

  - 多专家组合直接拼接 prompt、不做联合训练即可保留单域能力，适合快速叠加多业务能力进行 A/B 测试，避免每次全量模型重新合并的工程负担。

  - 服务侧用 input-space soft prompt 注入能力，吞吐比 rank-4 LoRA 高约 2.4 倍，且相对无适配骨干开销不超过 1.5%，适合高
  QPS 推荐/广告推理场景；可将关键能力模块化为 prompt，而非重参数化层。

  - 论文侧重通用 LLM 数学/代码/Agent 任务，对推荐模型直接指标提升有限；但“冻结骨干 + 可组合提示”是模块化多任务部署的可行架构，可迁移到多场景生成式推荐或
  Agent 能力管理。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RL post-training 常产出多个领域专家，需要合并到一个模型中；新专家持续出现时，权值合并和 multi-teacher on-policy distillation (MOPD) 必须重新整合整个模型，还可能侵蚀目标域之外的能力。

**方法**：CSPD 保持 pre-RL 基座模型冻结，将每个 RL 专家独立蒸馏为一个 soft prompt；组合多个专家时只需拼接对应 prompts，无需联合训练，支持动态增删专家 prompt。

**结果**：在 23 个数学、代码和 Agent 设置中，单个 soft prompt 在 22 个设置上至少恢复 90% 的教师增益；独立训练的 prompt 可以很好地组合。多专家设置下，平均分随专家增加而提升，完整组合在域内 4 任务上达到 67.83，与 MOPD 的 67.79 相当；在 6 个 held-out 基准上泛化最好，平均 56.6 vs MOPD 53.5。服务端输入空间适配几乎不增加开销，吞吐比 rank-4 LoRA 高 2.40 倍，相对无适配骨干下降不超过 1.5%。
