---
title: 'Coda-DaVinci: Reimagining Video Generation with Code2Video'
title_zh: Coda-DaVinci：任务自适应 Code2Video 视频生成框架
authors:
- Yiyan Ji
- Qixun Wang
- Yang Shi
- Zhuoran Zhang
- Yifan Xu
- Tengfei Liu
- Yuqi Tang
- Xiaohan Zhang
- Shujie Li
- Jiafu Tang
affiliations:
- Nanjing University
- KlingAI Research
- Peking University
- Hong Kong University of Science and Technology (Guangzhou)
- University of Hong Kong
arxiv_id: '2611.26595'
url: https://arxiv.org/abs/2611.26595
pdf_url: https://arxiv.org/pdf/2611.26595
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 视频生成 · 多智能体 Code2Video
tags:
- Code2Video
- Video Generation
- Multi-Agent
- Task-Adaptive Routing
- 3D Proxy
- Physics Simulation
one_liner: 提出任务自适应多智能体 Code2Video 框架，按实体粒度建模并协调物理仿真与提示，提升指令遵循与场景一致性
practical_value: '- 任务路由：在生成式推荐/文案生成中可借鉴“受控中间表示生成 vs 端到端直接生成”的路由。对需要结构可控或受约束的商品描述、广告创意，先生成结构化代理再生成最终内容；对简单
  query 直接端到端，节省算力。

  - 多粒度实体建模：不同实体（商品、用户、场景）可分配不同粒度代理。例如对服装类商品用细粒度属性代理保持一致性，对背景或穿搭场景用粗粒度布局代理保持自然感，按任务自适应调整表示粒度。

  - 物理仿真与提示对齐：在生成动态内容（如短视频广告、AR 试穿演示）时，可将物理仿真或动态约束注入生成提示，与代理表示对齐，提升物理合理性与一致性。

  - 多智能体审查修复：借鉴其多智能体 harness：一个智能体生成，一个做视觉检查/独立评审，保留场景资产只修复局部问题，可迁移到电商内容审核、商品标题/图片生成后的自动质检与修复流程。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：Code2Video 通过智能体编写 3D 代理引导视频生成，能显式控制结构和动态，但如何构建代理与提示以获得最优下游质量尚未系统研究。方法：通过控制实验和盲评，考察代理粒度、物理仿真和提示的作用。发现任务相关权衡：粗粒度代理利于自然运动，中粒度代理利于一致性；物理仿真和代理对齐提示进一步提升平均质量。据此提出 Coda-DaVinci，一个任务自适应智能体框架，在代理引导生成与直接生成之间路由，按实体调整建模粒度，并协同物理仿真与基于代理的提示。多智能体治理保留场景资产，通过视觉检查与独立评审驱动修复。结果：在 VTR 上取得领先的指令遵循、在 R2M 上取得领先的场景一致性，物理合理性优于直接生成，视觉真实感高于对比 Code2Video 基线；长视频评测显示事件结构与跨交互一致性提升，但在过渡稳定性和场景设置遵循上仍有局限。
