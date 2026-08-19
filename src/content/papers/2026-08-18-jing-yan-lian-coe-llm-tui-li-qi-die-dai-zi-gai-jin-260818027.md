---
title: Chain-of-Experience for Continual LLM Improvement
title_zh: 经验链 CoE：LLM 推理期迭代自改进
authors:
- Haoqin Tu
- Yunhao Fang
- Yizhong Wang
- Cihang Xie
- Shen Yan
affiliations:
- UC Santa Cruz
- Bytedance Seed
arxiv_id: '2608.18027'
url: https://arxiv.org/abs/2608.18027
pdf_url: https://arxiv.org/pdf/2608.18027
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM 推理期迭代学习 · 反馈驱动 test-time scaling
tags:
- Chain-of-Experience
- test-time learning
- self-feedback
- LLM reasoning
- inference-time scaling
- feedback-driven
one_liner: 系统证明让 LLM 在推理期用执行/自评/正确性反馈迭代累积经验，可稳定超越零样本与跨任务记忆基线，且成本更低
practical_value: '- 在电商/广告的 LLM Agent 流程（query 生成、素材文案、商品属性清洗、选品分析）中，可把单次生成改为 2-10
  轮 self-refine：每轮用轻量 evaluator/reward model 或规则信号（类目一致性、格式、点击/转化预估）给反馈，并将前几轮 response+feedback
  原样拼入 context；20 轮内大部分收益就到手，API 成本可能反而下降。

  - 不要急着把交互历史蒸馏成抽象 memory（类 DC/ACE 的跨任务 cheatsheet）或只保留最终答案；论文表明在同任务内 full experience
  trail 比压缩 memory 更优，激进压缩会丢中间 reasoning。线上 Agent 日志建议先存原始 trajectory，再按需做 retrieval/摘要。

  - feedback 质量依赖 verifier 能力：模型自评不适合小/弱模型，业务上可先用强模型做 critic，或配合规则/执行结果（SQL 可运行、页面可解析、价格库存合法）；对噪声反馈用
  selective majority voting 提高鲁棒性。

  - 测试时改进能力与 base 性能正相关。线上预算有限时，优先给强模型加反馈回路，而不是无差别扩展；弱模型先提升 base 任务能力。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：人类能从经验持续学习，但部署后的 LLM 通常固定权重、每次推理孤立，浪费解题过程中的反馈。现有 test-time 方法如 CoT、多数投票、Reflexion 多把经验压缩成单答案或浅层使用；跨任务记忆 DC/ACE 在强推理模型上也不一定可靠。该工作把整条迭代解题历史视为 experience，系统研究反馈驱动的推理期改进。

**方法关键点**：
- 定义 Chain-of-Experience (CoE)：a_t ~ P(a_t | Q, e_0...e_{t-1})，其中 e_i=(a_i, f_i)，模型反复与环境互动并累积经验。
- 反馈谱系：无反馈、execution feedback（代码执行/单测结果）、model feedback（LLM-as-judge）、correctness feedback（二值正确性，作为高信号上界）。
- 评估 8 个模型（GPT-5、GPT-5-mini、o3、o4-mini、Gemini-2.5 Pro、Claude 4.5 Sonnet 等）在 6 个 benchmark：AIME 2025、OmniMath、LiveCodeBench V6、LiveBench Code、EvaLearn、GPQA Diamond。
- 与 ICL、Dynamic CheatSheet (DC)、Agentic Context Engineering (ACE)、不同 reasoning effort 对比；迭代最多 20 轮，部分扩展至 50 轮。

**关键结果**：
- 仅用 self model feedback，平均准确率从 ICL/ACE/DC 的 62.1%/64.0%/62.7% 提升到 71.0%，也显著高于无反馈 CoE 的 66.8%；correctness/executor feedback 进一步提升到 79.3%。
- 整体在 6 个 benchmark 上平均 +5.6%，同时 API 成本下降 19%，token 效率更高。
- 代码任务中 executor feedback 从 66.4% 提升到 75.0%（+8.6%），self feedback +7.0%。
- 模型 base 能力与测试时改进能力正相关，平均 Pearson r=0.50，代码任务 r 高达 0.97/0.83。
- 对 spurious feedback 整体鲁棒，GPT-5-mini 退化仅 2.5%/0.6%；多数收益在前 20 轮早期出现。

**最值得记住的一句话**：在推理期保留完整交互轨迹并引入轻量反馈，比跨任务抽象记忆或单纯增长 reasoning 更划算，且强模型学得更好。
