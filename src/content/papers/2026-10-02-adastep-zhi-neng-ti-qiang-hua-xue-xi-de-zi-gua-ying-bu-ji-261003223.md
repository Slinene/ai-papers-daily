---
title: 'AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning'
title_zh: AdaStep：智能体强化学习的自适应步级信用加权
authors:
- Xin Wang
- Wenhao Wu
- Menghao Zhang
- Zhi Wang
- Kun Shao
- Jian Luan
affiliations:
- Tsinghua University
- Nanjing University
- Xiaomi Inc.
arxiv_id: '2610.03223'
url: https://arxiv.org/abs/2610.03223
pdf_url: https://arxiv.org/pdf/2610.03223
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: Agentic RL 步级信用加权
tags:
- Agentic RL
- GRPO
- Step-level credit assignment
- LLM Agent
- Advantage weighting
- Variance reduction
one_liner: 为GiGPO的步级优势推导逐状态收缩系数，按返回方差中信噪比自适应加权，无额外模型或rollout
practical_value: '- 在GRPO/GiGPO式多步决策训练（如购物Agent、多轮搜索、导购对话）中，不要用固定系数融合全局与局部优势；按同一anchor
  state分组，用 `1 - E_a[Var(R|s,a)] / Var(R|s)` 估计逐状态收缩权重，可抑制下游随机噪声对局部信用的污染。

  - 该权重只依赖rollout中的count/sum/sum of squares统计量，无额外前向或critic，几乎零成本；可直接嵌入现有优势计算，适合线上训练管道。

  - 对不可靠组（单一动作或每动作样本不足）采用fallback w=1，而不是w=0或均值，实验中更优；说明信息不足时不要过度收缩局部信号。

  - 若状态空间连续或部分可观测，直接hash锚点状态不可行，需要额外状态嵌入或聚类才能迁移；可优先在离散文本状态（如WebShop、ALFWorld风格任务）中使用。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长时程LLM Agent常用稀疏结果奖励，轨迹级GRPO把同一结局优势广播到所有步，无法区分哪些动作贡献成功/失败；GiGPO引入步级小组相对优势，但该估计受后续动作、环境转移和折扣时机等下游随机性影响，固定系数会放大噪声或抑制信号，导致有用动作被误惩、无关动作被误奖。需要根据每组估计可信度自适应控制局部修正强度。

**方法关键点**：
- 在GiGPO框架上，将每条轨迹的全局优势 AE 作为参考，叠加逐锚点状态的局部优势修正：`A(s,a)=AE(s,a)+w(s)AS(s,a)`。
- 把 w(s) 看作对潜在真实步级优势的 MSE 最优投影，推导最优权重为 `w*(s)=E[AS A*_S|s]/E[AS^2|s]`。
- 在组内样本iid假设下，将权重化为可计算的信噪比：`w*(s)=1 - E_a[Var(R|s,a)] / Var(R|s)`，即返回方差中由动作间Q值差异解释的比例；信号主导时趋于1，下游噪声主导时趋于0。
- 仅需现有rollout中count/sum/sum of squares统计量，无critic、无额外rollout、无额外前向；对不可估计组fallback到 w=1，对同回报组直接置零局部优势。

**关键实验**：在 ALFWorld、WebShop、ScienceWorld 三个长时程基准，Qwen3-1.7B、Qwen3-4B、Qwen2.5-7B-Instruct 三个backbone上训练。AdaStep一致超过 GRPO、GiGPO、HGPO 等训练基线，较GiGPO最大+9.36点（ScienceWorld，Qwen3-1.7B），ALFWorld和WebShop也有+0.54~+4.99点不等。计算开销仅增加约1%的credit-computation时间，低于HGPO。消融显示对有无std归一化均鲁棒，且优于固定全局系数；诊断表明AdaStep降低了同动作内加权优势波动，同时保持最低held-out reference MSE。

**最值得记住的一句话**：把步级局部优势当成含噪估计，用“动作间方差/总返回方差”作为收缩系数，几乎是零成本地让GRPO/GiGPO的信用分配更可靠。
