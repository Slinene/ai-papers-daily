---
title: Weak-to-Strong On-Policy Distillation
title_zh: 弱到强在线策略蒸馏：用更弱的模型提升强学生
authors:
- Fangxu Yu
- Zinan Lin
- Xiaodong Liu
- Weijia Xu
- Michael Xu
- Tianyi Zhou
- Jianfeng Gao
affiliations:
- University of Maryland, College Park
- Microsoft Research
- MBZUAI
arxiv_id: '2607.26246'
url: https://arxiv.org/abs/2607.26246
pdf_url: https://arxiv.org/pdf/2607.26246
published: '2026-07-27'
collected: '2026-08-04'
category: Training
direction: 弱到强蒸馏 · 在线策略蒸馏
tags:
- Weak-to-Strong
- On-Policy Distillation
- Contrastive Distillation
- LLM Reasoning
- Model Distillation
one_liner: 通过对比弱模型提取能力方向并锚定到学生基模型，构造代理教师实现弱到强蒸馏，使强学生超越弱教师
practical_value: '- **弱教师也能提升强模型**：当没有更强的教师可用时（如前沿推荐模型或Agent策略网络），用一对更小的模型（如不同规模的基模型或不同训练阶段的专家）通过logit差异提取“能力方向”，可以继续提升强模型。

  - **代理教师构造方法**：在在线策略蒸馏中，代理教师 = 学生基模型 + α*(正模型 − 负模型) logits。这种构造避免了分布不匹配，α控制信号强度与分布邻近度的权衡（图4：α≈1.0最优），可直接用于多领域推荐模型或Agent策略的合并。

  - **低成本多专家合并**：多个弱领域专家（如不同品类推荐模型）可通过各自与基础模型的对比方向求和，一次性蒸馏进同一个学生，无需顺序微调或担心灾难性遗忘（Eq.12）。

  - **保留通用能力**：锚定学生基模型作为参考分布，使代理教师保持与学生分布邻近，避免直接蒸馏弱教师导致的通用能力退化，这对需要保持广泛推荐能力的系统尤为重要。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
在线策略蒸馏（OPD）在LLM后训练中效果显著，但依赖一个至少与学生同样强的教师。当前做法要么用大模型蒸馏小模型（强到弱），在前沿模型无更强教师时失效；要么训练多个同规模领域专家再合并，成本高昂。弱到强学习（weak-to-strong）利用已有弱模型提升强模型，但直接OPD面临分布不匹配和拉低学生上限的问题。

**方法关键点**
- **代理教师构造**：用一对弱模型（正模型 m⁺、负模型 m⁻）的logit差异 z⁺−z⁻ 提取“能力方向”，加到学生初始基模型 logits 上： z_base + α(z⁺−z⁻) 。该方向剥离了弱模型的绝对能力水平，只保留相对提升部分。
- **锚定学生分布**：代理教师以学生基模型为参考，通过逆向KL（KL(π_S∥π_T)）进行在线蒸馏，保持分布邻近，防止通用能力退化。
- **三种实例化**：i) RL前后对比（专家 vs 初始）；ii) 不同规模基模型（大 vs 小）；iii) 同一模型加正确/错误提示。均无需训练同规模教师。
- **多代理教师合并**：只需将多对对比方向求和，一次性蒸馏（Eq.4）。

**关键实验结果**
- 在 AIME24/25、HMMT25 等数学和 HumanEval+、MBPP+、LCB 等代码基准上，**W2S-OPD 在单教师设置下数学平均相对提升11.4%，代码3.7%，学生超越4B弱教师（51.8 vs 48.8）**。
- 仅用两个弱基模型（4B和0.6B），学生数学绝对提升6.0个百分点（17.0→23.0）。
- 泛化能力不降反升：在 GPQA-Diamond 上从38.9升至56.5（OPD为54.4），IFBench 上 OPD退化而W2S-OPD提升。
- 不同对比强调不同推理模式：RL对比侧重规划与监控，规模对比侧重解题过程，提示对比侧重答案正确性。

**值得记住的一句话**：弱教师的能力方向（而非绝对水平）是可以转移的——通过对比减法提取这一方向并重新锚定到强学生上，即可稳定地实现弱到强的在线策略蒸馏。
