---
title: 'Game Arena: Strategic LLM Evaluation in Competitive Environments'
title_zh: 游戏竞技场：竞争环境下的战略LLM评估
authors:
- Bovard Doerschuk-Tiberi
- Yao Yan
- Justin Chiu
- Hann Wang
- Timothy Chung
- Martyna Plomecka
- John Schultz
- Jon Lipovetz
- Clayton Drazner
- Yuchen Zhuang
arxiv_id: '2609.31473'
url: https://arxiv.org/abs/2609.31473
pdf_url: https://arxiv.org/pdf/2609.31473
published: '2026-09-24'
collected: '2026-09-28'
category: Eval
direction: LLM 动态竞技评估
tags:
- LLM Evaluation
- Game Arena
- Strategic Reasoning
- Multi-agent
- Benchmark
one_liner: 通过国际象棋、扑克、狼人杀三类游戏构建动态对抗评估平台，避免静态基准饱和
practical_value: '- 评估推荐/搜索中的策略Agent时，可借鉴其设计：用不完全信息博弈环境（如扑克）测试模型在不确定反馈下的决策鲁棒性，比静态问答更贴近真实用户交互。

  - 狼人杀这类多人博弈可模拟多智能体协作与对抗，适合测试对话推荐系统中模型对用户意图的推理、欺骗识别和联盟策略，可用于电商智能客服、谈判Agent的评估。

  - 平台可扩展性设计值得参考：将评估环境标准化，支持快速接入新游戏/新场景，便于企业内部搭建LLM竞技场，持续对比不同模型版本的实战能力。

  - 结果揭示不同模型在战略规划、适应性上的差异，提示我们在生成式推荐中不要只看离线指标，应引入对抗性交互评估来区分模型真实水平。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：静态基准（MMLU、GSM8K等）逐渐饱和，难以区分前沿LLM的真实能力，尤其在战略推理、不确定环境下决策等方面缺乏动态评估。

**方法**：构建Kaggle Game Arena平台，通过竞技游戏进行LLM头对头对抗。选择三类游戏环境：国际象棋（完美信息）、扑克（不完全信息）、狼人杀（多人博弈）。平台提供基础设施，支持模型对战、排名和结果复现。

**结果**：报告了各模型在三个游戏中的完整竞赛结果和指标，显示不同模型在战略规划、适应性和不确定性鲁棒性上存在显著差异，且随着模型迭代，游戏强度自然提升，评估不会饱和。
