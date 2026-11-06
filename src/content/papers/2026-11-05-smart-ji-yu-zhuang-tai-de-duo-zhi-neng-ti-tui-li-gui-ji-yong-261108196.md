---
title: 'SMART: State-based Multi Agent Reasoning Traces for Verification-oriented
  Problem-Solving'
title_zh: SMART：基于状态的多智能体推理轨迹用于验证导向问题求解
authors:
- Sai Vallurupalli
- Francis Ferraro
affiliations:
- University of Maryland Baltimore County
arxiv_id: '2611.08196'
url: https://arxiv.org/abs/2611.08196
pdf_url: https://arxiv.org/pdf/2611.08196
published: '2026-11-05'
collected: '2026-11-06'
category: MultiAgent
direction: 多 Agent 状态推理与知识验证
tags:
- MultiAgent
- LLM
- Knowledge Grounding
- Scientific Claim Verification
- State Reasoning
one_liner: 提出多智能体框架 SMART，用角色化提示捕获实体状态并筛选互补前提，提升科学声明验证准确率最高20%。
practical_value: '- 角色化多智能体拆分实体状态，适合电商商品属性/卖点一致性校验、广告合规审核：让不同 agent 分别检查价格、功效、资质等维度，生成互补前提后再做最终判断。

  - 显式接入真实世界知识/领域知识库（商品知识图谱、平台规则库）能提升推理可信度，避免 LLM 仅凭参数知识误判；在文案生成、政策审核前先检索再推理。

  - 把推理中间产物（premises）作为可验证轨迹留存，便于排查错误和迭代 prompt；在业务 Agent 中可形成证据链，支持审核与人工复核。

  - 多 LLM 分工互补可能优于单模型自洽推理，但成本高；建议对高风险 case 使用多智能体交叉验证，普通场景用单模型快速推理。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：复杂问题如科学声明验证往往上下文有限，需要额外知识；LLM 虽预训练知识丰富，但推理时难以充分调用。  
**方法关键点**：SMART 多智能体框架通过结构化角色提示，捕获问题中参与实体的隐式状态，生成多样、互补且与求解高度相关的前提；使用多个 LLM 产出并筛选，再用经过真实世界知识验证的前提做知识引导推理。  
**关键结果数字**：在 3 个科学声明数据集上，验证性能最高提升 20%；将前提接地到真实世界知识可再提升最高 5%，表明外部知识接入对推理是必要的。
