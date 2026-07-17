---
title: 'Boogu-Image-0.1: Boosting Open-Source Unified Multimodal Understanding and
  Generation'
title_zh: Boogu-Image-0.1：开源统一多模态理解与生成模型
authors:
- Guoxuan Chen
- Chufeng Xiao
- Haoran Yang
- Siyue Xie
- Binxiao Huang
- Ming Zhang
- Cheuk Him Chau
- Xinyu Fu
- Yingzhao Lian
- Tom S. Y. Li
arxiv_id: '2607.13125'
url: https://arxiv.org/abs/2607.13125
pdf_url: https://arxiv.org/pdf/2607.13125
published: '2026-07-13'
collected: '2026-07-17'
category: Multimodal
direction: 统一多模态理解与生成
tags:
- multimodal
- text-to-image
- open-source
- agentic inference
- bilingual
- low-cost training
one_liner: 通过数据/训练管线优化和Agent式推理扩展，在极低计算预算下实现逼近闭源的多模态生成性能
practical_value: '- **Agent式推理扩展用于线上服务**：将推理时间计算量化为可控资源，通过增加推理步数提升生成质量，该范式可直接用于Agent推荐系统的多步决策、query生成等，在延时允许下动态扩展推理深度提升效果。

  - **数据效率与成本控制**：仅用2.08亿图片达到领先性能，训练成本压到40万美元。在推荐系统中，可借鉴其数据筛选、去重、质量过滤的流程，用小规模高质量多模态数据对齐用户偏好，降低数据采集成本。

  - **多模态生成能力迁移至商品创意**：模型支持高质量文本渲染和中文生成，可直接用于广告创意、商品海报、营销图片的自动生成，将生成式推荐从物品ID扩展到视觉内容创造。

  - **开源与可重现性**：提供全套训练代码与权重，推荐团队可基于此快速搭建企业级多模态生成服务，并融入检索增强或个性化微调，避免依赖黑盒API。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：闭源多模态系统（如GPT-Image-2）性能领先但实现细节不公开，开源方案在统一理解与生成任务上存在差距。本工作探索在极有限计算资源下（仅约2亿张训练图片、4万美元成本）能否通过针对性的训练改进和推理策略，大幅提升开源模型的竞争力。

**方法关键点**：
1. **模型架构与理解增强**：基于统一的多模态架构，强化模型对文本与图像的对齐理解，支持中英双语指令与文字渲染。
2. **数据质量优先**：精心筛选与清洗训练数据，仅使用208.62M独特图片，强调数据质量远重于数量，有效降低训练成本。
3. **训练流水线优化**：设计多阶段训练策略，平衡生成质量、速度与编辑能力，推出Base、Turbo、Edit等4个变体。
4. **Agent式推理时扩展**：通过引入“思考”步骤（Thinking mode），在推理时动态增加计算量，以可控的时间代价换取生成质量的提升，模拟系统级集成中的多步优化。

**关键结果**：
- Boogu-Arena评测中，Turbo-Thinking版本ELO分数1048，超越所有开源模型，接近GPT-Image-2（1196）和Nano-Banana-Pro（1087）。
- 推理时间与质量可平滑折中：Turbo-Thinking相比Turbo提升明显，仅在模型内实现，无需外部组件。
- 仅用208.62M图片，基础模型训练理论成本约$400K，证明高效开源路线的可行性。
