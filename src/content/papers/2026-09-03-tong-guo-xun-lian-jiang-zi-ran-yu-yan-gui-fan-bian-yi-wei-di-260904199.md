---
title: 'Compile by Training: Turning Natural-Language Specifications into Local Neural
  Functions'
title_zh: 通过训练将自然语言规范编译为本地神经函数
authors:
- Yuntian Deng
- Pengyu Nie
- Stuart Shieber
affiliations:
- University of Waterloo
- Harvard University
arxiv_id: '2609.04199'
url: https://arxiv.org/abs/2609.04199
pdf_url: https://arxiv.org/pdf/2609.04199
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: 自然语言规范编译为本地神经函数
tags:
- LLM
- knowledge distillation
- program synthesis
- adapter
- neural function
one_liner: 通过教师模型生成示例并训练小适配器，将自然语言规范编译为可本地运行、可组合的神经函数
practical_value: '- 在搜索/推荐/广告的高频文本规则场景（如 query 意图分诊、广告文案合规、商品标题清洗），可把 LLM 编译成轻量本地函数，替代每次远程调用；尤其适合高
  QPS 或低延迟要求的在线链路，能显著降低 token 成本和尾延迟。

  - 将自然语言规则视为可编译的"源"，用教师模型生成标注样本并训练小 adapter，使规则以模型权重形式版本化、可组合、可回滚；这比直接维护 prompt 或外部
  LLM 调用更可控，也便于嵌入 ML pipeline 和 Agent 工具链。

  - 编译时间约 1 分钟，准确率 83.6% 且语义匹配容错，适合作为模糊规则引擎的中间层；对关键业务可结合规则兜底或人工校验边界，避免在硬约束场景直接依赖。

  - 该思路可推广到电商 Agent：把多个子任务自然语言描述分别编译成小函数，供 Agent 按需调用，减少对单一远程大模型的依赖，提升响应稳定性和可审计性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：许多高频文本函数（如邮件分诊、意图分类、文本清洗）容易用自然语言描述，但难以用规则编码；每次输入都调用远程大模型会带来重复成本、网络延迟和对服务商的依赖。

方法关键点：在编译阶段，由教师模型根据自然语言规范生成任务特定示例，再通过梯度下降训练一个运行于 compact interpreter 上的小型 adapter。编译得到的神经函数不依赖教师模型，可像普通软件一样存储、版本化、组合；大模型仅在编译期充当数据/规则生成器，而非运行时依赖。

关键结果：在 FuzzyBench-Hard 子集上，此前 Program-as-Weights fast compiler 完全无法给出精确匹配，该方法达到 83.6% 语义准确率；代价是编译时间从秒级升至约一分钟。系统已在公开交互服务中部署，并演示了多站点网站助手、语言控制 3D avatar 和双向 English-Claudish 翻译器。
