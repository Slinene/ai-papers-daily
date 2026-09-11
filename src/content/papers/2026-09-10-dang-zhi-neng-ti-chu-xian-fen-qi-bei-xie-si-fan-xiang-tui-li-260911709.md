---
title: 'When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for
  Multi-Agent Collective Decision-Making'
title_zh: 当智能体出现分歧：贝叶斯反向推理作为无标签多智能体集体决策锚点
authors:
- Ken Chen
- Wei Wang
- Sachith Seneviratne
- Hansani Weeratunge
- Saman Halgamuge
affiliations:
- The University of Melbourne
- Sri Lanka Institute of Information Technology
arxiv_id: '2609.11709'
url: https://arxiv.org/abs/2609.11709
pdf_url: https://arxiv.org/pdf/2609.11709
published: '2026-09-10'
collected: '2026-09-11'
category: MultiAgent
direction: 多智能体决策聚合与校准
tags:
- Multi-agent systems
- Bayesian inference
- Decision aggregation
- Jensen-Shannon divergence
- LLM agents
- Calibration
one_liner: 用贝叶斯反向推理构造reverse posterior，以Jensen-Shannon散度衡量跨路径一致性，提升多智能体决策聚合性能
practical_value: '- 多智能体集成决策（如商品标签审核、广告文案质量打分、query意图分类）不要只对正向logits投票；可以额外让同一个LLM反向推理“给定该标签，证据出现的概率”，用两个方向分布的JS散度识别可靠agent，避开共享错误。

  - 在agent分歧大的样本上，log-linear融合（LogLin）比简单投票/加权更稳；若业务中有多路召回/多模型打分分歧严重，可用跨路径一致性作为融合权重，优先相信正反推理一致的模型。

  - 无标签场景下，反向推理可作为廉价校准信号；若积累少量标注数据，两阶段校准reverse anchor能进一步提升聚合，适合冷启动或低资源标注的电商场景。

  - 反向推理模型单独精度可能不高，但作为互补信号价值大于正向基线；架构上可保留轻量反向头或prompt模板，避免额外大模型训练。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：多智能体系统中多个LLM给出冲突答案时，现有投票、选举规则、LLM法官等方法都依赖正向推理（证据→标签），共享同一因子化，容易继承相关错误。

方法：为每个实例构建reverse posterior，即从显式似然做贝叶斯反向推理；正向与反向后验提供了不同因子化的近似，错误往往不会同时出现。用Jensen-Shannon散度度量每个agent在正向与反向路径上的一致性，并据此排序。基于该跨路径一致性信号提出三种策略：硬选择（MinJS）、软重加权（FwdJS）和对数线性融合（LogLin）。

结果：在DDXPlus上测试五个LLM骨干，MinJS在所有骨干上均优于随机选择；FwdJS普遍超过最强基线；LogLin整体表现最佳，在agent分歧大的子集上增益最大。反向后验虽然单独准确率较低，但作为锚点比仅用正向信息更有用；有标签数据时，轻量两阶段校准可进一步增强。
