---
title: 'CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI
  Scientists'
title_zh: CausaLab：面向 AI 科学家的可扩展交互式因果发现评测环境
authors:
- Junlin Yang
- Dylan Zhang
- Xiangchen Song
- Qirun Dai
- Xiao Liu
- Yuen Chen
- Aniket Vashishtha
- Jing Shi
- Chenhao Tan
- Hao Peng
affiliations:
- Tsinghua University
- University of Illinois Urbana-Champaign
- Carnegie Mellon University
- University of Chicago
- Adobe
arxiv_id: '2605.26029'
url: https://arxiv.org/abs/2605.26029
pdf_url: https://arxiv.org/pdf/2605.26029
published: '2026-05-27'
collected: '2026-05-30'
category: Eval
direction: LLM 智能体因果推理评测
tags:
- causal discovery
- LLM agents
- benchmark
- interactive reasoning
- structural causal models
one_liner: 提出 CausaLab 环境，评估 LLM 智能体在交互式因果发现中的预测与机制恢复差距，揭示其因果推理局限
practical_value: '- 在推荐系统或电商 Agent 中，若使用 LLM 进行因果推断（如 Uplift 建模），需同时评估预测精度与因果图恢复的
  F1，避免仅关注推荐指标而忽视因果机制正确性。

  - 交互式干预策略设计：混合观测-干预的效果优于纯干预，可指导 Agent 主动学习时平衡利用已有数据和干预获取新信息，适用于 A/B 测试策略优化。

  - 一致性验证可缓解过早停止，在 Agent 链式推理或迭代探索中引入自我验证机制，防止快速给出错误因果结论，提升决策可靠性。

  - 使用合成 SCM 生成可控测试环境，可用于离线评测推荐策略的因果效果，尤其适合模拟干预分配和反事实推理场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 LLM 因果推理评测多基于问答或分类，无法区分预测成功与真正理解因果机制。论文提出 CausaLab 环境，要求智能体通过观测与干预恢复隐藏的结构因果模型（SCM），并基于机制做出预测，从而衡量其交互式因果发现能力。

方法：每个 episode 生成一个随机 SCM，智能体在合成实验室中获取观测数据，可对“操纵器晶体”实施干预，最终预测“反应器晶体”的共振频率，并输出因果图。环境评估任务准确率和因果图恢复的 F1（如全边 F1），并分析观测/干预混合策略的影响。

结果：在纯观测 6 节点设置下，GPT-5.2-high 达到 92% 任务准确率，但全边 F1 仅 0.471，显示预测与机制恢复的显著差距；混合观测-干预策略提升结构保真度；纯干预场景下强 agent 仍然困难；过早停止是主要弱点，一致性验证可缓解。CausaLab 成功分离预测成功和因果理解，暴露了 LLM 智能体作为实验因果推理者的局限性。
