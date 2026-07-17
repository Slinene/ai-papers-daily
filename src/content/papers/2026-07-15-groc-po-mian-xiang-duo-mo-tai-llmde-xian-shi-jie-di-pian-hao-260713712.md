---
title: 'Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal
  LLMs'
title_zh: Groc-PO：面向多模态LLM的显式接地偏好优化
authors:
- Zhixiao Zheng
- Zheren Fu
- Zhiyuan Yao
- Chunxiao Liu
- Dongming Zhang
- Zhendong Mao
affiliations:
- University of Science and Technology of China
- Xiaomi Corporation
- State Key Laboratory of Communication Content Cognition, People's Daily Online
arxiv_id: '2607.13712'
url: https://arxiv.org/abs/2607.13712
pdf_url: https://arxiv.org/pdf/2607.13712
published: '2026-07-15'
collected: '2026-07-17'
category: Multimodal
direction: 多模态LLM对齐 · 分阶段接地偏好优化
tags:
- MLLM
- Preference Optimization
- Grounded Reasoning
- Hallucination Mitigation
- DPO
- Chain-of-Thought
one_liner: 通过在多模态推理的物体、上下文和推理阶段引入显式偏好监督，抑制错误传播并减少幻觉
practical_value: '- 在商品图文描述生成、多模态问答等场景中，可借鉴分阶段偏好优化思想：分别对物体识别、上下文理解和推理结论设计偏好对，在训练时注入更细粒度的真实监督，从而减少事实错误。

  - 构建偏好数据集时，可采用类似GCPD的三阶段结构（Object Grounding, Contextual Grounding, Grounded Reasoning），强制模型在生成中间步骤时保持与视觉证据的紧密一致性，这对需要多步推理的电商导购Agent尤其关键。

  - 工程实现上，可直接在流行的DPO训练框架（如trl）中添加按阶段分组的损失项，只需将偏好对按阶段标记，然后联合优化，无需大幅改动训练管线。

  - 该显式接地监督思路可迁移至搜索推荐中的多模态理解模块（如商品图、视频理解），提升对长尾商品或复杂组合的识别精度，最终改善推荐理由或搜索摘要的真实性。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态大语言模型(MLLM)仍存在严重的不真实问题，如视觉幻觉、内容捏造和不忠诚推理。标准DPO仅在最终答案层面对齐偏好，但推理错误往往从早期接地阶段就开始传播，最终答案错误可追溯至物体识别或上下文理解错误，因此需要更细粒度的阶段级偏好监督。

**方法**：提出Groc-PO框架，将多模态推理显式拆分为三个阶段：物体接地(Object Grounding)、上下文接地(Contextual Grounding)和接地推理(Grounded Reasoning)；并构建了对应的偏好数据集GCPD。在该框架下，偏好优化不再仅针对最终输出，而是对每个阶段的生成进行“选定-拒绝”对比学习，迫使模型在每个阶段都忠实于视觉输入和已有上下文，从而切断错误跨阶段传播的链条。

**结果**：在多个多模态幻觉和推理基准上，Groc-PO显著优于标准DPO和其他强基线，展示了更低的幻觉率和更高的推理可靠性，验证了阶段级显式接地监督在提升MLLM真实性方面的价值。
