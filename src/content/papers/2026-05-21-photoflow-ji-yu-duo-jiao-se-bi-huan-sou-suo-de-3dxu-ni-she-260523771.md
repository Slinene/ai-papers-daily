---
title: 'PhotoFlow: Agentic 3D Virtual Photography Missions'
title_zh: PhotoFlow：基于多角色闭环搜索的3D虚拟摄影智能体
authors:
- Jiarui Guo
- Haojia Wei
- Yiming Zhang
- Yifei Liu
- Yuning Gong
- Hongjie Zhang
- Xue Yang
- Zhihang Zhong
affiliations:
- Shanghai Jiao Tong University
- Northeastern University
- University of California, Los Angeles
- Cornell University
- Shanghai AI Laboratory
arxiv_id: '2605.23771'
url: https://arxiv.org/abs/2605.23771
pdf_url: https://arxiv.org/pdf/2605.23771
published: '2026-05-21'
collected: '2026-05-25'
category: Agent
direction: Agent 多角色协作 · 3D摄影闭环搜索
tags:
- Agent
- Multimodal
- 3D Vision
- Closed-loop
- Aesthetic Reasoning
- Visual Critique
one_liner: 提出Director-Reviewer-Reflector多角色Agent，实现语言引导的3D场景闭环相机搜索与照片渲染
practical_value: '- **多角色反思架构可复用于推荐/决策Agent**：Director提议、Reviewer评估、Reflector从失败提取经验的分工模式，可借鉴到生成式推荐候选生成、评估和优化循环中，提升决策质量。

  - **失败记忆与区域标记机制**：Reflector的region memory和dead-zone suppression能避免重复低质量区域探索，在电商搜索排序或流量分配中可标识低效候选并抑制。

  - **受限预算下的探索-利用平衡**：高探索重定位策略在有限渲染次数下兼顾多样性与收敛，可应用于在线推荐策略的探索调度。

  - **多模态自动评估**：Reviewer结合规则、视觉评论和成对比较，可启发生成式推荐中内容质量的自动评审设计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：虚拟摄影要求Agent在没有预设相机位姿和参考图的3D场景中，根据语言意图推断合适镜头并渲染照片，这同时考验复杂3D空间理解和抽象审美判断，现有方法难以综合评估。

**方法**：提出PhotoFlow，一个Director-Reviewer-Reflector闭环Agent。Director根据场景信息和摄影意图构建软蓝图，生成多样化候选相机参数；Reviewer通过规则检查、视觉批判和成对竞标筛选最佳候选；Reflector将失败经验转化为区域记忆、死区抑制和高探索重定位，引导后续搜索。所有操作基于VLMs和LLMs实现。

**结果**：在VPhotoBench（47个Blender场景，141个摄影任务）上，PhotoFlow在6轮渲染预算内，外部质量对齐综合得分和成功率均显著优于单次预测、单链反思、锚点库选择和随机搜索等方法，首次实现任意Blender场景的语言驱动虚拟摄影可执行Agent任务。
