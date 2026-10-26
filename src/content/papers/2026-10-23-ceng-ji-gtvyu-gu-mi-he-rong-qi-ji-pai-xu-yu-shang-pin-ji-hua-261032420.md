---
title: 'Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking
  and Item-Level Conversion'
title_zh: 层级GTV预估：弥合容器级排序与商品级转化差距
authors:
- Zerong Lan
- Fan Zhang
- Chuang Chen
- Tianchun Huang
- Teng Zhang
- Xingxing Wang
affiliations:
- Meituan
arxiv_id: '2610.32420'
url: https://arxiv.org/abs/2610.32420
pdf_url: https://arxiv.org/pdf/2610.32420
published: '2026-10-23'
collected: '2026-10-26'
category: RecSys
direction: 层级 GTV 预估 · 集合感知多任务
tags:
- GTV Estimation
- Sponsored Search
- Set-Aware Encoder
- Multi-Task Learning
- O2O Advertising
- Residual Ensemble
one_liner: HGE 用 HSAE、PLL、RCEF 解决容器级 GTV 预估的高方差、稀疏与粒度错配，离线 XAUC +0.63pp，在线 RPS +1.42%
practical_value: '- 容器级排序场景（店铺卡片、直播间、品牌专区）可将 GTV 按「转化概率 × 商品购买概率 × 购买数量 × 价格」分解，用
  Proxy-Label Learning 降低标签方差，适合直接迁移到 O2O 广告/电商容器预估。

  - 商品集合动态变化时，用 Transformer 对 top-K 商品序列做 self-attention，并在 attention 后拼接 user/POI/query
  上下文，先建模商品间竞争再注入个性化，比 mean pooling 效果好，可复用到店铺内商品 List 的泛化建模。

  - 工程上采用残差塔修正 top-K 外订单偏差 + 通用回归塔兜底，并用可学习 gate 融合；这种「细粒度聚合 + 粗粒度回归」的双路结构能稳定处理商品级转化稀疏，适合冷启动/长尾容器。

  - 多任务 loss 权重较小（item 级 CVR/qty 仅 0.03）仍带来明显提升；在转化稀疏场景可沿用 BCE 分类 + Huber 回归组合，并用
  PCOC 监控校准。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
O2O 与直播电商平台以容器（门店、直播间）作为排序单元，但真实交易发生在商品级。直接对容器 GTV 做回归存在三个问题：容器级标签方差高、商品级转化极度稀疏、商品组合动态异质。需要同时建模容器内商品集合与用户意图，稳定预估期望 GTV。

**方法关键点**
- **HSAE**：对 top-K 商品 embedding 加位置编码后过单层 Transformer；MHSA 输出与 user/POI/query/context 拼接再进 FFN，先学商品间竞争，再注入上下文调制。
- **PLL**：将 GTV 分解为容器级转化概率 × Σ(商品级购买概率 × 购买数量 × 价格)。三个预测头：POI-level CVR、Item-level CVR、Item-level quantity；用 BCE + Softplus，将高方差回归拆成多个低方差子任务。
- **RCEF**：残差塔修正 top-K 外订单偏差；通用回归塔（DIN+DCN）与 PLL 输出经可学习 gate 融合，缓解商品级稀疏。
- 训练采用多任务损失：Huber 回归 + BCE，权重 λ1=0.3，λ2=λ3=0.03。

**关键实验**
在美团广告系统 712M 样本上做 OOT 切分。HGE 离线 XAUC 0.8158、PCOC 0.9858、MAE 4.9915，优于 WLR、DLRM、RankMixer、CREAD；消融显示去掉 PLL 后 XAUC 大跌至 0.7873。在线 13 天 A/B 测试 RPS 提升 +1.42%（95% CI [+0.80%, +2.05%]），已全量部署。

最值得记住的一句话：**把高方差 GTV 分解为多个低方差子任务，配合集合感知编码与回归兜底融合，是提升容器级排序价值的有效范式。**
