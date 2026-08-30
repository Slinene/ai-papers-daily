---
title: 'Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans'
title_zh: Super Star：面向数字人的流式实时交互智能体
authors:
- Wentao Jiang
- Youchen Xie
- Haidi Fan
- Yajing Chen
- Xin Wang
- Ye Shi
- Jingya Wang
affiliations:
- ShanghaiTech University
- LIGHTSPEED
arxiv_id: '2608.24909'
url: https://arxiv.org/abs/2608.24909
pdf_url: https://arxiv.org/pdf/2608.24909
published: '2026-07-21'
collected: '2026-08-30'
category: Multimodal
direction: 多模态生成 · 实时交互数字人
tags:
- Co-speech Gesture
- Streaming
- Autoregressive Model
- Self-evolving
- Digital Human
one_liner: 提出因果多模态自回归模型与自进化数据闭环，实现数字人低延迟在线语音同步手势生成
practical_value: '- **实时流式生成范式**：在需要低延迟在线生成的场景（如对话式推荐、实时文案/回复生成、虚拟主播）可借鉴“仅用当前与历史信息”的因果模型设计，避免依赖未来信息，降低首字/首帧延迟。

  - **自进化训练闭环**：将在线交互中收集的用户反馈纳入数据生成与模型迭代，使系统持续适应用户偏好，这对电商导购 Agent、交互式推荐等长期在线服务有直接可迁移价值，但需设计反馈去噪与延迟更新机制。

  - **数据合成管线**：利用主题/情感感知的语料构建多样化对话，再条件生成训练数据，可用于解决交互式推荐或导购场景中高质量多轮对话数据不足的问题。

  - **工程实现参考**：流式多模态推理与缓存/增量计算的设计思路，可迁移到需要实时聚合文本、语音、用户行为等多路信号的 Agent 架构中。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 co-speech 手势生成多为离线方法，依赖完整语音片段，无法满足真实交互数字人在严格延迟约束下仅用当前响应音频在线生成手势的需求。

**方法关键点**：
- 提出 Super Star 框架，将流式语音响应模块与在线手势生成模块耦合，实现端到端实时交互。
- 手势生成器设计为因果多模态自回归模型，输入流式响应语音与运动历史，预测当前身体姿态，无需未来语音信息，从架构上保证低延迟与语音-动作对齐。
- 针对虚拟陪伴场景，构建离线数据合成管线：使用主题与情感感知的语料生成多样人机对话，并条件化生成相应的 co-speech 手势。
- 建立自进化训练回路：将在线交互中收集的用户反馈融入数据生成过程，使模型在部署后持续适应用户偏好，缩小离线数据与在线部署之间的分布差距。

**关键结果**：实验表明该框架在延迟-质量权衡、语音-动作同步性以及用户偏好上均优于现有基线方法，验证了流式因果建模与自进化数据闭环的有效性（论文未给出具体量化指标）。
