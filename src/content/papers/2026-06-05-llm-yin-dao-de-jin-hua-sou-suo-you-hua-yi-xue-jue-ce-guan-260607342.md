---
title: LLM-Guided Evolution for Medical Decision Pipelines
title_zh: LLM 引导的进化搜索优化医学决策管道
authors:
- Ivan Sviridov
- Artem Oskin
- Ivan Panin
- Iaroslav Bespalov
- Dmitry Dylov
- Ivan Oseledets
- Aleksandr Nesterov
affiliations:
- Sber AI Lab
- AIRI
arxiv_id: '2606.07342'
url: https://arxiv.org/abs/2606.07342
pdf_url: https://arxiv.org/pdf/2606.07342
published: '2026-06-05'
collected: '2026-06-08'
category: Other
direction: LLM 引导的进化优化与医学决策管道
tags:
- MAP-Elites
- Evolutionary Algorithms
- Medical Decision Pipelines
- Prompt Optimization
- LLM-guided Evolution
- Quality-Diversity
one_liner: 利用 LLM 引导的 MAP-Elites 进化算法在推理阶段自动发现超越人工设计的医学分诊、交互问诊和图像分类策略，无需微调模型。
practical_value: '- **程序级搜索代替手工调参**：将业务决策管道（如推荐排序、出价策略、Agent 对话流）设计为可执行的 Python 模块，以
  LLM 作为 mutator 自动变异 prompt、控制逻辑、投票规则等，而不仅是调整单个 prompt，可迁移到电商 Agent 的策略自动优化。

  - **安全/业务目标下的适应度设计**：借鉴论文中分诊任务的不对称加权适应度（高代价错误如漏召、低召回加权更高），在推荐场景中可为关键指标（如转化、高价值商品召回）赋予更高权重，同时约束输出合规性（如
  JSON 格式）作为准入条件。

  - **推理时进化代替模型微调**：在冻结模型上通过进化搜索优化策略，降低计算成本，适合频繁变更的业务规则或个性化策略迭代，例如对已部署的推荐 Agent 做安全策略补丁。

  - **交互式场景的成本-质量前沿探索**：通过 MAP-Elites 在对话轮次/ token 消耗与准确性之间找到帕累托前沿，可复用于电商客服 Agent
  的对话策略优化，实现低延迟高满意度的自适应询问与响应。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
将 LLM 适配到医疗决策（分诊、交互问诊、影像分类）通常依赖昂贵的微调或繁琐的手工提示工程。本文探索一种仅用推理时的进化搜索替代方案——LLM 引导的 MAP-Elites 算法，在冻结模型的基础上自动发现优化策略，避免人工反复试错。

**方法关键点**  
- 使用 MAP-Elites 质量-多样性算法，维护一个按行为描述符索引的档案，保留多样化高性能方案。
- 候选方案为可执行 artifact（完整 Python 程序或提示生成模块），包含提示、控制流、投票、检索、后处理等，而不仅是文本提示。
- 以开源稀疏 MoE 模型 gpt-oss-120b 作为 evolver，通过重写和结构化反馈执行变异。
- 三个任务分别设计特定适应度函数：分诊中强调急诊召回和安全加权；交互问诊兼顾准确率与对话 token 成本；影像分类要求严格 JSON 输出并优化准确率。
- 进化在有限标注数据上进行（如影像分类仅用 100 张图像），避免微调。

**关键实验结果**  
- **分诊**：在 Semigran 基准上，进化后的程序准确率从 77.3% 提升至 87.1%，急诊召回从 0.60 提升至 0.97；在 MIMIC-ESI 预测中，最佳进化程序精确准确率达 62.0%，优于手工基线 56.7%，且减少严重低分诊。
- **交互问诊**：在 MEDIQ 基准上，进化策略在 Llama-3-8B 上准确率 +3.1pp 且 token 降低 89.6%，在 Llama-3-70B 上 +3.6pp、-67.6% token；转移到更强模型 Qwen-3.5-27B 和 Gemma-4-31B 仍保持准确性-成本前沿优势。
- **影像分类**：在 PneumoniaMNIST 上，仅进化提示，MedGemma-4B 在 224×224 分辨率下准确率从 63.0% 提升至 72.5%，MedGemma-27B 从 83.3% 提升至 84.5%，且始终输出有效 JSON。
- 定性分析表明提升来自可解释的程序逻辑变化，如校准分诊边界、选择性证据获取与响应、发现导向的视觉决策规则。

**一句话核心发现**：LLM 引导的进化搜索能够在推理阶段为多样化临床任务自动生成既准确又安全合规的决策策略，其价值在于将手工调参转化为结构化的自动探索，并可观察策略内部逻辑。
