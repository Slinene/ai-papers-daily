---
title: 'MindForge: Teaching Small Language Models Whole-Life-Cycle Software Engineering
  via Source-Free Program Synthesis'
title_zh: MindForge：通过无源码程序合成教授小模型全周期软件工程
authors:
- Yihao Chen
- Shi Chang
- Khaled Chawa
- Feng Lin
- Boyuan Chen
- Shaowei Wang
- Ahmed E. Hassan
affiliations:
- Huawei Canada
- Queen's University
- University of Manitoba
arxiv_id: '2607.27146'
url: https://arxiv.org/abs/2607.27146
pdf_url: https://arxiv.org/pdf/2607.27146
published: '2026-07-28'
collected: '2026-08-01'
category: Training
direction: LLM 训练 · 程序合成 · 教师蒸馏
tags:
- Program Synthesis
- Teacher-Student
- Software Engineering
- Fine-tuning
- Code Generation
one_liner: 自动化将开源命令行程序转为无源码训练环境，用教师轨迹微调小模型，使编程从零构建性能大幅提升
practical_value: '- 可借鉴其自动构建**仅暴露接口和文档的无源码沙箱**的方法，为推荐系统 Agent 生成训练环境，例如基于推荐 API 文档和模拟用户行为合成决策轨迹。

  - 使用大模型作为教师生成高质量**全生命周期交互轨迹**，再微调小模型，这种蒸馏范式可直接用于将复杂推荐策略（召回、排序、重排）压缩为小型 Agent 模型，降低线上延迟。

  - 训练数据覆盖**需求分析、设计、实现、测试**多阶段，对推荐 Agent 训练有启发：可设计从用户画像分析、策略设计到配置、离线评估的完整任务流，提升模型全局优化能力。

  - 从与测试集不重合的仓库构建环境，泛化性提升显著，业务中可用**多样化历史推荐场景构造合成数据**，微调模型以应对未见过的运营需求或算法变更。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有编码智能体擅于修改已有代码库，但从零构建完整程序仍是巨大挑战，前沿模型在 ProgramBench 上完全解决率不足 1%。主要原因之一是缺乏覆盖软件工程全生命周期（需求、设计、实现、测试）的可扩展训练环境。

**方法关键点**：
- 提出 **MindForge** 自动化流水线，将开源命令行程序转化为**无源码训练环境**：仅暴露编译后的可执行文件和文档，模型需基于文档完成任务。
- 从与 ProgramBench 不重合的仓库中抽取程序，使用教师模型 **GLM-5.2** 合成**全生命周期轨迹**（计划、实现、测试、调试），不依赖于原始源代码。
- 用这些轨迹微调 **Qwen3.6-27B**，得到 MindForge-27B。

**关键结果数字**：
- ProgramBench 平均测试通过率从 **37.98% 提升至 49.51%**，超过同规模模型，与更大前沿模型可比。
- 在 7 个未见过的软件工程基准上一致提升，绝对值增幅最高达 **31.00 点**（RepoZero-C2Rust），DeepSWE 提升 **14.16 点**，SWE-bench Verified 提升 **5.04 点**等。
