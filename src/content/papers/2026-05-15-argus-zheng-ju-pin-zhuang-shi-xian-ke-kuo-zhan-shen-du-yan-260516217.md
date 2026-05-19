---
title: 'Argus: Evidence Assembly for Scalable Deep Research Agents'
title_zh: Argus：证据拼装实现可扩展深度研究Agent
authors:
- Zhen Zhang
- Liangcai Su
- Zhuo Chen
- Xiang Lin
- Haotian Xu
- Simon Shaolei Du
- Kaiyu Yang
- Bo An
- Lidong Bing
- Xinyu Wang
affiliations:
- MiroMind AI
arxiv_id: '2605.16217'
url: https://arxiv.org/abs/2605.16217
pdf_url: https://arxiv.org/pdf/2605.16217
published: '2026-05-15'
collected: '2026-05-19'
category: MultiAgent
direction: Agent多智体协作优化
tags:
- Agentic System
- Multi-Agent
- Evidence Graph
- GRPO
- Deep Research
- Test-time Scaling
one_liner: 通过Searcher和Navigator协作构建共享证据图，将深度研究转化为证据拼图，实现并行搜索的线性扩展。
practical_value: '- **用证据图解耦搜索与推理**：在电商知识图谱问答或Agent任务规划中，可以将并行执行的子任务结果抽象为图结构（节点=证据/主张，边=支持/矛盾），由协调Agent在图层面进行验证与派发，避免直接拼接长上下文，压缩比可达1200:1。

  - **对比奖励驱动验证学习**：借鉴GRPO+对比奖励（verification前后得分差），训练Agent学会识别回答中的缺失证据并主动查询，在电商多跳问答或生成式推荐中可让模型自动补全信息缺口，而非被动合并。

  - **独立训练、组合推理**：将Searcher（执行器）和Navigator（协调器）分开训练，Searcher保持标准ReAct，Navigator通过RL掌握何时验证、派发、合成，推理时可按需切换单/并行模式，类似电商场景中前端搜索Agent与后端推理Agent的解耦设计。

  - **图结构提高可解释性**：最终答案每个声称都追溯到证据节点和URL，实现完全可审计。在电商推荐理由生成中，可构建主张-证据链，提升用户信任和合规性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
深度研究Agent通过并行ReAct轨迹聚合（多数投票、best-of-N）提升性能，但并行轨迹常重复挖掘相同证据而非互补，导致收益递减，且聚合上下文随轨迹数线性膨胀，触及模型窗口上限。根本原因是缺乏对已收集证据全局结构的表征与缺失诊断。

**方法关键点**
- **双代理协作**：Searcher（标准ReAct，无状态）负责根据子查询收集证据轨迹；Navigator维护有向无环证据图G，节点为证据（带URL）和主张，边为支持/矛盾关系。
- **验证-派发循环**：Navigator通过分析G检测未验证主张、矛盾或未覆盖的子问题，针对性派发新Searcher查询，将并行算力分配到证据图的缺失缺口上。
- **图压缩合成**：合成阶段Navigator仅以q和结构化G为输入（而非原始轨迹）推理答案，G对原始轨迹的压缩比约1200:1，使推理上下文保持极小（最高21.5K tokens），解耦了并行规模与推理成本。
- **GRPO训练**：Navigator通过GRPO端到端训练，奖励设计为对比奖励（验证前后答案得分差值+完整答案得分），促使模型学会有价值的验证查询。Searcher独立SFT，与Navigator训练解耦，支持不同备选Searcher即插即用。

**关键结果**
- 基于35B-A3B MoE基座，在8个深度搜索基准上，单Searcher配置平均提升5.5点，8并行Searcher提升12.7点。
- 在BrowseComp上，64并行Searcher达到86.2%，超越所有被测商业Agent，Navigator上下文仅21.5K tokens。
- GAIA达93.2，Seal-0达56.2，均大幅领先商用最强Agent；图表示消融显示结构化图贡献5.2点绝对增益。
