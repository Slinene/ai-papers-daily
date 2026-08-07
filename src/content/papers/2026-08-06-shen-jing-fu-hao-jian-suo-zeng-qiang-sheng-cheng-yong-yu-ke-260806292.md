---
title: 'NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering'
title_zh: 神经符号检索增强生成用于可解释问答
authors:
- Jonas Gann
- Michael Gertz
affiliations:
- Data Science Group, Heidelberg University, Germany
arxiv_id: '2608.06292'
url: https://arxiv.org/abs/2608.06292
pdf_url: https://arxiv.org/pdf/2608.06292
published: '2026-08-06'
collected: '2026-08-07'
category: RAG
direction: 神经符号RAG · 可解释推理
tags:
- Neurosymbolic
- RAG
- Explainable QA
- Prolog
- Knowledge Gap Detection
one_liner: 将检索文本块合成为可归因的Prolog模块并引入知识缺口检测，实现透明可溯源的RAG推理
practical_value: '- 在对话式推荐或客服Agent中，可将检索到的商品知识/政策文本转化为Prolog谓词，实现决策步骤的可追溯和确定性验证，提升用户信任。

  - 知识缺口检测机制可移植到个性化推荐：当用户上下文不完整时（如未提供偏好尺寸、预算），系统主动追问，改善冷启动和动态探索。

  - 利用LLM从非结构化语料（商品描述、活动规则）自动抽取结构化规则（布尔断言），与推荐引擎结合，构建可解释的过滤/排序逻辑。

  - 在Agent关键推理节点，嵌入神经符号混合策略：用LLM完成灵活的语言理解，用符号执行保障逻辑一致性，平衡泛化与可靠性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有RAG推理不透明，中间步骤难以验证，无法可靠归因到证据，且缺少对不完整用户上下文的系统检测，导致回答错误或不全。亟需一种可解释、可溯源的RAG推理框架。

**方法**：提出NeSy-RAG，一种模块化神经符号框架。对每个检索到的文本块，LLM生成语义上有意义的Prolog谓词，编码为可依赖用户事实的布尔声明。通过联合自然语言-代码嵌入检索相关谓词，组合成Prolog查询。为弥补用户上下文缺失，设计符号化知识缺口检测：自动识别影响查询结果的缺失用户事实，并触发追问交互。执行Prolog查询得到确定性答案，并附带透明执行轨迹，关联每步推理与原始文本。

**结果**：在ShARC多轮推理问答基准上，未使用领域训练，NeSy-RAG准确率达61.1%，远超同一LLM的RAG基线（42.8%），验证了符号执行在透明性与准确性上的增益。
