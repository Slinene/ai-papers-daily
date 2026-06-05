---
title: 'DAR: Deontic Reasoning with Agentic Harnesses'
title_zh: DAR：基于Agent Harness的按需法规推理
authors:
- Guangyao Dou
- William Jurayj
- Nils Holzenberger
- Benjamin Van Durme
affiliations:
- Johns Hopkins University
- Télécom Paris
- Institut Polytechnique de Paris
arxiv_id: '2606.05009'
url: https://arxiv.org/abs/2606.05009
pdf_url: https://arxiv.org/pdf/2606.05009
published: '2026-06-02'
collected: '2026-06-05'
category: Agent
direction: Agent推理中的法规按需交互
tags:
- Deontic Reasoning
- Agentic Harness
- LLM
- Tool Use
- Reasoning Benchmark
- Capability Amplifier
one_liner: 提出让LLM按需检索法规的Agent推理框架DAR，揭示Harness仅放大已有能力：前沿模型获益，弱模型退化并消耗更多token。
practical_value: '- 在需要依据长文档规则（如电商政策、合规条款）进行推理的Agent场景，将规则文件外置，让模型通过grep/sed等工具按需检索关键段落，比一次性全量注入prompt更高效，尤其适合强模型。

  - 模型选型启示：仅足够强的基座模型（如GPT-5、Claude）能从工具交互中稳定获益；弱模型在同样的harness下反而性能下降且token消耗倍增（达4×），部署前务必评估基座能力与harness的匹配度。

  - Harness设计可借鉴Terminus-KIRA的思路：增加完成校验、防止提前提交、支持观察新信息后修订计划等机制，显著提升多步推理Agent的可靠性，避免模型过早给出错误答案。

  - 在工程实现中，需对Agent设置严格的时间与token预算，并监控超时与解析失败；开源模型主要失败于超时（占比达10.6%），合理的资源控制能避免无效算力浪费。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM在需要依据长文本、交叉引用密集的法规（如税法、移民政策）进行道义推理时，即使把全部规则塞进上下文，仍可能遗漏关键条款并推导错误。近期Agent搜索工作表明，让模型通过通用工具（grep、sed）按需检索长文档，比静态全量给入更能发挥其能力。本文探索这一范式在道义推理上的效果，提出Deontic Agentic Reasoning（DAR）框架。

## 方法关键点
- **DAR设置**：将法规作为文件（statute.txt）放入沙箱，模型通过终端工具（grep、sed、cat、Python）按需读取条款，而非一次接收全部规则。
- **实验设计**：在DeonticBench的四个硬子集（税法数值计算、二元蕴涵判断、航空行李费规则、移民上诉预测）上，对比直接求解与多种Agent Harness（Terminus-2、Terminus-KIRA、Codex CLI、Claude Code）。
- **模型矩阵**：覆盖9个模型，包括Qwen系列（35B–397B）、GPT-5.1/5.2、Claude Sonnet 4.5等，开源模型通过vLLM部署或OpenRouter API访问。

## 关键结果
- **前沿模型显著受益**：在Terminus-KIRA下，GPT-5.2在SARA-Numeric准确率从30%跃升至60%，Claude Sonnet 4.5从36%升至54%；在Airline任务上GPT-5.1保持86%高准确率。
- **开源模型大幅退化**：同样harness下，Qwen3.5-35B在SARA-Numeric从34%跌至11%，所有开源模型在Airline上趋近于零，平均token消耗却增至4倍（如Qwen3.5-122B达401k/次）。
- **Harness效应不对称**：Terminus-KIRA对强模型最优，Claude Code对部分开源模型有一定帮助，但整体上Agent Harness是“能力放大器”，无法弥补基座能力的不足。

## 一句话结论
Agent Harness为强大模型解锁了静态上下文中被埋没的推理能力，但将其套用到弱模型上只会放大错误并浪费计算，是典型的能力放大器而非万能药。
