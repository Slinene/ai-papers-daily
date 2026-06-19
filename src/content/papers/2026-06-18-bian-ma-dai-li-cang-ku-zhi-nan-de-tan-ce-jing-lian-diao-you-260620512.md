---
title: Probe-and-Refine Tuning of Repository Guidance for Coding Agents
title_zh: 编码代理仓库指南的探测-精炼调优
authors:
- Asa Shepard
- Jeannie Albrecht
affiliations:
- Williams College
arxiv_id: '2606.20512'
url: https://arxiv.org/abs/2606.20512
pdf_url: https://arxiv.org/pdf/2606.20512
published: '2026-06-18'
collected: '2026-06-19'
category: Agent
direction: Agent 上下文指导自动优化
tags:
- probe-and-refine
- repository guidance
- coding agent
- LLM tuning
- knowledge base
one_liner: 通过合成bug探测迭代优化仓库指南，使编码代理解决率提升4.7个百分点以上，增长源于覆盖扩大而非单一补丁精度提升
practical_value: '- **知识库迭代优化范式**：借鉴 probe-and-refine 思路，在电商搜索、推荐等 Agent 系统中，通过自动生成探测任务（如合成搜索请求、推荐场景）诊断当前知识/指南的缺失，再用
  LLM 自动生成补丁，实现领域知识的低成本持续优化。

  - **提升覆盖率 > 提升单点精度**：实验表明性能提升来自让 Agent 触达正确信息源的比例增加，而非每次决策的准确率。在构建推荐/搜索 Agent 的上下文或工具描述时，更应关注覆盖哪些流程、边界条件，确保
  Agent 能找到关键信息，而不是过度微调每一步的精准度。

  - **轻量级调优，免于复杂 Agent 循环**：调优过程仅使用单次 LLM 调用生成补丁，无需运行完整 Agent 流程，可大幅降低迭代成本。对于需要给 LLM
  Agent 配置系统指南、业务规则等文本的场景，可采用类似方法快速演进，无需复杂仿真环境。

  - **步数预算与指导协同**：更长的推理步骤只有在具备良好指导时才能正向收益。设计推荐/搜索 Agent 时，若允许动态步数，需同步提供高质量的上层指导，否则多余步数反而可能引入噪声或偏离任务。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 编码代理需要代码之外的高层仓库知识（如哪些文件对应哪些子系统、如何运行测试、易错流程），工程师常维护 AGENTS.md 文件提供这类指导，但现有研究对其是否有效存在矛盾。核心问题转为**如何生成有效的指导**。

**方法**：提出 **probe-and-refine 调优**——用合成的 bug 修复探测任务，迭代诊断当前指导文件的不足，并通过单次 LLM 调用生成补丁来修正指导。调优过程不使用 agent 循环或工具，仅需少量 LLM 调用，初始化时利用静态知识库（如代码结构说明），随后逐步精炼。

**关键结果**：在 SWE-bench Verified 基准上，采用 Qwen3.5-35B-A3B 模型、200 步预算、四次独立试验，probe-and-refine 获得 **33.0%** 平均解决率，显著优于静态知识库的 28.3%（p<0.001）和无指导基线的 25.5%。提升主要来自**覆盖率**：精炼后的指导使得 agent 能对多 14.5 个百分点的实例生成可评估补丁，但每个补丁的精度基本不变（约 59%，p=0.119），说明更好的指导帮助 agent **到达正确文件**而非改进修改质量。步数预算实验表明，更大的步数只有配合良好指导才能提高解决率；跨模型实验显示，当模型无法生成足够诊断性的输出时，调优环路会退化，但单补丁精度仍保持恒定。
