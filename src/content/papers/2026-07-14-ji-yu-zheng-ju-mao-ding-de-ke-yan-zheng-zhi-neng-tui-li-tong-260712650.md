---
title: 'Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM
  Hallucination in Empirical Inference via Tool-Attested Kernel Proofs'
title_zh: 基于证据锚定的可验证智能推理：通过工具见证内核证明消除LLM幻觉
authors:
- Junyu Ren
arxiv_id: '2607.12650'
url: https://arxiv.org/abs/2607.12650
pdf_url: https://arxiv.org/pdf/2607.12650
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: LLM推理验证 · 证据锚定
tags:
- LLM Hallucination
- Formal Verification
- Lean Theorem Prover
- Agentic Reasoning
- Audit Trail
- Evidence-Grounded
one_liner: 提出 EG-VAR 架构，用 Lean 证明内核确保 LLM 推理每一步有可靠证据来源，实现 100% 验证精度。
practical_value: '- 借鉴证据锚定思想：在电商搜索推荐 Agent 生成关键结论（如商品合规性判断、敏感推荐理由）时，强制输出附带数据源引用与验证链，减少幻觉风险

  - 轻量级审计机制：可简化 Lean 形式化验证，用规则引擎或数据库约束替代，对 Agent 输出关键字段做一致性检查并记录追溯日志

  - 分层设计思路：将高风险决策（如广告内容审核）剥离为独立验证模块，普通 LLM 调用保留灵活性，形成“主推理 + 形式化 sidecar”架构

  - 错误处理模式：明确区分“可验证断言”与“放弃输出”，避免 Agent 生成无法验证的内容，提升系统整体可信度'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：工具访问本身无法保证 LLM 实证推理可控——输出可能缺乏可验证证据，推理链经不起严格审查。

方法：提出 EG-VAR（Evidence-Grounded Verified Agentic Reasoning），将 Lean 4 证明内核作为唯一验证声明签发者，强制每个输出必须满足两个条件：（1）声明来源于已验证的工具调用；（2）推理链经过内核检查有效。不符合则输出 Abstain 并留下可重放审计轨迹。LLM 在此架构中充当形式化转换器，将自然语言命题转化为 Lean 可处理的形式。

关键结果：在 TableBench 数值推理子集（n=120）上，EG-VAR 取得 120/120 全对，相同工具基线仅 95%；在反事实压力测试（5 领域 × 2 模型）中，EG-VAR 保持 100% 源忠实度，而相同工具降至 80-90%（无工具 50-80%）。语义形式化错误率 Sonnet 3.3%，Opus 1.7%。该架构彻底消除了未经验证的输出，将形式化错误、源权威争议等明确化为审计目标，为高风险场景提供可治理接口。
