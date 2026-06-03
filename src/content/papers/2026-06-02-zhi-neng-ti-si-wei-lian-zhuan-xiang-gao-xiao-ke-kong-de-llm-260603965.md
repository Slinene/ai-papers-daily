---
title: Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning
title_zh: 智能体思维链转向：高效可控的 LLM 推理框架
authors:
- Yu Xia
- Zhouhang Xie
- Xin Xu
- Byungkyu Kang
- Prarit Lamba
- Xiang Gao
- Julian McAuley
affiliations:
- University of California San Diego
- Intuit AI Research
arxiv_id: '2606.03965'
url: https://arxiv.org/abs/2606.03965
pdf_url: https://arxiv.org/pdf/2606.03965
published: '2026-06-02'
collected: '2026-06-03'
category: Reasoning
direction: LLM 推理控制 · 预算自适应策略转向
tags:
- Chain-of-Thought
- Reasoning Steering
- Budget-Aware
- Reinforcement Learning
- MultiAgent
one_liner: 将推理过程建模为马尔可夫决策过程，用可训练的控制器代理在推理过程中动态选择策略和转向短语，实现预算感知的高效思维链转向
practical_value: '- **分步导向的推理控制可迁移到多步业务任务**：电商场景中的复杂客服、多轮谈判、商品对比推荐等需要长链推理的任务，可以采用类似的控制器-推理器架构，将推理过程分解为可引导的步骤（理解、规划、执行、检查、总结），在每一轮通过轻量级控制器选择最优策略短语，在保持答案质量的同时大幅降低
  token 开销。

  - **预算条件奖励塑形设计可控制生成长度与成本**：论文提出的非对称奖励函数（正确但超预算降分，错误但未用尽预算加重惩罚）可直接用于推荐系统中的生成式文案或解释生成，通过设定
  token 预算实现质量与成本的精细权衡，避免长而不实的输出或过早截断导致错误。

  - **异步控制器-推理器部署架构降低延迟**：将控制器与推理器部署为独立的 SGLang 服务器并通过异步 HTTP 通信，可以实现与直接批量推理相仿的吞吐量，这一架构可借鉴到在线推荐系统的多智能体编排中，以低延迟实现复杂的多步决策。

  - **可解释的节省来源分解支持精准优化**：论文将 token 节省区分为缩短正确答案、挽救错误尝试、提前终止错误路径等类型，业务系统可借鉴这种分类来定位推理环节的冗余部分，有针对性地优化推理策略，如减少不必要的验证轮次。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**

大语言模型的长链思维推理虽提升最终答案准确率，但常常产生冗余推导、重复自检和延迟终止，导致推理成本高且难以控制。现有高效推理方法主要通过缩短、压缩或提前终止思维链来控制“想多久”，但很少干预“怎么想”。近期研究发现长思维链存在结构化的功能阶段（理解、规划、执行、验证、总结等），这为细粒度的推理行为转向提供了新的控制维度。为此，本文提出一种在保持推理质量的同时大幅节省 token 的开销的可控框架。

**方法关键点**

- **推理转向的 MDP 建模**：将预算约束下的推理定义为马尔可夫决策过程，其中控制器代理在每一步观察已生成的思维轨迹和剩余预算，输出一个高级推理策略（如 `UNDERSTAND`、`PLAN`、`EXECUTE`、`CHECK`、`CONCLUDE`）和一个自然语言转向短语（如“Wait, let me verify…”）来启动下一段推理。
- **控制器训练两阶段**：首先从 DeepSeek-R1 的专家思维链中构建合成转向轨迹——按段落分割步骤，用 LLM 标注对应策略并提取开头短语作为转向短语，再通过多预算增强（缩放预算让轨迹在不同剩余预算处终止）训练控制器获得预算感知先验；随后使用组相对策略优化（GRPO）配合预算条件奖励塑形进行强化学习：正确但超预算给予递减奖励，错误且未用尽预算加重惩罚，从而同时抑制过度思考和过早放弃。
- **异步两服务器部署**：控制器与推理器分别部署为独立 SGLang 服务器，通过异步 HTTP 通信驱动每样本的 MDP 循环，将控制器调用延迟摊还给批量吞吐，达到与直接推理相近的实时性。

**关键结果**

在 MATH-500、AIME24、AMC、OlympiadBench 和 GPQA 等数学和科学 QA 基准上，使用 DeepSeek-R1-Distill-Qwen-{1.5B,7B} 和 Qwen3-8B 作为冻结推理器，ACTS 在匹配甚至超过全思考基线准确率的同时，平均节省 37%–57% 的总 token 数。例如，DeepSeek-1.5B 在 MATH-500 上准确率 82.8%（基线 83.6%）且 token 节省 53.3%，在 GPQA Diamond 上准确率提升 11.9 个百分点且 token 节省 59.4%。在不同预算尺度下，准确率-效率曲线平滑且位于全思考与无思考极端点连线上方，展现出严格更优的权衡。研究表明，通过策略级转向，弱推理器也能被提升至超过其无引导表现的水平，控制器可跨模型（如 Qwen3-8B）和跨领域（科学 QA）泛化。
