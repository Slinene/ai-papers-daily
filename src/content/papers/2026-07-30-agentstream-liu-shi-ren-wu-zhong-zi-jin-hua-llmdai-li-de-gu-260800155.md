---
title: 'AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming
  Tasks?'
title_zh: AgentStream：流式任务中自进化LLM代理的表现评估
authors:
- Dong Yan
- Jian Liang
- Dapeng Hu
- Ran He
- Nicholas Jing Yuan
- Qi Zhang
- Tieniu Tan
affiliations:
- University of Chinese Academy of Sciences
- Microsoft
- Institute of Automation, Chinese Academy of Sciences
- Nanjing University
arxiv_id: '2608.00155'
url: https://arxiv.org/abs/2608.00155
pdf_url: https://arxiv.org/pdf/2608.00155
published: '2026-07-30'
collected: '2026-08-05'
category: Agent
direction: 自进化Agent在流式任务下的评估框架与发现
tags:
- self-evolving agents
- streaming evaluation
- LLM agents
- benchmark
- agent evaluation
one_liner: 提出在流式任务流下评估自进化LLM代理的框架，揭示能力、方法与场景的交互规律
practical_value: '- 电商/搜索推荐的Agent（如对话式导购、广告策略优化）常面临持续变化的任务流，应使用类似AgentStream的流式评估替代单任务评估，以更准确地预测线上效果。

  - 自进化的收益存在模型能力阈值：基础模型较弱时，自进化可能无效甚至有害。在业务中引入自进化前，需确保基座模型能力达到一定水平。

  - 没有一种自进化方法在所有场景和模型上都最优，建议针对不同业务场景（如搜索Query意图分类、多轮对话推荐）进行组合测试，选择适合的方法。

  - 工程设计上，可借鉴AgentStream的任务流配置思路，构建可灵活组合的模拟任务流，用于持续集成评测自进化Agent的稳定性与泛化能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前自进化LLM Agent的评估多局限于独立单任务，无法反映实际部署中连续处理多任务流的行为。需探究在流式任务下，不同自进化方法和模型能力的交互影响。

**方法**：提出AgentStream评估框架。将多个Agent基准任务组织成可配置的任务流，并定义三种流式场景：隔离（Isolated）、顺序（Sequential）、交错（Interleaved），逐步增加任务流的范围和领域混合度。在这些场景下，组合评估5种代表性自进化方法（涉及提示上下文、记忆、技能库等组件）在3种前沿基础模型上的表现，系统解构模型能力、方法架构、流式场景的联合作用。

**关键结果**：自进化可靠性高度依赖流式场景；自进化收益被模型能力“门控”，且随模型强度呈非单调变化；没有任何单一方法在所有模型和场景中全面领先。研究为不同模型与场景下选型提供具体指导，并强调自进化Agent评估应基于现实任务流。
