---
title: 'CAFE: Self-Improving Search Agents Need Co-Evolving Feedback'
title_zh: CAFE：自我改进搜索智能体需要协同进化的反馈
authors:
- Boyang Liu
- Senjie Jin
- Peixin Wang
- Zhangyue Yin
- Yibo Wang
- Yuhao Zhou
- Xinbing Liang
- Shizheng Zhu
- Yuhui Wang
- Jingqi Tong
affiliations:
- Fudan University
- Tencent LLM Department
arxiv_id: '2608.24794'
url: https://arxiv.org/abs/2608.24794
pdf_url: https://arxiv.org/pdf/2608.24794
published: '2026-08-24'
collected: '2026-08-26'
category: Agent
direction: 搜索 Agent · 反馈协同进化
tags:
- Search Agent
- Self-Improvement
- Reinforcement Learning
- Preference Optimization
- Feedback
- Co-Evolution
one_liner: 提出 CAFE 框架，共享参数模型交替扮演搜索 agent 与 critic，通过在线反馈奖励整形与离线偏好优化让反馈随策略协同进化
practical_value: '- 在搜索/推荐 Agent 中引入显式 <request_feedback> 动作，用共享 backbone 做 role-conditioned
  agent/critic，避免单独部署 critic 的额外开销；适合多轮商品搜索或深度信息检索 Agent，让模型在轨迹中途主动请求诊断。

  - 奖励整形技巧可直接借鉴：CFE 用同一 prompt 下 call feedback 与 skip feedback 的成功率差作为请求反馈的 utility
  信号，再配合 repeat penalty；feedback-aware advantage shaping 对反馈前/后 token 分开加权，避免强化错误的失败前缀，改善
  RL 中的信用分配。

  - 离线反馈优化用 RDPO：从 on-policy rollout 中挖掘 prefix-matched 成功/失败反馈对，用 DPO 训练反馈生成，比只用成功轨迹的
  SFT 更干净，能缓解只有最终成交/转化标签导致的 outcome confound，适合业务中无逐步人工标注的场景。

  - 交替更新策略值得工程化：不要固定 critic 或 agent 单侧优化，否则会 plateau；每轮 agent RL 后用最新 rollout 更新 critic，保持反馈与当前策略的错误分布对齐，可参考
  100 步 RL × 5 轮的节奏。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长程搜索 agent 依赖 terminal reward 学习何时检索、如何检索，但终局奖励无法定位早期方向错误，错误会在后续轨迹中传播并复合。现有细粒度信号（信息增益、置信变化等）是评价性而非指导性的，只能事后归因，不能中途纠偏。本文提出把纠正反馈作为轨迹内的可学习干预，但由此引入三个耦合挑战：agent 要学何时请求反馈、critic 要在无 ground truth 下学出有用反馈、critic 必须随策略演化保持对齐。

## 方法关键点
- **共享参数的角色化 agent-critic**：同一个模型根据角色提示分别执行搜索 agent 或 critic；agent 可发射 `<request_feedback>` 动作，critic 基于当前轨迹生成诊断与下一步建议，随后 agent 从增强上下文继续。
- **失败轨迹恢复初始化**：保留 base agent 自己的错误前缀，在最早出错 turn 插入反馈请求，由教师模型生成反馈和成功续写，作为 SFT 恢复示范，让模型在真实访问的状态上学会请求、生成和利用反馈。
- **在线 RL：CFE + advantage shaping**：CFE 用同一 prompt 下 call/skip 反馈的成功率差作为请求反馈的效用估计，叠加任务奖励和重复请求惩罚；feedback-aware advantage shaping 将第一次请求前的 token advantage 减去 λ·clip(gap)，请求后的 token advantage 加上该值，避免同时强化错误前缀和修复续写。
- **离线偏好优化 RDPO**：从最新 on-policy rollouts 中按 prompt 和请求前状态匹配成功/失败反馈对，用 DPO 更新反馈生成；交替执行在线 RL 和 RDPO，使 critic 与 agent 的错误分布同步进化。

## 关键结果
在 7 个 SearchQA 基准上，7B CAFE 平均 EM 52.5、F1 60.7，超过最强 RL 基线 IGPO 2.1 EM / 1.3 F1，并在全部 6 个 out-of-domain 数据集上一致提升。相比 GRPO，CAFE 将 answer-level 幻觉率从 17.6% 降至 12.6%。消融显示 CFE 与 advantage shaping 均有贡献，RDPO 优于 rollout 正样本 SFT；交替优化比只更新 agent 或 critic 在 2Wiki 上高 3.0 分。

最值得记住的一句话：**一个自改进搜索 agent 需要与其策略一起进化的反馈，而不是固定在上一个错误分布上的静态 critic。**
