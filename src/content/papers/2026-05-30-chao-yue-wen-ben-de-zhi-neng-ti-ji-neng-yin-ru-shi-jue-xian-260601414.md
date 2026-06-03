---
title: 'Agent Skills Should Go Beyond Text: The Case for Visual Skills'
title_zh: 超越文本的智能体技能：引入视觉先验实现可复用多模态技能
authors:
- Binxiao Xu
- Ruichuan An
- Bocheng Zou
- Hang Hua
affiliations:
- Peking University
- University of Wisconsin
- MIT-IBM Watson AI Lab
arxiv_id: '2606.01414'
url: https://arxiv.org/abs/2606.01414
pdf_url: https://arxiv.org/pdf/2606.01414
published: '2026-05-30'
collected: '2026-06-03'
category: Agent
direction: Agent 多模态视觉技能复用
tags:
- Visual Skills
- Agent Skills
- Multimodal Agents
- GUI Grounding
- Textual Bottleneck
one_liner: 指出纯文本技能在视觉任务中存在空间信息瓶颈，提出结合文本规则与视觉先验的可复用多模态技能范式 VISUALSKILL 及自动生成流水线 AutoVisualSkill。
practical_value: '- GUI 自动化与电商平台操作：将常用控件的空间布局、点击区域等制作为静态视觉先验（如按钮模板、热区图），与文本规则绑定，可显著提升
  Agent 在网页/App 上的定位精度，类似思路可用于商品页面自动化测试、数据采集。

  - 密集计数与货架管理：在库存盘点、货架商品计数等场景，采用动态视觉锚点将已计数对象做可视化标记并反馈给模型，形成外部空间工作记忆，有效减少重复计和漏计。

  - 可复用技能库构建：借鉴 VISUALSKILL 的分离式设计，将业务规则（文本）与视觉参考（截图、布局原型）打包为可检索、可组合的技能单元，降低对新模型的尺寸敏感度，方便技能跨任务迁移。

  - 自动技能生成流水线：AutoVisualSkill 的诊断门控和双轨生成方法可用于自动判断任务是否需要视觉支撑，并将少量示例转化为通用视觉协议，适合大规模构建面向电商运营、广告设计等视觉密集型任务的
  Agent 技能库。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
当前智能体技能复用几乎完全依赖文本（指令、推理轨迹），这造成了一个“文本瓶颈”：许多视觉核心任务（GUI 操作、布局设计、密集计数）中的可复用知识本质上是空间性的——边界、比例、对齐、视觉检查轨迹，纯文本描述会损失空间细节并引入歧义。作者指出，文本技能能说明“做什么”，却未保留“在哪看、如何检验”的视觉证据，导致在需要精确定位、持续空间状态跟踪时性能受限。

**方法关键点**  
- 提出 **VISUALSKILL**，将可复用技能定义为三元组：文本逻辑 L + 视觉先验 Pv + 绑定协议 B。视觉先验分三类：静态先验（空间约定、边界原型）、动态先验（推理过程中在图像上叠加锚点/轨迹以维持空间状态）、交错视觉技能（将步骤与源截图/关键帧绑定）。  
- 设计 **AutoVisualSkill** 自动生成框架，包含诊断门控（判断任务是否需要视觉支持）、双轨生成（文本轨道写规则，视觉轨道提取区域/生成图表/调用模型）、打包为可执行技能包（skill.md + 视觉资产 + manifest.json）。  
- 定义**文本退化率（TDR）**，量化纯文本技能丢失的空间信息，使文本瓶颈可度量。

**关键实验结果**  
在 GUI 定位（ScreenSpot/ScreenSpot-v2/GroundUI-18K）上，添加静态视觉先验的 Visual Skill 比纯文本技能 Point-in-Box 精度平均提高约 2.8 百分点（91.1% vs 88.1%），Mean IoU 提升更显著（0.386 vs 0.332），TDR 约 17%。在密集计数（CountBenchQA）上，动态视觉先验方案将准确率从 93.00% 提升到 97.12%（p=0.003），MAE 降低约 60%。定性分析表明，视觉先验修正了点击粒度、提供了可见的计数状态，解决了纯文本无法传递的空间约定与状态塌陷问题。
