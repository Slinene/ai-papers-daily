---
title: Cascading Relevance-driven Recommendation Network for CTR Prediction in Trigger-Introduced
  Recommendation
title_zh: 触发式推荐CTR预估的级联相关性驱动网络
authors:
- Kaixuan Chen
- Wenwen Wang
- Xing Fang
- Yang Huang
- Jing Wang
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2608.22973'
url: https://arxiv.org/abs/2608.22973
pdf_url: https://arxiv.org/pdf/2608.22973
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 触发式推荐 · 相关性与兴趣融合
tags:
- Trigger-Induced Recommendation
- CTR Prediction
- Relevance Modeling
- Attention
- Pairwise Loss
- E-commerce
one_liner: 提出CRRN，通过trigger-target交互门控、级联注意力融合与类别辅助pairwise loss，在TIR场景显著提升CTR
practical_value: '- 在承接页/详情页相似推荐中，不要把trigger当作普通特征；用element-wise乘法+coaction门控做显式交互，参数量小、工程友好，能捕捉同类别/品牌/价格段等高阶关系。

  - 引入类别辅助pairwise loss：利用商品类别构造“相关点击 > 非相关点击 > 相关曝光 > 非相关曝光”的偏序，不用额外数据就能强化相关性排序，适合电商商品/广告场景。

  - 意图预测辅助任务：用页面级类别与trigger是否一致作为label，训练时辅助监督，线上不引入额外特征和延迟；同时用预测意图分和cosine相似度做显式门控融合，可解释且便于调试。

  - 工程上该模型额外增加2ms推理延迟，训练时间增加约7分钟，适合低延迟承接页；在线统计显示同类+相关类占比大幅提升但保留约11%不同类，可作为相关性/个性化平衡的参考阈值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
传统推荐模型忽视trigger item携带的强即时兴趣；在触发式推荐（TIR）场景中，用户点击首页商品进入承接页，目标商品与trigger的相关性对CTR影响很大。论文通过统计发现同类别trigger-target的CTR显著更高，但现有方法如DIN、DIHN、DIAN等未充分显式建模trigger-target相关性与即时/个性化兴趣的融合。

**方法关键点**
- **Trigger-Target Interaction层**：对trigger和target做element-wise乘法，再基于coaction特征（同类别/品牌/价格段）通过双层门控自适应调整，得到显隐式交互特征。
- **Cascading Interest Fusion模块**：先用MLP预测trigger intention概率（页面级类别相同为标签，辅助loss）；再用级联多头注意力，先target-query对历史行为序列得到个性化兴趣，再trigger-query对target attention输出得到trigger相关兴趣；最终用预测意图和余弦相似度加权融合：`V_fuse = y_int*s(E_t,E_i)*V_tri + (1-y_int)*(1-s)*V_tar`。
- **Category-assisted Pairwise Loss**：构造四层偏序（相关点击 > 非相关点击 > 相关曝光 > 非相关曝光），显式优化trigger-target相关性。

**关键结果**
工业数据集（约4.5亿样本）AUC 0.6752，比DIN+TRA提升+6.31% RelaImpr；公开Alimama数据集AUC 0.6448，+7.18%。消融显示三个模块分别贡献+0.54%、+0.78%、+0.43%。在线A/B：IPV +5.75%，PV +3.25%，CTR +3.87%；推理延迟仅多2ms。线上同类/相关类占比从47.67%提升到88.76%，不同类从52.33%降到11.24%。

最值得记住的一句话：在TIR场景中，显式建模trigger-target交互和类别相关性，并用预测意图+相似度动态融合即时/个性化兴趣，是提升CTR和沉浸体验的关键。
