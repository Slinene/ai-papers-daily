---
title: 'Bridging Short Videos and Live Streams: Reasoning-Guided Multimodal LLMs for
  Cross-Domain Representation Learning'
title_zh: RGCD-Rep：推理引导的跨域表征学习，连接短视频与直播推荐
authors:
- Le Zhang
- Xiaolan Zhu
- Yuchen Wang
- Shilong Kang
- Jiaqi Xue
- Xiaoyu Zhang
- Xiang Chen
- Yalong Guan
- Xiangyu Wu
- Shijun Wang
affiliations:
- Kuaishou Technology, Beijing, China
arxiv_id: '2606.04448'
url: https://arxiv.org/abs/2606.04448
pdf_url: https://arxiv.org/pdf/2606.04448
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: 跨域推荐 · 多模态蒸馏 · 可迁移表征学习
tags:
- cross-domain recommendation
- multimodal LLM
- knowledge distillation
- live streaming
- contrastive learning
- representation learning
one_liner: 首次将多模态大模型推理蒸馏到轻量模型，学习行为协同的跨域可迁移 item 表征，部署到快手直播推荐系统
practical_value: '- **用行为对构造跨域蒸馏数据**：从用户日志构建 (短视频, 直播) pair 并量化行为共现强度，作为监督信号。电商场景可直接套用，用
  “点击-加购” 或 “浏览-转化” 行为对，将源域兴趣迁移到目标域。

  - **大模型推理结果结构化**：教师 MLLM 的输出不只是自由文本，而是分解为「垂直领域、关键主体、内容主题」三个维度的标签和匹配判断。在电商中，可将商品属性（品类、功能、场景）结构化，用于引导跨域匹配，避免噪声。

  - **Chorus Tokens + 可迁移/残差分离**：用少量可学习 token（16个）聚合多模态信息，再用可学习 Query 向量拆出可迁移和残差部分。这种轻量设计适合离线生成
  item embedding 并直接供检索使用，低延迟部署友好。

  - **路由损失解决负迁移**：对高可信 pair 鼓励用可迁移空间匹配，低可信 pair 用残差空间吸收噪声，缓解跨域不一致。在电商多域（如搜索、推荐、内容）统一表示时，可借鉴这种“软路由”机制，避免强行对齐带来的性能损失。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
快手平台同时提供短视频和直播服务。短视频流量大、行为数据丰富，直播是核心转化场景但行为稀疏、冷启动严重。跨域推荐可将短视频的用户兴趣迁移到直播推荐。已有方法多使用预提取的多模态静态特征，缺乏深层语义推理，难以解释两个域的 item 为何可迁移。多模态大模型（MLLM）能提供丰富理解和推理，但直接用于跨域推荐面临计算开销大、开放域知识可能不相关、跨域兴趣不一致导致负迁移三大挑战。

### 方法关键点
- **行为协同 Pair 构造**：基于用户真实行为日志，计算短视频和直播在同一时间窗内的共现频率与行为强度，形成高置信度的行为 pair，作为训练和推理蒸馏的素材。
- **结构化跨域推理生成**：用冻结的 35B MLLM（教师）对每个 pair 生成立体结构化知识：(1) item 级多模态内容理解，分解为垂直领域、关键主体、内容主题三个维度；(2) pair 级匹配判断与简要理由，并聚合为语义可迁移分数。
- **两阶段训练框架**：
  - **Stage 1 推理感知蒸馏**：将 pair 级推理分解为独立 item 监督样本，基于可学习的 Chorus Tokens 和 next-token prediction，把教师的理解能力蒸馏到轻量 2B MLLM（学生）。
  - **Stage 2 可迁移表征学习**：共享学生 MLLM 编码两个域的 item，通过可迁移-残差查询感知聚合模块，将 chorus token 拆分出可迁移表示和域残差表示；结合跨域对比损失和可迁移路由损失进行优化，路由损失利用行为和语义联合分数区分高/低纯度 pair，防止负迁移。

### 关键结果
- 数据集：快手一周真实日志，109,523 用户，2.27M 直播交互，24.6M 短视频交互。评估指标 HR@10 和 NDCG@10。
- 离线匹配任务：RGCD-Rep 的 HR@10 和 NDCG@10 分别达到 0.0254 和 0.0127，比最强基线 UniEmbedding 提升 17.59% 和 30.93%。
- 长尾和冷启动场景：RGCD-Rep 在尾部 item 和冷启动用户上的优势更明显，证实了利用短视频行为缓解直播稀疏性的有效性。
- 线上 A/B 测试：部署在快手和快手极速版的直播召回通道，关注率（follow）分别提升 0.83% 和 0.93%，有效房间进入和点击等核心指标也稳定增长，服务超 4 亿日活用户。

### 核心洞见
通过结构化蒸馏将大模型的多模态推理能力压缩到轻量编码器，并用行为协同信号和路由机制学习可迁移的 item 表示，既获得了语义深度又保持了工程部署的低成本，为工业级跨域推荐提供了一条实用路径。
