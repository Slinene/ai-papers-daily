---
title: Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language
  Models in Commonsense Reasoning
title_zh: 揭示大语言模型常识推理中的显著偏差：知识抑制而非缺失
authors:
- Zheng Wu
- Chenhao Xue
- Shijie Zheng
- Yijie Lu
- Cheng Yang
- Zhuosheng Zhang
affiliations:
- Shanghai Jiao Tong University
- ByteDance Inc
arxiv_id: '2607.28478'
url: https://arxiv.org/abs/2607.28478
pdf_url: https://arxiv.org/pdf/2607.28478
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: LLM常识推理中的显著偏差与知识抑制
tags:
- Salience Bias
- Commonsense Reasoning
- LLM Evaluation
- Distractor Robustness
- Knowledge Suppression
one_liner: LLM在常识推理中易被无关显式干扰项劫持，实为知识被抑制而非缺失，轻量提示即可大幅恢复。
practical_value: '- **推理时加入忽略干扰指令**：在推荐Agent或搜索任务的prompt中显式加入“忽略无关数字/显式条件，基于常识前提推理”的指引，能低成本缓解类似偏差。

  - **两步式推理设计**：先让模型剥离任务框架单独激活领域常识（知识探测），再结合具体条件进行决策，可避免关键知识被干扰项抑制，适用于商品适用性判断、场景化推荐等需常识推理的场景。

  - **干扰项隔离与测试**：在构建面向Agent的评估集时，引入无关高显著度特征（如随机用户ID、冗余时间戳），检验模型是否会错误依赖这些特征，借鉴SaliTrap的陷阱构造方式提前暴露系统脆弱性。

  - **提示工程优先于微调**：该工作表明常识推理瓶颈主要在于知识引出而非模型能力，因此优先优化提示策略（如加入“先思考隐含前提”的思维链）的ROI远高于重训模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM在推理时过度重视输入中的显式条件，导致其在日常常识推理中被无关干扰项（如无关数字）劫持，产生“显著偏差”。关键问题是这种失败源于常识知识缺失还是知识被任务框架抑制。

**方法**：构建SaliTrap基准，涵盖四类陷阱维度的高质量数据，评估12个主流LLM。通过剥离任务框架的“无上下文知识探测”对比实验，区分知识抑制与缺失。进一步探索推理时轻量提示策略的缓解效果。

**结果**：所有模型均受显著偏差影响，严重程度随干扰项密度增加而升高，且察觉陷阱与避免陷阱常解耦。孤立知识探测可恢复超90%的逢迎性失败，表明常识内在存在但被显著干扰项挤出。仅靠推理时提示（无需重训）即可大幅缩小差距，将常识推理瓶颈从模型能力重定位至知识引出。
