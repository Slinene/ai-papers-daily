---
title: 'D2C-Routing: Dimension-to-Composition Evidence Routing for Mixed-Origin AI-Generated
  Text Detection'
title_zh: 混合来源AI文本检测的维度到组合证据路由
authors:
- Xin Chen
- Fuwei Zhang
- Yiqi Tong
- Wei Guo
- Yutian Xiao
- Fuzhen Zhuang
affiliations:
- Institute of Artificial Intelligence, Beihang University
arxiv_id: '2608.27380'
url: https://arxiv.org/abs/2608.27380
pdf_url: https://arxiv.org/pdf/2608.27380
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 混合来源AI文本检测 · 证据路由
tags:
- AI-generated text detection
- mixed-origin text
- content-expression routing
- gated composition
- HART benchmark
one_liner: 提出D2C-Routing，将内容与表达来源分维度路由再门控组合，显著提升混合AI文本检测
practical_value: '- 维度解耦思想可直接迁移到UGC审核/商品评论真实性判断：将“内容来源”与“表达来源”拆成两个监督头，再组合成四类标签（HH/HA/AH/AA），比单一AI二分类更适合人工分层审核与申诉流程。

  - 门控组合层代替简单 concat：业务中有多维度文本特征需要融合时，可借鉴 learned gated composition，让模型自适应加权不同维度证据，比固定拼接更容易适配不同混合比例场景。

  - 评估指标使用 TPR@1%FPR 这类低假阳率阈值，比 Accuracy 更适合线上风控：电商/广告中AI生成内容检测往往要求极低误杀率，可直接复用该评估口径。

  - 整体主要是文本检测学术贡献，与推荐/Agent直接相关性有限；但若业务涉及LLM生成推荐理由、商品文案的溯源与合规标记，可参考内容/表达双维度的归因标签体系。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

## 动机
当前AI生成文本检测普遍是二分类：人类写 vs. 机器写。但混合写作场景中，一个文档可能保留人类内容但用AI润色表达，或AI生成内容后由人类改写；单一标量分数无法区分哪一层来源发生了变化。

## 方法关键点
论文借用HART基准的 content-expression 标签空间，将混合来源检测重构为 **dimension-to-composition source attribution**：先分别推断 content origin 和 expression origin，再组合为四种协作类型——HH、HA、AH、AA。

提出 **D2C-Routing**：把 content-side 和 expression-side 的 evidence 分别路由到两个有监督的维度头，输出维度级表征；随后通过 learned gated composition layer 融合两个维度的证据，预测最终四分类标签。相比传统直接四分类或简单融合，路由设计让每个维度先获得明确监督信号。

## 关键结果
在基于 HART 重建的 MixD2C 数据集上，D2C-Routing 达到 **0.8603 four-way Avg TPR@1%FPR**，较同 split 的 RACE-local rerun 高 **6.5 points**。核心消融支持路由结构有效性；错误分析显示最难区分的是 AI-content/human-expression 与完全 AI 生成文本之间的边界。
