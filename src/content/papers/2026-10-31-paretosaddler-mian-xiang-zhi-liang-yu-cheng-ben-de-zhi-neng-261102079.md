---
title: 'ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and
  Cost'
title_zh: ParetoSaddler：面向质量与成本的智能体 Harness 帕累托优化
authors:
- Xingzhi Qian
- Sungho Park
- Rongyuan Tan
- Jianbo Yu
- Jue Zhang
- Lorenzo Cavallaro
- Menglin Xia
- Yanzhi Chen
- Xinnuo Xu
- Yu Kang
affiliations:
- University College London
- Pohang University of Science and Technology
- Southern University of Science and Technology
- Southeast University
- Microsoft
arxiv_id: '2611.02079'
url: https://arxiv.org/abs/2611.02079
pdf_url: https://arxiv.org/pdf/2611.02079
published: '2026-10-31'
collected: '2026-11-04'
category: Agent
direction: Agent 系统调优 · 多目标优化
tags:
- Agent Harness
- Pareto Optimization
- Bayesian Bootstrap
- Quality-Cost Tradeoff
- LLM Agents
one_liner: 分离中间候选提升与最终部署选择，用 Bayesian bootstrap Pareto 支持联合优化 Agent 质量与成本
practical_value: '- 在 Agent/RAG 优化流程里引入 Pareto 支持度而非单目标打分：电商搜索/推荐 Agent 常需同时优化答案质量与
  token/API 成本，中间迭代可先接受任一维度的可信提升，避免高质量但高成本的中间方案被过早丢弃。

  - 用 Bayesian bootstrap 对多次执行结果做显著性过滤：LLM 评估噪声大，只保留跨 run 有稳定增益的 harness 候选，能减少线上实验浪费；可直接用于
  prompt、tool 选择、中间件参数的 A/B 调优。

  - 将候选提升与部署选择解耦，保留 Pareto 前沿而非单一 best：便于业务按实时的成本/质量约束从前沿选配置，例如大促期选低成本兜底、高价值用户选高质量方案。

  - 可迁移到推荐 Agent 的 harness 搜索：固定模型权重，只优化 prompts/tools/control logic，通过重复执行与 Pareto
  提升做低成本多目标迭代。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 agent harness 优化主要只看回答质量，扩展到质量-成本联合优化时，若在中间步骤直接使用部署偏好（如线性加权）会过早淘汰后续可能带来改进的候选。

方法关键点：
- 将“中间候选提升”与“最终部署选择”解耦：中间优化只看候选是否在质量或成本至少一个维度上取得可信进步，最终再从 Pareto 前沿选择。
- 每次迭代以父 harness 生成候选，重复执行多次，用 Bayesian bootstrap 估计 Pareto support，提升在质量或成本上可信进步的候选；提升后的候选获得更完整的开发评估，并可作为父代继续优化。
- 最终部署从 Pareto 前沿按质量/成本偏好选择。

关键结果：
- ClawMark：质量 70.86%→81.35%，成本 $1.17→$1.01/task
- GAIA2：质量 56.22%→62.89%，成本 $0.78→$0.45/task
- Pareto 选择优于仅质量优化：质量更高且成本更低；分析显示保留中间候选可支持后续改进，Bayesian bootstrap 过滤弱证据增益。
