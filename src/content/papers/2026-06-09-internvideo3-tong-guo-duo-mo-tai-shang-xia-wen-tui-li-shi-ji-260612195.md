---
title: 'InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning'
title_zh: InternVideo3：通过多模态上下文推理实现基础模型智能体化
authors:
- Ziang Yan
- Sheng Xia
- Jiashuo Yu
- Yue Wu
- Tianxiang Jiang
- Songze Li
- Kanghui Tian
- Yicheng Xu
- Yinan He
- Kai Chen
affiliations:
- Shanghai AI Laboratory
- Shanghai Innovation Institute
- Nanjing University
arxiv_id: '2606.12195'
url: https://arxiv.org/abs/2606.12195
pdf_url: https://arxiv.org/pdf/2606.12195
published: '2026-06-09'
collected: '2026-06-11'
category: Agent
direction: 多模态 Agent · 长视频推理
tags:
- Multimodal Agent
- Video Understanding
- Long-context
- MCR
- M2LA
- Agentic AI
one_liner: 提出多模态上下文推理（MCR）与多头潜在注意力（M²LA），将开放视频模型推向长程视觉智能体
practical_value: '- **MCR 闭环范式可用于多步商品理解**：将商品多模态信息、用户查询、工具调用结果维护在统一上下文中，递归观察-推理-动作，适合直播切品、复杂选品等需要动态环境交互的场景，可直接借鉴其对证据积累和信念更新的设计。

  - **M²LA 可降低多模态 Agent 的 KV Cache 开销**：通过潜在注意力压缩保留全部视觉 token 的同时减少缓存内存，对于需要长对话历史、多轮商品对比或超长视频分析的电商客服
  Agent 很实用，可尝试类似低秩映射和模态自适应适配器来优化线上成本。

  - **分阶段训练配方可复用**：先通过 M²LA 转换后的 continued pretraining 恢复能力，再用短到长的课程 SFT、基于规则验证的 RL
  和 on-policy 蒸馏，这种组合对公开基座模型增强长程推理和工具使用能力路径清晰，适合在自身业务基座上微调推理能力。

  - **层次化记忆与递归验证可提升回答可靠性**：论文中的分层记忆（帧/片段/场景）、问题路由、检索与自我验证机制，可用于商品视频问答或导购 Agent 中，降低幻觉并强制答案有据可依，特别是遇到不确定时重新检索证据再修正答案的思路值得实现。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：开放模型在文本主导的智能体任务上已有长足进步，但在视频等长程多模态场景中仍以单次问答为主，缺乏持续观察、工具交互、证据积累与验证的能力。真实世界的长视频分析、监控回顾、自我中心感知等任务需要模型在长时序中动态推理，这正是多模态智能体的核心挑战。

**方法关键点**：
- **多模态上下文推理（MCR）**：将观察、推理过程、工具动作、反馈和记忆统一在一个动态上下文中，实现闭环的“观察-推理-动作-反馈-更新信念”流程，而非单次推断。
- **M²LA 高效注意力**：将 KV Cache 从按头存储改为按潜在向量压缩存储，在解码时动态重建多头键值，同时通过 RoPE 感知聚合、低秩分解和模态自适应处理，在保留全部视觉 token 的情况下大幅降低内存，支撑更长 rollout。
- **分阶段训练**：M²LA 转换后进行 continued pretraining 恢复能力；短到长短课程 SFT（至 256k token 上下文）；在可验证任务（视频 QA、时间定位）上用规则奖励的组序列策略优化（GSPO）做 RL；最后用 on-policy 蒸馏从更强教师模型（Qwen3‑235B）迁移复杂推理行为。
- **数据**：构建了大规模长视频 SFT 数据集（379K 视频，平均 15.8 分钟），通过层次化注释（片段字幕→场景汇总→全局叙事）合成逾 100 万 QA 对，覆盖感知、时空推理、事件链和全局语义。

**关键结果**：
- 在 **Video‑MME 上达 73.8**，MLVU 上 **77.3**，VRBench **69.4**，EgoSchema **76.6**，均为开源模型中最佳，相比上一代 InternVideo2.5‑7B 提升显著（如 Video‑MME +8.7，EgoSchema +12.7）。
- 短视频综合平均得分 **69.0**（NextQA 85.5，PerceptionTest 81.4），超越所有同规模开源基线，证明长程优化未损害短程能力。
- 视频 Agent 实例中，结合检索和递归验证能产生更稳健的证据支撑推断。

**核心价值**：通过“压缩注意力缓存 + 闭环上下文推理 + 强化学习与蒸馏”的组合，把 8B 规模开放模型提升到接近甚至超越某些大闭源模型的水平，为构建实用长程视觉 agent 提供了高效的架构和训练方案。
