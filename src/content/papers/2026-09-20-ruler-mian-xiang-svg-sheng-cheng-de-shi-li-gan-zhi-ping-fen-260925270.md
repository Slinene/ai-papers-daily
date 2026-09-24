---
title: 'RULER: Instance-aware Rubric Rewards for SVG Generation'
title_zh: RULER：面向 SVG 生成的实例感知评分规则奖励
authors:
- Hangyu Ran
- Yuhao Zheng
- Yingying Zhang
- Kevin Qinghong Lin
- Han Peng
affiliations:
- Ant Group
- The Hong Kong University of Science and Technology (Guangzhou)
- Independent Researcher
- University of Oxford
arxiv_id: '2609.25270'
url: https://arxiv.org/abs/2609.25270
pdf_url: https://arxiv.org/pdf/2609.25270
published: '2026-09-20'
collected: '2026-09-24'
category: Training
direction: RL 奖励设计 · SVG 生成
tags:
- SVG Generation
- Rubric Reward
- Reinforcement Learning
- GRPO
- Vision-Language Judge
one_liner: 用实例感知 rubric 奖励替代标量指标，VLM 逐项评分并结合 GRPO，无需真值即大幅提升 SVG 生成质量
practical_value: '- **用多维 rubric 替代标量奖励**：商品文案、广告创意、AI 生成图片等开放式生成任务中，若仍用 CLIP/Aesthetic
  等单一 scalar 作为 reward，容易出现 reward hacking；让 VLM judge 按语义、视觉、风格多轴逐项打分，可提升与人类判断的一致性，并作为
  RL reward。

  - **instance-aware rubric 动态生成**：不依赖固定评估模板，而是针对每条 instruction / 用户场景生成定制评分项；在推荐解释、push
  消息、搜索 query 生成中，可按用户意图或商品属性动态生成评估维度，比全局统一指标更精细。

  - **无真值/无偏好标注的 RL 训练**：RULER 仅从文本生成 rubric，不要求配对 ground truth 或人类偏好标签；对电商场景的生成式推荐/文案任务，可用现有
  VLM 做自动评估器，降低人工标注成本，再结合 GRPO 优化。

  - **先验证 judge 相关性再用于 RL**：在工程上，可先构建 rubric prompt + VLM judge，验证其与少量人工评分的相关性，确认可靠后再接入
  GRPO 训练；避免直接采用不可靠 reward 导致策略退化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：SVG 代码生成是开放任务，缺乏绝对视觉 ground truth；scalar 指标（CLIP、Aesthetic）在风格化矢量内容上迁移差，作为 RL 奖励易 reward hacking。
**方法**：先将多轴 rubric 提示 VLM judge，证实其与人类判断相关性显著优于 scalar 指标。RULER 把每条 instruction 转换为 instance-aware rubric，包含六个打分项，覆盖语义、视觉、风格三轴；judge VLM 对渲染结果逐项打分，加权 satisfaction 形成细粒度奖励，用 GRPO 优化。奖励只依赖文本生成 rubric，不需要配对 SVG 真值或人类偏好标签。
**结果**：在 MMSVG-Illustration 与 MMSVG-Icon 上，rubric score 从 0.432/0.395 提升到 0.693/0.683，超过专用 SVG 专家并匹配更大的 DeepSeek-V3；消融表明 rubric 设计是开放 SVG 生成 RL 的关键杠杆。
