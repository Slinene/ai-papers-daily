---
title: 'VGI-Bench: Probing Visual Intelligence in Video Generation Models'
title_zh: VGI-Bench：视频生成模型视觉智能评测基准
authors:
- Xuan He
- Cong Wei
- Yuhao Cheng
- Linrui Ma
- Yuxuan Zhang
- Zuojun Li
- Yuhao Wen
- Jize Jiang
- Zeyi Liu
- Yuren Hao
affiliations:
- University of Illinois Urbana Champaign
- Tsinghua University
- University of Waterloo
- Massachusetts Institute of Technology
- University of British Columbia
arxiv_id: '2608.19583'
url: https://arxiv.org/abs/2608.19583
pdf_url: https://arxiv.org/pdf/2608.19583
published: '2026-08-25'
collected: '2026-08-29'
category: Eval
direction: 视频生成模型视觉推理评测
tags:
- visual reasoning
- video generation
- benchmark
- evaluation
- world model
- zero-shot reasoning
one_liner: 构建27任务810实例的VGI-Bench基准，评估视频生成模型零样本视觉推理，最强模型仅51.0%准确率
practical_value: '- 评测生成式模型时，采用与模型视觉先验对齐的输入格式，且同时要求过程有效与最终状态正确，而非仅看最终生成结果；在商品视频、多模态内容生成评估中可借鉴其任务分层与难度校准方法（27
  tasks / 810 instances / skill tags），避免基准过难或过易。

  - 分析输入条件敏感性和失败模式：在生成式推荐文案、商品视频或创意生成中，可系统性地改变 prompt 条件（如视角、物体属性、时间演化）来定位模型不稳定点，用于指导
  prompt 模板设计和后处理过滤。

  - 合成数据微调转移边界：对使用合成数据训练生成式推荐模型有参考意义，需注意性能提升存在域转移边界，在合成数据与真实业务数据混合时应评估跨域泛化能力。

  - 去噪过程自校正有限的结论（后期步骤主要细化早期假设而非纠正推理错误）与 LLM 推理中 self-correction 有限类似，提示在生成式推荐流水线中不要依赖模型生成过程中的自我修正，应引入外部验证器或约束（如规则、知识图谱）保证推理正确。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
视频生成模型逐渐被视为视觉世界模拟器，近期研究显示其能通过生成帧表现出零样本视觉推理，但可靠评测仍面临挑战：基准输入需对齐当前视频模型的视觉先验，要求有效的演化过程而非仅看似合理的最终状态，且任务难度需校准至既具挑战性又部分可解。

**方法关键点**  
提出 VGI-Bench，包含 27 个任务、810 个实例，采用两级分类法（任务域 + 技能标签）对视频生成模型的视觉推理能力进行细粒度评估。评测覆盖空间-时间关系、规则约束、动作-结果依赖等，输入条件与视频模型先验对齐，强调过程有效性。

**关键结果**  
当前生成系统能解决部分视觉接地推理任务，但远未可靠；最强模型 Seedance 2.0 在评测标准下仅达到 51.0%。分析进一步揭示输出失败模式、输入条件敏感性、合成微调的性能转移边界；内部去噪视角显示有限的自校正能力，后期去噪步骤主要细化早期假设而非纠正推理错误。
