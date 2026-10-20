---
title: 'RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent'
title_zh: RSIFlow：自适应自改进工作流与演化元Agent
authors:
- Huan Zhang
- Mingju Chen
- Dongxu Zhou
- Can Lv
- Sen Cui
- Faguo Wu
- Shiji Zhou
affiliations:
- Beihang University
- Tsinghua University
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2610.21791'
url: https://arxiv.org/abs/2610.21791
pdf_url: https://arxiv.org/pdf/2610.21791
published: '2026-10-14'
collected: '2026-10-20'
category: Agent
direction: Agent 递归自改进与元演化
tags:
- Self-Improvement
- Meta-Agent
- Workflow Orchestration
- RSI
- LLM Agents
- Harness Evolution
one_liner: 提出 RSIFlow，将自适应工作流编排与元Agent harness 演化耦合，动态诊断瓶颈并更新模型/框架/工件，6基准11/12领先
practical_value: '- 将搜索推荐系统中的多类组件（召回/排序/重排模型、prompt/规则、索引/内容/策略配置）抽象为 Model/Harness/Artifacts
  三种可更新目标，由 Meta-Agent 根据线上失败轨迹和 A/B 反馈诊断瓶颈，动态选择“微调模型 / 改 prompt 或规则 / 修内容或索引”，避免固定优化路径。

  - 借鉴 Harness 三组件抽象 Action/Skill/Planning 管理推荐 Agent 的 prompt 与工具调用规则；用结构化技能库存储“当出现
  XX 失败时→修改 YY→保留 ZZ”的经验，通过 Add/Supplement/Revise/Merge 持续维护，降低重复调优成本。

  - Meta-Agent 模型参数冻结、只更新其 harness（提示词/技能库/规划规则），能以较低成本迭代编排策略；在需要频繁调整策略的广告投放、活动选词、push
  文案场景尤其适用。

  - 采用“所有候选共享同一 parent + 统一评估 batch + 正增益才接受”的批量更新策略，可防止无效更新累积，并让失败尝试也作为负证据进入经验库，提升更新稳定性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM Agent 的自改进通常聚焦单一组件（模型参数、harness、可执行产物），但实际性能瓶颈会随任务分布与 Agent 能力状态动态迁移。固定优化路径无法持续匹配瓶颈，而递归自改进（RSI）要求改进机制本身也能从经验中提升。关键挑战在于：如何让自改进工作流适应动态瓶颈，同时让工作流编排能力在经验积累中持续演化。

**方法关键点**  
- 系统解耦为 Task-Agent \(T_t=(\theta, H^{Task}, A^{Task})\) 与 Meta-Agent \(M_t=(\phi, H^{Meta})\)；Meta 模型参数冻结，只演进 Meta-Harness。  
- Harness 统一为 Action / Skill / Planning 三组件；Meta-Agent 根据执行轨迹与环境反馈诊断瓶颈，动态选择 Model / Harness / Artifacts 三种组件更新工作流之一。  
- Model 更新用成功轨迹做 SFT 或 GRPO；Harness 更新执行 localize–refine–generate–validate；Artifacts 更新基于诊断指导生成修订，保持模型与 harness 不变。  
- 所有候选共享同一 parent 与评估 batch，首个有效且正增益候选被接受，否则保留 parent；拒绝的尝试仍作为经验证据。  
- Meta-Harness 演化：从 parent-candidate 配对轨迹差异中蒸馏组件特定技能和跨组件原则，每条经验包含适用条件、更新范围、条件指导、保留要求、期望行为、证据；通过 Add / Supplement / Revise / Merge 维护技能库，并更新 Meta-Harness 的 Action 接口、检索调用与执行指令。

**关键实验**  
- 6 个基准：HumanEval+、MBPP+、BFCL-v3、ACEBench、HotpotQA、2WikiMultiHopQA；两个 backbone：Qwen3-4B / Qwen3-8B。  
- 对比 SFT、GRPO、AFlow、MermaidFlow、HarnessForge、SIA、Hyperagent。  
- 12 个 benchmark-backbone 组合中 11 个领先；平均超过最强 baseline +3.11%。Qwen3-4B 总分 51.21%，Qwen3-8B 59.86%，分别超过最强 baseline 6.06% 和 3.86%。最大提升在 HumanEval+：4B 提升 14.02%。消融显示同时启用自适应编排与 Meta 演化带来 13.72% 提升，去掉 Meta 演化平均下降 5.74%。

**最值得记住的一句话**  
单一的组件更新难以应对动态瓶颈，瓶颈诊断与编排能力本身应当被设计为可学习、可演化的组件。
