---
title: 'ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical
  Reasoning'
title_zh: ClinSeekAgent：自动化多模态证据寻找的临床Agent推理框架
authors:
- Juncheng Wu
- Letian Zhang
- Yuhan Wang
- Haoqin Tu
- Hardy Chen
- Zijun Wang
- Cihang Xie
- Yuyin Zhou
affiliations:
- UC Santa Cruz
arxiv_id: '2605.20176'
url: https://arxiv.org/abs/2605.20176
pdf_url: https://arxiv.org/pdf/2605.20176
published: '2026-05-18'
collected: '2026-05-23'
category: Agent
direction: 动态多模态证据寻找 · 轨迹蒸馏
tags:
- evidence-seeking
- multimodal
- distillation
- clinical reasoning
- agentic framework
one_liner: 提出动态多模态证据寻找Agent，可蒸馏轨迹至小模型，将被动证据消费转为主动获取
practical_value: '- **主动证据获取回路**：在推荐/电商场景中，可借鉴Agent主动调用搜索、商品知识库、用户画像等异构工具，动态收集信息并迭代优化判断，替代静态查询。

  - **多模态工具集成**：医学图像工具调用模式可迁移至多模态商品理解（图文视频），Agent自主决定何时调用图像分析API，提升决策丰富度。

  - **轨迹蒸馏策略**：将大模型Agent的高质量推理轨迹蒸馏到本地小模型，在保持部分效果的同时降低在线推理成本，适合电商高并发服务。

  - **评测范式借鉴**：构建“预选证据”与“自动寻找”对等基准，可复用于评估推荐系统从被动排序到主动信息检索的增益。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有临床LLM假设已提供精选证据，与真实临床中需从原始数据（EHR、知识库、影像）主动搜索、迭代综合的多步骤流程脱节。  
**方法**：提出ClinSeekAgent，给定查询和原始数据源接入，Agent自主规划工具调用（查询医学知识库、浏览EHR、调用影像工具），边收集新证据边修正假设，最终整合多模态信息做出决策。框架既可作推理时Agent挂载前沿LLM（如Claude、MiniMax），也可作为训练pipeline收集高质量轨迹，蒸馏至开源稠密模型（ClinSeek-35B-A3B）。构建ClinSeek-Bench，对比“Curated Input”（预选证据）与“Automated Evidence-Seeking”（自动寻找）两种设定。  
**关键结果**：文本EHR任务上，ClinSeekAgent将Claude Opus 4.6 F1从60.0提至63.2，MiniMax M2.5从43.1提至47.3，9个模型其中7个获得正向提升；多模态任务上Claude Opus 4.6从47.5跃升至62.6（+15.1），所有模型在CXR相关任务上均有提升。蒸馏模型ClinSeek-35B-A3B在AgentEHR-Bench平均F1 34.0，超Qwen3.5-35B-A3B基线11.9点，接近Claude Opus 4.6水平。
