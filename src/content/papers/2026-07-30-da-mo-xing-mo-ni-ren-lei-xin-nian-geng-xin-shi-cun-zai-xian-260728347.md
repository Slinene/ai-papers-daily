---
title: LLMs struggle to simulate human belief updates in controlled environments
title_zh: 大模型模拟人类信念更新时存在显著偏差
authors:
- Sebastian Pohl
- Harsh Mehta
- Pranav Mambayil
- Abdul Ghafoor
- Franziska Lesigang
- Yufang Hou
- Christian Hilbe
affiliations:
- IT:U, Interdisciplinary Transformation University Austria
arxiv_id: '2607.28347'
url: https://arxiv.org/abs/2607.28347
pdf_url: https://arxiv.org/pdf/2607.28347
published: '2026-07-30'
collected: '2026-08-02'
category: Eval
direction: LLM 模拟人类信念的评估
tags:
- belief simulation
- LLM evaluation
- persona
- bias
- human alignment
one_liner: LLM 仅在给定真实初始立场时可匹配人群分布，自身生成初始立场与更新过程均不忠实
practical_value: '- 在电商/推荐场景中使用 LLM 模拟用户反馈或 A/B 测试时，必须为模型提供真实的初始偏好（如历史行为标签），否则模拟结果会严重失真，尤其会将中立选项过度膨胀。

  - 基于人口统计与性格画像的 persona 对提升模拟保真度无一致效果，不应依赖该类特征做生成式用户建模；模型的实际行为分布主要受 prompt 中给定的立场起点约束。

  - 模型倾向于产生更频繁但幅度更小的偏好转移，且无法正确评估信息说服力的排序，用于模拟推荐解释或广告文案对用户态度影响时，需用真实用户数据做校准。

  - 当前多轮社交媒体仿真中若缺少真实起始条件，LLM 模拟的信念动态并不可靠，若需模拟用户兴趣演化，应考虑从真实交互序列冷启动，而非让模型自行生成初始兴趣。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 越来越多被用作社会科学实验中人类被试的代理，但其模拟人类信念更新（尤其是社交媒体讨论后态度变化）的忠实度缺乏直接检验。该工作将 6 个 LLM 与 391 名英国被试的 Reddit 评论阅读实验进行 1 对 1 对比，检验模型能否复现个体立场更新。

**方法**：收集被试在三个讨论话题上阅读评论前后的立场变化数据，为每名被试构建包含人口统计与大五人格特征的 persona prompt；LLM 在该 persona 下模拟初始立场生成与评论后立场更新。评估指标包括立场分布匹配、个体对齐度、信念转移幅度与方向，以及评论说服力排序的准确性。

**关键结果**：
- Qwen3-32B 和 GPT-5-Mini 在**被赋予被试真实初始立场**时，能复现事后立场分布，但所有模型均**无法自行生成可信的初始立场**，且从自生成立场出发的更新完全不忠实。
- 出现三种系统性偏差：① 过度生成中性立场；② 比人类产生更频繁但幅度更小的信念转移；③ 无法正确排序评论的说服力。
- 人口统计与性格画像对模拟保真度无显著且一致的影响。

结论：LLM 仅在基于真实起始条件时才可能可靠模拟信念动态，当前多轮社交媒体仿真若缺少真实初始立场则结果不可靠。
