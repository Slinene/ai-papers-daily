---
title: Empowering VLMs for Few-Shot Multimodal Time Series Classification via Tailored
  Agentic Reasoning
title_zh: 面向少样本多模态时间序列分类的 VLM 智能体推理框架 MarsTSC
authors:
- Lin Li
- Jiawei Huang
- Qihao Quan
- Dan Li
- Boxin Li
- Xiao Zhang
- Erli Meng
- Wenjie Feng
- Jian Lou
- See-Kiong Ng
affiliations:
- Sun Yat-sen University
- Xiaomi Corporation
- University of Science and Technology of China
- National University of Singapore
arxiv_id: '2605.09395'
url: https://arxiv.org/abs/2605.09395
pdf_url: https://arxiv.org/pdf/2605.09395
published: '2026-05-10'
collected: '2026-05-16'
category: LLM
tags:
- VLM
- Time Series
- Agentic Reasoning
- Few-Shot Learning
- Multimodal
one_liner: 设计三协作智能体与自进化知识库，让 VLM 在少样本下通过反思推理显著提升时间序列分类准确率
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**：时间序列分类在医疗、工业、金融等场景至关重要，但标注样本稀缺，少样本学习成为关键瓶颈。传统方法依赖数值时序，无法联合利用文本、图像等多模态互补信息；VLM 虽具备跨模态理解能力，但现有尝试仅使用静态上下文和简单提示，缺乏动态任务适配，无法从有限的标注样本中充分榨取判别性知识，且不具备精准定位决策证据的机制。

**方法关键点**：提出 MarsTSC，围绕一个可自我演化的**知识库**，通过三个协作智能体进行迭代反思推理，无需微调 VLM 参数：
- **知识库设计**：采用结构化特征项（bullet points），支持原子级增量更新（ADD/MODIFY/DELETE），防止上下文坍塌。
- **三角色协作**：
  - **Generator**：基于知识库进行可解释分类，并显式引用支撑证据。
  - **Reflector**：诊断推理错误，通过对比正负样本，提取被忽略的时间模式与判别性洞察。
  - **Modifier**：将经验精确写入知识库，并通过标签计数器剔除噪声项。
- **测试时更新**：采用双次生成（two-pass）实现自我复核，产生伪标签；利用延迟更新机制（候选→参考→原型知识三级分层）谨慎演化知识库，缓解分布偏移。

**关键实验**：在 12 个 UCR/UEA 基准（ArrowHead、ECG200、Lightning7 等）上，3-shot 设定下，MarsTSC 平均准确率达到 75.51%，远超经典方法（HIVE-COTE 2.0 65.71%）、深度模型（TimesNet 53.79%）和时序基础模型（MOMENT 64.54%），并在 7 个数据集上取得最优。在与增大训练样本的基线对比中，固定 3-shot 的 MarsTSC 仍普遍优于用多达 50 倍样本训练的全量模型。消融实验显示测试时更新可提升约 3-10% 绝对准确率，没有双次生成的伪标签反射更会导致显著性能下降。

**值得记住**：少样本多模态时间序列分类的关键不是更强的基础模型，而是一个能动态积累判别经验、避免上下文崩溃、并谨慎自校正的任务适配推理范式。
