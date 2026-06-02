---
title: 'ESPO: Early-Stopping Proximal Policy Optimization'
title_zh: ESPO：基于近端策略优化的早停机制
authors:
- Zihang Li
- Rui Zhou
- Yingcheng Shi
- Wenhan Yu
- Zhewen Tan
- Zixiang Liu
- Zeming Li
- Binhua Li
- Yongbin Li
- Tong Yang
affiliations:
- Tongyi Lab, Alibaba Group
- Peking University
arxiv_id: '2605.29860'
url: https://arxiv.org/abs/2605.29860
pdf_url: https://arxiv.org/pdf/2605.29860
published: '2026-05-27'
collected: '2026-06-02'
category: Training
direction: 面向LLM推理的强化学习训练效率优化
tags:
- LLM
- Reinforcement Learning
- Early Stopping
- PPO
- Reasoning
one_liner: 通过logit遗憾值与价值门控在rollout中即时终止失败轨迹，提升数学推理准确率并节省超20%训练token
practical_value: '- **Agent多轮交互训练可复用早停逻辑**：在电商导购、多智体协作等长轨迹RL训练中，可基于策略logit与价值估计设计类似的门控，提前截断已明显失败的对话或动作序列，减少无效计算，并将截断点作为吸收失败状态注入负TD误差，改善信用分配。

  - **无需额外模型或人工标注的失败检测**：利用已有policy的logit向量计算代理遗憾值（当前token与贪心选择的概率差），结合EMA归一化与critic价值比较，几乎零额外计算成本即可判断是否继续生成，适合资源敏感的业务场景。

  - **可作为现有PPO-based方法的即插即用组件**：ESPO不改变PPO优化目标，只修改rollout收集过程，可与GRPO、DAPO等改进方案叠加。实际部署时只需在采样循环中加入轻量判断，且可通过比例控制器动态调整终止率，适配不同任务难度。

  - **避免熵崩溃与不当压缩探索**：实验表明ESPO不会导致策略熵下降过快，反而较标准PPO维持更高熵，这对推荐/对话场景下保持多样性有意义。同时约2.7%的假阳性截断率可控，整体收益远大于误杀代价。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
在LLM进行多步推理的强化学习中，如果模型在生成早期犯下关键错误，标准PPO仍会强制完成整个轨迹，导致大量后失效token被纳入训练，既浪费计算又向优势估计注入噪声，误导梯度。现有方法如过程奖励模型需要人工标注，GRPO/DAPO虽改进信用分配但仍全量生成。为此，需一种轻量的在线失败检测机制，在不额外引入模块的前提下提前终止无望轨迹。

**方法关键点**  
- **逐步遗憾信号**：每一步利用采样时已计算的logit向量，取`max logπ(a) - logπ(sampled a)`作为代理遗憾值，衡量当前token偏离策略最偏好的程度，计算开销可忽略。
- **EMA归一化与累积统计量**：使用在整个批次完成后才更新的EMA均值/方差归一化遗憾值，并经过指数平滑得到累积终止统计量`z_t`，保证尺度可比且不泄露未来信息。
- **价值门控停止准则**：当`z_t > β · max(V(s_t), ε)`时触发早停，将高价值状态赋予更大容忍度，避免误杀有恢复潜力的轨迹。`β`通过比例控制器动态调整以维持设定终止率。
- **吸收失败转换**：截断点赋予固定负奖励（如-1），后续token不再生成，GAE将集中负TD误差反向传播至停止步附近，精准分配负反馈，不引入逐步奖惩带来的非平稳偏置。
- **自适应critic预热**：训练初期禁用早停，待critic收敛后再逐步开放，防止因价值函数未校准导致的错误截断。

**关键实验结果**  
在DeepSeek-R1-Distill-Qwen-7B上，以数学推理任务（AIME 2024, AMC 2023, MATH-500）评估：ESPO相比PPO在三个基准上分别达到46.28% vs 45.25%、85.83% vs 82.94%、87.42% vs 85.43%，平均准确率73.17% vs 71.20%，同时累积rollout token消耗减少22%。在1.5B模型上趋势一致，平均准确率59.09% vs PPO的57.03%，token节省13%。消融实验显示随机截断（同等截断率）仅获42.4% AIME准确率，证明收益来自正确的截断位置而非简单的序列缩短。训练过程中策略熵保持更高，假阳性截断率仅约2.7%，说明方法在移除噪声的同时未抑制有效探索。
