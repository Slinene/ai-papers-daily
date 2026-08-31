---
title: 'Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative
  Engine Optimization'
title_zh: 竞争感知的生成式引擎优化：组合策略选择
authors:
- Vaibhav Sourirajan
- Yao Zhang
- Himanshu Kumar
- Sahil Wadhwa
- Mann Patel
- Amirfarrokh Iranitalab
affiliations:
- Capital One, AI Foundations
arxiv_id: '2608.27631'
url: https://arxiv.org/abs/2608.27631
pdf_url: https://arxiv.org/pdf/2608.27631
published: '2026-08-27'
collected: '2026-08-31'
category: Other
direction: 生成式引擎优化 · 竞争感知组合策略选择
tags:
- GEO
- BOCS
- DPO
- Competitor-Aware
- Content Optimization
- LLM Fine-tuning
one_liner: 用BOCS搜索竞争感知改写策略组合，再经DPO蒸馏为selector，在GEO基准上大幅超越agentic方法并抗竞争饱和
practical_value: '- 在电商产品详情页/广告文案优化中，不要只优化单品内容，要把同query下竞品内容一起输入模型，让策略模型做「相对优化」；生成式搜索/推荐场景中，竞争饱和会显著侵蚀固定策略收益，条件于竞争语料可以减缓衰减。

  - 两阶段「离线搜索+在线蒸馏」范式可直接复用：用BOCS等组合黑盒优化在离线环境搜索最优策略组合，再用SFT+DPO将黑盒观测蒸馏成轻量selector LLM，部署时仅需一次推理，避免在线运行昂贵的Bayesian
  optimization。

  - 构造DPO偏好对时，先用Welch''s t-test过滤统计不显著的观测，再选Hamming距离最小的hard negative，使模型学会区分相似策略组合之间的细微性能差异，比随机偏好对更高效。

  - 推理轨迹蒸馏时，给teacher提供特权评分卡但强制其从可观测内容特征推理，然后把内容条件化推理教给学生；上线前要做泄露审计，并注意改写可能带来faithfulness/attribution下降，建议加入检索与事实性约束。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
传统生成式引擎优化（GEO）在真空中优化单个文档，忽略其他文档也采用同样策略时的竞争外部性。随着采用率α上升，固定策略收益下降甚至低于未优化基线。于是作者将GEO形式化为竞争感知的组合策略选择问题：给定query、目标文档和竞争语料，选择最大化其生成式响应中可见度的改写策略组合。

## 方法关键点
- 构建geo-benchcomp：在geo-bench上模拟竞争对手改写，混合三种竞争者类型（随机组合、最强单策略Quotation Addition、AutoGEO全量），按采用率α∈{0,0.2,0.4,0.6,0.8}重写周围文档。
- 第一阶段用BOCS搜索15个二元改写策略的2^15=32768组合空间，采用二阶多项式代理模型、horseshoe先验、Gibbs采样和模拟退火获取函数，每次评估重写一次+5次生成引擎评估PAWC均值/标准误。
- 第二阶段硬负样本挖掘：从BOCS观测中选统计显著优于基线的最佳组合作为chosen，再在显著劣于它的候选中选Hamming距离最小的作为rejected，构造DPO偏好对。
- Teacher model（gemma-4-31b-it）根据privileged scorecard（top-10 BOCS评分）生成post-hoc reasoning traces，但禁止泄漏分数；再对gemma-4-E2B-it LoRA进行SFT+DPO（length-normalized loss），selector仅看query、全文当和策略菜单，不看α或BOCS分数。

## 关键实验
- geo-bench上PAWC 32.62（gpt-oss-120b）和29.55（Llama-3.3-70B），比最强AgenticGEO分别提升+4.67和+2.75，恢复Oracle BOCS上限39.00的84%。
- geo-benchcomp上平均PAWC 29.93，比AgenticGEO（25.20）高18%以上；随α从0→0.8，方法仅下降11.4%，单策略baseline在α=0.8时低于未优化基线。
- 零样本迁移到E-Commerce和Researchy-GEO分别取得37.78和33.48 PAWC，比最强baseline高>8%。
- 消融显示scorecard-grounded reasoning traces是DPO有效性的关键，去掉后SFT+DPO仅约27；但存在faithfulness/attribution tradeoff。

## 最值得记住的一句话
竞争感知的GEO不是追求绝对最优改写，而是从完整竞争语料中推断相对优势并选择策略组合，因而对采用率饱和更鲁棒。
