---
title: Self-Distilled Agentic Reinforcement Learning
title_zh: 自蒸馏智能体强化学习：门控辅助蒸馏稳定多轮训练
authors:
- Zhengxi Lu
- Zhiyuan Yao
- Zhuowen Han
- Zi-Han Wang
- Jinyang Wu
- Qi Gu
- Xunliang Cai
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
affiliations:
- Zhejiang University
- Meituan
- Tsinghua University
arxiv_id: '2605.15155'
url: https://arxiv.org/abs/2605.15155
pdf_url: https://arxiv.org/pdf/2605.15155
published: '2026-05-13'
collected: '2026-05-15'
category: Agent
tags:
- Agent
- RL
- GRPO
- Self-Distillation
- On-Policy
- Token-Level Gating
one_liner: SDAR 用 token 级 sigmoid 门控自适应调节 OPSD 信号，保持 RL 主导并稳定提升多轮智能体性能
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
将 On-Policy Self-Distillation (OPSD) 与 RL 结合训练多轮智能体面临两大核心障碍：（1）**多轮 OPSD 不稳定**：学生策略漂移后，教师 token 级监督逐渐失效，KL 散度随轮次激增，导致性能崩溃。（2）**特权教师信号不对称**：教师通过检索技能获得额外上下文，其给出的负面对数概率差可能源于技能质量或利用缺陷，而非真正的错误，直接蒸馏会放大误导。因此，需要一种机制让 RL 保持主优化目标，蒸馏仅作为谨慎控制的辅助角色。

**方法关键点**  
- **门控辅助损失**：在 GRPO 策略损失外附加 OPSD 项，通过一个 sigmoid 门控 $g_t = \sigma(\beta \Delta_t)$ 对每个 token 的蒸馏强度进行软调制，其中 $\Delta_t$ 为师生在该 token 上的对数概率差。  
- **非对称信任**：正差距（教师更自信）的 token 获得较大蒸馏权重，负差距（教师更不自信）的 token 被软衰减，避免不信任的监督干扰 RL。  
- **梯度解耦**：门控值被 detach，确保蒸馏梯度仅通过学生 log 概率流动，避免自引用耦合。  
- **模式寻求的散度**：选用 reverse KL 散度，在学生采样 token 上估计，使策略集中于教师支持的模式，自然抑制不可靠的 token。  
- **鲁棒的技能检索**：支持多种技能检索策略（UCB、关键词匹配等），门控机制可自动滤除低质量检索带来的噪声信号。

**关键结果**  
在 ALFWorld、Search-QA、WebShop 三个多轮智能体基准上，基于 Qwen2.5-3B/7B 和 Qwen3-1.7B 训练。
- 相比 GRPO，SDAR 在 7B 模型上获得 **+9.4%** (ALFWorld)、**+7.0%** (Search-QA)、**+10.2%** (WebShop-Acc) 的提升。
- 完全避免 GRPO+OPSD 的灾难性退化（如 Qwen3-1.7B 上 GRPO+OPSD 仅 32.0，GRPO 46.1，SDAR 53.9）。
- 性能优于 Skill-SD 和 RLSD 等 RL-蒸馏混合方法，且对技能检索质量高度鲁棒：即使随机检索，仍优于纯 GRPO。
- 训练动态显示门控激活率随策略改善逐步上升，平均师生 gap 向零收敛，验证了自适应课程的有效性。
