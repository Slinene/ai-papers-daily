---
title: 'Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative
  Decoding'
title_zh: Domino：解耦推测解码中的因果建模与自回归草稿
authors:
- Jianuo Huang
- Yaojie Zhang
- Qituan Zhang
- Hao Lin
- Hanlin Xu
- Linfeng Zhang
affiliations:
- EPIC Lab, Shanghai Jiao Tong University
- School of Software Engineering, HUST
- UESTC
- Fudan University
- Huawei
arxiv_id: '2605.29707'
url: https://arxiv.org/abs/2605.29707
pdf_url: https://arxiv.org/pdf/2605.29707
published: '2026-05-27'
collected: '2026-06-03'
category: LLM
direction: 推测解码 · 推理加速
tags:
- Speculative Decoding
- LLM Inference
- Causal Modeling
- Training Curriculum
- Draft Model
one_liner: 通过并行草稿骨干与轻量因果细化头解耦因果建模，配合基锚定训练，实现最高5.49倍端到端加速
practical_value: '- 在电商对话Agent或推荐理由生成等实时LLM场景中，可借鉴Domino的并行草案+轻量因果头架构，以低计算成本引入块内依赖，提升整体吞吐。

  - 基锚定训练课程（先巩固并行骨干再渐进加入因果信息）可迁移到多阶段推荐模型训练，避免直接引入强因果约束导致的不稳定。

  - 解耦设计思路：将生成过程中的耗时顺序建模替换为并行初稿→顺序修正，可推广到多Agent协作中的子任务规划与结果校准。

  - 工程上，Domino在SGLang服务中的实现展示了如何将推测解码无缝集成到生产级推理框架，对电商中大批量请求的LLM服务优化有直接参考价值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推测解码通过并行验证草稿令牌加速LLM推理，但草稿模型面临两难：自回归草稿能建模令牌间因果依赖，却带来高昂的序列开销；并行草稿虽降低成本，却弱化了块内依赖，导致验证拒绝率高。

**方法**：Domino将因果依赖建模从自回归草稿执行中解耦。先使用并行草稿骨干为整个块生成初步分布，再引入轻量Domino头，利用前缀相关的因果信息进行分布细化。训练上，设计了基锚定课程：先强化并行骨干，再逐步将优化目标转向因果修正后的最终分布，以稳定训练。

**结果**：在Qwen3-8B上，Domino在Transformers后端实现最高**5.49×端到端加速**，在SGLang服务下吞吐加速达**5.8×**，验证拒绝率明显低于纯并行草案，且额外计算开销极小。
