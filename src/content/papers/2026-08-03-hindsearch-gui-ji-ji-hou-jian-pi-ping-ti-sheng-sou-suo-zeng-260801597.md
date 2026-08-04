---
title: 'HindSearch: Trajectory-Level Hindsight Critique for Search-Augmented Reinforcement
  Learning'
title_zh: HindSearch：轨迹级后见批评提升搜索增强RL
authors:
- Haowei Liu
- Jiamian Wang
- Hsin-Tai Wu
- Zhiqiang Tao
- Yi Fang
affiliations:
- Santa Clara University
- Rochester Institute of Technology
- Independent Researcher
arxiv_id: '2608.01597'
url: https://arxiv.org/abs/2608.01597
pdf_url: https://arxiv.org/pdf/2608.01597
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 后见批评 · 搜索增强强化学习
tags:
- GRPO
- hindsight critique
- search-augmented
- on-policy distillation
- multi-turn search
- agent training
one_liner: 利用黄金答案生成失败轨迹的指令性批评，通过on-policy distillation使搜索RL获得密集信号，平均EM提升至39.4%
practical_value: '- **训练搜索型Agent时可复用**：电商搜索、推荐对话等场景可将最终正确答案（如成交商品）作为后见，让冻结裁判生成“本应搜索什么”的批评，转化为密集训练信号，缓解稀疏奖励下信用分配困难。

  - **简单可插拔的密集奖励方案**：直接在GRPO上叠加一个OPD损失，只作用于搜索动作token，无需训练过程奖励模型，额外计算开销仅在训练时、只在失败轨迹上（约15%
  wall-clock），推理时零成本。

  - **批评生成技巧**：用强大但冻结的裁判LLM，输入完整轨迹+正确答案，输出1-2句具体指令（“应该查询导演名而非演员表”），广播到所有搜索步作为hint前缀；使用同尺寸学生模型作为教师，避免教师过大导致KL崩塌。

  - **可迁移结论**：后见批评带来的提升同等覆盖训练域内和零样本任务（+5.85pp vs +5.80pp），表明学到的搜索策略是通用的，适用于新场景快速泛化。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
搜索增强的LM Agent训练通常仅依赖二元EM奖励（成功/失败），将一条失败的多轮搜索轨迹压缩为一个标量0，丢失了“具体哪里出错、应当如何修正”的丰富信息。这使得信用分配极其稀疏，训练不稳定，且收敛慢。已有过程奖励模型或在线hint蒸馏方法仍然依赖评估性信号或未使用正确答案，不能直接告诉agent“应该怎么做”。

## 方法关键点
**HindSearch** 在GRPO基础上引入 **轨迹级后见批评(TLHC)** 与 **on-policy蒸馏(OPD)**：
- 每次rollout后，将失败轨迹τ和黄金答案a⋆送给冻结裁判LLM，裁判生成1-2句**指令性批评**（如“第一查询应当加‘1985 film’以避免歧义”）。
- 将批评作为hint前缀，拼接到学生上下文中，用冻结教师模型（与学生同尺寸的初始checkpoint）计算teacher log-probabilities ℓTt。
- 构造辅助损失 L_OPD：只在失败轨迹的搜索动作token上，当teacher更自信时提升student log-probability（clamp[ℓTt - ℓst, 0, 1] · ℓst），避免滥用。
- 整体损失为 L_PPO + λ_OPD * L_OPD（λ=0.01），仅训练学生，裁判和教师冻结，推理时无额外开销。
- 批评**广播到所有搜索步**，而非仅最早错误步，提供更全面的指导。

## 实验结果
- 使用 Qwen2.5-3B-Instruct 作为backbone，E5-base-v2/Wikipedia-18 作为检索器，top-3，最多4轮搜索，在 NQ+HotpotQA（169k）上训练300步，在7个QA基准上验证。
- **HindSearch 达到平均EM 39.4%**，比Search-R1 GRPO（33.6%）高5.8个点，训练曲线平稳上升，无停滞。
- 消融实验：移除裁判对正确答案的访问 → EM降至34.7%；替换为PPO-clipped top-K损失 → 降至32.7%；按步最早错误批评 → 35.5%。
- 后见批评带来的提升在训练域内（+5.85pp）和零样本域（+5.80pp）几乎一致，表明学到的搜索行为是通用的。

> **一句话**：将失败轨迹+正确答案交给冻结裁判生成一句批评，再用它蒸馏搜索动作token，是在搜索RL中获得廉价且有效密集信号的关键trick。
