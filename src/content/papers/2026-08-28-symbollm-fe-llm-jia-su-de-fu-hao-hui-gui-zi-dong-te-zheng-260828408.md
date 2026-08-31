---
title: 'SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering
  on Tabular Data'
title_zh: SymboLLM-FE：LLM 加速的符号回归自动特征工程
authors:
- Zi-Jian Cheng
- Zi-Yi Jia
- Zhi Zhou
- Yu-Feng Li
- Lan-Zhe Guo
affiliations:
- Nanjing University
arxiv_id: '2608.28408'
url: https://arxiv.org/abs/2608.28408
pdf_url: https://arxiv.org/pdf/2608.28408
published: '2026-08-28'
collected: '2026-08-31'
category: Other
direction: 自动特征工程 · 符号回归+LLM
tags:
- Symbolic Regression
- AutoFE
- LLM
- Tabular Data
- Feature Engineering
one_liner: 符号回归生成高相关公式，再用 LLM 一次性精炼解释，实现高性能且可解释的自动特征工程
practical_value: '- 在 CTR/CVR 等表格特征场景，可用符号回归自动挖掘高阶交互与非线性组合（如 ratio、log 交互），替代盲目数学变换，产出高预测力且具可解释性的特征。

  - 用统计先验（候选公式与目标的相关性）限定候选集，再让 LLM 只做一次语义重命名/筛选，避免多轮 LLM 迭代带来的成本与幻觉风险；工程上可将 LLM 调用控制在个位数。

  - 可把该方案嵌入现有特征平台：符号回归负责生成、选择大量公式特征，LLM 只负责后处理解释，适合批量生产特征并沉淀可复用特征库。

  - 在电商风控、归因等对可解释性要求高的场景，符号回归天然提供公式形式，LLM 补全领域语义，能同时满足模型效果与业务审查要求。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：表格数据常因特征信息量不足影响模型效果；传统 AutoFE 通过盲目的数学变换生成特征，可解释性差；LLM 驱动的 AutoFE 需要多轮迭代且存在幻觉与偏置，成本高。

方法：SymboLLM-FE 先用符号回归从数据中搜索与目标变量强相关的数学公式，生成高预测力的特征候选；随后利用基于统计先验的 LLM 精炼机制，借助大模型丰富先验知识对这些公式进行语义解释和筛选，确保最终特征具备可解释性。整个过程仅需个位数 LLM 调用。

结果：在 6 个真实世界数据集和 4 个 Kaggle 竞赛上，SymboLLM-FE 优于现有 AutoFE 方法，同时解决了可解释性差与迭代成本高的问题。
