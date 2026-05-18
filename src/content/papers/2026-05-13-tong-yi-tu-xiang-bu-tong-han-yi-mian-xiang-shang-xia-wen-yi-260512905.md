---
title: 'Same Image, Different Meanings: Toward Retrieval of Context-Dependent Meanings'
title_zh: 同一图像，不同含义：面向上下文依赖语义的检索研究
authors:
- Ayuto Tsutsumi
- Ryosuke Kohita
affiliations:
- Tokyo Metropolitan University
- CyberAgent
arxiv_id: '2605.12905'
url: https://arxiv.org/abs/2605.12905
pdf_url: https://arxiv.org/pdf/2605.12905
published: '2026-05-13'
collected: '2026-05-18'
category: Multimodal
direction: 图像检索 · 上下文感知 · 语义抽象层次
tags:
- image retrieval
- context-aware search
- visual-semantic embedding
- abstraction levels
- vision-language models
one_liner: 提出L1-L4框架量化图像语义的上下文依赖程度，发现上下文注入图像嵌入更有效，但最抽象语义层次仍难解决。
practical_value: '- 按抽象层次解耦商品图像语义：借鉴L1-L4框架，将商品搜索意图分解为具体属性（形状、颜色）和抽象含义（氛围、适用场景），分层设计召回与排序策略，提升复杂查询的匹配度。

  - 上下文注入策略：在电商多模态检索中，可将商品评论、用户场景描述等叙事上下文编码后融入图像侧嵌入（而非仅融合文本侧），增强对抽象查询（如“浪漫晚餐裙”）的检索能力。

  - 构建场景化评测集：参考合成故事和查询的方法，为商品图像设计不同叙事故事（如“职场通勤” vs “闺蜜聚会”），检验检索系统是否理解同一商品在不同上下文中的差异化匹配，诊断模型抽象语义能力。

  - 对于L4级抽象（意图/氛围）的挑战，可结合外部知识图谱或因果推理先验，辅助模型推断图像在特定叙事中的隐含含义，弥补纯嵌入方法的不足。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机：** 当前图像检索系统将图像映射到固定嵌入，无法捕捉同一图像在不同叙事上下文（如重逢 vs 离别）中的含义变化。研究者观察到上下文依赖性与语义抽象程度相关：具体元素（物体、动作）稳定，抽象元素（氛围、意图）随上下文显著变化。

**方法：** 提出L1-L4框架，将图像语义从上下文无关（L1：对象/属性）到最大上下文依赖（L4：意图/全局氛围）分为四个层次。利用合成故事上下文和对应查询进行受控评估，探索在文本查询嵌入、图像嵌入或两侧同时注入叙事上下文，对跨抽象层检索效果的影响。

**关键结果：** 在合成数据集上，L1查询无需上下文即可精准检索，L2-L3查询在注入上下文后准确率显著提升，且上下文注入图像侧嵌入比注入查询侧更有效；但L4级别即使在完全上下文下仍表现不佳，揭示了上下文依赖图像检索的开放难题。
