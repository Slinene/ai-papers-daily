---
title: 'MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm
  Discovery'
title_zh: MLEvolve：面向自动化机器学习算法发现的自演化多智体框架
authors:
- Shangheng Du
- Xiangchao Yan
- Jinxin Shi
- Zongsheng Cao
- Shiyang Feng
- Zichen Liang
- Boyuan Sun
- Tianshuo Peng
- Yifan Zhou
- Xin Li
affiliations:
- Shanghai Artificial Intelligence Laboratory
- East China Normal University
arxiv_id: '2606.06473'
url: https://arxiv.org/abs/2606.06473
pdf_url: https://arxiv.org/pdf/2606.06473
published: '2026-06-03'
collected: '2026-06-05'
category: MultiAgent
direction: 多智体长周期自演化与算法搜索
tags:
- MultiAgent
- Self-Evolving
- MCGS
- Memory
- Code Generation
- MLE
one_liner: 通过图搜索、回顾记忆与分层规划实现长周期自演化，在 MLE‑Bench 上以半数时间达到 65.3% 奖牌率 SOTA。
practical_value: '- **图搜索 + 跨分支信息复用**：Progressive MCGS 在有向图中引入引用边，允许非父‑子节点间的策略组合，可迁移到多方案
  A/B 实验或推荐模型架构搜索，打破单支探索的信息孤岛。

  - **动态经验积累**：回顾式记忆将每次尝试的计划、结果、分析存入全局记忆，通过 BM25+FAISS 混合检索在规划和调试阶段自动召回相关经验，可直接用于
  Agent 的“失败经验库”或营销策略迭代记忆。

  - **规划‑编码解耦与自适应模式**：分离“改什么”与“怎么改”，根据搜索阶段和代码成熟度在全量生成、模块化生成、diff 编辑间自动切换，能稳定长周期代码迭代，适用于
  LLM 驱动的自动化特征工程或流水线优化。

  - **渐进式探索‑利用调度**：熵启发的软开关在 UCT 探索与精英引导利用间平滑过渡，可在有限计算预算（如广告竞价、推荐排序在线调参）下自动从宽探索收敛到高价值方向，避免后期资源浪费。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 LLM 驱动的机器学习工程（MLE）代理在长周期算法发现中普遍面临分支信息隔离、无记忆搜索、规划与编码耦合三大瓶颈，导致后期优化效率低下、经验无法复用。

**方法关键点**：
1. **Progressive MCGS**：将 MCTS 扩展为有向图，通过主边和引用边实现跨分支信息流；引入熵启发渐进调度，利用软开关从 UCT 探索转向精英引导利用；定义四种扩展操作（主扩展、分支内演化、跨分支引用、多分支聚合），分别对应反思历史、借鉴他支和融合多路经验。
2. **回顾式记忆**：静态领域知识库提供冷启动先验，动态全局记忆自动积累每次成功/失败的结构化记录；采用 BM25+FAISS 混合检索与 RRF 融合，并分阶段检索（规划/调试），实现经验驱动的决策。
3. **分层规划与自适应代码生成**：将 Planner（决定修改什么）与 Coder（如何实现）解耦，根据搜索状态自动选择基础模式（全新生成）、逐步模式（按模块生成）或 diff 模式（补丁编辑），提升长周期迭代的稳定性。

**关键结果**：
- 在 MLE‑Bench 75 个 Kaggle 任务上，12 小时预算（标准 24 小时的一半）下平均奖牌率 **65.3%**，金牌率 34.7%，100% 有效提交，超过所有开源与闭源基线（次优 MARS+ 为 62.7%）。
- 在 AlphaEvolve 的 15 个数学优化题目中，11 题取得最优，展示跨域泛化。
- 消融实验：移除 Progressive MCGS 导致奖牌率下降最显著（从 81.82% 降至 68.18%），分支内演化是其中最关键算子。
