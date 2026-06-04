---
title: Fast & Faithful Function Vectors
title_zh: 快速且忠实的函数向量
authors:
- Minh An Pham
- Anton Segeler
- Thomas Wiegand
- Wojciech Samek
- Sebastian Lapuschkin
- Patrick Kahardipraja
- Reduan Achtibat
affiliations:
- Fraunhofer Heinrich-Hertz-Institute, Berlin, Germany
- Technische Universität Berlin, Berlin, Germany
- BIFOLD – Berlin Institute for the Foundations of Learning and Data, Berlin, Germany
- Technological University Dublin, Dublin, Ireland
arxiv_id: '2606.05079'
url: https://arxiv.org/abs/2606.05079
pdf_url: https://arxiv.org/pdf/2606.05079
published: '2026-06-03'
collected: '2026-06-04'
category: LLM
direction: LLM可解释性 · Function Vectors
tags:
- function vectors
- LRP
- attention heads
- in-context learning
- steering
- LLM control
one_liner: 引入LRP归因与分布式引导，提升函数向量在LLM中的任务控制效率与准确率
practical_value: '- **用LRP定位任务关键注意力头**：可直接迁移到LLM推理优化中，通过LRP归因剪枝无关头，降低电商问答、文案生成场景的推理延迟。

  - **分布式引导提升控制精度**：在控制LLM生成时，将引导向量插入多层多头比仅在一层注入更有效，可改善商品详情生成的事实一致性和风格控制。

  - **加速Function Vectors提取**：LRP仅需少量样本即可识别有效头，大幅减少ICL示例数，适合电商中需频繁更新prompt的动态场景（如大促自动卖点生成）。

  - **分析ICL任务表示的工具**：方法可推广用于诊断LLM在推荐解释生成、用户意图分类中的任务编码方式，辅助Prompt工程与示例选择。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Function Vectors (FVs) 被认为是LLM在上下文学习（ICL）中形成的任务表示，可用于引导模型输出，但其定义中的注意力头选择与引导方式缺少系统比较。

**方法关键点**：
- 将FVs提取分解为两步：注意力头筛选、任务向量构建与引导应用。
- 头选择对比了基于注意力值的AIE方法与基于梯度传播的相关性归因（LRP），后者能直接评估每个头对任务输出的贡献。
- 引导方式对比了标准FV（所有样本向量平均后一次性注入）与分布式FV（DFV）：先按头计算向量，再在多个层多头分别注入。

**关键结果**：
- 在Llama-3.2-3B上，LRP选出的头数仅为AIE的1/5~1/2，但最终控制准确率更高（最高提升约8个百分点）。
- DFV比单层聚合FV平均准确率提升3-5%，且对超参数不敏感。
- 组合LRP头选择+DFV引导，在保持高准确率（>0.85）的同时，吞吐量可达100+ samples/min，显著优于基准。
