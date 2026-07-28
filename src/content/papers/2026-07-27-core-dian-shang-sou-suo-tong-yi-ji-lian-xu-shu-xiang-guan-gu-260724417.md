---
title: 'CORE: A Unified Cascaded Ordinal Relevance Estimation Framework for E-commerce
  Search'
title_zh: CORE：电商搜索统一级联序数相关性评估框架
authors:
- Zhi Jin
- Xi Wang
- Yunfei Li
- Guojun Liu
- Qingsong Hua
- Wei Lin
affiliations:
- Meituan
- Beijing Institute of Technology
arxiv_id: '2607.24417'
url: https://arxiv.org/abs/2607.24417
pdf_url: https://arxiv.org/pdf/2607.24417
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 序数感知的搜索相关性评估
tags:
- cascaded binary classification
- step-level GRPO
- relevance estimation
- e-commerce search
- LLM reasoning
- knowledge distillation
one_liner: 将多级相关性预测重构为题序二分类级联，用步级GRPO优化LLM推理并蒸馏至BERT，线上坏例率降低15.94%
practical_value: '- **级联二分类适配序数标签**：电商搜索相关性有自然顺序，高相关必须精准、低相关允许模糊，改为级联二分类可避免平坦多分类的代价不敏感，在线模型用双头BERT即可实现，计算量零增加。

  - **结构化推理+步级GRPO**：为LLM设计“意图分析→高/非高→中/低”的推理步骤，各步有独立二分类奖励，归一化到同阶段比较，避免容易步骤主导训练。这种细粒度信用分配可迁移到其他多步决策场景（如Agent规划）。

  - **低成本移植LLM推理能力**：用PostCoT蒸馏，让LLM将答案放在前缀，从首个token提取logits，按头聚合成对齐信号，结合硬标签训练双头BERT，既利用LLM的推理优势又满足在线延迟要求。

  - **阈值校准控制线上风险**：双头设置阈值τ1、τ2可单独调整，业务可按高召回或高精度要求调优，线上实测Badcase率下降15.9%，适合电商对排序错误零容忍的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
电商搜索相关性评估本质上是有序分类：高相关要求严格匹配用户意图，中、低相关边界更模糊且错判代价不对称。但主流做法将其视为平坦多分类，忽视序数结构，导致次优目标。本文提出级联二分类框架，将多级判断分解为顺序决策，先判高相关，若否再判中/低，更贴合业务逻辑。

**方法关键点**  
- **级联架构**：Step1 意图与实体分析；Step2 高相关vs.非高相关，是则终止；Step3 中相关vs.低相关。每一步有独立可验证的二分类标签。  
- **LLM步级GRPO**：按步骤分组奖励，独立归一化，令牌级广播优势，实现细粒度信用分配。仅对激活步骤计算梯度，跳过步骤不产生信号。  
- **BERT双头级联**：共享编码器，两个二分类头顺序执行，无额外推理开销。采用PostCoT方式蒸馏LLM：LLM生成标签在前的推理，从首token取logits，按头聚合后与BERT双头输出做KL散度对齐，结合硬标签训练。  
- **蒸馏公式**：对于头1，将LLM的非高logits用log-sum-exp合并为单个得分，与高logits构成二分类目标；头2直接取低、中logits。同时保留BCE损失。

**关键结果**  
- 离线人工标注9万样本，Cascaded-StepGRPO准确率0.7648，比Direct-GRPO高1.7个百分点；Cascaded-BERT-Distilled准确率0.7622，比Direct-BERT高1.81个百分点。  
- 级联结构在BERT和LLM上一致提升，蒸馏带来额外增益。步级GRPO比标准GRPO收敛更稳，两步决策错误均减少。  
- 线上A/B：Cascaded-BERT使NDCG@5提升0.20%，Badcase@5相对降低15.94%，表明序数建模有效抑制将低相关项排至高位。

**核心洞见**：显式建模序数关系并通过级联二分类与步级奖励对齐，是提升搜索相关性并减少线上恶劣排序的关键套路。
