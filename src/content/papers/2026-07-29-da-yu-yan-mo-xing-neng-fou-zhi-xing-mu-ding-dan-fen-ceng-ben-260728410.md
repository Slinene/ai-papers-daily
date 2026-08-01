---
title: Can Large Language Models Execute Parent Orders?
title_zh: 大语言模型能否执行母订单？分层零样本交易决策
authors:
- Zane Shen
- Xinli Xu
- Guangyi Zhang
- Jialong Chen
- Jinsong Zhou
- Cong Chen
- Guibao Shen
- Dongyu Yan
- Luozhou Wang
- Zhen Yang
affiliations:
- Independent Researcher
- HKUST(GZ)
- ZJU
- SYSU
arxiv_id: '2607.28410'
url: https://arxiv.org/abs/2607.28410
pdf_url: https://arxiv.org/pdf/2607.28410
published: '2026-07-29'
collected: '2026-08-01'
category: Agent
direction: LLM驱动的分层决策与规划
tags:
- LLM
- Hierarchical Planning
- Zero-shot Decision Making
- Algorithmic Trading
- Agent
one_liner: 首次系统研究用LLM做母订单执行，提出分层框架PACE，零样本超越传统和学习型基线0.65基点
practical_value: '- 分层规划思想可直接用于电商大促的预算/流量分配：用LLM做高层计划（每天/每时段的预算比例），底层执行器按计划实时出价，无需针对具体场景重训模型。

  - LLM零样本决策能力可替代强化学习在冷启动或快速变化的推荐场景（如新品冷启推送节奏）中做时序动作决策，降低训练成本。

  - 长期规划+短期执行的分解范式适合多Agent协作：一个Plan Agent制定整体策略，多个Execute Agent按约束执行，解耦决策粒度，便于工程实现和调试。

  - 行为分析中的“模型自信与绩效正相关”提示：可在在线决策系统里结合LLM输出置信度做风险控制，高置信动作放量，低置信动作交人工审核或降级。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：母订单执行（将大订单拆分为小单以降低冲击成本）的传统方法依赖预设市场假设或需任务特定训练，难以适应变化。LLM在金融领域已从“交易什么”扩展到“如何执行”，但尚无系统研究。

**方法**：提出PACE（Plan-Ahead Controlled Execution），将母订单执行分解为长时规划与短时执行两层。长时规划由LLM根据历史数据生成拆分计划，短时执行由轻量控制模块按计划实时调整，整个过程无需显式市场模型或训练，通过提示工程实现零样本迁移。

**结果**：在深交所Level-1数据上，PACE超越TWAP、Almgren-Chriss以及学习型基线，相对最强基线额外降低0.65 bps成本。行为分析显示LLM的决策模式与人类交易者不同：模型置信度越高表现越好（而非人类常见的过度自信导致亏损），且倾向尽早交易而非拖延至截止期。
