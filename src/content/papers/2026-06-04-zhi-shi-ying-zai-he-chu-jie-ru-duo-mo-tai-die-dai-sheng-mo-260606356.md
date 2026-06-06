---
title: Where Should Knowledge Enter? A Layered Framework for Knowledge Infusion in
  Multimodal Iterative Generative Mo
title_zh: 知识应在何处介入？多模态迭代生成模型的知识注入分层框架
authors:
- Renjith Prasad
- Chathurangi Shyalika
- Anushka Pawar
- Amit Sheth
affiliations:
- University of South Carolina
- Indian AI Research Organization
arxiv_id: '2606.06356'
url: https://arxiv.org/abs/2606.06356
pdf_url: https://arxiv.org/pdf/2606.06356
published: '2026-06-04'
collected: '2026-06-06'
category: Multimodal
direction: 多模态生成模型的知识注入与安全对齐
tags:
- Knowledge Infusion
- Diffusion Models
- Layered Intervention
- Safety Alignment
- Multimodal Knowledge Graph
one_liner: 将知识注入视为干预层问题，提出表面、轨迹、潜在、参数四层框架，多层组合可互补降低70.97%的知识违规。
practical_value: '- **按失败类型分层干预**：输入侧知识改写解决 prompt 级问题，生成中轨迹/潜在干预修正结构违规，输出侧过滤残留 artifact，可借鉴到生成式推荐的结果后校验与中间状态调控。

  - **共享知识源统一控制**：所有层查询同一个知识图谱，避免冲突，在推荐系统里可作为统一的事实约束源，用于物品属性合规、敏感概念过滤。

  - **训练自由的推理时堆叠**：所有干预均不修改扩散 backbone，适合冻结大模型快速上线，推荐场景下可对已有生成模型叠加业务规则而无需重训。

  - **组合互补优于单层**：实验表明单层输入端只能降部分违规，叠加中间层和输出层能持续提升，推荐安全对齐可采纳类似堆叠策略。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：多模态生成模型虽流畅但难以遵循领域知识（如安全、结构约束），现有知识注入方法按技术分类（prompt、引导、潜变量编辑、微调），而非按其作用于生成过程的哪个组件，导致设计选择缺乏原则。本文提出应将知识注入看作“干预层”问题，因为迭代生成过程可分解为输入/输出边界、转移函数、中间状态和模型参数四个形式组件，对应四种干预层：表面、轨迹、潜在、参数。

**方法关键点**：
- 形式化定义四层及其作用点：表面修改输入或后处理输出；轨迹在推理时改变转移函数；潜在直接编辑中间状态；参数内化知识到权重。
- 在扩散模型中实例化，映射现有方法（如 RAG、无分类器引导、Prompt-to-Prompt、DreamBooth）到各层，并分析五维特性（可控性、可解释性、持久性、成本、失败覆盖）。
- 提出多层组合原则：按失败类别匹配层、组合以互补覆盖、使用共享知识源避免冲突。

**关键实验**：
- 任务：安全对齐，使用多模态知识图谱（MMKG）控制文本到图像扩散模型（SDXL、SD-v1.5），冻结骨干网络。
- 逐层添加：表面输入（prompt 中性化）、轨迹-潜在（检测仇恨激活并回退修复）、表面输出（局部修复）。
- 在 Detonate 基准（25K 提示）上，毒性从原始 0.31 降至 0.09（SDXL），降幅 70.97%，且每增一层毒性单调下降，CLIP 和美学质量保持提升，超越 SAFREE、SLD 基线。
- 验证了不同层纠正不同失败类别，组合产生互补收益。

**一句话关键**：知识注入应针对生成轨迹的不同组件分层干预，多层组合能互相补充，大幅提升生成的一致性。
