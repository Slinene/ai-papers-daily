---
title: 'SPAR: Enhancing Industrial-Scale Generative POI Recommendation via Real-World
  Spatial Perception'
title_zh: SPAR：通过真实世界空间感知增强工业级生成式 POI 推荐
authors:
- Fangye Wang
- Yunjin Gu
- Haowen Lin
- Yifang Yuan
- Song Yang
- Xiaojiang Zhou
- Pengjie Wang
affiliations:
- AMAP, Alibaba Group
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2609.02062'
url: https://arxiv.org/abs/2609.02062
pdf_url: https://arxiv.org/pdf/2609.02062
published: '2026-09-02'
collected: '2026-09-03'
category: GenRec
direction: 生成式推荐 · 地理空间感知
tags:
- Spatial Perception
- Semantic ID
- Generative Recommendation
- LLM
- Task Vector
- POI Recommendation
one_liner: 用空间内禀 SID、多粒度地理继续预训练和任务向量锚定 SFT，将真实城市空间知识注入生成式 POI 推荐
practical_value: '- 有强地理属性的业务（到店、O2O、本地生活）不要把经纬度只当文本字段；用正弦/NeRF 式坐标编码与语义向量拼接后再 RQ-Kmeans，让
  SID 的 L0 层自然按地理分区，能同时改善距离约束和冷启动。

  - 多阶段 LLM 微调时，用“任务向量”保护特定能力：把领域知识 CPT 后的参数差 τ=W_MG-CPT−W_base 冻结，SFT 期间只加 LoRA 做轻量适配，可避免大规模行为数据覆盖已学知识。

  - 构造多粒度结构化语料做 CPT：基础属性、两两关系（距离/方向/周边）、系统级可达性（导航/路网），比只用 item 文本更能让 LLM 内化真实场景约束，适合搜索/推荐中的上下文知识注入。

  - 离线评估别只看 Hit/NDCG，加上“推荐结果到用户实时位置的距离/可达性”和冷启动分层，能暴露模型是否真正学到空间或场景约束；模块增量贡献分解也有助于定位优化优先级。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

生成式 POI 推荐（如 AMAP）通常把地理信息仅作为 SID 的文本属性，模型主要从用户行为序列学习兴趣，缺少显式距离、方向、可达性机制。结果往往“行为上合理但离用户真实位置很远”，尤其在城市中，直线距离近但隔河、需绕路的情况常见。因此需要把真实城市空间知识显式注入兴趣空间，而不是只靠行为共现推断地理。

## 方法关键点

SPAR 用三个协同阶段构建、培养和保存城市空间知识：

- **SI-SID（Spatially-Intrinsic SID）**：用正弦地理编码显式编码经纬度，得到地理嵌入；与 POI 语义向量拼接并 L2 归一化后，用 RQ-Kmeans 生成层级 SID。坐标相近的 POI 会共享 L0 前缀，使地理邻近成为码本内禀属性。
- **MG-CPT（Multi-Granular Geospatial CPT）**：构造 25 个地理空间数据集，分三层——基础属性（POI/道路属性）、关系知识（POI-POI 距离/方向、POI-道路周边）、系统知识（导航距离、时间、路网序列），对基础 LLM 做继续预训练，让离散 POI 连成可推理的城市空间。
- **TV-SFT（Task-Vector Anchored SFT）**：提取 MG-CPT 与基础模型的参数差 τ=W_MG-CPT−W_base 作为空间任务向量并冻结；在行为 SFT 时，冻结 τ，仅训练基础模型全参数和 τ 上的 LoRA 适配器，最终 W_TV-SFT=W_base+α(τ+ΔLoRA)，防止行为数据覆盖空间知识。

## 关键实验结果

在 NYC/TKY 两个公开数据集上，SPAR-8B 较最强 baseline PLUM 在 R@5/N@5 等指标相对提升 11.91%–19.29%。四个工业 AMAP 数据集上，SPAR-8B 较 PLUM 平均相对提升 38.32%，SPAR-4B 和 0.6B 分别 +28.54%/+9.92%，且 0.6B 超过所有 8B baseline。

消融显示：SI-SID 平均贡献 +10.76%，MG-CPT 再 +15.38%，TV-SFT 进一步 +2.15%–17.90%；上海/天津 Top-K 推荐到用户位置的距离大幅下降，冷启动 R@5 相对提升 47.6%（上海）/48.0%（浙江）。空间认知基准上，4B 模型经 MG-CPT 后平均准确率从 36.8% 升至 76.1%，超过 32B 通用 LLM 的 45.3%。

## 最值得记住的一句话

把地理编码进 SID、用城市级空间语料做 CPT 并冻结任务向量，是生成式 POI 推荐从“行为合理”走向“空间可达”的关键。
