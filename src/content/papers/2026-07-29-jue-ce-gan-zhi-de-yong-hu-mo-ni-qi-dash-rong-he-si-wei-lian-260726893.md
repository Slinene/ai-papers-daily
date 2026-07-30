---
title: 'Beyond Action Imitation: Learning a Decision-Aware User Simulator for Online
  Advertising'
title_zh: 决策感知的用户模拟器DASH：融合思维链与跨域历史的广告行为仿真
authors:
- Zipeng Chen
- Jiaer Zheng
- Xiangyang Xu
- Xinyu Lin
- Zhaobin Wang
- Zhaohui Liu
- Qianjin Xiang
- Xiaoyu Zhao
- Zhuozhen Yu
- Guangshuo Wang
affiliations:
- Tencent Inc.
- National University of Singapore
arxiv_id: '2607.26893'
url: https://arxiv.org/abs/2607.26893
pdf_url: https://arxiv.org/pdf/2607.26893
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 决策感知的用户模拟器
tags:
- User Simulator
- LLM
- Online Advertising
- RL
- Thinking Traces
- Cross-domain History
one_liner: 提出DASH，通过异构上下文折叠和思维轨迹联合建模，提升广告用户仿真的动作准确性及诊断价值
practical_value: '- **异构行为压缩**：针对不同动作类型（跳过/点击/转化/负反馈）采用差异化压缩策略，保留全量高信息交互字段，低信息交互仅留类目元数据。电商/广告场景可通过类似分层压缩处理超长用户历史，在有限context下保留关键信号。

  - **思维链生成与评估**：让模拟器输出“Focus-Draft-Verify-Finalize”结构化思考链，带来可诊断性。可将此范式用于Agent策略验证或推荐解释，通过rubric奖励模型对思考质量的三个维度（形式/内容/逻辑）进行细粒度打分，替代稀疏的动作奖励。

  - **SFT-RL训练框架**：利用强模型蒸馏思维轨迹做SFT，再用分组优势策略优化（GRPO）结合混合奖励（动作正确+思考质量）微调小模型。这种teacher-student方案可在保证仿真精度的同时满足在线低延迟要求，适合业务部署。

  - **提示闭环优化**：通过模拟器错误案例自动分析并迭代优化prompt，使模型输出的动作分布更接近真实分布。该思路可直接用于Agent交互式任务的提示工程，减少人工调试成本。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有用户仿真器多基于单域行为序列且仅预测动作（如点击），忽略了用户决策过程中的内在思维线索，导致仿真保真度不足且缺乏诊断价值。广告场景中，用户行为通常跨多个内容域，且海量历史存在大量噪声与超长依赖，直接输入大语言模型（LLM）会超出上下文预算。为此，DASH 提出同时建模用户的思考轨迹与行为动作，并引入跨域异构上下文折叠与思维质量监督，以提升仿真可靠性。

## 方法关键点
- **上下文工程（CE）**：设计分层压缩策略：**项级**根据动作类型（跳过仅保留类目；点击/转化/负反馈保留全属性）提取关键信号；**流级**按信息量分配 token 配额（广告流优先高信息交互，内容流只保留近期行为），确保总上下文 ≤32K。同时采用结构化提示（Focus / Draft / Verify / Finalize）并通过闭环提示优化器不断修正错误案例。
- **监督微调（SFT）**：利用强模型（教师）生成思考轨迹，对教师预测与真实动作一致的样本直接保留为“easy sample”，否则在注入真实动作后重新生成思考轨迹作为“hard sample”，再通过评判LLM依据rubric筛选高质量轨迹用于学生模型训练。
- **强化学习（RL）**：设计混合奖励：动作奖励（预测与真实匹配则1） + 细粒度思考质量奖励（形式、内容、逻辑三个维度，每个维度由多个子rubric加权求和）。采用GRPO算法，通过组内优势归一化和KL正则化，结合SFT初始化和混合奖励，进一步提升动作预测与思考质量。

## 关键结果
基于腾讯跨域广告真实数据（含5类内容域）的测试结果显示：
- DASH（Qwen3.5-35B骨干，小型SFT + RL）在动作预测上达到加权F1 62.15%，大幅领先原始模型（55.18%）及多种大型LLM（最强者Kimik2.5仅56.47%）。
- 消融实验表明上下文工程贡献最大（移除后W-F1降至51.93%），RL与混合奖励带来显著提升（仅SFT的W-F1为59.07%）。
- 思维质量评估与人类评分高度一致（LLM评估各维度与人类偏差 ≤3分），验证rubric奖励的有效性。
- 案例分析证实思维轨迹能提供明确的可解释错误诊断（如用户过去负反馈未在思考中体现），为广告策略优化提供线索。

> 核心启示：**将可观测动作与不可观测思考轨迹联合建模，并通过跨域信息压缩与分层次质量奖励进行训练，是构建高保真、可诊断用户仿真的关键范式。**
