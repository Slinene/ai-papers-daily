---
title: 'LoMo: Local Modality Substitution for Deeper Vision-Language Fusion'
title_zh: LoMo：局部模态替换促进视觉-语言深度融合
authors:
- Feng Han
- Zhixiong Zhang
- Zheming Liang
- Yibin Wang
- Jiaqi Wang
affiliations:
- Fudan University
- Shanghai Innovation Institute
- Shanghai Jiao Tong University
- University of Science and Technology of China
- JD.COM
arxiv_id: '2605.30265'
url: https://arxiv.org/abs/2605.30265
pdf_url: https://arxiv.org/pdf/2605.30265
published: '2026-05-27'
collected: '2026-05-29'
category: Multimodal
direction: 多模态表征对齐与数据增广
tags:
- Vision-Language Models
- Modality Substitution
- Cross-modal Invariance
- Data Augmentation
- Multimodal Fusion
- Carrier Sensitivity
one_liner: 通过将文本片段渲染为图像来构造交错多模态数据，迫使VLM学习跨模态表征不变性，显著缓解“载体敏感”问题。
practical_value: '- **弱图文对齐场景的增效思路**：电商商品信息中图文往往分离，LoMo 的“文本→图像再重写”范式可直接用于商品描述增强，例如将规格参数渲染为图片，迫使多模态模型更关注视觉细节，提升详情页图文一致性校验。

  - **低成本跨模态对齐数据合成**：无需额外标注，仅需将现有纯文本 Splits 中的关键词（如属性、尺寸）动态渲染成图像，就能构造出强对齐的多模态序列，适合推荐系统里的多模态冷启动或属性抽取任务。

  - **模型架构无关的轻量增强**：LoMo 仅作用于数据端，不修改 VLM 架构，可以快速插入到现有 Agent 的视觉推理链路（如商品图片问答、图文简历解析）作为
  fine-tuning 阶段的简单增强，提升对同一语义在不同载体下的鲁棒性。

  - **对 Deep 融合的启发**：LoMo 通过“视觉载体与文本载体交替”施加表征不变性约束，这一思想可迁移到多模态推荐中，例如在序列建模中将物品图像与文本标题交替编码，迫使模型学习模态无关的物品表征，有望缓解模态缺失时的性能下降。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前视觉-语言模型（VLM）存在“载体敏感”现象：将文本问题直接渲染成图像后，模型性能大幅下降。根源在于训练数据中的文本和图像角色不对称（文本作为提问，图像作为参考），导致模型对信息获取渠道形成偏好，无法对齐语义相同但载体不同的表述。

### 方法
提出**局部模态替换（LoMo）**，一种数据端轻量范式。核心操作是：对单模态文本序列，动态选取关键词或短语（如实体、数值），将其渲染为图像，并嵌入原文本位置，形成“文本-图像-文本”的交错多模态序列。这一过程保持语义完全等价，但迫使模型学习跨模态表征不变性。LoMo 无需修改模型架构或训练目标，仅在 SFT 数据中注入此类增强样本。

### 关键结果
在 13 个多模态基准上，LoMo 一致性提升基础 VLM 的多模态推理能力：LLaVA-OneVision-8B 平均提升 2.67 分，Qwen3.5-9B 提升 2.82 分。消融实验表明，这种跨模态不变性监督显著增强了图文深度融合，缓解了载体敏感问题。
