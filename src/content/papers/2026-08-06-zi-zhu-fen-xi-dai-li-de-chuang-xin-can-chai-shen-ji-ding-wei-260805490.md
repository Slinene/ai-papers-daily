---
title: 'Innovation-Residual Auditing of Autonomous Analysis Agents: Localization,
  Detection Limits, Error Control, and Identifiability'
title_zh: 自主分析代理的创新残差审计：定位、检测限与错误控制
authors:
- Ahmed Hassoon
- Mark Dredze
affiliations:
- Johns Hopkins University
arxiv_id: '2608.05490'
url: https://arxiv.org/abs/2608.05490
pdf_url: https://arxiv.org/pdf/2608.05490
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: 代理审计的检测极限与错误可控性分析
tags:
- Autonomous Agents
- Error Localization
- Auditing
- False Discovery Control
- Identifiability
- Statistical Inference
one_liner: 对无监督代理错误审计进行理论分析，揭示评分选择对错误传播的影响并给出统计控制方法
practical_value: '- 设计代理操作审计系统时，需谨慎选择评分函数：基于单步条件概率的评分会掩盖下游继承错误，导致一个错误只触发一处警报；基于长程重构的评分能使单次错误扩散为多操作标记，有助于暴露错误影响范围。

  - 在电商推荐场景中，若用Agent自动生成分析报告（如活动效果归因），可借鉴论文的统计错误控制程序，在无标注错误样本下，仅利用历史正确分析的可交换性，控制单次审计的错误发现比例。

  - 错误检测灵敏度主要受限于操作表示的维度（而非训练数据量），提示在开发审计工具时应优先优化表示质量，盲目增加正确分析样本收益甚微。

  - 对于累积型错误，需动态调整比较窗口长度以平衡检测延迟与误报风险，这与推荐系统中在线模型退化的渐进式监控问题有相通之处。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机** 自主数据分析代理（如自动选队列、连表、建模）的输出若出错，需定位具体操作。最新无监督审计方法通过学习正确分析的模式来标记异常操作，但其可靠性缺乏理论支撑。

**方法关键点** 论文分析了评分函数对错误定位的影响：若用“给定前一步操作的惊奇度”打分，下游操作会原样继承上游错误，导致一个错误只产生一个标记，无法区分始作俑者；若用“相对于完整正确分析的重构误差”打分，单个错误会扩散到多个操作，形成错误传播链。量化了这种扩散的幅度，并针对错误逐渐累积的场景给出了比较长度的选择策略。提出统计错误控制程序，在仅假定正确分析可交换（而非模型完美）的条件下，控制单次审计中错误标记的比例；并分析了模型不完美和事后选择分析样本时保证的弱化程度。

**关键结果** 建立了错误检测的可识别性极限：幅度过小的错误因与正确分析的正常波动不可区分而无法定位。该极限随正确分析样本量的增加而下降极为缓慢（百倍样本量增加仅降低不到2%），表明表示维度是检测灵敏度的主要瓶颈，而非数据量。
