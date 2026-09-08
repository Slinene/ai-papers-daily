---
title: 'WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation
  and Editing'
title_zh: 多模态智能体图像生成与编辑全栈方案
authors:
- Hui Zhang
- Zongkai Liu
- Liqiang Niu
- Juntao Liu
- Han Li
- Zhen Cao
- Wenchao Chen
- Chengduo Zhao
- Fandong Meng
affiliations:
- Weixin AI, Tencent
arxiv_id: '2609.05171'
url: https://arxiv.org/abs/2609.05171
pdf_url: https://arxiv.org/pdf/2609.05171
published: '2026-09-04'
collected: '2026-09-08'
category: Agent
direction: 多模态 Agent 图像生成编辑全栈
tags:
- Multimodal Agent
- Image Generation
- Image Editing
- Post-training
- RL
- Benchmark
one_liner: 提出全栈式多模态 Agent 方案，含运行时、数据、基准与后训练，30B总/3B激活策略逼近1T参数 agent 性能
practical_value: '- 在电商商品图/营销素材生成 Agent 中，借鉴其「持久证据管理 + dense carrier」设计：将商品属性、品牌规范、历史文案等检索到的多模态证据沉淀为统一上下文，避免每轮重复检索，提升多轮编辑一致性。

  - 把 verification/integration 拆成独立工具而非塞进 policy 模型，降低策略模型负载并提高可靠性；在推荐/搜索 Agent 中可加结果验证与证据融合工具，先验证再输出。

  - 用三层可验证 checklist 构建 RL 奖励，解决生成/推荐任务难以自动打分的痛点；可迁移到文案生成、创意推荐的离线评估。

  - 小参数策略（3B active）通过 SFT+RL 后训练接近大模型，适合线上成本敏感场景；数据构造上优先合成 prompt + agent trajectory，再
  SFT 后 RL。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

动机：图像生成/编辑模型在需要外部世界知识时不可靠，参数知识覆盖长尾不足；现有检索型 agent 方法存在视觉验证不足、策略模型过载、证据整合弱等问题。

方法关键点：
1. WeAgent-Harness 多模态运行时，支持持久证据管理，并将检索到的多模态证据组织成 dense carrier；
2. 可扩展 prompt 合成与轨迹收集管线，生成 23K 监督轨迹和 14.7K RL 任务，带三层可验证 checklist；
3. WeBench-MMGenEdit 双语基准覆盖知识密集型图像生成和多图编辑；
4. SFT 与 RL 双面后训练同时优化 agent policy 与 image backend。

关键结果：30B 总参数 / 3B 激活策略模型超过同规模策略模型，接近 1T 参数 agent 性能。
