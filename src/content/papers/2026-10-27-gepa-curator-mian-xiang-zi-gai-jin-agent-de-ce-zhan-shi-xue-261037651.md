---
title: 'GEPA-Curator: Curated Learning for Self Improving Agents'
title_zh: GEPA-Curator：面向自改进 Agent 的策展式学习框架
authors:
- Zack Yu
- Nicholas Lee
- Minjae Lee
- Lakshya Agarwal
- Luca Manolache
- Wonjun Kang
- Matei Zaharia
- Michael W. Mahoney
- Kurt Keutzer
- Sehoon Kim
affiliations:
- UC Berkeley
- ICSI
- LBNL
- Furiosa AI
- KAIST
arxiv_id: '2610.37651'
url: https://arxiv.org/abs/2610.37651
pdf_url: https://arxiv.org/pdf/2610.37651
published: '2026-10-27'
collected: '2026-10-29'
category: Agent
direction: 自改进 Agent 的策展式提示优化
tags:
- LLM Agents
- Self-Improvement
- Prompt Optimization
- Data Curation
- Reflective Learning
one_liner: 用任务策展与成功轨迹检索过滤噪声失败，提升 reflective prompt optimizer 性能，多基准最高超 GEPA 20.7%
practical_value: '- 在构建 agentic 流程（客服助手、推荐理由生成、自动选品）时，不要把所有失败轨迹都喂给 prompt 优化器；先做失败归因，区分
  prompt 缺陷、工具/harness 不稳定、环境随机性和 judge 噪声，只保留可归因于 prompt 的失败，提升学习信号质量。

  - 成功轨迹检索可迁移到电商场景：为某类商品生成文案或操作手册时，检索相似商品/任务的历史成功 trajectory 作为 few-shot context 注入优化器，稳定优化方向并减少灾难性遗忘。

  - 若线上已使用 GEPA/ACE 等 reflective optimizer，可前置“任务是否值得学习”的判断，并维护带 embedding 索引的成功轨迹库做检索，工程成本可控且效果提升显著（最高
  20%+）。

  - 结果提示数据飞轮中噪声样本会污染优化器；在推荐/广告的自动 prompt 优化与失败样本筛选上，应引入置信度过滤和成功案例检索机制。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
现有 reflective prompt optimizers（如 GEPA）主要从失败 rollout 中学习，但在 agentic 环境中，失败可能来自 prompt 弱点、harness 限制、随机执行或 noisy judge，并非都能提供有用信号，甚至可能有害。因此需要策展哪些任务可以进入 prompt 优化器。  

**方法关键点**  
GEPA-Curator 在原有优化器上增加两个组件：  
- **Task Curation**：过滤掉可能提供噪声或不可靠学习信号的任务，避免错误归因；  
- **Prior Success Retrieval**：按任务检索历史成功轨迹，作为额外上下文提供给 prompt optimizer，增强优化稳定性。  

**关键结果**  
在 GoBrowse、ALFWorld、AppWorld、τ-bench 四个基准上，使用 Gemini 3.1 Pro 与 Claude Opus 5 作为优化模型，GEPA-Curator 匹配或超过基线均值，最高比 GEPA 提升 20.7%，比 ACE 提升 21.2%。
