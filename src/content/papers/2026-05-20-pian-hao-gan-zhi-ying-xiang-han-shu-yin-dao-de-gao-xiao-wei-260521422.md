---
title: Preference-aware Influence-function-based Data Selection Method for Efficient
  Fine-Tuning
title_zh: 偏好感知影响函数引导的高效微调数据选择
authors:
- Qihao Lin
- Guanxu Chen
- Dongrui Liu
- Jing Shao
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2605.21422'
url: https://arxiv.org/abs/2605.21422
pdf_url: https://arxiv.org/pdf/2605.21422
published: '2026-05-20'
collected: '2026-05-21'
category: Training
direction: 数据选择 · 影响函数 · 偏好感知
tags:
- Data Selection
- Influence Function
- Preference Weighting
- Efficient Fine-Tuning
- Safety Repair
- LLM
one_liner: 利用当前模型对目标示例的偏好加权构造目标方向，通过影响函数评分选择最有价值样本，提升微调数据效率
practical_value: '- 在生成式推荐微调中，可用当前推荐模型对目标行为的响应概率作为权重，聚焦模型“附近”的高价值样本，避免均匀聚合造成的方向偏差。

  - 影响函数评分公式 $s(z) = g_z^\top H_{\lambda}^{-1} g_{\text{KL}}$ 可直接嵌入现有微调流水线，配合 LoRA
  等高效更新计算梯度，用于预算有限下的训练样本选择。

  - 安全修复场景下，该方法能有效识别并移除导致有害行为的微调数据，可迁移到电商内容审核或多智体行为对齐中的训练数据清洗。

  - 理论保证了一阶最优性：选择偏好加权方向下的 Top-$m$ 样本能最大化目标行为偏好的局部提升，为策略提供可靠依据。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
LLM 微调成本高昂，数据选择是提升数据效率的关键。现有方法通常将目标行为描述为一组示例，并平均聚合其梯度方向进行影响评分。然而，不同目标示例对当前模型的指导价值不同：与模型当前行为接近的示例能提供更可操作的局部方向，而远离的示例贡献较弱。均匀聚合会混合多样化信号，导致选中的数据不聚焦于最能推动模型进化的样本。

**方法**  
PRISM 提出**偏好感知的目标方向构造**：对于每个目标正/负示例对，计算当前模型对正样本的偏好概率 $\pi_q = p_\theta(y_p|q)/(p_\theta(y_p|q)+p_\theta(y_n|q))$，用 $\pi_q$ 加权梯度差 $g_{\text{KL}} = \frac{1}{|Q_\Delta|}\sum \pi_q (g_{(q,y_p)}-g_{(q,y_n)})$。该加权梯度对应目标偏好风险 $K(\theta)$ 的负梯度，理论上是一阶最优的局部方向。然后，通过**影响函数评分**：$s_\pi(z) = g_z^\top H_\lambda^{-1} g_{\text{KL}}$，选出与目标方向最对齐的训练样本。该分数既可用于前向选择（保留高影响样本微调），也可用于反向修复（移除高影响样本以消除有害行为）。

**实验**  
前向选择：从 270K 指令数据中用 5% 预算选择微调数据，在 Llama-2-7B/13B 上评估 MMLU、BBH、TyDi QA、MATH-500。PRISM 在 8/10 个模型-基准组合中取得最优，尤其在 MMLU、TyDi QA 和 MATH 上显著超越 LESS、IF-GUIDE 等基线。  
反向修复：针对 Llama-3.1-8B、Qwen-3-8B/14B 的有害 SFT 数据（不安全代码、错误数学/医学），用 benchmark 派生信号排名并移除部分有害样本后重新微调。PRISM 在大部分混合比例下获得最低的不诚实度，排名质量（AUROC）和修复效果（benchmark dishonesty）均领先基线。消融证实偏好权重和配对锚点缺一不可。  

**一句话**  
“偏好感知”让目标方向的表征更贴近模型当前的优化空间，是预算有限时数据选择的核心改进。
