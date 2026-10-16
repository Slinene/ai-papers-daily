---
title: 'TransX Technical Report: Scaling Sequence Transduction for Recommendation'
title_zh: TransX 技术报告：面向推荐系统的序列转导规模化
authors:
- Da Xu
- Liyan Fang
- Divya Venugopalan
- Sunny Hsu
- Xukai Wang
- Rishav Roy Chowdhury
- Cindy Liang
- Nishant Satya Lakshmikanth
affiliations:
- LinkedIn
arxiv_id: '2610.20913'
url: https://arxiv.org/abs/2610.20913
pdf_url: https://arxiv.org/pdf/2610.20913
published: '2026-10-14'
collected: '2026-10-16'
category: RecSys
direction: 序列转导推荐 · 模型-基础设施协同
tags:
- Sequence Transduction
- Behavior Memory
- Disaggregated Serving
- Compute Allocation
- KV Cache
- CTR Prediction
one_liner: 提出 TransX 序列转导框架，将行为编码、记忆与候选融合解耦，通过摊销执行实现模型扩容而不等比增加在线成本
practical_value: '- 商品/广告精排或召回中，候选集常达数百到上千，可借鉴 TransX 的**共享行为记忆 + 候选条件融合**：把用户长期行为压缩成
  global-local memory，在线用 GQA 交叉注意力对候选做融合，避免每个候选都重算历史表示，显著降低在线 GPU 成本。

  - 服务架构上，把用户行为编码从在线路径剥离，改为**离线 bulk prefill + 近线增量 refresh**，在线只消费不可变行为 memory KV
  快照。适合电商推荐中用户行为更新频率远低于请求频率的场景，但需注意版本一致性、KV 量化与分层存储。

  - 训练侧可复用**多前缀共享一次编码 + blocked prefix scan + batched local gather**：在长序列行为模型训练时，消除多个
  event cutoff 的重复前缀编码，实测吞吐提升 84%，MFU 从 41% 提升到 57%，显存峰值下降约 44%，对大用户行为序列训练很有价值。

  - 通过共享行为记忆接口进行多任务后训练（检索、排序、生成式推荐），避免为每个任务重新训练 backbone，适合业务中同时存在召回、精排和生成式推荐需求的团队降低维护成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统扩容通常把更多计算放在在线路径，导致成本随请求量线性增长。TransX 提出关键问题不是“加多少计算”，而是“计算放在哪个组件、何时执行、状态能在多大范围复用”。现有序列推荐模型往往把历史编码、记忆和候选交互混在一起，难以分别控制容量和执行位置。

### 方法关键点
TransX 基于**请求条件序列转导**，将推荐建模为对演进行为流的重复查询，并把计算拆成三个可独立扩展的角色：
- **序列编码**：因果 Transformer 对行为轨迹编码，可跨前缀摊销；
- **行为记忆**：bounded global-local memory，保留最近窗口和较旧历史的可学习标量注意力摘要，控制暴露给下游的 memory resolution；
- **候选条件融合**：候选 query 通过 GQA 交叉注意力迭代读取共享记忆，支持大量候选 fanout。

基础设施同步保留该分解：训练采用 packed trajectory + multi-prefix seq-to-seq，一次编码多个 cutoff，通过 batched local gather 和全局 prefix scan 避免重复前缀计算；服务阶段 disaggregated 为离线 bulk prefill、近线 refresh、在线预测，在线只访问紧凑的行为记忆 KV，不再重算历史。

### 关键结果
在 LinkedIn 大规模社交推荐场景（约 20K QPS，每请求 0.5K–1.2K 候选）进行生产 A/B：
- 核心 TransX CTR +6.02%，转化 +4.45%；
- 检索变体 CTR +2.96%；排序变体转化 +1.33%；
- 匹配训练条件下，监督目标吞吐 +84%；
- disaggregated serving 总服务成本下降近 80%，可支撑约 5× per-request FLOPs，或同等 FLOPs 下 H200 吞吐约 4×。

### 最值得记住的一句话
推荐 scaling 的边界由计算放置和状态复用共同决定：把历史依赖计算移出在线路径，并按组件边际回报分配容量，才能在不等比推高服务成本的情况下提升效果。
