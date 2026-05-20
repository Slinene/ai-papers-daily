---
title: 'Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code
  Synthesis'
title_zh: Code-as-Room：基于 Agent 代码合成从俯视图生成 3D 房间
authors:
- Yixuan Yang
- Zhen Luo
- Wanshui Gan
- Jinkun Hao
- Junru Lu
- Jinghao Yan
- Zhaoyang Lyu
- Xudong Xu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Innovation Institute
- Southern University of Science and Technology
- University of Warwick
arxiv_id: '2605.18451'
url: https://arxiv.org/abs/2605.18451
pdf_url: https://arxiv.org/pdf/2605.18451
published: '2026-05-17'
collected: '2026-05-20'
category: Agent
direction: MLLM Agent 生成 3D 场景
tags:
- MLLM
- Agent
- 3D Generation
- Code Synthesis
- Blender
- Spatial Reasoning
one_liner: 提出一个 MLLM Agent 框架，通过结构化执行流水线从俯视图生成 Blender 代码来构建 3D 房间
practical_value: '- 多阶段流水线 + 跨阶段记忆模块：将复杂生成任务拆解为解析、几何、材质、灯光等子阶段，并用记忆模块保持上下文一致，可借鉴到电商场景中自动生成商品布局或店铺装修，避免长流程遗忘。

  - 代码作为可执行中间表示：用 Blender Python 脚本表示 3D 场景，具备可编辑性和确定性，类似思路可用于生成式推荐中，用代码描述推荐理由或布局，便于二次编辑与调试。

  - 结构化执行 harness：为 Agent 设定明确的阶段输出 schema 和校验步骤，有效减少无限循环，可迁移到 Agent 业务系统中，提升稳定性与可控性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：从俯视图图像生成 3D 房间时，文本方法缺乏空间精度，现有图像条件 Agent 容易出现不稳定和无限循环。为此，作者提出 Code-as-Room，利用 MLLM 的代码能力直接生成 Blender 脚本。

**方法**：框架采用多阶段流水线：解析俯视图提取物体及其空间关系，然后依次生成几何体、材质和灯光的 Blender Python 代码。每个阶段输出结构化结果，并通过跨阶段记忆模块维持上下文，防止遗忘。最终代码可直接在 Blender 中执行，生成完整的 3D 房间。

**结果**：构建了专用基准，与已有 Agent 方法相比，Code-as-Room 能稳定生成更合理、更多样的 3D 房间，验证了结构化执行 harness 的有效性。
