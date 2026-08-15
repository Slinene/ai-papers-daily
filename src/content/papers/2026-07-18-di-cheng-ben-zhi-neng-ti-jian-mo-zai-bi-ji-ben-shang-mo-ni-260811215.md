---
title: 'Poor Man''s Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop'
title_zh: 低成本智能体建模：在笔记本上模拟大规模LLM智能体社会
authors:
- Igor Itkin
affiliations:
- Independent Researcher, Tel Aviv, Israel
arxiv_id: '2608.11215'
url: https://arxiv.org/abs/2608.11215
pdf_url: https://arxiv.org/pdf/2608.11215
published: '2026-07-18'
collected: '2026-08-15'
category: MultiAgent
direction: LLM多智能体社会模拟 · 低参数代理模型
tags:
- LLM multi-agent systems
- surrogate models
- behavioural cloning
- mean-field theory
- agent-based modelling
- scaling
one_liner: 用低参数代理模型替代LLM智能体，仅需数百次查询即可在笔记本上模拟大规模智能体社会并预测误差趋势
practical_value: '- 在电商/推荐系统的用户模拟或A/B仿真中，用几百条LLM决策样本蒸馏一个轻量行为克隆模型，即可在普通服务器上模拟百万级用户/Agent，成本降低几个数量级；尤其适合生成式推荐中评估策略的宏观指标（转化率、GMV、多样性）。

  - 构造多智能体仿真时，先根据 agent 的交互阶数（是否只依赖历史均值等低阶统计量）与记忆长度预估替代误差的 N 缩放；若响应接近饱和或强曲率，需升级代理模型阶数或保留部分
  LLM 调用，避免宏观结论失真。

  - 把 LLM 决策策略蒸馏到小模型用于线上近线推理，可作为 Agent 策略降本方案；结合 error trend 先验判断哪些场景可以安全蒸馏，哪些需要保留大模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：模拟大规模 LLM 智能体社会成本高昂（千个智能体单次运行可达数十美元、数十小时），但研究问题通常是宏观的（相变、风格化事实、N 缩放），而非单个智能体认知。受统计物理启发，可用低参数模型替代每个 LLM 智能体。
**方法**：用几百到几千次廉价 LLM 查询做行为克隆，训练轻量代理模型，之后在笔记本上运行任意 N 的社会模拟；提出 [interaction order × memory] 分类法，将感知与记忆映射到有效理论，预先预测代理误差随 N 的趋势。
**结果**：在 EconAgent 宏经济学模拟及另外 7 个具名 LLM 模拟上验证，代理决策克隆自真实 LLM 诱导（主要是 DeepSeek），成本几美元。预测的误差趋势逐格成立；两个被反驳的预测均出现在强饱和响应上，理论在无自由参数下定量匹配了实际误差。
