---
title: Contestable Multi-Agent Debate with Arena-based Argumentative Computation for
  Multimedia Verification
title_zh: 面向多媒体验证的竞技场式多智能体辩论计算框架
authors:
- Truong Thanh Hung Nguyen
- Vo Thanh Khang Nguyen
- Hoang-Loc Cao
- Phuc Ho
- Van Pham
- Hung Cao
arxiv_id: '2605.14495'
url: https://arxiv.org/abs/2605.14495
pdf_url: https://arxiv.org/pdf/2605.14495
published: '2026-05-14'
collected: '2026-05-17'
category: MultiAgent
direction: 多智能体辩论与结构化论证推理
tags:
- Multi-agent Debate
- Argumentation
- Multimedia Verification
- Multimodal LLM
- A-QBAF
- Uncertainty-aware
one_liner: 提出基于竞技场量化双极论证（A-QBAF）的竞争性多智能体辩论框架，实现透明可争议的多模态验证
practical_value: '- **多智能体辩论的轻量裁决机制**：将全局论辩分解为小型局部论证图，通过选择性冲突解决避免全量计算，适合电商中多模态商品审核、虚假评论检测等需要快速结论的场景。

  - **证据到论据的结构化转换**：把多源证据转化为带出处和强度评分的支持/攻击关系，可借鉴到推荐系统的可解释性生成，让模型给出带置信度的正反理由。

  - **不确定性感知的递进式仲裁**：在冲突无法自动化解时触发人工审核或更强模型，这种分层决策思路可直接用于Agent客服的争议处理流水线。

  - **透明可编辑的章节级报告**：生成分块验证报告允许人工修正，适合生成式推荐中需要用户可见且可干预的决策说明。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：多媒体真伪验证不仅要求结论准确，更需要推理过程透明、可质疑。现有方法缺乏结构化论辩与多源证据的对抗性融合，难以在复杂场景下给出可靠且可审查的判断。

**方法**：该工作提出竞争性多智能体辩论框架，整合多模态大语言模型、外部验证工具与基于竞技场的量化双极论证（A-QBAF）。流程上，首先将待验证案例分解为以主张为中心的独立章节，针对每项主张检索相关证据；随后将证据自动编码为结构化的支持或攻击论元，每项论元附带出处链与强度评分。所有论元被送入局部论证图，通过选择性冲突解决机制快速识别关键矛盾，并对无法自动裁决的高不确定性节点进行升级处理（调用更强模型或标记人工介入）。最终生成章节级可编辑验证报告，所有中间论据均可追溯。

**结果**：系统作为ICMR 2026多媒体验证挑战赛的提交方案，公开了完整实现。框架在小规模论证图上实现了低延迟的透明推理，实验表明其结构化的论辩输出具备良好的可读性与可操作性，且计算开销可控，适用于真实多媒体验证场景。
