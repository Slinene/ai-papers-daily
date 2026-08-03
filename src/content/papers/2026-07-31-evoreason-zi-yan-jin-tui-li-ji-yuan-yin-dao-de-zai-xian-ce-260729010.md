---
title: 'EvoReason: Self-Evolving Reasoning Primitive-Guided On-Policy Distillation
  for Latent Reasoning in Generative Recommendation'
title_zh: EvoReason：自演进推理基元引导的在线策略蒸馏用于生成式推荐潜在推理
authors:
- Zhuang Zhuang
- Zhipeng Wei
- Rongfeng Guo
- Shijie Li
- Peng Zhao
- Jie Chen
- Fei Pan
affiliations:
- Kuaishou Technology
- Shenzhen University
arxiv_id: '2607.29010'
url: https://arxiv.org/abs/2607.29010
pdf_url: https://arxiv.org/pdf/2607.29010
published: '2026-07-31'
collected: '2026-08-03'
category: GenRec
direction: 生成式推荐·潜在推理·在线策略蒸馏
tags:
- Latent Reasoning
- On-Policy Distillation
- Generative Recommendation
- Semantic ID
- Reasoning Primitives
- Self-Evolving
one_liner: 提取可复用推理原语并自演进，引导结构化链式思考，通过在线蒸馏将推理能力迁移到潜在表示，实现高效生成式推荐。
practical_value: '- 借鉴从 Agent 轨迹中诱导推理原语的方法，将复杂用户意图推理拆解为可复用的函数式工具（如偏好提取、冲突检测），提升 CoT
  稳定性与可解释性，适用电商搜索推荐场景。

  - 在线策略蒸馏机制可将大模型推理能力压缩进轻量潜在表示：通过置信门控过滤低质量监督，KV 缓存对齐将显式推理信息注入潜在空间，线上推理无需生成显式 CoT，延迟极低。

  - 自演进原语库的设计支持根据线上反馈动态更新推理模式，适应电商促销、季节变化等分布迁移，无需全模型重训练。

  - 教师与学生共享 backbone，训练时仅通过额外上下文增强，不引入额外参数，工程实现友好。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐中，LLM 推理能显著提升效果，但显式链式思考（CoT）推理延迟过高。潜在推理是高效替代方案：将推理过程编码为连续表示再输入生成模型，但现有方法直接蒸馏原始CoT轨迹，存在冗余表述、静态监督和不可控推理等问题，导致迁移效率低下。EvoReason 旨在通过可演化的推理原语和在线策略蒸馏，实现精简、自适应的潜在推理迁移。

**方法关键点**：  
- **推理原语发现**：从 ReAct 风格的 agent 推荐轨迹中，提取可复用的推理行为模式，抽象为函数式“伪工具”库，每条原语包含输入输出约束和结构化推理流程。  
- **原语引导的结构化 CoT**：用原语库指导教师模型生成低冗余、高一致性的CoT，替代自由形式的推理链，提供更稳定的监督信号。  
- **自演进在线蒸馏**：学生产生潜在推理轨迹，教师基于学生潜在状态和原语库对轨迹进行修正，生成优化后的 CoT；再通过置信门控的 On-Policy Distillation（OPD）和 KV 缓存对齐，将推理能力蒸馏回学生，原语库随学生行为不断更新，形成闭环。  
- **推理时高效**：学生仅执行潜在推理，无需显式 CoT，延迟接近传统生成式推荐模型。

**关键结果**：在 Amazon Beauty 和 Sports 数据集上，EvoReason 相比最优基线 LASAR 的 Recall@5 分别提升 17.9%（0.0613→0.0724）和 17.1%（0.0561→0.0657），工业数据集提升 15.4%；在线 A/B 测试中，广告主价值提升 8.11%，平台收入提升 6.23%。消融实验证实原语、自演进、OPD 均对性能有显著贡献。

> 最值得记住的一句话：将代理轨迹中的复杂推理抽象为可演化的原语，通过在线策略蒸馏动态对齐潜在空间，为生成式推荐提供了一种低延迟、高性能的推理范式。
