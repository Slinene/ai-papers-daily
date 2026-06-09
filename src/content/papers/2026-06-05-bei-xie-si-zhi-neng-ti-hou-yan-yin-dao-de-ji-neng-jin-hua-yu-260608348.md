---
title: 'Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses'
title_zh: 贝叶斯智能体：后验引导的技能进化驾驭LLM代理
authors:
- Xiaojun Wu
- Cehao Yang
- Honghao Liu
- Xueyuan Lin
- Wenjie Zhang
- Zhichao Shi
- Xuhui Jiang
- Chengjin Xu
- Jia Li
- Jian Guo
affiliations:
- IDEA Research
- The Hong Kong University of Science and Technology (Guangzhou)
- DataArcTech Ltd.
arxiv_id: '2606.08348'
url: https://arxiv.org/abs/2606.08348
pdf_url: https://arxiv.org/pdf/2606.08348
published: '2026-06-05'
collected: '2026-06-09'
category: Agent
direction: 贝叶斯证据驱动的代理技能进化
tags:
- Bayesian Agent
- Skill Evolution
- LLM Agent
- Posterior-Guided
- Harness Optimization
one_liner: 将代理技能视为贝叶斯假设，基于验证轨迹后验指导技能修补、压缩与退役，实现无需改权重的可靠进化。
practical_value: '- 技能维护引入贝叶斯后验：不要仅凭成功/失败次数决定是否保留技能，使用特征条件后验（如失败模式、上下文）估计技能可靠性，避免小样本下的决策噪声。

  - 分离审计与执行：后验诊断信息只留给开发者，模型提示仅注入确定的失败补丁与 guardrail，避免 LLM 直接处理概率数字，提升 prompt 稳定性。

  - 增量修复模式：对已完成的代理运行，仅重跑失败任务并基于证据修补技能，可用较低 token 成本提升整体成功率（如 RealFin 从 45% 修到 65%）。

  - 轨迹特征离散化：将失败模式、token 数、回合数等桶化编码为离散特征，适合小样本技能效果推断，可借鉴至电商多轮代理的失败模式分析与自动护盾生成。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM 代理的能力越来越依赖外部推理环境——即 prompts、工具、记忆、SOP 和可复用技能，这些资产无需修改模型权重即可改变任务成功率。但现有方法大多通过启发式反思或单纯累积成功/失败频率来修订技能，容易引入噪声或忽视上下文影响。当代理轨迹稀疏且非独立同分布时，频率估计不可靠，需要更明确的证据模型来管理技能演化。

**方法关键点**
- **技能作为贝叶斯假设**：每个技能 k 在一个冻结模型和环境条件下，根据验证轨迹更新成功信念 p(y=1|θ, hk, zt)，其中 zt 为离散特征（上下文、失败模式、token 桶等）。
- **因子化分类证据模型**：采用拉普拉斯平滑的类先验与条件似然乘积计算后验，并维护 Beta-Bernoulli 共轭概要，支持低证据下的保守决策。
- **后验驱动五类动作**：根据后验状态触发探索（无证据）、修补（同一失败模式出现≥2次即生成可执行补丁）、分割（跨上下文异质时拆分技能）、压缩（估计成功率≥0.72 时压缩文本以释放上下文）或退役（失败证据占优时移除技能）。
- **审计与执行分离**：模型上下文仅接收可执行补丁和 guardrail，后验摘要保留给开发者调试；通过适配器边界可接入 GenericAgent、mini-swe-agent、Claude Code 等外部 harress。
- **双模式运行**：Full 模式从空注册表在线进化，Incremental 模式基于已有运行轨迹仅修复失败任务。

**关键实验**
使用 deepseek-v4-flash/pro，在 SOP-Bench、Lifelong AgentBench、RealFin-Bench 上评估。与 GenericAgent 基线相比，Incremental 修复将 SOP-Bench 准确率从 80% 提升至 95%，Lifelong AgentBench 从 90% 提升至 100%，RealFin-Bench 从 45% 提升至 65%，且修复仅消耗失败任务的 token。后端消融实验表明，Bayesian-Agent 在原生后端、mini-swe-agent、Claude Code 上均能实现一致的改进。但也有负面案例：Lifelong AgentBench 上 Full 模式出现 85% vs 90% 的下降，说明在线进化对稀疏证据敏感。

**最值得记的一句话**
“代理技能进化应被视为一种证据校准、可审计且对不确定性明确的贝叶斯后验优化过程，而非不加校准的提示积累。”
