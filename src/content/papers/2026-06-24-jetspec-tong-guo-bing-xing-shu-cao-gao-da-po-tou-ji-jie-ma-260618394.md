---
title: 'JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel
  Tree Drafting'
title_zh: JetSpec：通过并行树草稿打破投机解码的规模天花板
authors:
- Lanxiang Hu
- Zhaoxiang Feng
- Yulun Wu
- Haoran Yuan
- Yujie Zhao
- Yu-Yang Qian
- Bojun Wang
- Peng Zhao
- Daxin Jiang
- Yibo Zhu
affiliations:
- UC San Diego
- Zhejiang University
- UIUC
- Nanjing University
- StepFun
arxiv_id: '2606.18394'
url: https://arxiv.org/abs/2606.18394
pdf_url: https://arxiv.org/pdf/2606.18394
published: '2026-06-24'
collected: '2026-06-27'
category: LLM
direction: 投机解码 · 并行树草稿突破 scaling 瓶颈
tags:
- Speculative Decoding
- Tree Drafting
- Causal Parallel Head
- LLM Serving
- vLLM Integration
one_liner: JetSpec使用因果并行草稿头一次性生成树形候选，将更大预算转化为更长接受前缀，实现最高9.64倍加速
practical_value: '- 在搜索推荐或Agent的LLM推理服务中，可直接应用JetSpec的并行树草稿方案，突破budget增大后的加速天花板，降低长文本生成（如解释性推荐理由、对话式Agent）的延迟。

  - 草稿头训练方法：冻结目标LLM，将多层隐藏状态融合后作为输入，训练因果并行草稿头，可在不修改目标模型前提下降低部署风险，适合工业环境快速迭代。

  - 树状注意力设计：采用分支因果条件，生成内部自洽的候选树，避免分支间不一致造成的接受率下降，可迁移到其他基于树搜索的解码加速方案（如搜索评分、query改写候选生成）。

  - 与vLLM的集成验证了JetSpec在真实负载下的有效性，可为工程化落地提供参考，尤其适合高并发、对延迟敏感的在线推荐/Agent系统。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：投机解码（SD）加速LLM时面临扩展瓶颈——增大draft budget只有在接受率高且draft开销低的条件下才有效。自回归draft按路径条件生成候选，接受长度高但draft成本随树深度线性增长；双向块扩散draft一次生成所有位置，但分支不可知导致候选树内部不一致，浪费预算且接受率低。

**方法**：JetSpec提出一种因果并行草稿头，从冻结的目标模型多层隐藏状态融合后一次性生成所有分支的候选token，同时引入分支因果条件，确保草稿树的得分与目标模型的自回归分解对齐。训练时仅更新草稿头参数，保持目标模型不变；推理时通过树状注意力一次前向获得完整候选树，再用目标模型并行验证。

**结果**：在Qwen3（dense/MoE）上的数学、编程、对话测试中，JetSpec持续优于双向头和基于树的SD基线。H100上MATH-500加速达9.64×，开放对话负载加速4.58×；与vLLM集成后进一步降低延迟。该方法使大预算（如16 tokens）能有效转化为更长接受前缀，打破了先前SD的scaling天花板。
