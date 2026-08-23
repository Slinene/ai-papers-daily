---
title: 'VTInstructor: Visual Trajectory Prompting for Navigation Instruction Generation
  in Continuous Environments'
title_zh: VTInstructor：连续环境下基于视觉轨迹提示的导航指令生成
authors:
- Haolin Yang
- Yuxing Long
- Zihan Yang
- Hao Dong
affiliations:
- Peking University
- PrimeBot
arxiv_id: '2608.15284'
url: https://arxiv.org/abs/2608.15284
pdf_url: https://arxiv.org/pdf/2608.15284
published: '2026-08-15'
collected: '2026-08-23'
category: Multimodal
direction: 视觉语言导航 · 指令生成
tags:
- Visual Prompting
- VLN
- Instruction Generation
- Continuous Environments
- GRPO
- Egocentric Video
one_liner: 将隐式轨迹几何转为显式视觉轨迹提示，首个连续环境 VLN 指令生成框架，刷新 R2R-CE/RxR-CE SOTA
practical_value: '- 行为序列显式化提示：可把用户长点击/浏览/加购序列压缩成关键行为节点，并叠加“转向/目标”类结构化提示注入多模态或序列编码器，提升电商场景下
  query 推荐、购物路径描述或决策理由生成。工程上可用点击率、停留时长等阈值抽取关键行为，形成轨迹图 prompt。

  - 弱化图谱依赖：无需 navigation graph/map/scene reconstruction，适合业务中缺少完整商品知识图谱或用户路径图的情况。可借鉴其从稠密事件流中恢复轨迹、仅靠关键锚点构造上下文的方法，降低图构建与维护成本。

  - 用下游 reward 校准生成：VT-GRPO 不止优化文本 NLL，而是让生成指令能提升下游 follower 成功率。迁移到生成式推荐/搜索词生成时，可用点击率、转化率等下游反馈作为
  GRPO reward，使生成文本直接服务业务目标。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：连续环境中导航指令生成只能依赖稠密 ego-centric RGB 视频，缺少离散视点图提供的显式轨迹结构，既有方法难以恢复轨迹线索。

方法关键点：VTInstructor 将隐式轨迹几何转为显式视觉轨迹提示。EDTC 把长 RGB 轨迹压缩为导航关键帧；VTP 在锚点帧上叠加路径、转弯、目标等视觉线索；VTMod 将轨迹信号注入视觉编码器，全程无需 navigation graph、预建地图或场景重建；VT-GRPO 在训练阶段校准空间注入，使生成指令与下游导航表现对齐。

结果：在 R2R-CE 与 RxR-CE Val Unseen 上，所有标准 NLG 指标达到 SOTA，CIDEr 分别 +0.357 和 +0.109；生成指令驱动 frozen follower 成功率达 63.3%，较最佳竞争指令源 +14.7 pp；作为数据增强使下游导航任务 +3 SR。
