---
title: 'RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts
  Language Models'
title_zh: RARE：在 MoE 语言模型中解耦表示引导与专家路由
authors:
- Zhibo Zhang
- Zhen Ouyang
- Ling Shi
- Kailong Wang
affiliations:
- Huazhong University of Science and Technology
- AIDX TECH PTE. LTD.
- National University of Singapore
arxiv_id: '2608.21236'
url: https://arxiv.org/abs/2608.21236
pdf_url: https://arxiv.org/pdf/2608.21236
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: MoE LLM 表示工程与路由解耦
tags:
- MoE
- Representation Engineering
- Steering
- Router Null Space
- Safety Alignment
- Truthfulness
one_liner: 将行为扰动投影到路由器矩阵零空间，保持 MoE 路由一致，提升表示工程的控制效果与效用保留
practical_value: '- 如果业务用 DeepSeek/Qwen 等 MoE LLM 做生成式推荐、query 改写或商品文案，需要对安全性、合规性、事实性进行在线控制时，避免直接对
  hidden states 加扰动导致 expert 路由漂移；可借鉴 RARE 把扰动投影到 router matrix 的 null space，以保留下游能力。

  - 该方法是轻量、无需训练的推理期控制手段，相比 SFT/RLHF 可以快速上线、实时调节，适合电商大促、广告审核等需要动态调整输出约束的场景。

  - 工程实现只需缓存各层 router matrix 并计算其零空间投影，可在 vLLM 等推理框架中作为后处理插件集成，对延迟影响较小；论文在多个开源 MoE
  模型上验证了通用性。

  - 路由对语义内容敏感、对行为变化不敏感这一发现，提示在做 RAG 检索、query 改写时如果希望改变模型输出风格而不破坏专家选择，可以优先在表示空间的 router-null
  子空间内操作。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
Representation engineering 通过修改中间 hidden states 轻量控制 LLM 行为，但直接应用于 MoE 模型存在结构不匹配：干预 hidden states 会改变 router 的 expert 选择，导致能力下降。作者先通过实验验证该失败模式，发现保持干净路由能大幅恢复 steering 性能，且路由对语义内容更敏感、对行为变化不敏感。

### 方法关键点
提出 RARE，一个 router-agnostic 的 MoE 表示工程框架。核心是把任意行为扰动投影到 router matrix 的零空间，移除 router 可见成分，从而保持 expert 路由一致；同时修正传播到选定下游层的路由漂移。论文评测了 5 种扰动估计器、6 个异构开源 MoE 模型、3 个场景：有害性、真实性、事实编辑。

### 关键结果数字
- 有害性 steering：平均 attack success rate 达 53.3%，同时保留 67.8% MMLU accuracy，效用-效果权衡优于基线。
- 真实性：平均 TruthfulQA MC1 从 41.0% 提升到 58.6%。
- 事实编辑：CounterFact efficacy 从 16.8% 提升到 96.3%。
