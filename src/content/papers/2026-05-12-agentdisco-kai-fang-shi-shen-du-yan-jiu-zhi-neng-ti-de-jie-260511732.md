---
title: 'AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research
  Agents'
title_zh: AgentDisCo：开放式深度研究智能体的解耦与协作
authors:
- Jiarui Jin
- Zexuan Yan
- Shijian Wang
- Wenxiang Jiao
- Yuan Lu
affiliations:
- Xiaohongshu Inc.
arxiv_id: '2605.11732'
url: https://arxiv.org/abs/2605.11732
pdf_url: https://arxiv.org/pdf/2605.11732
published: '2026-05-12'
collected: '2026-05-16'
category: Agent
tags:
- Deep Research
- Agent
- Adversarial Optimization
- Policy Bank
- GALA Benchmark
one_liner: 通过解耦信息探索与利用为对抗式循环，并构建元优化策略库，在多个深度研究基准上超越闭源系统
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

## 动机

当前深度研究智能体将信息探索（搜索查询生成）与信息利用（大纲/报告生成）耦合在同一模块，缺乏明确的优化信号，导致迭代过程不稳定、覆盖不完整。绝大多数基准也聚焦于学术或咨询类查询，无法反映真实用户的生活化信息需求。

## 方法关键点

- **解耦式对抗协作架构**：将深度研究建模为双智能体合作MDP，**critic agent** 评估当前大纲（信息利用状态），生成缺失的蓝图与目标搜索查询（信息探索状态）；**generator agent** 执行搜索并更新大纲和参考文献，形成交替迭代的对抗优化，明确优化方向。
- **文档银行与连续性约束**：引入文档银行对多轮检索结果进行去噪、评分和摘要，防止上下文过载；同时强制蓝图只能扩展不能删除、保留已验证参考文献，确保优化有序收敛。
- **元优化策略库（Policy Bank）**：围绕critic agent构建外层优化harness，将generator重用作评分智能体，自动评估搜索结果的完备性、多样性等，生成质量信号；利用Claude-Code自动探索搜索策略空间，积累可复用的设计策略，实现搜索查询的自进化优化。
- **GALA生活化基准**：从10,000名高活跃用户的小红书浏览与互动记录中，自动挖掘真实生活信息需求，构建包含家居、旅行、时尚等主题的100条高质量查询，弥补现有基准在日常生活领域的空白。
- **渲染智能体**：将结构化报告转化为红书风格海报、幻灯片或HTML页面，打通从需求挖掘到视觉呈现的全链路。

## 关键实验

- 在**DeepResearchBench**上，AgentDisCo w/ Harness (Gemini‑2.5‑Pro) 取得 **52.11** 的RACE得分，超过GPT‑DeepResearch (46.45) 与Gemini‑2.5‑Pro‑DeepResearch (49.71)；引用准确率达 **89.55%**。
- **DeepConsult** 上 win rate **56.86%**，平均质量 **6.86**，优于OpenAI‑DeepResearch；**DeepResearchGym** 上总体得分 **96.21**。
- 切换到Claude‑Opus‑4.6 后RACE得分升至 **54.02**，文献准确率 **93.56%**，验证架构的可扩展性。
- 在**GALA**基准上，仅使用小红书搜索引擎的AgentDisCo即显著优于Doubao‑Research与OpenAI o3‑DeepResearch，证明社区内容对日常信息需求的优势。
