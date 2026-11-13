---
title: Human or Synthetic? What a Fixed Budget Buys for Post-Training
title_zh: 人类还是合成数据？固定预算对LLM后训练的影响
authors:
- Shourik Banerjee
- Ethan Mendes
- Mohit Raghavendra
- Wei Xu
- Alan Ritter
affiliations:
- Georgia Institute of Technology
arxiv_id: '2611.16895'
url: https://arxiv.org/abs/2611.16895
pdf_url: https://arxiv.org/pdf/2611.16895
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: LLM 后训练 · 数据成本效益
tags:
- LLM post-training
- synthetic data
- human preference data
- DPO
- cost-efficiency
- annotation budget
one_liner: 在相同美元预算下比较人类与合成偏好数据的后训练效果，发现合成数据在低预算下成本效益远高于人类数据
practical_value: '- **预算分配策略**：在LLM后训练（如对话式推荐、生成式推荐理由的偏好对齐）中，预算有限时优先使用合成偏好数据做DPO，可先用$200–$400级别预算快速获得较高胜率，再根据业务需求评估是否追加人类标注。

  - **人类标注源选择**：不同人类标注平台/团队可靠性差异可能很大，即使经过领域限制和去重仍无法消除，业务方应建立标注质量评估机制，不要默认高价人类标注一定更好。

  - **数据配比思路**：可以采用「合成数据打底 + 少量高质量人类数据校准」的策略，尤其适合需要快速迭代的电商推荐场景，避免把所有预算都投入昂贵的人类标注。

  - **对推荐系统Agent的启示**：如果涉及用LLM模拟用户偏好或评估推荐结果，需注意合成偏好标签在摘要类任务上已全面超过人类数据，可以放心扩大使用范围。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
LLM 后训练通常结合 SFT 和 DPO，人类标注与合成偏好数据在单样本成本上差异很大，但此前研究在比较两者时固定样本数量，忽略了成本因素。

## 方法关键点
在固定的美元预算下，分别用人类标注和 LLM 合成偏好数据进行 DPO 后训练，覆盖 helpfulness 和 summarization 任务，训练多个 base model 家族。预算从低到高逐步变化，评估成本与性能的权衡。

## 关键结果数字
- 合成数据在低到中等预算下成本效益极高：仅 $200–$400 即可取得高胜率。
- 在 helpfulness 上，人类数据需要大约两个数量级更大的预算才能追平合成数据。
- 在 summarization 上，任何测试预算下人类数据均未追平。
- 不同人类标注源可靠性差异显著：一个广泛使用的源显著低于另一个，且标准处理（领域限制、去重）后差距仍存在。
