---
title: 'ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and
  Dynamic Self-Feedback'
title_zh: ToolLoop：基于分解生成与动态自反馈的闭环工具使用数据合成
authors:
- Min Zeng
- Yuzhou Liu
- Zhenyu Cao
- Hanxiu Chen
- Heng Li
- Caiquan Liu
- Yafei Wen
- Xiaoxin Chen
affiliations:
- vivo AI Lab
arxiv_id: '2609.09072'
url: https://arxiv.org/abs/2609.09072
pdf_url: https://arxiv.org/pdf/2609.09072
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: 工具调用数据合成 · 闭环自反馈
tags:
- tool-use
- synthetic data
- self-feedback
- function calling
- LLM
- data synthesis
one_liner: 用分解生成与阶段自反馈替代一次性生成过滤，11K数据训练4B模型在BFCL达86.40%
practical_value: '- 电商/推荐系统若需训练Agent调用商品搜索、订单查询、优惠券服务等API，可借鉴ToolLoop三阶段分解：先选函数组合作为ground
  truth，再反向生成用户query，最后正向生成tool call，确保用户意图与工具调用严格对齐，避免生成噪音。

  - 动态自反馈比静态过滤更高效：在合成训练数据时，用LLM验证器+规则+AST解析发现错误后，将具体问题反馈给生成模型进行修正（最多3次），而不是直接丢弃，能保留困难样本、改善数据分布多样性，适用于query改写、搜索suggestion等数据合成。

  - 候选函数构建采用embedding+K-means聚类+LLM采样，可迁移到电商API管理：将海量商品/订单等API按语义聚类，从每个簇采样构建候选集，既避免上下文过长，又保证候选API语义相关，提升筛选效率和训练效果。

  - 移除与测试集重叠的函数后模型性能几乎不下降（86.40 vs 86.07），说明合成数据的价值在于构造过程的内部一致性而非记忆特定schema；业务中应关注数据生成流程的合理性，而非盲目扩大数据量或依赖特定API覆盖。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
训练LLM有效调用外部工具需要高质量工具使用数据，但现有合成方法多采用generate-then-filter，一次性生成完整样本后静态过滤，导致数据分布偏差、样本效率低，且缺乏中间监督，容易产生query与tool call不一致等系统性错误。

## 方法关键点
ToolLoop将合成分解为三个阶段：
- **Ground Truth采样**：先确定要调用的函数名组合（并行场景用LLM选择，非并行随机采样），作为后续生成的目标。
- **反向推导用户query**：给定函数组合，生成自然用户指令，要求与函数一一对应、参数完备、表达自然。
- **正向生成tool calls**：根据query和候选函数，生成符合OpenAI格式的工具调用，严格遵循schema。

每阶段集成**动态自反馈**：LLM语义验证 + 规则格式检查 + AST语法解析，发现错误后将具体问题反馈给生成模型，指导重生成，最多重试3次。相比静态过滤，这种generate-verify-refine机制能保留困难样本，修正中间不一致性，而非直接丢弃。

候选函数构建采用embedding+K-means聚类，将API按语义分组后再采样，避免上下文过长和随机采样不相关的问题。

## 关键实验
基于Qwen3-4B-Instruct-2507，仅用11K ToolLoop合成数据训练，在BFCL上达到86.40% overall accuracy（non-reasoning模式），超过APIGen-4B（83.11%，60K数据）和ToolMind-4B（83.53%，55K数据）。去除与BFCL重叠的候选函数后，Isolate变体仍达86.07%，说明增益不来自记忆测试函数。在ACEBench上，ToolLoop-4B取得72.1% overall，超过APIGen-4B（67.0）和ToolMind-4B（70.2），且仅用了APIGen 18.3%的训练数据。消融实验显示，无反馈版本仅79.97%，最终过滤版本82.56%，闭环反馈版本86.40%，证明迭代反馈是关键。

## 最值得记住的一句话
有效的工具使用数据应通过迭代generate-verify-refine构建，而不是一次性生成后过滤；分解生成+阶段反馈能大幅提升数据质量和模型性能，同时显著降低数据量需求。
