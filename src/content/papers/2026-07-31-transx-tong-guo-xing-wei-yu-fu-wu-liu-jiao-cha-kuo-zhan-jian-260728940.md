---
title: 'TransX: Scaling Transformer-based Recommendation via Behavioral and Serving
  Stream Crossings'
title_zh: TransX：通过行为与服务流交叉扩展Transformer推荐
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
arxiv_id: '2607.28940'
url: https://arxiv.org/abs/2607.28940
pdf_url: https://arxiv.org/pdf/2607.28940
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 工业推荐 · 序列建模 · 延迟优化
tags:
- Encoder-Decoder
- Cross-Attention
- Streaming Sequence Model
- Model-Infrastructure Co-design
- Production Scale
- KV Caching
one_liner: 用Encoder-Decoder解耦行为流和服务流，结合分组稀疏交叉注意力与近线缓存，在LinkedIn实现CTR+6.0%且在线计算降低80%
practical_value: '- 将用户行为序列与候选服务流显式解耦，Encoder专注长期意图，Decoder通过Cross-Attention融合当前候选，避免将异质信号混在一个序列中，既保留因果结构又提升预测力。电商/广告场景中用户浏览、加购等行为与曝光上下文天然分离，可直接套用这种双流交叉架构。

  - 近线行为编码 + 缓存策略：利用因果自注意力一次性编码用户全历史，生成行为表示并持久化，在线推理时只做轻量级候选编码和交叉注意力，延迟与行为序列长度无关。可借鉴到实时推荐场景，大幅降低成本。

  - 分组多查询稀疏交叉注意力：所有候选共享行为序列的Key/Value，每个候选仅有独立Query，并引入局部最近行为窗口+全局锚点（pooling token）的稀疏模式，既能捕捉短期意图和长期偏好，又将复杂度从O(mL)降到O(mL_local)。高QPS下非常实用。

  - 序列到序列的单次前向传播训练：利用行为前缀复用，训练成本从O(T L^2 d)降为O(L^2 d+T)，相比传统逐事件训练每epoch时间减少约50%。在大量用户历史场景下训练效率提升明显。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
工业推荐日益依赖Transformer建模长序列，但主流做法将用户长期行为、实时服务事件和反馈全部折叠成单一token流，忽略了它们不同的因果角色和时序特性，导致语义混淆和巨大计算冗余。尤其在高吞吐、低延迟约束下，逐请求重编码整个行为前缀不可行。  

**方法关键点**  
- **Encoder-Decoder架构**：Encoder处理用户行为流（点击、搜索、关注等），用因果自注意力和相对位置编码学习意图；Decoder通过交叉注意力将服务事件候选与行为表示交互，预测动作token（如点击/未点击）。  
- **分组多查询稀疏交叉注意力**：所有候选共享行为序列的Key/Value，每个候选独立Query；注意力限制在局部最近行为和全局池化锚点，计算复杂度与行为总数脱钩，仅依赖局部窗口大小。  
- **流式Seq-to-Seq训练**：一次因果编码整个行为流，为所有服务事件复用前缀表示，单次前向-反向传播累积所有事件损失，训练复杂度从O(T L^2 d)降为O(L^2 d+T)，训练吞吐提升约50%。  
- **近线缓存与KV缓存**：行为表示离线/近线异步计算并缓存（bf16量化），在线仅需轻量候选编码、稀疏交叉注意力和并行动作解码，延迟与行为序列长度无关，整体在线计算降低约80%。  

**关键结果**  
在LinkedIn最大社交推荐场景，180天行为窗口，对比LiDLRM、SASRec、TransAct、GRM等基线。离线：TransX取得AUC 0.862，显著优于TransAct（0.860）和GRM（0.858），且在线MFLOPs仅为后者的约20%。在线A/B测试：CTR +6.0%，转化率 +4.4%，每日活跃用户 +0.26%，而硬件成本与原有DLRM持平。  

**一句话核心**  
显式建模“行为流×服务流”的交叉，加上从训练到推理的协同设计，让Transformer推荐模型在工业系统中首次同时获得最大CTR涨幅与成本骤降。
