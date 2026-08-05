---
title: 'Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for Streaming
  Recommendation'
title_zh: 知识–几何解耦：流式推荐中可持续刷新的预训练迁移
authors:
- Zixuan Wang
- Yuhong Chen
- Yuxuan Zhu
- Guidong Lei
- Zhiluohan Guo
- Yu Zhao
- Kun Wang
- Bangyang Hong
- Kangle Wu
- Yabo Ni
affiliations:
- Xiamen University
- Shopee Pte. Ltd.
arxiv_id: '2608.02738'
url: https://arxiv.org/abs/2608.02738
pdf_url: https://arxiv.org/pdf/2608.02738
published: '2026-08-02'
collected: '2026-08-05'
category: RecSys
direction: 流式推荐 · 预训练知识迁移 · 参数解耦
tags:
- Streaming Recommendation
- Pretrain-Transfer
- Knowledge Decoupling
- Sequential Recommendation
- E-commerce Search
- A-B Test
one_liner: 通过解耦预训练知识刷新与任务几何学习，使每日更新不干扰下游模型，在电商搜索中提升GMV 1.75%
practical_value: '- **BMTP 去噪预训练**：仅对协同 (item co-occurrence graph) 和语义 (text embedding
  cosine) 相关的未来 item 做预测，过滤掉 session 边界的噪声 transition。可在行为序列预训练中引入双阈值过滤，提升知识纯度。

  - **解耦读写所有权**：让任务模型通过只读交叉注意力读取编码器状态，并通过正交低秩残差 (ACR) 写入任务特有几何，预训练编码器可每日刷新而不破坏下游适配。可推广到多任务排序：每个任务持有独立的
  ACR 和 task learner，共享编码器。

  - **工程落地友好**：训练成本约为单次编码器更新的两倍，推理延迟不增加（任务 learner 仅增加旁路参数）。在实时流式场景可直接复用这种每日刷新 + 任务冻结调优的管线。

  - **长期流式下的稳定性**：冻结迁移 (如 GPSD) 在 90 天线上会衰减，KGD 持续有效。若自己业务面临分布漂移，可借鉴 decoupled owner
  思路，避免共享参数导致刷新与任务冲突。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
工业推荐中行为分布持续漂移，预训练模型需频繁刷新。传统 next-token 预测将行为序列中相邻 item 一律视作依赖，引入跨 session 的噪声；同时刷新时预训练知识与任务特定几何在共享参数上冲突，导致刷新覆盖已学知识，或冻结迁移无法适应新分布。这两点使得流式场景中预训练收益难以维持。

**方法关键点**  
- **BMTP (Behavioral Multi-Token Prediction)**：预训练时仅对与当前位置协同相似 (item graph) 或语义相似 (text embedding) 的未来 item 做正样本，过滤无关跳转，构建干净、可刷新的基础几何。  
- **ACR (Anchored Calibration Residual)**：任务端为每个 item 计算一个任务特有的低秩残差，强制与预训练 embedding 正交，通过标量缩放保留原有方向的同时写入任务判别几何。  
- **只读交叉注意力**：任务模型通过 stop-gradient 的键值对读取编码器隐藏状态，不允许梯度回传，确保编码器参数只受预训练刷新控制，任务几何与预训练知识完全解耦。  
- **每日刷新管线**：每天先刷新编码器，再冻结编码器参数并单独更新任务 learner，刷新和适配不互相干扰。

**关键结果**  
- 8个 Amazon 公开数据集上，KGD 比最强基线 (GPSD 等) 提升 4–12% NDCG@50/Recall@50。  
- 工业 28 天流实验中，所有共享参数方法 (微调、冻结、LoRA) 均低于 KGD；90 天轨迹显示冻结方法随时间衰减，KGD 保持优势。  
- Shopee 首页搜索线上 A/B 测试：GMV per user +1.75%，广告收入 +1.53%，CTR +0.95%，CVR +0.72%。

**核心一句话**：让知识归编码器、几何归任务 learner，二者通过正交低秩残差与只读注意力耦合，即可在每日刷新中持续受益于预训练。
