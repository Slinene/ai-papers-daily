---
title: 'Articraft: An Agentic System for Scalable Articulated 3D Asset Generation'
title_zh: Articraft：可扩展的铰接式 3D 智能体生成系统
authors:
- Matt Zhou
- Ruining Li
- Xiaoyang Lyu
- Zhaomou Song
- Zhening Huang
- Chuanxia Zheng
- Christian Rupprecht
- Andrea Vedaldi
- Shangzhe Wu
affiliations:
- University of Cambridge
- University of Oxford
- Nanyang Technological University
arxiv_id: '2605.15187'
url: https://arxiv.org/abs/2605.15187
pdf_url: https://arxiv.org/pdf/2605.15187
published: '2026-05-14'
collected: '2026-05-16'
category: Multimodal
tags:
- LLM
- Agent
- 3D Generation
- URDF
- Articulated Objects
- Dataset
one_liner: 将铰接式 3D 资产生成转化为代码编写任务，搭配专用 SDK 与迭代 harness，无需视觉反馈即可规模化产出高质量资产
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

**动机**  
铰接式 3D 对象（如家电、工具、家具）在机器人仿真、VR/AR 和内容创作中至关重要，但现有公开数据集规模小、类别窄、质量参差不齐（如 PartNet-Mobility 仅 2.3K 资产 46 类），导致数据驱动模型泛化能力受限。生成式合成数据是打破这一瓶颈的关键，但传统方法依赖图形软件或单步生成，难以兼顾多样性与物理合理性。

**方法关键点**  
Articraft 的核心思路是将「生成一个铰接资产」规约为「编写一段 Python 程序」，并为此构建了一个**智能体系统**，包含两个核心组件：  
1. **LLM 友好的 SDK**：提供从基础图元（Box、Cylinder）到高级铰接抽象（Revolute、Prismatic、Continuous 关节）的编程接口，内置几何验证钩子（如重叠检测、隔离部分警告），让 LLM 通过编写 `model.py` 文件同时定义零件、关节与自检逻辑。  
2. **受限 harness**：智能体的工作区仅暴露一个可写程序文件与只读文档，动作空间精简为读文件、打补丁、查示例、编译验证、几何探测五类工具。Harness 自动执行编译、运行基础 QC 与用户自定义测试，并将失败/警告/注释以结构化形式返回，驱动下一轮迭代。整个闭环**完全基于代码反馈，避免依赖昂贵的渲染或图像验证**，使规模化生成成本可控。  
此外，系统支持图像条件生成：参考图像持续驻留在对话中，引导比例、材料与关节设计，随后可通过 LiteReality 细化 PBR 材质。

**关键结果与数字**  
- 使用 Articraft 构建了 **Articraft‑10K** 数据集，包含 **10K+** 个铰接资产，覆盖 **245 个日常类别**，远超现有数据集（如 Infinigen‑Sim 的 20K 但仅 18 类，PartNet‑Mobility 的 2.3K 46 类）。  
- 与 Articulate‑Anything、PhysX‑Anything、URDF‑Anything 以及通用编码智能体 Claude Code/Codex 相比，Articraft 生成的质量更高，且不需要外部图形软件。  
- 用 Articraft‑10K 重训分析铰接结构的模型 **Particulate**，获得**显著性能提升**（论文未列精确指标，但强调其效用）。  
- 数据集与生成代理将开源，包含推理轨迹与可重用的智能体环境。  

**最值得记住的一句话**  
“为铰接 3D 生成设计一个专用编程接口和验证闭环，就能让普通 LLM 迭代写出正确程序，从而摆脱视觉监督，实现大规模、低成本的高质量资产创建。”
