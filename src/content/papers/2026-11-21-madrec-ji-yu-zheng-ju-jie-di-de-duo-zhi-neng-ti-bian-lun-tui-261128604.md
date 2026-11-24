---
title: 'MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation'
title_zh: MADRec：基于证据接地的多智能体辩论推荐框架
authors:
- Zunlong Liu
- Weijie Feng
- Jingzhi Li
- Lei Zhu
- Zhiyong Cheng
- Meng Wang
affiliations:
- Hefei University of Technology
- Tongji University
arxiv_id: '2611.28604'
url: https://arxiv.org/abs/2611.28604
pdf_url: https://arxiv.org/pdf/2611.28604
published: '2026-11-21'
collected: '2026-11-24'
category: MultiAgent
direction: LLM 多智能体辩论推荐排序
tags:
- Multi-Agent Debate
- Evidence-Grounded Reasoning
- LLM4Rec
- Error Propagation
- Ranking Calibration
one_liner: 用交互与语义双视角多轮辩论、独立证据验证和裁判动态校准，抑制多智能体推荐中的中间错误传播
practical_value: '- 多智能体辩论适合候选集重排：在电商/广告精排阶段，让行为序列 agent 和商品内容/属性 agent 对同一批召回候选互相
  challenge 和 revise，能暴露单一信号（如交互偏好）忽略的好 item，尤其适合需要解释性的场景。

  - 证据接地是可信推理的关键：对 LLM 生成的商品卖点/推荐理由，用独立微调的轻量 verifier（如 DeBERTaV3）判断 claim 是否被 item
  详情支持，并按支持概率调权，可有效抑制 LLM 幻觉和不受支撑的语义判断，降低线上风险。

  - 裁判自适应加权融合多分支：利用辩论历史中的可靠性线索，让 judge 动态分配行为分支和语义分支权重，优于固定等权融合；多路召回/多模型排序融合时，可以借鉴轻量
  judge 或直接用分支置信度/一致性做动态加权。

  - 工程上采用“冻结召回模型 + LLM 只重排 top-N”的两阶段架构，N=30 即可获得显著提升；生产环境可将传统模型作为召回底座，LLM agent 只做精排，配合证据校验控制推理成本和输出风险。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
多智能体推荐系统让不同 specialist agent 处理交互信号、语义信号等异构偏好，但中间推理结果不可靠时会跨 agent 传播，污染后续判断和最终排序。已有 review/reflection 机制通常作用于推理后期，难以阻止早期错误对下游 agent 的影响。多智能体辩论提供过程级交叉检查机会，但单纯辩论缺乏对语义 claim 的证据支持，agent 仍可能依据无根据的内容声称修改排序。

## 方法关键点
- **两阶段检索-排序**：先用传统推荐模型（SASRec/BERT4Rec）检索 top-N 候选，再用 LLM agents 精排，控制推理成本。
- **MAD 模块**：Interaction Agent 和 Semantic Agent 对同一候选集分别从行为序列和内容语义评估，进行多轮双向辩论，每轮包含 observation→think→action，双方可挑战对方判断并修正自己的排序。
- **EG-RAR 模块**：离线构建 item 级证据库，在线生成 Claim-Evidence Table；用独立微调的 DeBERTaV3-base 做证据一致性验证（ECV），输出 claim 被证据支持的概率 γ，将语义分数调整为 eη = p × ρ × γ，抑制无证据支持的语义判断。
- **JRC 模块**：Judge Agent 基于用户历史、辩论历史和两个分支最终 Top-K 并集，生成推理 trace，输出自适应分支权重 ω_I 和 ω_S，加权融合交互偏好分与证据调整后的语义分，得到最终排序。

## 关键结果
在 ML-1M、Amazon-Beauty、Amazon-Book 三个数据集上，MADRec 显著超过 SASRec、BERT4Rec、P5、ChatRec、LLMRank、RecMind、MACF、ThinkRec、RecPO 等 baseline。默认 MADRec 相对最强非 MADRec baseline 的 Recall@10 提升分别为 14.15%、22.77%、32.79%，NDCG@10 提升 10.31%、13.26%、23.19%。消融显示，去掉 EG-RAR、ECV、Debate 或 Judge 均导致性能下降；同 LLM 调用预算下，MADRec 优于 self-refinement 和 one-way interaction。中间排序错误注入实验中，MADRec 的 Transfer 14.7%、Correction 87.9%、Persistence 1.8%，远优于 MACRec、MACF、Self-refinement、One-way interaction。Judge 权重分析显示，91.4% 的用户中被赋更高权重的分支正是 NDCG@10 更高的分支，Spearman 相关 0.89。
