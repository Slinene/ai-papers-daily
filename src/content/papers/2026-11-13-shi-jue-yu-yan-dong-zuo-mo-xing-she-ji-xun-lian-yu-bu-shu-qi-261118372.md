---
title: 'Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and
  Deployment'
title_zh: 视觉-语言-动作模型：设计、训练与部署全生命周期综述
authors:
- Suvarna Kadam
- Soran Parsa
affiliations:
- Witsense AI
- University of Huddersfield
arxiv_id: '2611.18372'
url: https://arxiv.org/abs/2611.18372
pdf_url: https://arxiv.org/pdf/2611.18372
published: '2026-11-13'
collected: '2026-11-16'
category: Multimodal
direction: 多模态具身模型 · VLA 综述
tags:
- VLA
- Embodied AI
- Survey
- Robot Learning
- Vision-Language Models
- World-Action Models
one_liner: 综述88篇VLA工作，沿设计-训练-部署七轴分析22个模型，揭示数据扩大、模型分化与泛化趋势
practical_value: '- 模型设计：若在电商/Agent 场景构建多模态动作输出模型，可参考 VLA 的轴拆解——显式定义输入与记忆、动作空间、中间预测（reasoning
  trace / future obs），而非直接端到端；这在 GUI Agent、RPA 等需要控制操作流程的场景可复用。

  - 训练数据：VLA 趋势显示互联网知识 + 少量领域机器人数据即可启动，电商 Agent 也可用大规模 VLM 预训练 + 少量真实操作/点击轨迹做后训练，降低数据采集成本；社区收集数据模式值得借鉴。

  - 模型规模与部署：主流 3–7B 与 <1B 边缘可跑分化，选择需结合实时性；若在电商推荐/Agent 服务上跑实时多模态交互，可考虑小模型蒸馏或动作 token
  压缩，控制 KV cache 与推理延迟。

  - 评测鲁棒性：基准近满分模型在物体或相机微小移动下失败，提示线上不能只看 benchmark；电商 Agent 或推荐模型应加入语义不变扰动（图片裁剪、文案改写、UI
  微调）做分布外鲁棒性测试。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：VLA 把互联网规模 VLM 知识迁移到物理控制，领域从 RT-2 起不到四年发展迅速，但缺少横跨设计、训练和部署的系统梳理。

方法：按生命周期拆成七轴——输入与记忆、架构、动作输出、中间预测；预训练数据、后训练适配；实时执行。分析 22 个代表模型，覆盖操纵、导航、人形控制、世界-动作模型与评测。

关键结果：训练数据扩大，从约 10k 小时遥操作（π0）到 23k 社区收集片段（SmolVLA）和 20k 小时第一人称人类视频（GR00T N1.7）；模型规模分化为主流 3–7B 和 <1B 消费级 GPU 可跑；出现统一操纵与导航的通用 VLA（UniVLA、Qwen-VLA）；部分基准近满分模型在物体或相机微小移动时失败，鲁棒性仍是核心问题。
