---
title: 'LinTree: Improving LLM Reasoning with Explicitly Structured Search Histories'
title_zh: LinTree：显式结构化搜索历史提升 LLM 推理
authors:
- Liwei Kang
- Yee Whye Teh
- Wee Sun Lee
affiliations:
- National University of Singapore
- University of Oxford
arxiv_id: '2605.31492'
url: https://arxiv.org/abs/2605.31492
pdf_url: https://arxiv.org/pdf/2605.31492
published: '2026-05-29'
collected: '2026-06-01'
category: Reasoning
direction: LLM 推理 · 搜索结构优化
tags:
- LLM Reasoning
- Search Tree
- Parent Pointers
- Structured Trace
- GRPO
- Search Efficiency
one_liner: 为 LLM 推理的搜索痕迹添加父指针形成显式线性树结构，在 SFT+GRPO 下显著提升任务成功率和搜索效率
practical_value: '- 在需要多步推理与回溯的 Agent 场景（如电商客服、多轮任务规划）中，显式记录搜索树节点之间的父子关系（即使只是简单的 sid
  编号）能大幅降低模型对搜索历史的混淆，提升正解率与规划效率，可直接嵌入现有 CoT 或反思式 prompt 设计中。

  - 对于生成式推荐或查询改写中涉及“尝试-评估-回退”的多步生成，可采用类似的 LinTree 格式将生成路径结构化，方便 RL 训练时准确追踪路径与提取最终方案，避免因隐式结构导致的高错误率。

  - 工程实现上，仅需在搜索痕迹的文本表示中加入 `sid=X` 与父状态引用，改动极小；在 SFT 后接 GRPO 的训练范式已被验证有效，可复用其效率奖励函数（式
  (1)）来平衡正确性与搜索开销。

  - 若业务中存在基于 LLM 的启发式搜索（如用 LLM 为 A* 打分），可参考将 LLM 从局部状态评估转为全轨迹条件化推理的策略，利用显式树结构帮助模型更有效地探索状态空间，减少无谓的局部重访。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：LLM 的推理过程可视为隐式搜索树线性化，模型回退或切换分支时并不显式标识父状态，导致即使观察全部搜索历史也难以可靠超越仅观察局部状态的启发式搜索。受此启发，研究是否通过简单的父指针标记就能让搜索痕迹更易被利用。

方法与关键点：  
- 在三个完全可观察的推理环境（积木世界、栅格导航、推箱子）上，用宽度 BFS 生成搜索痕迹，通过两种格式对比：隐式格式只记录动作与结果状态；显式格式在每次扩展时加入 `sid=X` 与前驱 sid，形成可追溯的线性树（LinTree）。  
- 使用 Qwen3-0.6B 作为基座，先监督微调（SFT）模仿规则启发式搜索，再通过 GRPO 强化学习优化正确性与搜索效率，奖励函数采用有界几何折扣惩罚鼓励短路径。  
- 同时训练仅依赖局部状态（当前状态+目标）的 LLM 启发式作为基线，对比全轨迹条件推理的优势。  

关键实验与结果：  
- 在积木世界、导航、推箱子三个域中，SFT 后显式痕迹即提升成功率（平均 +5 个百分点）；GRPO 后显式模型在积木世界和导航达到 100% 成功率，推箱子从 85.9% 提升至 89.6%（加生成约束后 98.9%），且搜索效率均优于隐式模型与局部启发式。  
- 分析显示，显式结构大幅减少计划提取失败（从搜索成功但输出错误计划的比例下降），并使模型在导航任务中探索更分散的状态空间（平均成对距离 4.19 > 4.11 > 3.99），表明树结构帮助模型更有效地利用历史避免重复搜索。  

核心启示：搜索历史的收益不取决于是否看到历史，而取决于历史是否以显式树结构呈现；简单父指针即可将非结构化的推理流变成便于学习与优化的表示，为 LLM 推理的结构感知训练提供了方向。
