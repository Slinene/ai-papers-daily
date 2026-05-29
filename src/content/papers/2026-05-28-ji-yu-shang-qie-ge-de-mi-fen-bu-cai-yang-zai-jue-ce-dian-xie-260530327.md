---
title: 'Reasoning with Sampling: Cutting at Decision Points'
title_zh: 基于熵切割的幂分布采样：在决策点重写推理轨迹
authors:
- Felix Zhou
- Anay Mehrotra
- Quanquan C. Liu
affiliations:
- Yale University
- Stanford University
arxiv_id: '2605.30327'
url: https://arxiv.org/abs/2605.30327
pdf_url: https://arxiv.org/pdf/2605.30327
published: '2026-05-28'
collected: '2026-05-29'
category: Reasoning
direction: Power Distribution 采样 · 推理决策点重采样
tags:
- Power Distribution
- Metropolis-Hastings
- Entropy-Guided
- Reasoning
- LLM
- Decision Points
one_liner: 利用下一token熵跳跃定位决策点，改进MH采样以高效从幂分布中激发基础模型的推理能力
practical_value: '- 在生成式推荐（如查询改写、文案生成）或Agent推理链中，可用模型输出的熵跳跃识别「关键决策点」，在这些位置重新采样可提升最终输出的质量与多样性，无需额外训练。

  - 若业务中已使用类似MCMC的重采样策略优化生成结果，用熵跳跃替代均匀切割能加速收敛、减少在局部细节上的浪费计算，尤其适合token长度较长的推理场景。

  - 该方法完全无训练、无验证器，可直接套用在现有自回归模型上，为搜索词推荐、个性化消息生成等业务快速试验推理能力提升提供了轻量级途径。

  - 在多智体协作中，可将每个Agent的推理链视为一条轨迹，利用熵跳跃定位其策略选择点，在后续回合中引导更有效的探索与决策回溯。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
前沿推理模型通常通过RL后训练获得强推理能力，但近期工作表明直接从基础模型的“幂分布”（p(x)^α）中采样，同样能激发出与RL训练相当的推理表现，且无需额外训练、数据集或验证器。然而，高效采样该分布是难点，现有均匀切割的Metropolis–Hastings (MH) 采样器混合缓慢：它很少重新访问早期的关键决策点（如证明策略、算法选择），而多在小范围改写局部细节，导致在不同推理路径间切换的效率低下。

**方法关键点**  
- 将基础模型输出的**下一token熵的差分**（阳性跳跃）作为决策点的代理：直觉上熵剧增的位置往往意味着面临多个可能的分支。  
- 提出**Entropy-Cut MH**：在MH采样器中，切割位置不再均匀选择，而是以熵跳跃的β次方为概率分布，将切割集中在这些高不确定性决策点上。  
- 理论分析在推理树模型下证明：当推理轨迹由少量分支节点和大量链节点组成时，熵切割的混合时间与分支节点数 k 成比例，而均匀切割须与 token 深度 T 成比例，二者可相差数个数量级。  

**实验与结果**  
在 Qwen2.5‑7B、Qwen2.5‑Math‑7B、Phi‑3.5‑mini 等模型上，对 MATH500、HumanEval、GPQA Diamond、AIME26 四个推理基准进行了单次生成评测。结果表明，Entropy‑Cut MH 一致优于均匀切割 MH 及其他采样基线（低温度采样、SMC、TMC）。例如 Qwen2.5‑7B 在 MATH500 上从标准采样的 35.9% 提升至 71.9%，均匀切割为 67.4%；HumanEval 从 33.0% 提至 68.9%。同时，该方法的 pass@k 多样性保持与标准采样相当，无崩塌。  

**一句话总结**  
“在熵骤增的位置重写后缀，能让采样器更频繁地在不同推理策略间跃迁，从而更高效地从幂分布中抽取高质量推理路径。”
