---
title: 'All Explanations are Wrong, But Many Are Useful: Exploring the Rashomon Explanation
  Set with Large Language Models'
title_zh: 多数解释是一组正确解释的集合——用 LLM 代理工作流探索 Rashomon 解释集
authors:
- Pan Li
affiliations:
- Scheller College of Business, Georgia Tech
arxiv_id: '2607.09502'
url: https://arxiv.org/abs/2607.09502
pdf_url: https://arxiv.org/pdf/2607.09502
published: '2026-07-10'
collected: '2026-07-13'
category: LLM
direction: LLM 代理生成解释 · Rashomon 解释集
tags:
- Rashomon Explanation
- LLM Agents
- Interpretable ML
- CTR Prediction
- Double-loop Learning
- Sensemaking
one_liner: 将解释与预测耦合，通过 LLM 代理的“解释-预测-反思”循环生成多个忠实且有用的解释，在提升可解释性的同时提高了预测精度。
practical_value: '- **生成解释集合而非单一解释**：在电商推荐中，单一解释（如 SHAP 值）在分布偏移下容易失效，可以借鉴本工作的思路，对同一个物品/用户生成多组不同的解释（通过调整
  prompt、特征子集采样），再用多数投票或语义聚合得到更稳健的解释，提升推荐理由的鲁棒性。

  - **解释-预测-反思迭代循环**：将解释生成与预测任务耦合，让解释 agent 根据预测误差自动修正解释内容（double-loop learning）。在广告
  CTR 预估或搜索排序中，可仿照这个结构：一个 LLM 代理生成影响点击的因素解释，另一个代理基于解释做预测，反思代理根据错误修正解释——这种自改进循环可同步提升解释质量和模型效果。

  - **将自然语言解释作为预测的输入特征**：实验证实向预测模型提供高质量解释（即使是带噪声的解释）能显著降低误差。在推荐系统中，可以尝试将 LLM 生成的用户行为解释（如“用户在午后对低价商品点击率高”）作为特征加入深度模型或
  LLM 预测器中，可能带来增益。

  - **批处理 LLM 学习机制**：针对大规模日志，通过数据分 batch 和设置哨兵行（data monitor）来防止长上下文退化，这为在十亿级推荐曝光日志上用
  LLM 做解释和预测提供了工程参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有可解释 AI（XAI）方法普遍面临准确度与可解释性之间的权衡，根源在于将解释和预测视为两个分离的目标。作者从组织理论（sensemaking、double-loop learning、互补性理论）出发，指出单一解释在分布偏移下必然失效，标量形式的归因（如 SHAP）无法刻画条件或非线性关系，且解释与预测过程脱节。因此，需要转向生成一组忠实的、能引导预测的解释（Rashomon Explanation），使模型在解释自身的同时提升预测性能。  

**方法关键点**  
- 提出 **RashomonLLM**：一个 LLM 代理工作流，包含解释代理、预测代理和反思代理，三者通过“解释→预测→反思→更新解释”的循环进行迭代优化。  
- **解释代理** 利用特征 dropout（随机屏蔽 20% 特征）和多样化初始 prompt 生成多个不同视角的解释，每个解释捕捉不同的特征交互模式。  
- **预测代理** 基于当前解释直接输出预测结果。  
- **反思代理** 分析预测错误案例，修改解释 prompt 以修正错误模式，实现 double-loop 学习。  
- **聚合模块** 通过多数投票从解释集合中抽取共识解释（支持度 > 50% 的命题保留）。  
- 扩展 **Batch LLM Learning** 机制，将数据分批次输入 LLM 并设置哨兵行监控上下文质量，支持大规模工业数据。  

**关键实验与结果**  
在三个任务上验证：银行客户流失分类（Kaggle）、临床生存回归（HCT Survival）和快手直播平台的大规模 CTR 预测（来自真实曝光日志）。  
- 在 CTR 预测任务上，RashomonLLM **显著超越** 多个强深度 CTR 模型（如 DCN-V2、DeepFM 等），并在解释质量上（与 SHAP、LIME 等相比）取得最佳。  
- 消融实验表明，预测增益由解释忠实度驱动，而非单纯加入额外信息；即使向解释注入 10% 噪声，LLM 预测误差仍远低于无解释的情况。  
- 稳健性测试显示，在时间分割和数据分布偏移下，RashomonLLM 的优势依然保持。  

**核心启示**  
当解释与预测耦合时，解释和预测成为互补品——教会模型解释自己，不会牺牲准确性，反而能提升准确性。
