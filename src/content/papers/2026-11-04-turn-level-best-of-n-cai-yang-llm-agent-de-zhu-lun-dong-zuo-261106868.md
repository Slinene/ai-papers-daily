---
title: On Turn-Level Best-of-N Sampling for Scaling LLM Agents
title_zh: Turn-Level Best-of-N 采样：LLM Agent 的逐轮动作择优扩展
authors:
- Jalaj Bhandari
- Dhawal Gupta
- Hongli Zhan
- Zhenting Wang
- Varad Pimpalkhute
- Zhengzhong Liu
- Eric Xing
- Rupesh Srivastava
affiliations:
- Institute of Foundation Models (IFM)
- MBZUAI Labs
arxiv_id: '2611.06868'
url: https://arxiv.org/abs/2611.06868
pdf_url: https://arxiv.org/pdf/2611.06868
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 推理时动作选择 · Turn-BoN
tags:
- LLM Agents
- Best-of-N
- Inference-time Scaling
- Action Selection
- Terminal-Bench
- Generator-Selector
one_liner: 提出 Turn-BoN：每步生成 N 个候选动作并由 LLM 选择器在环境执行前择优，提升长程 Agent 准确率与一致性
practical_value: '- 对电商/Agent 场景，可在每轮工具调用前用 generator-selector 采样 N=4~8 个候选动作，用更强或同等级
  LLM 做 listwise 选择，只执行选中动作；相比 trajectory-level BoN 不需要多个并行 sandbox，更适合真实用户机器上的 terminal、GUI
  或购物助手场景。

  - 成本控制上：N=2 提升微弱，建议 N≥4；不必全 trajectory 每个 turn 都做 Turn-BoN，可在关键决策点（需求理解、最终提交、高风险操作前）触发；可蒸馏一个小
  selector 做 pointwise/listwise 排序替代大模型，降低 3~8 倍 token 开销。

  - 用行为 rubrics/LLM judge 监控 agent 轨迹质量，而不只看任务成功率：重点追踪 looping、retry without diagnosis、ignored
  instructions、insufficient testing 等坏行为；Turn-BoN 能改善失败轨迹的行为，暴露真实能力缺口，对线上归因和迭代更有价值。

  - 该思路可迁移到推荐/搜索 Agent 的中间步骤：如 query 改写、筛选条件组合、商品对比、消息推送文案生成等，用 LLM 选择器优先选择“真正推进任务”的动作，减少只读、空工具调用和循环。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
LLM Agent 在长程交互任务中表现不稳定：同一任务多次采样结果不一致，trajectory-level Best-of-N 只在轨迹完成后选择，无法改变中间动作分布。本文研究在每轮动作执行前进行 sampled policy improvement：采样 N 个候选动作，用现成 LLM 直接选择最优动作再执行，避免训练独立 critic，也避免 checkpoint 和并行 sandbox。

**方法关键点**  
- 采用 generator-selector 框架：generator 以 temperature 1.0、top-p 0.95 采样 N 个候选动作；selector 以 listwise 方式阅读任务上下文和候选列表，输出最优候选索引；只有被选动作进入真实环境执行。  
- 实验 N∈{4,8}，发现 N=2 与 baseline 接近；selector 使用更强的 open-weight 模型（Kimi-K3、DeepSeek-v4.1-Flash）。  
- 理论上将 Turn-BoN 看作一步策略改进的采样版：命题 2 给出改进条件——在 Turn-BoN 策略的访问分布下，选中动作的期望 advantage ≥0 即可保证 J(π_N)≥J(π)，比逐状态 greedy 条件更弱。

**关键实验**  
- 数据集：Terminal-Bench v2.1 的 89 个任务，使用 mini-SWE-agent harness；generator 为 Qwen3.6-35B 和 K2-Horizon-375B，selector 为 Kimi-K3 和 DeepSeek-v4.1-Flash。  
- 相对 baseline：K2-Horizon pass@1 从 73.3% 提升到约 77.9%（N=4），Qwen3.6-35B 从 47.5% 提升到 55.2%（N=8）；pass@k 和 consistency@k 同步改善。  
- 轨迹行为：平均所需 turns 减少约 40~50%；looping 坏行为下降 14~18%；selector 更偏好 edit/test/组合 shell 命令，减少只读、空工具调用和重复失败命令。  
- 成本：总 tokens 约为 baseline 的 3.6~8.7 倍，selector tokens 约 67k~125k，推理开销显著。

**最值得记住的一句话**  
Turn-BoN 用“每轮生成候选 + LLM 择优执行”实现了无需 critic 训练的推理时策略改进，在长程 Agent 上显著提升 pass rate 和行为质量，代价是 3~8 倍 token 开销。
