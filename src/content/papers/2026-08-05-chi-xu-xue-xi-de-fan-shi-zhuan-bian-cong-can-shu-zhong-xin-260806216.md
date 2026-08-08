---
title: Continual Learning in Transition
title_zh: 持续学习的范式转变：从参数中心到系统级适应
authors:
- Zhiyan Hou
- Dan Zhang
- Tao Feng
- Liyuan Wang
- Wei Li
- Xiangzhao Hao
- Hongyan An
- Junfeng Fang
- Haokai Ma
- Zhaohui Xu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- National University of Singapore
- Tsinghua University
- Shanghai Jiao Tong University
- Alibaba Group
arxiv_id: '2608.06216'
url: https://arxiv.org/abs/2608.06216
pdf_url: https://arxiv.org/pdf/2608.06216
published: '2026-08-05'
collected: '2026-08-08'
category: Training
direction: 持续学习 · 系统级适应框架
tags:
- Continual Learning
- System-level Adaptation
- Survey
- Off-policy
- Inference-time Training
- Memory-augmented
one_liner: 提出三轴框架（何时、如何、何处）刻画持续学习从参数更新到系统级适应的演进
practical_value: '- **系统级在线更新**：推荐模型可将部分能力外置到记忆库或技能库中，新知识通过写入外部存储而非修改模型参数来实现，避免灾难性遗忘，适合高频变化的电商场景（如新品冷启、大促策略调整）。

  - **推理时自适应**：借鉴 test-time training 思想，在推荐服务推理阶段根据当前上下文（如用户实时行为）快速调整模型子集或 prompt，无需完整重训，降低延迟并提升实时性。

  - **多策略混合更新**：结合 off-policy（历史数据回放）与 on-policy（在线交互）更新，利用 LLM 驱动的 Agent 生成合成交互数据，平衡稳定性和探索，适合搜索广告的竞价策略持续优化。

  - **Agent 交互协议**：将推荐系统组件（召回、排序、出价）作为 Agent，通过标准化协议交换记忆和技能，实现不同模块的独立持续进化，提升整体系统的长期适应能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前持续学习研究正从传统的参数中心视角（如正则化、架构调整）转向系统级适应，包括 on-policy 学习、推理时训练、外部记忆和技能库等新范式。然而缺乏统一框架来理解这一转变。

**方法**：论文提出一个三轴分析框架——**何时（When）**：学习发生的阶段（预训练、后训练、推理时）；**如何（How）**：更新机制（off-policy、on-policy 及超越梯度的优化）；**何处（Where）**：更新作用于内部参数还是外部构件。基于该框架系统综述了代表性方法，揭示了持续学习从模型适配到系统进化的整体趋势。

**关键结论**：传统参数隔离和重放方法正被更灵活的系统级机制补充，如记忆增强、技能库、交互协议等。该转变能更好地应对开放环境中的持续变化，但也带来可解释性、安全性和工程复杂度等新挑战。综述为未来持续学习系统设计提供了理论指引。
