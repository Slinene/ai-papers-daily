---
title: 'The Clustering Strikes Back: Building Cost-Effective and High-Performance
  ANNS at Scale with Helmsman'
title_zh: 聚类反击：用Helmsman构建高性价比大规模向量检索系统
authors:
- Yuchen Huang
- Baiteng Ma
- Yiping Sun
- Yang Shi
- Xiao Chen
- Xiaocheng Zhong
- Zhiyong Wang
- Yao Hu
- Erci Xu
- Chuliang Weng
affiliations:
- East China Normal University
- Shanghai Jiaotong University
- Xiaohongshu Inc
arxiv_id: '2606.13145'
url: https://arxiv.org/abs/2606.13145
pdf_url: https://arxiv.org/pdf/2606.13145
published: '2026-06-11'
collected: '2026-06-14'
category: RecSys
direction: 近似最近邻搜索 · 聚类索引系统优化
tags:
- ANNS
- Clustering
- GPU Acceleration
- User-space I-O
- Learned Pruning
- Cost Efficiency
one_liner: 用聚类索引+用户态闪存栈+学习型剪枝+GPU加速，替代全内存HNSW，成本降90%且维持高性能
practical_value: '- 当向量库规模导致全内存HNSW成本不可接受时，可参考聚类+全闪存架构，利用用户态I/O栈（如SPDK）消除内核开销，大幅降低硬件投入的同时满足低延迟SLA。

  - 学习型剪枝（leveling-learned pruning）思路可用于多级检索系统：动态预测每层需扫描的聚类数量，避免固定剪枝造成的精度损失或冗余计算，可迁移到推荐召回的分层索引中。

  - GPU加速索引构建流水线使十亿级索引能在小时内重建，适合电商场景下频繁全量/增量更新需求，缩短模型到上线的延迟。

  - 系统层面将ANNS负载从数万核CPU+大内存下沉到少量闪存机器，对团队评估检索架构演进方向有直接参考价值：优先考虑存储优化和计算下推，而非线性堆资源。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：小红书（RedNote）的搜索、推荐与广告服务重度使用近似最近邻搜索（ANNS），此前依靠全内存的HNSW图索引满足高吞吐、低延迟SLA。随着业务规模膨胀，内存占用达到PB级，硬件成本（CapEx/OpEx）难以承受。团队尝试转向基于聚类的ANNS并部署在全闪存服务器上，但遭遇内核I/O栈开销大、固定剪枝策略低效、索引构建缓慢等问题。

**方法**：提出的HELMSMAN系统结合三方面创新：1）ANNS导向的用户态存储栈，绕过内核I/O，充分利用NVMe闪存带宽；2）分级学习型剪枝模块（leveling-learned pruning），借鉴LSM-tree的分级思想，通过机器学习预测每层应访问的聚类数以平衡精度与开销；3）GPU加速的索引构建流水线，将聚类、量化和图索引等多阶段任务并行化。

**结果**：生产部署中，40台全闪存机器替代了原先约35,000核CPU和0.35 PB DRAM，硬件成本节省超90%，可稳定承载相等的查询负载，且支持在数小时内完成十亿级索引全量重建，已稳定运行数月。
