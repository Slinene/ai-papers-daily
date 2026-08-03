---
title: 'LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from
  Preference Feedback'
title_zh: LEMUR：从偏好反馈中学习多目标强化学习的对齐框架
authors:
- Manith Adikari
- Bei Peng
- Samuele Vinanzi
- Angelo Cangelosi
affiliations:
- University of Manchester
- University of Sheffield
- Sheffield Hallam University
arxiv_id: '2607.29559'
url: https://arxiv.org/abs/2607.29559
pdf_url: https://arxiv.org/pdf/2607.29559
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 多目标偏好强化学习
tags:
- Multi-Objective RL
- Preference-based RL
- Human Feedback
- Reward Modeling
- Policy Learning
one_liner: 通过多人偏好反馈联合学习多奖励模型与策略，无需预定义奖励函数即可平衡多个竞争目标
practical_value: '- **交互式多目标推荐学习**：在推荐系统中，可直接收集用户对推荐列表的偏好（如“列表A优于B”）而非设计显式奖励，自动学习CTR、GMV、多样性等目标的隐奖励模型。

  - **无权重预设的多目标折中**：不需手动指定各目标权重，通过偏好反馈隐式学习用户或业务方的偏好结构，使策略自动适应不同权衡需求，适合电商中动态变化的业务指标。

  - **Agent决策优化**：对对话推荐或任务型Agent，可用此法同时优化任务完成率、对话长度、用户满意度等多目标，利用人类反馈交互式训练，降低奖励函数设计的成本。

  - **工程借鉴**：联合训练策略与多个目标奖励模型的架构可用于实际在线学习系统，配合主动查询（选择信息量高的轨迹对进行标注）提升样本效率。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
实际决策常涉及多竞争目标（如性能 vs 效率），但传统RL依赖单一标注奖励，多目标RL（MORL）又假设各目标有明确奖励函数，两者都面临奖励设计困难。偏好RL（PbRL）在单目标中成功从人类反馈学习奖励，但未处理多目标。  
**方法**  
提出LEMUR框架，智能体交互式地从多个人类偏好反馈中学习多目标策略。核心是同时学习策略和多个目标特定的奖励模型：人类对轨迹段对给出偏好，系统通过多目标偏好模型推断各目标的奖励，再合成多目标策略用于决策。训练过程结合了奖励模型更新与策略优化，使智能体能平衡多个竞争目标。  
**结果**  
在多种多目标基准任务（如资源收集、导航等）上，LEMUR性能显著优于现有PbRL与MORL基线方法，验证了在没有预定义奖励时直接从偏好学习多目标策略的有效性。
