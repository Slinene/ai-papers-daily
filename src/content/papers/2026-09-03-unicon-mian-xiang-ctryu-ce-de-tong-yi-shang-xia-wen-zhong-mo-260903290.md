---
title: 'UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction'
title_zh: UniCon：面向CTR预测的统一上下文中心建模范式
authors:
- Jiajun Cui
- Zhengqi Xu
- Fan Zhang
- Zhangteng
- Gu Tang
- Honghong Zhu
- Mengxi Wu
- Yulin Liang
- Xingxing Wang
affiliations:
- Meituan
arxiv_id: '2609.03290'
url: https://arxiv.org/abs/2609.03290
pdf_url: https://arxiv.org/pdf/2609.03290
published: '2026-09-03'
collected: '2026-09-04'
category: RecSys
direction: 统一上下文建模 · CTR预测
tags:
- CTR Prediction
- Context Modeling
- Unified Architecture
- Scaling Laws
- Industrial Recommendation
one_liner: 将历史曝光列表与当前候选集统一为上下文单元，通过分层注意力建模上下文内局部性与跨上下文动态
practical_value: '- **上下文单元抽象**：在电商搜索/推荐中，把每次展示列表（共现商品、位置、环境信号）组织成一个上下文单元，而不是把行为序列展平。这能显式建模同一曝光内商品的竞争/互补关系，以及跨曝光的状态演化，对货架、瀑布流等强上下文场景特别有用。

  - **历史与目标结构对齐**：训练时历史曝光带点击标签，目标候选集用可学习占位符对齐，再通过曝光和绝对位置预测辅助任务将目标单元引导到真实展示分布。这套做法可以迁移到重排或生成式推荐中，让候选集表示更贴近最终展示情境。

  - **目标感知的上下文压缩**：在长历史序列中，每层用target-context的query-key相似度选择保留top-k个最相关的历史上下文单元，大幅降低attention计算量而几乎不损失精度（压缩比0.5时计算减少75.4%，AUC仅降0.0001）。这对长序列用户建模很有借鉴价值。

  - **工程化细节**：padding-free变长注意力、segment offsets表示上下文边界、AOT编译和融合算子，以及候选分片策略（固定300个候选一个分片），这些是让高计算量上下文模型上线可行的关键。训练和推理使用一致的分片规则也很重要。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
传统工业级CTR模型虽然走向统一建模，但仍沿袭“序列特征 vs 非序列特征”的划分，这本质上是遗留特征工程造成的，与用户真实决策过程脱节。用户行为是一连串同构的上下文单元：每次曝光展示一组物品，用户在局部竞争条件下做出选择。在电商搜索、货架、瀑布流等强上下文场景中，用户点击往往取决于同屏其他物品（如价格对比、距离对比），而展平token序列会混淆同屏共现与跨屏时序邻近。因此需要以“上下文单元”为核心重新组织输入。

## 方法关键点
- **上下文单元定义**：一次曝光中共同展示的物品集合 + 用户意图与环境信号（查询、类目偏好、时间、位置、设备等）。历史曝光带真实反馈标签，当前候选集用可学习占位符对齐反馈字段，形成统一的token schema。
- **分层注意力架构**：堆叠UniConBlock，每个block先做**intra-context attention**（只在同一上下文单元内交互，捕捉局部竞争/互补与共享条件），再做**inter-context attention**（跨上下文单元交互，捕捉用户兴趣与环境的时序演化）。
- **目标上下文监督**：三个预测头——点击、曝光、绝对位置。曝光和位置辅助损失将候选初始化的目标上下文单元引导向最终展示列表的潜在分布，提升CTR预测质量。
- **上下文级序列压缩**：首层做全量inter-context，之后每层用target-context query与历史context key计算相关性，Gumbel-TopK选择保留top-k个历史上下文单元，计算量从O(LN²)降至几何级数有界形式。
- **高效工程实现**：padding-free变长注意力、segment offsets表示上下文边界、dense MoE FFN、候选分片（最多300个候选一个分片）、AOT编译推理等。

## 关键实验
在美团搜索广告一年生产数据上，对比Base（DIN+SENet+DCN-V2）及OneTrans、HyFormer、RankMixer及其+DSIN+CIM变体。UniCon-Large压缩版AUC 0.8697，比Base提升0.0139，比最强context baseline RankMixer+DSIN+CIM提升0.0036；LogLoss 0.1991。在线7天A/B：RPM +3.09%，CTR +2.07%，Revenue +2.95%，均显著（p≤0.01）。压缩比0.5时计算减少75.4%，AUC几乎不变。消融显示上下文组织、目标侧统一、分层建模、辅助损失均有贡献。

**最值得记住的一句话**：把每次展示看作一个上下文单元，在同屏内建模局部竞争与互补，在跨屏之间建模兴趣演化，能显著提升上下文丰富场景的CTR预测效果。
