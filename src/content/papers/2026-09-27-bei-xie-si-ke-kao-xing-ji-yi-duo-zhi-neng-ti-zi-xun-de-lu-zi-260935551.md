---
title: 'BaRe-Mem: Bayesian Reliability Memory for Robust and Adaptive Agent Consultation'
title_zh: 贝叶斯可靠性记忆：多智能体咨询的鲁棒自适应机制
authors:
- Peilin Feng
- Zhengyang Huang
- Soujanya Poria
affiliations:
- DeCLaRe Lab, Nanyang Technological University
- Peking University
arxiv_id: '2609.35551'
url: https://arxiv.org/abs/2609.35551
pdf_url: https://arxiv.org/pdf/2609.35551
published: '2026-09-27'
collected: '2026-09-29'
category: MultiAgent
direction: 多智能体可信咨询 · 在线贝叶斯记忆
tags:
- multi-agent consultation
- Bayesian memory
- reliability estimation
- attention steering
- worker routing
- Kalman filter
one_liner: 用在线贝叶斯可靠度记忆同时决定信任谁与是否咨询，使中心模型在误导信息下保持鲁棒
practical_value: '- 在线贝叶斯可靠性记忆适合流式稀疏反馈，用少量 verify label 即可更新模型/工具/召回源的可靠度；电商/推荐中标注昂贵，可先以
  1% 流量反馈冷启动。

  - 无参数 attention bias：对低可靠来源 token 的 attention logit 加 γ log(p/max_p)，可直接嵌入现有多路 RAG、多模型融合或
  Agent 集成，无需 finetune，适合防止不可靠外部知识污染主模型。

  - 是否咨询/调用外部能力的决策规则值得借鉴：比较“可靠证据收益” T(ρ-κ) 与“不可靠证据损失” (1-T)δ，并计算可信阈值 T*；可迁移到 Agent
  中决定是否调用工具/咨询其他模型，或推荐系统中决定是否触发外部广告/LLM 重排。

  - Worker routing：把可靠度记忆用于子任务到 worker 的分配，比历史成功率更快识别 capable worker；可借鉴到多模型/多策略路由和级联系统，降低无效调用成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多智能体系统中 LLM 能力异质，advisor 在某领域可靠、另一领域可能给出流利但错误的答案；仅聚合当前回复的投票/辩论会因群体一致但错误而失败。重复交互历史可提供可信度线索，但需要把历史转化为上下文可靠度估计，并同时决定“信任谁”和“是否咨询”，避免外部信息把模型带偏。

**方法关键点**
- 候选表示：用冻结中心模型编码当前问题和候选回答，构造 x_{t,k}=[e_k⊗ψ_q(t); ψ_c(t,k); 1]，分解来源可靠度与内容可靠度。
- 在线 Bayesian regression：s=2y-1，w 先验 N(0,λ^{-1}I)，后验用 Kalman rank-one 更新，避免重算逆矩阵，适合在线流式交互。
- 可靠度估计：p=Φ(μ/√(1+v))，无证据时 p=1/2；更新时间由 Kalman gain 自适应控制。
- 注意力调制：在 full attention logits 给 advisor token 加 β=γ log(p/max p)，最可靠 advisor 不变，其余按相对可靠度降权，无训练参数。
- 是否咨询：consultation ability A(T)=Tρ+(1-T)(κ-δ)，κ 为中心模型自主能力，T=max advisor p；用历史在线估计 ρ 和 δ，比较 A(T) 与 κ，阈值 T*=δ/(ρ+δ-κ)。

**关键实验**
9 个 benchmark、6 个中心模型、6 个 advisor；分 capability-supported 和 capability-challenging 两套任务，misleading ratio 从 0% 到 100%。对比 Question+Peers、Debate、Majority voting 和只保留注意力调制的 ablation。结果显示 BaRe-Mem 在所有误导比例下保持不低于 no consultation；在 capability-challenging 下，其他方法在误导比例超过 50% 后低于自主推理。咨询比例在 Qwen3-14B 上从 90% 降到 21%、Phi-4 从 85% 降到 18%，说明自适应切换。预测增益与真实增益单调一致，零点约在 Δ=0。稀疏反馈 <1%（约 170 样本）即有明显收益。在 MuSiQue worker routing 上，BaRe-Mem 无验证时 task completion 38.9% vs 历史成功率 35.5% vs random 23.4%，数据集验证下 54.3% vs 50.4% vs 43.0%，且更快识别 capable worker。

**最值得记住的一句话**
可靠记忆必须同时回答“信任谁”和“是否咨询”，单靠相对权重无法防止整个 advisor 池不可靠时的性能退化。
