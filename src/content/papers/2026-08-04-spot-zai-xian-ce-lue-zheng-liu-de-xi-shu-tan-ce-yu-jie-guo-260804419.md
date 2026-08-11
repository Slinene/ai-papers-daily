---
title: 'SPOT: Sparse Probing and Outcome Calibration for On-Policy Distillation'
title_zh: SPOT：在线策略蒸馏的稀疏探测与结果校准
authors:
- Zikun Qu
- Min Zhang
- Mingze Kong
- Zhiwei Shang
- Yikun Ban
- Shuang Qiu
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- East China Normal University
- Beihang University
- City University of Hong Kong
arxiv_id: '2608.04419'
url: https://arxiv.org/abs/2608.04419
pdf_url: https://arxiv.org/pdf/2608.04419
published: '2026-08-04'
collected: '2026-08-11'
category: Training
direction: 在线策略蒸馏 · 稀疏探测与结果校准
tags:
- On-Policy Distillation
- Sparse Probing
- Outcome Calibration
- Knowledge Distillation
- LLM Reasoning
one_liner: 通过稀疏探测关键位置并利用下游结果校准蒸馏目标，在有限预算下提升推理模型多样解覆盖。
practical_value: '- **稀疏探测+结果校准框架**：在生成式推荐或对话Agent中，可在模型不确定性高且候选集紧凑的位置进行额外探索，利用下游业务指标（点击、转化）校准局部目标，替代全量教师监督。

  - **位置重要性得分**：使用公式 `s_t = 归一化熵 × top-k概率质量 × 学生-教师gap` 的连乘得分，作为触发多路采样的信号，可用于AIGC场景平衡生成质量与多样性。

  - **指数倾斜校准**：结果校准的封闭解（式10）提供了一种在保持KL约束下依奖励调整概率分布的方法，可应用于离线策略评估或A/B测试中的概率调整。

  - **预算可控的工程化设计**：探测位置数M、候选数k_p和每条候选续写数N_p均为显式超参数，便于在实践中根据延迟和成本进行权衡，仅对最有希望的候选展开额外推理。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
在线策略蒸馏（OPD）利用学生自生成轨迹上的教师反馈进行训练，但标准反向KL会压制其他合理续写，仅凭教师熵无法区分不确定性是集中在少量候选上还是分散在长尾上，也无法判断教师偏好的候选是否真能引导学生生成正确解答。此外，教师局部概率不一定反映下游成功。因此，需要在有限探测预算下，智能决定**在哪探测**（哪些位置值得探索候选分支）和**蒸馏什么**（如何利用探测结果修正监督目标）。

## 方法
SPOT采用三阶段获取-探索-利用流程：
1. **位置获取**：对每步位置计算得分 `s_t = 归一化教师熵 × top-k_s概率质量 × 学生-教师gap`，选取得分最高的M个位置进行探测。这个连乘得分确保了只有在教师不确定性集中、候选集紧凑且学生与其存在偏差时才分配预算。
2. **稀疏探索**：在选中位置，对教师top-k_p个候选词分别采样学生续写，并用验证器（如答案匹配）评估续写是否成功，得到每个候选的估计价值。
3. **结果校准与利用**：保留至少有一个候选获得正奖励的位置，通过指数倾斜公式 `˜π_T(v) ∝ π_T(v) exp(γ·价值(v))` 构造结果校准目标，该目标在保持与教师先验KL约束的同时提升高价值候选的概率。在训练中，除标准OPD损失外，加入按位置平均的校准分支损失。

## 实验结果
在Qwen3-0.6B/1.7B/4B三个学生模型上，使用MATH或DAPO-Math训练，评估6个数学推理基准：SPOT在所有设置下均取得最高宏平均Pass@8，比EOPD提升2.49–3.19个百分点；Avg@8保持领先或次优。消融实验证实获取得分的三个因子不可或缺，去除验证器引导导致Pass@8显著下降（如1.7B模型上宏平均Pass@8下降7.38点）。随采样预算k从4增至64，SPOT持续领先。方法在Llama架构和分布外任务上也展现了泛化性。

**核心结论**：将“在哪探测”与“探测什么”解耦，用不确定性指导探测分配，用下游结果校准监督目标，是提升在线策略蒸馏效率和覆盖率的关键。
