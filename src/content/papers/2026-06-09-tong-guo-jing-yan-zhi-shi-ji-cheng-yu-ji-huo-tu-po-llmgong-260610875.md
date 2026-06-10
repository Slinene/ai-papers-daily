---
title: Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration
  and Activation
title_zh: 通过经验知识集成与激活突破LLM工具调用极限
authors:
- Yupu Hao
- Zhuoran Jin
- Huanxuan Liao
- Kang Liu
- Jun Zhao
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2606.10875'
url: https://arxiv.org/abs/2606.10875
pdf_url: https://arxiv.org/pdf/2606.10875
published: '2026-06-09'
collected: '2026-06-10'
category: Agent
direction: LLM工具调用 · 经验知识获取与激活
tags:
- Tool Calling
- Experiential Knowledge
- Parallel Sampling
- Knowledge-Augmented
- Multi-turn Agent
one_liner: 系统研究经验知识在工具调用中的获取、激活与内化，提出KA TE框架，通过并行采样和知识增强训练大幅提升多步工具调用准确率。
practical_value: '- **实例级轨迹知识更有效**：直接使用高质量执行轨迹（Scenario Trajectory）作为few-shot示例注入prompt，比抽象意图描述能更可靠地提升工具调用准确率。电商Agent在调用库存、物流API时可复用历史成功轨迹。

  - **推理宽度优于推理深度**：用并行采样（如4路）配合自一致性聚合，成本可控地激活模型潜在知识，避免复杂prompt工程的边际收益递减。适合在agent决策步骤中增加少量并行调用。

  - **用RL做知识内化**：将检索到的经验知识显式拼入训练数据，用GRPO等RL方法微调，比SFT更能将知识固化为模型能力。电商推荐Agent可对高频场景构建经验库并RL微调。

  - **简单检索够用**：Top-K相似度检索+阈值过滤已能取得明显收益，不必在检索机制上过度设计，工程实现简单，适合快速落地。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM作为自主Agent进行多步工具调用时常因缺乏具体、可执行的经验知识（如参数约束、操作模式、错误恢复策略）而失败。现有工作多聚焦prompt设计或API规范，但对经验知识在工具执行中的系统性作用认知不足。本文首次系统研究经验知识的获取、激活和内化，回答哪种知识形式最有效、如何激活、训练能否进一步收益三个核心问题。

**方法关键点**
- **知识获取与分类**：将经验知识分为实例级（场景轨迹知识ST、经验总结知识ES）和意图级（脚本式意图聚类SIC、文本式意图聚类TIC），构建检索知识库。实例级知识直接提供步骤级示例，意图级则抽象为按意图聚类的操作脚本。
- **推理时激活**：对比深度提示（prompt hints）和宽度并行采样。发现提示hint引导模型加深推理深度收益递减甚至有害；而并行采样（每步生成多个候选动作，可选自一致性或LLM聚合）能有效激活潜藏知识，尤其在低温度解码下被抑制的正确行为。
- **训练时内化**：将检索到的经验知识拼接到训练数据中，使用SFT和RL微调。RL（GRPO）效果优于SFT，且直接RL优于先SFT后RL，揭示在对齐阶段RL更能将知识内化到参数中。
- **KA TE框架**：集成实例级ST知识、宽度并行采样、LLM聚合，并可选知识增强后训练，统一覆盖知识获取、激活和内化阶段。

**关键实验**
在BFCL-V3（多步API调用）和AppWorld（交互式编码agent）上评估。BFCL-V3包含Base、Miss Func、Miss Param、Long Context四类场景。Qwen3-8B: KA TE推理阶段比FC基线提升13.25个点（32.75→46.00），结合RL后提升15.5个点（48.25），超越GPT-4.1/4.5。Qwen3-32B: 推理增益4.5个点，仍稳健。消融表明：实例级知识贡献最大，堆叠多种知识无额外增益；并行采样是关键激活杠杆；RL内化带来额外收益。在AppWorld上KA TE也显著优于ReAct基线。
