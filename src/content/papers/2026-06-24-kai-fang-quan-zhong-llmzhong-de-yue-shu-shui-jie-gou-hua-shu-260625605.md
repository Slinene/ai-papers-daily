---
title: 'Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression
  Under Structured Output Constraints'
title_zh: 开放权重LLM中的约束税：结构化输出导致工具调用抑制的实证研究
authors:
- Fangzheng Li
- Aimin Zhang
- Chen Lv
affiliations:
- Focus AI Center, Focus Technology Co., Ltd.
- Nanjing University of Science and Technology
arxiv_id: '2606.25605'
url: https://arxiv.org/abs/2606.25605
pdf_url: https://arxiv.org/pdf/2606.25605
published: '2026-06-24'
collected: '2026-06-25'
category: Agent
direction: Agent工具调用与结构化输出约束交互
tags:
- Tool Suppression
- Structured Output
- Constrained Decoding
- Open-Weight LLM
- Agent Systems
- Grammar Masking
one_liner: 多个开源模型在工具调用与JSON Schema约束共存时工具调用被完全抑制，根因是语法解码掩码排除工具token，并提出两阶段执行缓解
practical_value: '- 在电商/推荐Agent中，若同时启用工具调用（如检索数据库、调用API）与JSON Schema结构化输出，需警惕工具调用被静默抑制的风险。生产环境可考虑解耦：先执行工具调用获取结果，再让模型生成符合schema的最终回复，避免约束在解码层互相冲突。

  - 推理框架选型时注意：SGLang/vLLM等通过语法掩码强制schema合规，会从logits层面排除工具调用token（如XML标签的`<`）。若必须同时约束，可探索允许工具调用token的混合语法，或使用非掩码的schema引导（如仅靠prompt约束）。

  - 评估Agent系统不能仅独立测试工具使用和格式合规。必须设计联合约束下的端到端成功率测试，监控工具调用率与抑制率，防止上线后出现“格式合规但未获取外部数据”的隐性失效。

  - 微调（SFT、GRPO等）无法绕过掩码层限制，因为权重优化在掩码之前。该发现表明，常规对齐手段无法解决此问题，需要从推理栈层面进行工程化防护。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
在生产Agent系统中，工具调用（Tool Calling）与结构化输出（Structured Output，如JSON Schema）常被同时激活，但两者交互缺乏研究。作者在真实部署中发现，当同时启用时，多个开放权重模型完全停止调用工具，尽管仍能生成符合schema的输出——这一现象被定义为工具抑制（Tool Suppression）。传统评估分开测试，忽略了联合约束下Agent动作执行的可靠性。

## 方法
- 设计三条件对照实验：T1（仅工具）、T2（工具+Schema约束）、T3（仅Schema），在7个模型（涵盖MoE、混合架构，20B~397B参数）和两种推理框架（SGLang、vLLM）上测试。
- 构建5类需要外部信息获取的业务任务，统一Prompt和工具定义，记录工具调用率（TIR）、抑制率（SR）、JSON合规率。
- 对推理栈逐层追踪，发现JSON Schema通过xgrammar编译为有限状态机，并在每步解码应用词汇掩码，将非JSON token（包括`<tool_call>`标签）的logits设为-∞，使工具调用token不可达。
- 提出行为假说——约束优先反转（CPI），认为模型在多重约束下优先满足Schema，牺牲工具执行。
- 提出透明两阶段执行（Transparent Two-Pass Execution）：先将工具调用与结构化输出解耦，分别独立处理，无需重训模型。

## 关键结果
- **完全抑制**：所有被测开源模型在T2条件下TIR均为0%，SR为100%；T1和T3下功能正常。
- **消融实验**：改变Schema复杂度（1~20+字段）、工具强制策略（包括`tool_choice="required"`）、部署环境、微调（SFT/GRPO，最多6000样本）均无法消除抑制。
- **根因确认**：语法掩码使得以`<`开头的工具调用标签在任何JSON FSM状态下均被不可达，权重层面的优化无法绕过掩码。
- **缓解效果**：两阶段执行方案恢复工具调用，同时保持结构化输出合规。

最值得记住的一点：**“当JSON Schema约束通过语法掩码强制执行时，工具调用token被硬性排除，即使模型认识到工具需求也无法实际执行，这是推理栈层面的系统性故障。”**
