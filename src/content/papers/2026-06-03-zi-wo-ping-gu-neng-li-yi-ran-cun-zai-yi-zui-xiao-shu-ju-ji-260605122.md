---
title: 'Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base
  LLMs with Minimal Data'
title_zh: 自我评估能力已然存在：以最小数据激发基座LLM的潜在评判校准
authors:
- XiuYu Zhang
- Yi Shan
- Junfeng Fang
- Zhenkai Liang
affiliations:
- National University of Singapore
- Beijing University of Technology
arxiv_id: '2606.05122'
url: https://arxiv.org/abs/2606.05122
pdf_url: https://arxiv.org/pdf/2606.05122
published: '2026-06-03'
collected: '2026-06-04'
category: Eval
direction: LLM自评估能力激发
tags:
- self-evaluation
- reinforcement learning
- calibration
- LLM judge
- few-shot
- elicitation
one_liner: 发现基座LLM已能预测外部多属性评分，提出SEE通过小样本交替RL与屏蔽蒸馏高效激发校准能力
practical_value: '- **小样本激发评估能力**：仅需约160条样本的交替训练即可显著提升模型对自身输出质量的预测校准，对于电商内容生成、对话Agent的回复自我判断可直接借鉴，无需大量标注即可获得可信度评分。

  - **解耦训练避免质量退化**：采用屏蔽蒸馏（只在自评token上训练），保持回答主体参数不动，避免了校准提升时损害生成质量。在推荐文案生成、Agent多轮对话中，可将自评模块作为插件训练而不干扰主任务性能。

  - **利用自评进行结果筛选与路由**：模型产出自我评估后，可依此分数对候选生成结果进行重排序，或在低置信时自动拒答、转接更强模型，降低线上调用外部评判器的成本。在搜索问答、客服Agent中，该机制可直接提升系统可靠性和效率。

  - **非线性校准奖励设计**：训练中采用指数γ>1放大预测与真实评分的大偏差，强制模型学习极端分数分布，避免预测趋向均值，这对推荐系统的评分预测训练或强化学习中的奖励校准具有通用启发。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM评判已成为评估与训练的主流，若模型能预测外部评判器给自己的评分，便可在推理时自主进行自我筛选、拒答或路由，节省成本并提升可靠性。现有自我评估工作局限于可验证任务，开放域多属性评分能力未知，且通常依赖大规模训练。本文从基座模型直接测量出发，发现其已具备显著预测能力，从而将问题从能力获取转化为能力激发。

**方法关键点**：
- **Self-Evaluation Elicitation (SEE) 循环**：交替进行 Calibration-Coupled RL 与 Masked Judge Distillation 两阶段。
- **Calibration-Coupled RL**：模型生成答案后附加 `[SELF_EVAL]` 块预测五大属性（helpfulness, correctness, coherence, complexity, verbosity）的0-9分；奖励由回答质量（前三属性均值）和校准项 `(1 - MAE/9)^γ` 加权组成，γ>1 惩罚大偏差；使用GRPO优化整个输出，同时写入有效 rollout 至缓冲。
- **Masked Judge Distillation**：从缓冲中以分层轮询策略选取均衡覆盖各属性与分值区间的 rollout，将自评块替换为法官真实分数，仅对分数token进行微调，答案token不参与损失，从而在保持回答质量的同时准确校准自评。
- **极低数据需求**：循环运行15轮，仅用160条独特样本（约2.4k样本通过），约为纯RL基线（5k条）的1/31。

**关键实验与结果**：
- 基座模型 Qwen3-4B-Base 在 HelpSteer2 验证集上的校准已达0.632，top-5 token准确率77.07%，远高于随机。
- 在 HelpSteer2 及三个开放基准（AlpacaEval 2.0, Arena-Hard v2.0, WildBench v2）上，SEE 显著提升校准（如 WildBench 从0.504到0.609），且回答质量未受损甚至微升，全面超越 Adapted RLCR (5k数据)。
- 样本效率：SEE 仅需约0.8k样本通过即可达到基线在10k处的质量与校准水平。
- 跨评判器泛化：使用 GPT-5.4 训练后，模型在 Claude Sonnet 4.6 和 Gemini 3.1 Flash-Lite 上的校准提升同样保持，表明学习的是可迁移的”质量概念”。
- 自评极度局部化：法官分数在模型 top-5 token 中的概率高达87.76%（HelpSteer2）至90.78%（AlpacaEval），证明预测确定且可直接用于下游决策。

**核心认识**：面向评判器的自我评估能力在预训练中已大体形成，后训练的作用在于激发与校准而非从头安装，这改写了任务范式，使得用一个极简的双阶段循环+极小数据即可达到高效能。
