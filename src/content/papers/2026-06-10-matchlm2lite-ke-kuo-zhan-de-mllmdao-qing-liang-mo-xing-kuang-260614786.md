---
title: 'MatchLM2Lite: A Scalable MLLM-to-Lite Framework for Reproduced Content Identification'
title_zh: MatchLM2Lite：可扩展的MLLM到轻量模型框架，用于复制内容识别
authors:
- Xiaotian Fan
- Hiok Hian Ong
- David Yuchen Wang
- Zirui Zhu
- Kanchan Sarkar
- Kun Xu
affiliations:
- TikTok
- National University of Singapore
arxiv_id: '2606.14786'
url: https://arxiv.org/abs/2606.14786
pdf_url: https://arxiv.org/pdf/2606.14786
published: '2026-06-10'
collected: '2026-06-17'
category: RecSys
direction: 多模态内容去重 · 蒸馏
tags:
- Multimodal
- Knowledge Distillation
- Video Copy Detection
- Production System
- Recommendation Pipeline
one_liner: 将多模态大模型蒸馏为小模型，实现实时视频对复制检测，F1提升+8.57/+6.55，计算成本降35倍
practical_value: '- **Teacher-Student蒸馏架构**：可借鉴到电商视频/直播去重——用大模型打标或提供软标签，训练轻量模型在线推理，兼顾精度与效率。

  - **多模态融合方案**：联合视频、音频、文本信号进行配对打分，适用于识别电商短视频、直播间切片复制，减少低质内容分发。

  - **工程化指标**：35倍计算成本下降、延迟<30秒、支持高QPS，证明蒸馏模型可在推荐链路中承担实时过滤任务，不影响用户体验。

  - **线上业务验证**：在保持用户参与度不变的前提下，使重复观看率降低2.5%，直接提升推荐列表多样性，可作为去重系统的效果度量。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：在线视频平台需大规模识别复制内容，保证用户看到多样化原创视频，避免低质重复内容的泛滥。传统单模态或规则方法难以准确捕获跨模态的细微复制，而大模型推理成本过高。

**方法**：提出MatchLM2Lite系统，包含两个模块：
- MatchLM：多模态大模型（MLLM），作为教师模型，在成对视频的多模态信号（视频、音频、文本）上训练，输出细粒度复制分数，设定了性能上界。
- MatchLite：轻量学生模型，通过知识蒸馏继承MatchLM的理解能力，将计算成本降低**35×**，支持实时高吞吐推理。

系统采用两阶段训练：先用强标注数据训练教师，再通过蒸馏策略将教师的知识迁移到学生模型。学生模型直接接收原始多模态特征，输出复制概率。

**结果**：在TikTok大规模部署中，MatchLM的F1值相比上一代生产模型提升**+8.57**，MatchLite保留**+6.55**的F1增益。线上服务时，MatchLite以低于**30秒**的端到端延迟稳定处理高QPS流量，最终使平台复制视频观看率下降**2.5%**，且未降低用户参与度。
