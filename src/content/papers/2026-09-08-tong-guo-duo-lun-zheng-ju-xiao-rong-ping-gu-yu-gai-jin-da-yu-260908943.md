---
title: Evaluating and Improving Evidence-Grounded Fact-Checking in LLMs via Multi-Round
  Evidence Ablation
title_zh: 通过多轮证据消融评估与改进大语言模型事实核查的证据依据性
authors:
- Xingyu Deng
- Mingzi Cao
- Nikolaos Aletras
- Xi Wang
- Mark Stevenson
affiliations:
- University of Sheffield
arxiv_id: '2609.08943'
url: https://arxiv.org/abs/2609.08943
pdf_url: https://arxiv.org/pdf/2609.08943
published: '2026-09-08'
collected: '2026-09-11'
category: RAG
direction: RAG 事实核查 · 证据依赖性评估与训练
tags:
- Fact-Checking
- Evidence Grounding
- RAG
- LLM-as-Verifier
- Counterfactual Training
- Evaluation
one_liner: 提出 FAE 多轮证据消融评估与 REAL 反事实训练，揭示 LLM 更依赖参数知识并提升证据依赖性
practical_value: '- 在商品/广告审核、评价真实性验证等 LLM-as-verifier 场景，可用 FAE 式多轮证据消融做上线前审计：逐条移除或替换
  cited evidence，观察模型预测是否翻转，识别“参数记忆强于上下文”的风险。

  - REAL 的反事实证据训练可直接迁移：不只使用完整证据+标签，也构造删除支撑证据、替换为不相关或相反证据的样本，强制模型在证据缺失时改变判断，增强系统对检索质量的敏感性。

  - 把“证据依赖度”作为与准确率并行的评测指标，特别适用于广告合规、商品属性校验等高风险任务，避免高准确率但弱 grounding 的 LLM 上线。

  - 若在用 LLM 生成推荐理由或搜索解释，可借鉴多轮 evidence ablation 验证解释是否真实来自用户历史/商品信息，而非模型通用说辞。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 做事实核查准确率高，但可能主要依赖参数知识而非提供的证据，导致 evidence grounding 不足。

**方法**：提出 FAE，对 cited evidence 做多轮消融，观察 LLM 是否随证据移除而修正预测；进一步提出 REAL，通过反事实证据监督（构造删除/替换支撑证据的样本）训练 LLM-as-verifier，使其更依赖证据。

**结果**：现有 off-the-shelf LLM 更依赖参数知识；在四个不同领域事实核查数据集上，REAL 训练的模型比标准微调具有更强的证据依赖能力，准确率与证据使用更一致。结果说明高准确率可与弱证据依赖并存，REAL 能缓解该问题。
