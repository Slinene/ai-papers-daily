---
title: 'DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimodal
  Agents'
title_zh: DeepVoyager-VL：长程多模态循环视觉搜索框架
authors:
- Huanyao Zhang
- Jiepeng Zhou
- Runhao Zhao
- Yanzhe Shan
- Jiaoyang Chen
- Bowen Zhou
- Bo Li
- Fang Wang
- Jialong Wu
- Zhengwei Tao
affiliations:
- PKU
- HKUST(GZ)
- NUDT
- OUC
- HITSZ
arxiv_id: '2608.01827'
url: https://arxiv.org/abs/2608.01827
pdf_url: https://arxiv.org/pdf/2608.01827
published: '2026-08-02'
collected: '2026-08-05'
category: Agent
direction: 多模态Agent · 视觉增强搜索
tags:
- Multimodal Agent
- Deep Search
- Vision-in-the-Loop
- Long-Horizon
- Data Synthesis
- Event Graph
one_liner: 通过多模态事件图合成中间视觉依赖的推理数据，训练Agent主动获取视觉证据驱动多轮搜索。
practical_value: '- 借鉴事件图驱动的数据合成范式，为电商搜索构建包含多轮视觉对比（如商品图、评价截图）的长链推理训练数据，训练具备中间视觉依赖推理能力的搜索Agent。

  - 主动视觉获取与按需图像加载设计，可降低多模态搜索Agent在实际应用中的计算开销，适合淘宝等大型商品图像索引场景。

  - 纯SFT微调（无需RL）即可显著提升多模态搜索能力，实现简单且稳定，适合业务快速迭代。

  - 视觉在循环中的交互模式可迁移至电商导购：通过用户上传的图片逐步澄清需求，动态驱动下一轮检索或提问。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态LLM受限于静态参数知识，难以处理需要动态视觉证据的开放式长程搜索问题。现有方法仅将视觉用于输入或最终答案，中间推理缺乏视觉驱动，导致交互深度和推理跨度受限。

**方法**：提出DeepVoyager-VL，构建多模态事件图，通过采样事件链自动生成具有中间视觉依赖和长推理链的问题；设计Agent框架支持主动视觉获取（主动请求图像）与按需图像加载；最后仅用合成数据对模型进行微调，无需强化学习。

**结果**：在10个多模态搜索基准上验证，性能显著优于基线，证明了视觉在循环中的搜索范式能有效扩展多模态Agent的推理深度与准确性。
