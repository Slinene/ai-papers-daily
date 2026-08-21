---
title: 'Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL'
title_zh: 多智能体 RL 中通过多样化群组涌现无监督推理
authors:
- Yunhao Yang
- Yuexin Bian
- Yunjie Tian
- Di Fu
- Tianjin Huang
- Yuanyuan Shi
- Ziang Xiao
- Nuno Vasconcelos
- Yijiang Li
affiliations:
- Johns Hopkins University
- UC San Diego
- University of Exeter
- Independent Researcher
arxiv_id: '2608.17253'
url: https://arxiv.org/abs/2608.17253
pdf_url: https://arxiv.org/pdf/2608.17253
published: '2026-08-18'
collected: '2026-08-21'
category: MultiAgent
direction: 多智能体无标签 RL · 推理训练
tags:
- Multi-agent RL
- Self-rewarding
- GRPO
- Cross-agent Supervision
- Model Diversity
- Unsupervised Reasoning
one_liner: 用多个异构模型的同行投票作为无标签奖励，打破自奖励偏差，在文本与多模态推理上匹配甚至超过有监督 RL
practical_value: '- 在搜索/推荐里的生成式任务（query 改写、商品标题/广告文案生成、Push 消息选词）缺少 ground-truth 标注时，可以用多个异构模型互相生成
  majority-vote 伪标签作为 GRPO 奖励；reward 规则就是“答案是否等于 peer 的多数投票”，无需 reward model 或 LLM
  judge。

  - 多样性要落到实处：选不同模型家族、不同参数规模、不同输入改写（原始 prompt 与改写 prompt 分开投喂）以及独立 optimizer 状态，能显著降低伪标签错误相关性；上线前可用
  error-overlap 或 Cohen''s kappa 快速筛选互补性强的模型 pair。

  - 工程上轻量：每个模型独立采样 K 个 response（论文里 K=8/12，温度 1.0），各自做 GRPO，agent 间仅通过 cross-reward
  耦合、不共享梯度；比 debate/LLM judge 更省推理预算，也方便跨团队部署和隐私隔离。

  - 如果业务里已经有多套不同架构的生成/排序模型（如 Qwen、Llama、Gemma 等），可以直接交叉训练、单次 run 同时提升，论文三 agent 实验平均提升
  6–8%，并匹配有监督 GT reward，适合标注稀缺但现成模型多的场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
RLVR 在推理模型上很强，但依赖 verifiable reward，人工标注成本高，且能力超过人类评估后标签会越来越稀缺。自奖励 RL 只用模型自身信号（majority vote、置信度、熵等），容易放大已有偏差、降低响应多样性，最终训练崩溃。核心问题是：无标签下如何获得足够独立的学习信号。

## 方法关键点
CO-RL 的核心假设是：独立训练模型之间的错误不相关，因此可以互相提供纠正信号。

- **多解耦 agent 同时训练**：多个参数不共享、梯度不互传的模型组成 cohort；每个 agent 对同一 unlabeled prompt 独立采样 K 个 completion 并提取答案。
- **peer 伪标签奖励**：agent n 的奖励来自 peer n-1 的 majority vote；若自身答案与 peer 伪标签一致则 reward=1，否则为 0。两 agent 时互相监督，多 agent 时按环形传递。
- **策略优化**：每个 agent 独立使用 GRPO（或 REINFORCE++）更新，仅通过 cross-reward 耦合，无需 critic、LLM judge 或 learned reward。
- **多样性驱动**：push 多样性到极致——不同模型家族/架构、不同参数规模、不同输入改写、独立 optimizer 状态，以降低错误相关性、增强纠错信号。

理论分析表明，自奖励是 self-confirming 的：当某个答案当前更可能，就强化它，无论对错。CO-RL 则把 agent A 的更新方向交给 agent B 的监督信号；在两 agent 对称情形下，只要 pA+pB>1，就能收敛到正确答案，从而扩大正确收敛 basin。

## 关键实验与结果
在文本 LLM 上，CO-RL 在四个模型（Qwen2.5-3B/7B、Llama-3.2-3B/Llama-3.1-8B）的七个推理基准上平均提升 3.0–8.6%，超过 TTRL、RENT、Intuitor、Co-rewarding-II 0.8–2.0%。在 CoMAS 多智能体协议下，CO-RL 平均 62.97%，比 CoMAS 高 4.0%，且只用一半 agent、不需要 judge。三 agent 联合训练（Qwen2.5-3B + Llama-3.2-3B + Qwen3-1.7B）分别提升 7.8%、6.0%、8.2%，匹配或超过 GT-Reward。多模态上，五个 VLM（2B–12B）在 MathVision/MathVerse/MathVista/We-Math 上提升 2.3–7.2%，有时超过有监督 GT-Reward。训练动态显示 CO-RL 保持 reward std 与生成长度稳定，而自奖励方法可能出现发散。

**最值得记住的一句话**：用“独立同行的多数投票”作为无标签奖励，是打破自奖励偏差循环、让无监督推理接近甚至超过有监督 RL 的关键。
