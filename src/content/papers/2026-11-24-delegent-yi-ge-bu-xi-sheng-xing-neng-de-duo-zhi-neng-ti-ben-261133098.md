---
title: 'Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance'
title_zh: Delegent：一个不牺牲性能的多智能体降本框架
authors:
- Lingwei Gu
- Jimmy Lin
affiliations:
- University of Waterloo
arxiv_id: '2611.33098'
url: https://arxiv.org/abs/2611.33098
pdf_url: https://arxiv.org/pdf/2611.33098
published: '2026-11-24'
collected: '2026-11-25'
category: MultiAgent
direction: Agent 多智能体协作降本
tags:
- multi-agent
- SLM
- cost reduction
- agentic coding
- agentic search
- delegation
one_liner: 前沿模型主导任务，把易子任务委托给本地 SLM，在 coding 和搜索智能体上成本降 59%-67% 且性能不降
practical_value: '- **电商搜索/问答 Agent 架构借鉴**：让 frontier LLM 只做最终推荐、排序或答案生成，把商品详情解析、评论证据抽取、候选召回验证、活动规则查询等大量读取类子任务委托给本地
  SLM。按角色路由模型调用，不训练 router，frontier 始终掌握最终决策权，业务可控且成本大幅下降。

  - **用短指令改变模型行为**：在 system prompt / 配置中明确告诉主模型“每多一步都会重读上下文，最便宜的计划是减少自己的工具调用”，要求它把工具密集型子任务委托出去、并发放置独立子任务、子报告不超过
  150 字、禁用维护任务清单。这种 prompt 级干预可以在不改模型的情况下显著降低主模型调用次数。

  - **只回传结构化报告并自动校验证据**：让子代理返回带来源、行号、置信度的短报告，而不是原始工具输出；harness 对引用的证据做 verbatim 校验。这适用于商品问答、政策咨询等对事实性要求高的业务，能减少主模型上下文膨胀和幻觉传播。

  - **工程上重视 prompt cache**：frontier 使用稳定 cache key，SLM 子代理绑定 GPU replica 缓存前缀，可显著降低长程任务成本。即使
  2B 级本地模型也能承担搜索、读文件、跑测试等 legwork，适合在已有 GPU 资源上落地。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

Agent 运行中，frontier 模型每一步都要重读整个上下文，且所有子任务无论难易都用同一个昂贵模型执行，导致长程 Agent 成本极高。但大量工作是查找代码、复现 bug、跑测试、读文档等容易的 legwork，不需要 frontier 模型。自然的问题是：能否把这类子任务委托给本地小模型，从而大幅降低成本而不损失任务表现。

**方法关键点**

Delegent 是一个基于 Claude Code 的 multi-agent harness，核心思想是让 frontier 模型始终主导任务，只把聚焦的子任务交给本地 SLM 执行。

- 按角色路由：主循环调用 frontier 模型，子代理和辅助模型调用 SLM；不训练 router，模型可自由替换。
- Coding 场景：frontier 通过 Agent tool 写 brief 派发子任务，SLM 子代理负责搜索代码、读文件、跑测试、复现 bug；主模型自己负责改代码。
- Search 场景：新增 Delegate tool，借用 AREX-Turbo 的 prompts/tools；SLM 子代理搜索语料、访问文档、压缩历史，返回答案、证据和置信度；harness 自动校验证据是否在原文中逐字出现。
- 短指令引导：告诉 frontier 模型经济账，要求委托工具密集型工作、限制报告长度、并发放置独立子任务、不要维护任务清单、对子代理报告做事实核查。
- 工程细节：frontier 调用保持稳定 prompt-cache key；SLM 通过 vLLM 服务，每个子代理绑定一个 GPU replica 以缓存前缀。

**关键实验**

- Coding：在 SWE-bench Verified、SWE-bench Pro、DeepSWE 上，GPT-6.1-Sol + Qwen3.8-27B-FP8 的方案在解决任务数不下降的情况下，frontier 成本在 DeepSWE 上从 $2.11/任务 降到 $0.70/任务，相对成本 33%；MiniCPM5-2B 也达到 34% 相对成本。
- Search：在 694 个搜索问题上，frontier 模型加 Qwen3.8-27B-FP8 正确回答 663 个，与单独运行时完全相同，但平均 frontier 成本降到 41%；在 ClimbMix 语料上成本降至 25%-31%，在 BrowseComp-Plus 自有语料上仅降至 63%。
- 消融：没有短指令时，弱 SLM 会掉点；短指令约贡献 3/5 节省，SLM 替换贡献 2/5。不同 frontier 模型节省幅度不同：GPT-6.1-Sol 长循环风格节省最多，Claude Opus 5.5 计划型只降到 69%。

**最值得记住的一句话**

在 Delegent 中，frontier 模型始终主导并给出最终答案，只把寻找、验证、跑测试等 legwork 委托给本地 SLM，无需训练即可在长程 coding 和 agentic search 上把 frontier 成本降到 1/3 到 41%，且任务表现不降。
