---
title: Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence
  in Chain-of-Thought Models
title_zh: 推理模型Token预算饱和与不收敛早期检测
authors:
- Renuka Oladri
- Niveda Jawahar
- Abdirisak Mohamed
affiliations:
- University of Maryland
arxiv_id: '2607.21433'
url: https://arxiv.org/abs/2607.21433
pdf_url: https://arxiv.org/pdf/2607.21433
published: '2026-07-23'
collected: '2026-07-25'
category: Reasoning
direction: 推理收敛早期探测与退出机制
tags:
- Chain-of-Thought
- Early Detection
- Probe
- Token Budget
- Convergence
- Reasoning
one_liner: CoT推理呈双峰收敛，内部表征可早期预测失败，为提前退出开辟路径
practical_value: '- 在LLM推理链生成中部署线性探针监测隐藏状态，当检测到高概率收敛失败时提前终止，可节省大量推理成本，适用于推荐理由生成、搜索解释等业务场景。

  - 对简单到中等复杂度任务（如商品描述优化、query意图分类解释），采用budget forcing限制思考token数至256，几乎不损失准确率，显著降低延迟。

  - 工程实现中优先使用内部激活探针而非基于输出文本熵或重复率的行为指标，前者信号更强且更早。

  - 根据问题难度或早期探针信号动态分配计算资源，使推理预算自适应，实现成本与效果的平衡。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：Chain-of-Thought推理模型推理成本高昂，思考预算与准确性的关系不清，且能否早期预测推理失败是提升效率的关键。方法：在DeepSeek-R1-Distill-Qwen-7B上，通过budget forcing限制思考token数，在GSM8K、MATH-500、AIME三个基准上测量准确率。发现GSM8K和MATH-500仅需256 tokens即达全预算准确率的95%，而AIME呈现双峰：56.5%生成自然收敛且准确率96.5%，其余即使分配10000 tokens也不收敛且准确率仅11.5%。进一步训练线性探针，扫描28层和token位置50-300，发现token 150的层20激活给出AUC 0.608，显著高于机会水平，且优于基于文本熵和重复统计的行为基线。置换检验p=0.063。结果：AIME上收敛生成准确率90.3%，非收敛仅6.6%，整体收敛率62.0%。收敛命运在生成早期即被内部表征部分编码，证实了早期检测的可能性。
