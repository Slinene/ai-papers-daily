---
title: 'WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce'
title_zh: 微信电商多模态内容理解模型 WeMM-Ecom
authors:
- Binhui Xie
- Jinmin Li
- Haomiao Tang
- Guangting Wang
- Song Jin
- Jianwei Zhu
- Fengyun Rao
- Jing Lyu
affiliations:
- WeChat Vision, Tencent Inc.
arxiv_id: '2611.30662'
url: https://arxiv.org/abs/2611.30662
pdf_url: https://arxiv.org/pdf/2611.30662
published: '2026-11-22'
collected: '2026-11-24'
category: Multimodal
direction: 电商多模态大模型与评测
tags:
- MLLM
- E-commerce
- Continued Pre-training
- On-policy Distillation
- GRPO
- Benchmark
one_liner: 开源五尺度电商多模态模型，通过两阶段CPT与混合思维后训练，在电商和通用基准上双超同尺寸Qwen3.5
practical_value: '- **数据配方可直接迁移**：两阶段 CPT，电商占比从45.8%提到61.1%，不要一步拉满；电商池内从属性/感知转向审核/知识问答，通用池内从
  caption 转向 OCR/图表/STEM。业务侧可复用其 CPV 预测、SKU 同品匹配、规则审核、标题生成等任务构造方式。

  - **领域专精与通用能力兼得的训练 trick**：OPD 后与通用 post-trained checkpoint 做一次等权参数空间 merge，再进入
  GRPO，能显著缓解领域训练遗忘；单 checkpoint 用 4:1 thinking/non-thinking 配比同时支持低延迟与深度推理，适合推荐/搜索
  Agent 中快速判断和复杂推理并存。

  - **轻量模型落地**：0.8B/2B 领域模型通过 CPT+蒸馏仍能获得强电商和通用能力，适合边缘/实时商品识别、SKU 匹配和标题生成；可借鉴其小模型用大模型
  teacher 的配对策略。

  - **评测框架设计**：按真实业务工作流拆成8个场景，明确输入、决策目标、评分规则，尤其包含变体级检索/匹配（250g vs 500g vs two-pack）和直播帧商品定位；业务团队可对应自建内部
  benchmark，避免只测通用 VQA。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**
电商商品常以多视图、详情长图、直播帧呈现，关键证据如卖点、净含量、认证标识只出现在图片内部；模型必须把视觉文本链接到具体 SKU 变体，并满足平台治理规则的约束。同时，面向电商做领域化不能牺牲通用视觉与推理能力，尤其是轻量部署模型。

**方法关键点**
- 模型家族：从 Qwen3.5 初始化，覆盖 0.8B/2B/4B/9B dense 和 35B-A3B MoE 五个尺度，全参数训练。
- 两阶段 CPT：阶段1 370.3B tokens，电商占比45.8%；阶段2 76.7B tokens，电商占比61.1%，上下文从16K扩至32K。电商数据强调变体级粒度、可追溯证据、规则条件输出；通用池保留 OCR/文档/grounding/STEM。
- 后训练：混合思维 On-Policy Distillation（OPD）+ 与 post-trained Qwen3.5 的等权参数空间 merge + GRPO。OPD teacher 按模型尺度分配；单 checkpoint 通过 4:1 thinking/non-thinking 配比同时支持两种模式。
- 评测：构建 28 个电商基准（23内部+5公开）共 207,117 实例，覆盖 Product OCR/Grounding/Knowledge/Attributes/Retrieval/Moderation/Reasoning/Open 八个场景，另配 64 个通用基准。

**关键结果**
- WeMM-Ecom-35B-A3B 电商总分 74.4，超过 Qwen3.8-Flash-Next 73.2、HY4 72.1、DeepSeek-V4.1-Flash-1017 69.1，参数量少 5-22 倍。
- WeMM-Ecom-9B 超越 3 倍大的 Qwen3.8-27B；较同尺寸 Qwen3.5-9B 电商提升 5.2/6.4 分。
- 所有五个尺度在电商上均超同尺寸 Qwen3.5，0.8B/2B 非思维模式提升 +15.5/+12.3 分。
- 通用 64 基准上，35B-A3B 非思维 72.6 超 Qwen3.5-35B-A3B 的 71.0；2B 在轻量模型中综合第一。
- 生产已服务微信电商数百场景，日请求十亿级。

**最值得记住的一句话**：领域 CPT 保留足够通用数据，并在后训练后用一次参数空间 merge 恢复通用先验，是电商专精与通用能力兼得的关键。
