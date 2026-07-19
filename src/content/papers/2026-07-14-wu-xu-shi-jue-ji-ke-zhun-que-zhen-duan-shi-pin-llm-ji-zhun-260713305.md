---
title: 'Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video
  LLM Benchmarks'
title_zh: 无需视觉即可准确：诊断视频 LLM 基准的视觉依赖解离
authors:
- Jae Joong Lee
affiliations:
- Purdue University
arxiv_id: '2607.13305'
url: https://arxiv.org/abs/2607.13305
pdf_url: https://arxiv.org/pdf/2607.13305
published: '2026-07-14'
collected: '2026-07-19'
category: Eval
direction: 视频LLM基准的视觉依赖性诊断
tags:
- video LLM
- visual dependency
- benchmark evaluation
- language priors
- black-screen baseline
- measurement validity
one_liner: 提出视觉依赖差距(VDG)审计视频LLM，发现模型黑屏下准确率相当，帧多样性而非时序贡献视觉增益
practical_value: '- 在评估推荐/Agent模型时，引入“黑屏基线”（无输入/随机基线）隔离语言先验，避免高估新增特征贡献

  - 设计消融阶梯（如传感器剥离、序列乱序）量化各信息源增益，借鉴FPS与帧序消融思路定位模型真正依赖的信号

  - 警惕对话Agent或文案生成中的语言模式作弊，用黑屏测试验证模型是否依赖视觉/结构化输入而非纯文本补全

  - API与开源模型的VDG差异（0.025~0.315）提示私有模型可能更依赖非视觉捷径，选型时需定制诊断基准'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：视频LLM的基准准确率常被等同于视觉理解能力，但模型可能靠语言先验和文本模式得分，导致leaderboard提升并未反映真正的多模态进步。本研究系统审计该假设。

**方法**：提出**视觉依赖差距(VDG)**，即原始视频与黑屏条件下每道题正确率的差值。在MVBench上对20个模型（2-78B参数，10种架构）进行配对McNemar检验；构建诊断阶梯（黑屏→单帧→乱序帧→原始视频）分解视觉收益来源；消融帧率(0.5-24FPS)排除稀疏采样影响；通过H.264实验揭示答案翻转现象；检测4个API模型VDG的普适性。

**关键结果**：
- 模型在黑屏条件下无显著差异(p=0.53)，但原始视频上差异显著(p=0.0003)，表明总体准确率提升未必来自视觉；
- 任务类型排序稳定：属性感知强依赖视觉，时序推理接近纯语言基线；
- 诊断阶梯显示，帧多样性贡献大部分视觉增益，时序顺序几乎不增加准确率（16个开源模型）；
- 增加FPS未能弥补视觉依赖缺失；H.264下稳定总体准确率掩盖了双向答案翻转；
- API模型VDG从0.025到0.315，说明部分商业模型可能严重依赖非视觉捷径。
**结论**：VDG应作为视频基准的标准化审计指标，确保评测真正衡量视觉基础能力。
