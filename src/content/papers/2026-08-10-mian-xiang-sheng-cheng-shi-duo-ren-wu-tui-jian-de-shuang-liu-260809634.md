---
title: 'IntHQ: Task-Interactive Hierarchical Query on Dual-Stream Representations
  for Generative Recommendation'
title_zh: 面向生成式多任务推荐的双流层次查询交互建模
authors:
- Junjie Sun
- Longfei Xu
- Huimin Yan
- Wei Luo
- Kaikui Liu
- Xiangxiang Chu
affiliations:
- DreamX, Alibaba Group
arxiv_id: '2608.09634'
url: https://arxiv.org/abs/2608.09634
pdf_url: https://arxiv.org/pdf/2608.09634
published: '2026-08-10'
collected: '2026-08-11'
category: GenRec
direction: 生成式多任务推荐 · 任务交互层次查询
tags:
- Generative Recommendation
- Multi-task Learning
- Dual-Stream
- Hierarchical Query
- Task Interaction
- Representation Collapse
one_liner: 通过双流解耦、自适应任务交互和层次查询机制，解决生成式多任务推荐的源坍塌、关系坍塌与层次坍塌，线下指标全面最优、线上UVCTR提升1.60%
practical_value: '- **任务token与上下文token的解耦编码**：将任务专属 learnable token 组成独立序列，使用独立参数的自注意力和交叉注意力，在编码早期注入任务信号，避免任务信息在共享流中被稀释，可迁移到多目标推荐场景。

  - **自适应任务交互的因果掩码自注意力**：在任务token流上加入因果约束的自注意力，自动学习任务间的输入依赖强度，替代预设漏斗结构，适合电商中搜索→点击→购买等多步依赖的动态建模。

  - **层次查询选多尺度特征**：每个任务通过可学习的深度注意力从不同层抽取信息，让细粒度检索（如 POI 预测）用浅层局部信号，粗粒度意图（如出行方式）用深层全局模式，可为多任务推荐中不同粒度的目标提供专用特征。

  - **工业部署的离线–在线分离架构**：用户历史序列离线预计算并存入 KV 存储，在线仅执行推理与最近邻检索，使模型在 30k QPS 下平均延时 40ms，适合大流量推荐系统的工程化落地。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐统一了传统推荐的多阶段级联，但多任务学习依然沿袭“单流共享编码+条件独立预测头”的范式，导致三种表示崩溃：①源崩溃——任务信号在共享底层中稀释；②关系崩溃——任务间依赖被隐式吸收或固定漏斗限制；③层次崩溃——不同任务对不同层特征的需求差异被抹平。地图旅行推荐中同时预测何时、何地、如何、经由何处四个耦合决策，迫切需要在编码阶段注入任务信号并建模动态依赖。

**方法关键点**：
- **双流解耦 (DSD)**：构建独立的场景 / 物品 / 反馈 token 序列（上下文流）与任务 token 序列（任务流），二者参数完全分离。上下文流做自注意力，任务流用交叉注意力查询上下文，并在同一层内并行执行，保持计算独立。
- **任务交互建模 (TIM)**：在任务流上增加因果约束的自注意力，使得当前任务的表征能显式依赖同一会话中已决策的前置任务输出，学习实例级自适应依赖强度。
- **层次查询 (HQ)**：收集每层任务 token 输出形成深度维序列，用可学习的深度注意力为每个任务聚合不同层的表示，自动选择最优深度。
- **训练**：各任务分别使用 InfoNCE 损失（大空间任务采用采样 softmax），联合端到端优化。

**关键实验**：在工业级出行数据集 IntTravel（163M 用户、4.1B 交互、7.3M POI）上，用 4 种编码器和 4 种多任务头交叉对比。IntHQ 在所有头配置下全面超越 IntTravel、OneTrans、HGenPush，尤其在最易受关系坍塌影响的 How 任务上提升显著（Acc 从 0.5657→0.6896）。消融证实各组件的必要性，且模型性能随层数（2→32）和宽度（24→384）呈可扩展趋势。线上 Amap 全流量 A/B 测试获得 1.60% 相对 UVCTR 提升，平均响应时间 40ms。

**一句话**：将任务身份注入编码起点、解耦参数空间并让任务自主选择特征深度，是生成式多任务推荐的有效范式转变。
