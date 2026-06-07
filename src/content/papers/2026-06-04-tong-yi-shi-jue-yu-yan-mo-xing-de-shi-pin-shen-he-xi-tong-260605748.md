---
title: 'UNIVID: Unified Vision-Language Model for Video Moderation'
title_zh: 统一视觉语言模型的视频审核系统
authors:
- Kejuan Yang
- Yizhuo Zhang
- Mingyuan Du
- Yue Zhang
- Dixin Zheng
- Kaili Zhao
- Yang Xiao
- Hanzhong Liang
- Kenan Xiao
affiliations:
- Bytedance
arxiv_id: '2606.05748'
url: https://arxiv.org/abs/2606.05748
pdf_url: https://arxiv.org/pdf/2606.05748
published: '2026-06-04'
collected: '2026-06-07'
category: Multimodal
direction: 多模态视频理解与工业级内容审核
tags:
- Video Moderation
- Vision-Language Model
- Captioning
- Interpretable AI
- Content Safety
- Multi-modal
one_liner: 用统一VLM生成策略感知字幕实现可解释视频审核，将违规泄露和过度封杀相对降低42.7%与37.0%
practical_value: '- 可解释中间表示：在电商直播/短视频审核中，可训练VLM生成与平台规范对齐的自然语言描述，直接作为审核依据，方便人工抽检和规则迭代。

  - 统一骨干替代多模型：借鉴UNIVID用单一VLM取代上千个专用分类器，大幅降低工程维护成本和计算资源，适合策略频繁变更的电商场景。

  - 多级漏斗架构：结合缓存嵌入和风险信号融合，先粗筛后精审的思路可迁移到商品内容安全、侵权过滤等链路，平衡效率与精度。

  - RAG增强召回：在审核决策时检索历史违规案例作为参考，有效减少遗漏，类似方法可用于商家资质审核或评论风控中的相似违规召回。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：工业级视频审核面临细粒度多模态推理和可解释输出的双重挑战。传统方案依赖大量专用分类器，维护困难且缺乏透明度。已有开源或商用VLM又常因安全护栏拒绝响应、缺乏细粒度策略对齐而无法直接使用。

**方法**：提出统一VLM（UNIVID），核心是生成**策略感知的字幕**作为可解释中间表示，支持人机验证与多任务复用。训练数据由专家精炼标签与合成数据混合组成，使模型对齐安全准则。系统分三阶段：（1）**风险漏斗**融合UNIVID字幕、OCR、风险信号等多模态Embedding过滤高风险视频；（2）**审核Actor**包含UNIVID-Lite和UNIVID-RAG，前者快速决策，后者通过检索历史违规事件减少遗漏；（3）**趋势治理**利用缓存的UNIVID Embedding自适应检测新兴风险。

**结果**：新系统使违规泄露相对减少42.7%，过度封杀相对降低37.0%，同时用单一UNIVID骨干替代超过1000个策略专用模型，大幅节省计算与维护开销，首次验证了高效字幕生成VLM能在工业审核与跨业务中落地。
