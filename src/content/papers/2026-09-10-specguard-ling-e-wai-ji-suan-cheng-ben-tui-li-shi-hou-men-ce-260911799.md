---
title: 'SpecGuard: Inference-Time Backdoor Detection For Free'
title_zh: SpecGuard：零额外计算成本推理时后门检测
authors:
- Rui Wen
- Ahmed Salem
- Andrew Paverd
- Mark Russinovich
- Zheng Li
affiliations:
- Institute of Science Tokyo
- Microsoft Security Response Center
- Microsoft Azure
- Shandong University
arxiv_id: '2609.11799'
url: https://arxiv.org/abs/2609.11799
pdf_url: https://arxiv.org/pdf/2609.11799
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: LLM 后门检测 · 投机解码
tags:
- Speculative Decoding
- Backdoor Detection
- LLM Security
- Inference-time
- Model Safety
one_liner: 利用投机解码中的草稿token接受率变化，实现零额外计算成本的LLM推理时后门检测
practical_value: '- 若线上 LLM 推理服务（如生成式推荐文案、Agent 工具调用）已启用投机解码，可几乎零成本监控“草稿 token 接受率”异常波动，作为模型行为突变或后门触发的预警信号，无需额外模型前向。

  - “干净小模型作参照”的思路可迁移到推荐模型监控：用训练冻结的干净基线模型对比线上微调模型的输出分布，捕捉因数据投毒或环境漂移导致的异常行为，尤其是对用户输入中的罕见/语义触发模式。

  - 工程实现上，接受率是一个标量，计算开销极低，适合部署在 gateway 或 serving 层；但接受率受输入难度影响，应结合分位数或滑动窗口做自适应阈值，避免正常长尾输入引发误报。

  - 业务可借鉴点有限：后门检测主要服务于 AI 供应链安全，电商推荐团队若无第三方模型微调部署场景，直接迁移价值不大。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
LLM 常从第三方微调、共享或下载，可能被植入后门：正常输入表现正常，遇到秘密触发才切换为攻击者行为。部署前审计难以覆盖所有触发形式，尤其是隐蔽触发；而现有推理时检测器要么依赖触发形式假设，要么需要额外模型计算（输入扰动或额外生成），与延迟敏感的 LLM serving 冲突。

**方法关键点**
SpecGuard 复用投机解码机制：用小型 draft model 提出 token，target model 验证并接受或拒绝。观察到当后门被触发时，target model 输出向攻击者行为偏移，而干净的 draft model 不会预测该偏移，导致 draft token 接受率发生变化。该信号在验证过程中自然产生，无需额外模型计算。论文形式化了信号出现的条件，并证明攻击者若想抑制该信号，必须同时削弱后门效果。

**关键结果**
在多种后门类型和模型家族上，SpecGuard 能可靠检测触发行为，包括输入级过滤器失效的 stealthy 情形；与现有检测器相比，不引入额外生成成本，适合在线持续监控。
