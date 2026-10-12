---
title: 'RSI-Anything: Unlocking Recursive Self-Improvement with World Models'
title_zh: RSI-Anything：用世界模型解锁递归自改进
authors:
- Taoyong Cui
- Pinxian Zeng
- Wanghan Xu
- Hao Xiao
- Shuhan Xue
- Qiang Gao
- Wanli Ouyang
- Pheng Ann Heng
- Zhenfei Yin
- Yingcheng Wu
arxiv_id: '2610.13912'
url: https://arxiv.org/abs/2610.13912
pdf_url: https://arxiv.org/pdf/2610.13912
published: '2026-10-08'
collected: '2026-10-12'
category: Agent
direction: 世界模型驱动的递归自改进
tags:
- Recursive Self-Improvement
- World Models
- JEPA-Anything
- Policy Optimization
- Agent
one_liner: 提出基于预测世界模型的递归自改进框架，在代码、GUI、科学任务中提升成功率并降低交互成本
practical_value: '- 可借鉴其「预测选择 + 条件自适应」思路：在电商 Agent 或推荐流程中用世界模型预筛候选 action / 训练样本，减少对昂贵外部反馈（人工标注、在线实验）的依赖。

  - 将 policy 与 world model 作为配对版本管理，通过 component / compatibility check 决定是否保留更新，能防止
  Agent 多模型链路中的版本漂移，适合多阶段生成式推荐管线。

  - GUI 评估中平均 actions 减少 39.4%，说明世界模型引导能在保持任务完成率的同时降低交互步数，对需要控制 token / 工具调用成本的 Agent
  工作流有直接迁移价值。

  - 小规模但一致的提升模式：代码修复 26.3%→29.2%→31.2%，说明预测选择与模型自适应可叠加，业务上可作为低成本增量优化手段。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：递归自改进（RSI）希望把交互经验转化为持续能力提升，但外部反馈成本很高，且策略演化后世界模型预测容易失效。

**方法关键点**：提出 RSI-Anything，基于 JEPA-Anything 的跨领域预测基础，用世界模型引导动作选择和学习数据筛选；观察反馈驱动 policy 或 workflow 更新，并对世界模型做条件自适应；通过 component check 和 compatibility check 控制是否保留更新后的 policy-model pair。

**关键结果**：在代码修复任务中，coder 固定时，成功率从静态 verifier 的 26.3% 提升到预测选择的 29.2%，再经世界模型自适应达到 31.2%；GUI 任务完成率更高，平均 actions 减少 39.4%；实验室规划经过五个连续策略版本，得分从 21.80% 翻倍至 46.01%；反应优化在相同 40 次实验预算下，平均最佳观测产率达 96.15%，显著高于 Bayesian optimization 的 82.16%；端到端免疫科学应用进一步连接 workflow evolution 与预测建模，支持治疗假设生成。
