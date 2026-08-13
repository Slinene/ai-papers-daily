---
title: 'AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses'
title_zh: 推理期脚手架实现强模型到弱模型的能力迁移
authors:
- Cheng Qian
- Wenting Zhao
- Liangwei Yang
- Heng Wang
- Jielin Qiu
- Heng Ji
- Silvio Savarese
- Huan Wang
- Shelby Heinecke
affiliations:
- Salesforce AI Research
- University of Illinois Urbana-Champaign
arxiv_id: '2608.12307'
url: https://arxiv.org/abs/2608.12307
pdf_url: https://arxiv.org/pdf/2608.12307
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: 强模型构建推理期脚手架
tags:
- Strong-to-Weak
- Scaffolding
- Harness Engineering
- Inference-time
- Theory-of-Mind
- LLM
one_liner: 强模型不更新弱模型参数，仅靠推理期脚手架将弱模型ToM平均准确率从0.49提至0.91
practical_value: '- 业务中用小模型/弱模型做 query 改写、意图分类、商品属性解析、Push 文案生成时，可先让强模型离线构造推理期脚手架：严格输出格式校验、greedy
  decoding、按任务子类型路由；把正则/规则/策略计算等确定性逻辑外置到代码，不让小模型做脆弱的符号推理。

  - 用 5% 左右验证集做脚手架迭代即可，best validation 与 held-out 相关性极高（r=0.96）；跑 2-3 个 scaffold 选验证集最优、取上界，比反复加验证采样更划算。

  - 把 builder 的 inference budget 投在深层任务分析而非多次验证上：builder reasoning effort 单调提升效果，而
  validation iterations 几乎无关。具体到推荐/Agent pipeline，让强模型写出任务分解、状态提取、分支规则和 fallback，成本低但增益大。

  - Headroom law：只对“弱模型有大量可纠正错误”的环节做脚手架；对已接近饱和的强模型或子任务，过度 prompt/rule 可能把原来对的答案改坏（strong
  target 在 Hi-ToM/MuMA 上出现负增益）。建议按子任务 headroom 做灰度和回退开关。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：传统蒸馏通过更新弱模型参数迁移能力，但很多失败来自任务呈现带来的认知负荷，而不只是模型能力不足。如果把强模型的认知结构外化为推理期脚手架（routing、deterministic solver、format enforcement、verification），就能在不动参数的情况下让弱模型更可靠。这对电商/广告 Agent 日益普及的小模型部署很相关。

**方法关键点**
- 设强 builder 模型与弱 target 模型；builder 只看到 5% 验证集，设计可执行推理入口 scaffold，在隐藏测试集评估。
- 允许任意形式：prompt 模板、路由、代码/规则求解、格式强制、验后、few-shot 等；目标是在验证集上优化 scaffold 以迁移到测试集。
- 任务聚合 4 个 ToM 基准：BigToM、Hi-ToM、MMToM-QA、MuMA-ToM，共 3900 隐藏测试；target 为 GPT-5.4-mini 与 Gemini-3.5-flash；builder 跨 GPT/Claude/Gemini 等，平台 Cursor/Claude Code/GPT Codex，每配置跑 3 次。
- 记录 builder 迭代轨迹、scaffold 代码、12 种技术标签，做归因。

**关键结果**
- GPT-5.4-mini 无 scaffold 为 0.488；最佳 scaffold 0.912，+0.423（87%）；平均 0.763，+0.275，100% 运行超过 baseline。
- 最佳 scaffold 超过未 scaffold 的更强 GPT-5.4 和 GPT-OSS-120B，在 BigToM 达到 1.00，但整体仍低于 human-inspired UserHarness 0.939。
- 技术归因：几乎全部用 format enforcement、greedy、benchmark routing；强增益来自 polarity/negation logic (+0.09)、structured extraction (+0.06)、hybrid fallback/deterministic solver；而 greedy/routing 是通用可靠性底线。
- builder 推理 effort 单调提升（Spearman 0.77）；validation iterations 与最终成绩弱相关（r=0.17），best validation 与测试高度相关（r=0.96）。
- Headroom law：弱 target GPT-5.4-mini 增益更大；强 target Gemini-3.5-flash 只在仍有 headroom 的 BigToM 获增益，在已强 Hi-ToM/MuMA 上出现负增益；builder 会自动减少确定性 machinery、退回 model-only。
- top scaffolds 修复的 baseline errors 之间互补，union 覆盖 97% baseline errors。

**最值得记住的一句话**：把能编译为规则/代码的推理从弱模型身上卸载到 scaffold，配合严格输出约束和子任务路由；并为 builder 保留深度推理预算，而不是用更多验证轮次堆反馈。
