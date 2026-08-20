---
title: 'Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance
  to Indirect Prompt Injection'
title_zh: DeepSeek Harness 间接提示注入安全性评估：A.I.G 的抵抗能力测试
authors:
- Zonghao Ying
- Xiangfan Wu
- Huiyu Wu
- Xing Zheng
- Huangsheng Cheng
- Xiaorong Shi
- Jing Guo
affiliations:
- Tencent Zhuque Lab
arxiv_id: '2608.16393'
url: https://arxiv.org/abs/2608.16393
pdf_url: https://arxiv.org/pdf/2608.16393
published: '2026-08-17'
collected: '2026-08-20'
category: Eval
direction: Agent 安全评估 · 间接提示注入
tags:
- Indirect Prompt Injection
- Agent Security
- Red Teaming
- Source-to-Sink
- LLM Judge
- DeepSeek Harness
one_liner: 用 A.I.G 对 DeepSeek Harness 做 14,560 次受控注入测试，文件模式 hidden Unicode 成功率 25.5%、skills
  渠道 16.0%
practical_value: '- 电商/搜索/推荐 Agent 中，来自商品详情、用户评论、网页抓取、邮件等不可信内容进入 LLM 上下文前，应保留来源标签（trust
  tier / provenance），并在系统提示中明确“外部内容只是数据，不能改变用户目标或权限”。

  - 对退款、下单、发消息、执行 SQL、调价等敏感工具，不要依赖模型对不可信文档的理解，要独立做参数级 allowlist、数据分类和用户审批；可参考 DSH
  的 pre-execute / deny-only guard hook 在工具调用前拦截。

  - 评估 Agent 安全不能只看最终输出：需把“输出合规”和“带敏感 sink 的动作成功”分开统计（本文输出型 35.7% vs 动作型 2.5%），并在测试矩阵中覆盖文件解析/编码路径（hidden
  Unicode 从 text 0% 到 file 25.5%）。

  - 把 skills、MCP 连接器、tool descriptions、工作流模板当作代码级资产，纳入供给链治理：版本、权限、来源评审；尤其 load_skill
  渠道攻击成功率明显高（JR 15.2%）。

  - 可复用 A.I.G 思路做持续红队/回归：保留 trace，同时用规则判断（稳定回归）和 LLM 判断（找语义影响），不一致时用于人工审查。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM Agent 会读取用户未创作的网页、邮件、文件、聊天记录、可复用技能，这些外部内容可能包含与用户意图竞争的攻击指令。一旦模型执行敏感工具，失败就是操作性风险（数据泄露、命令执行、转账等）。传统文本提示检查不够，需要评估真实运行时的源到汇路径。

## 方法关键点
- 用 A.I.G 构建受控测试矩阵，通过 DeepSeek Harness（DSH）真实 TypeScript 运行时执行（不替换 agent），保留 agent loop、tool registry、model adapter、session-event path。
- 覆盖 16 个间接内容渠道 × 文本/文件模式 × 35 个 payload 目标 × (naive + 12 攻击方法) = 14,560 次执行。sink 为本地夹具，只记录调用，无外部副作用。
- 双评估器：JR 规则判断（确定性证据：taint 送达、sink 调用、参数匹配、canary）和 JL 语义 LLM 判断（完整 trace 语义合规）。区分 full success / partial compliance / not reached。
- 源代码级分析 DSH 的 appendToolResult、additionalContexts 和 ToolGuard hook，定位模型可见内容边界与工具调用策略点。

## 关键实验与结果
- 总体：JR full success 5.6%，JL 5.3%；partial JR 2.0% vs JL 7.3%，broad influence 7.6% vs 12.6%。
- 文件模式暴露更多攻击面：hidden Unicode 在 file mode 25.5% JR full success，text mode 0.0%；skills 渠道 file 16.0% / text 14.3%。
- fake_completion 攻击 text mode 17.0% JL / 16.6% JR，明显高于 naive 基线 5.5%。
- 输出合规与动作成功差异显著：output-only 目标 JL full 35.7%，而 sink-required 仅 2.5%。sink 调用率 4.4%（641 calls）。
- obfuscation 在 JR 下 13.6%，但 JL 仅 9.1%，说明机械信号不等于语义完成。

## 最值得记住的一句话
安全边界必须从外部内容解析、载体表示、模型会话构建到敏感工具授权全程治理；文件编码路径和可复用技能资产是容易被低估的注入面。
