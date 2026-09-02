---
title: Two-Sided State-Space Models for Sequential Recommendation with Non-Random
  Multimodal Review Feedback
title_zh: 双边状态空间模型：非随机多模态评论反馈的序列推荐
authors:
- Ziwen Pan
- Zihan Liang
- Ruoxuan Xiong
affiliations:
- Emory University
arxiv_id: '2609.00165'
url: https://arxiv.org/abs/2609.00165
pdf_url: https://arxiv.org/pdf/2609.00165
published: '2026-08-31'
collected: '2026-09-02'
category: RecSys
direction: 双边状态空间序列推荐 · 非随机多模态反馈
tags:
- Sequential Recommendation
- State-Space Model
- Multimodal
- Missing Not At Random
- Review Feedback
- Item Dynamics
one_liner: 提出 TS-SSM，同时更新用户与物品状态，利用模态缺失模式与正负反馈不对称衰减，Recall@20 平均提升 14.8%–18.8%
practical_value: '- 将「是否传图、文本长度偏差、评分偏差」作为模态可用性/历史偏差特征，而不是简单缺失掩码：电商推评中可构造类似 δU, δI
  的特征，提升对异常满意/不满意的捕捉；即使只有评论文本，text-length deviation 也有效。

  - 物品侧维护动态 latent state + 正负反馈不对称衰减：比静态 item embedding 更贴近商品口碑演化，尤其适用于差评长期影响的商品降权或商家质量分；负反馈
  decay 更慢，可作为业务策略参考。

  - 局部图传播以最近交互商品为 anchor，向同图邻居传递偏好更新，可低成本迁移到召回后重排或实时特征：差评某商品后提高相似替代品权重。

  - 工程上：对非目标候选做最新状态 + 时间对齐 gate，避免全量实时更新；辅助预测 drift/carryover/conflict proxies 帮助状态解耦，可在排序模型训练中借鉴。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

双边平台中用户偏好与物品口碑同时演化，评论既是偏好表达也是影响后续用户的信号。但多数序列推荐仅把评论视作用户侧的静态特征或被动更新源，忽略两点：评论的产生本身非随机——是否留评、是否发图、文本长度异常都携带着状态变化信息；评论会改变物品状态并通过相似物品溢出，影响后续用户决策。Amazon 数据显示，图片与文本长度偏离伴随着 5 星率下降近 10 个百分点，负反馈衰减半衰期比正反馈更长（4.62 vs 2.77 月 bin）。

方法关键点：
- 多模态非随机缺失融合：编码评论内容、模态 availability pattern，并与用户/物品历史表达模式比较得到偏差特征 δU, δI。
- 用户状态演化：当前事件消息 + 历史观测加权消息 + 时间趋势 + 偏差门控；再用最近交互商品作 anchor，在局部 item-item 图上传播相关商品状态，产生图更新。
- 物品状态演化：以历史偏差门控当前事件，并用 carryover memory 记录每次 review 的创新，正负反馈使用独立衰减率；Boundα 限制状态突变。
- 排序：目标 item 用 post-event 状态，非目标 item 用最新状态 + 时间对齐 MLP/gate；训练使用 BPR + drift/carryover/reliability 辅助损失。

关键结果：
六个 Amazon 类别上，TS-SSM Recall@20 比 BSARec 提升 14.8%–18.8%，平均超过 HM4SR 11.7%；Goodreads Fantasy 从 0.5191 到 0.5847（+12.6%）。消融：移除物品状态更新 -3.50%，局部传播 -2.79%，用户状态更新 -2.50%；MNAR gating 替换为 indicator -2.97%；静态 item-level 文本替换 -2.67%，完全去文本 -6.30%。

最值得记住：评论的观察模式与行为偏差本身就是推荐信号；让物品也有动态状态、并让负反馈衰减更慢，是实际业务里便宜而有效的升级。
