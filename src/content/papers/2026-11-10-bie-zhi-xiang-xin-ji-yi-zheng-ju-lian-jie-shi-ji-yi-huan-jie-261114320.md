---
title: 'Don''t Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced
  Degradation in LLM Agents'
title_zh: 别只相信记忆：证据链接式记忆缓解 LLM Agent 记忆诱导退化
authors:
- Yukyeong Lee
- Yumin Choi
- Jinheon Baek
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2611.14320'
url: https://arxiv.org/abs/2611.14320
pdf_url: https://arxiv.org/pdf/2611.14320
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 记忆可靠性 · 证据链接
tags:
- LLM Agents
- Memory
- Experience Reuse
- Evidence-Linked
- Memory-Induced Degradation
one_liner: 提出 WikiTrace，让每条经验教训链接到其原始轨迹，Agent 可在任务执行中下行核查并修正洞见，从而降低记忆副作用、提升增益
practical_value: '- 在电商/推荐的 Agent 工作流中，将历史 trajectory 蒸馏成 SOP、规则或话术时，不要只注入 insight；给每条规则保留
  source run、成功/失败结果和当时的观察。可以为 Agent 挂载只读文件系统，并提供 read/bash 等终端工具，在规则冲突或不够具体时让 Agent
  下行读原始日志，比在 prompt 中堆更多规则更能避免错误记忆误导。

  - 上线 Agent memory 时建议将 Gain 和 Regression 分开监控，而不是只看平均准确率；重点排查“无 memory 能成功、有 memory
  失败”的 case，定位是错误规则、越界使用还是 Agent 误用。

  - 失败经验有价值但风险更高：失败 trajectory 中提取的 insight 如果直接注入，回归明显升高；保留失败过程的 source evidence
  能降低这种风险。业务中失败 case 不应只存一句结论，要保留完整过程日志。

  - 该方法构造阶段只需额外生成 compilation，测试阶段 token 成本约为 Insights Only 的 1.17 倍，换来平均 3.2 点提升；若
  memory 池较大，需要先解决检索问题，因为全文注入所有 insight 会撑大 prompt。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
LLM Agent 通过外部记忆把历史轨迹蒸馏成经验教训，以在新任务中复用。但记忆并不总是有帮助，甚至会导致 **memory-induced degradation**：Agent 在原本能解决的任务上失败。分析显示，52% 的此类失败追溯到被采用的记忆项，最多的是错误教训、教训越界使用或被误用。原因在于轨迹只有成功/失败二元标签，难以判断哪一步动作真正导致结果；而现有方法只提供教训、不提供来源轨迹，Agent 无法核查。

## 方法关键点
WikiTrace 采用三层链接记忆：
- **insight**：简洁的经验教训，说明该做什么、何时适用、来源 run 及结果；
- **compilation**：对来源轨迹成功/失败原因的诊断，含关键决策和支持观察；
- **raw trajectory**：原始轨迹，保留每轮 reasoning、action、observation。

构造时，compiler 对每个训练轨迹独立生成 compilation 和至多 3 条 insight，所有层保持链接。测试时，初始 prompt 接收全部 insight 及最相似的若干历史 run；当 insight 缺少执行细节、与其他 insight 冲突或来自失败 run 时，Agent 通过 read/bash 工具下行到来源轨迹核查，必要时代替或修订 insight 后再行动。

## 关键实验
在 ALFWorld、ScienceWorld、PlanCraft、τ3-bench Retail、AppWorld 共 8 个 suite 上评估。对比 No Memory、AWM、ExpeL、ReasoningBank 和只注入相同 insight 的 Insights Only。

- WikiTrace 在所有 suite 上最高，平均 90.2，显著高于 No Memory 的 79.5；比 Insights Only 高 3.2 分。
- 将 Gain（失败转成功）和 Regression（成功转失败）分开：WikiTrace Regression 为 4.5%，低于 Insights Only 的 6.5% 和无记忆重跑的 9.7%；Gain 比无记忆重跑高 35 个百分点。
- 更难任务上 Agent 更频繁下行；证据改变计划时收益更大；失败 run 的 insight 保留来源证据后，回归显著降低。GLM-5.3-flash 骨干上结果同样成立。

## 最值得记住的一句话
Agent memory 只存可复用教训是不够的，还应保留能支持重新评估这些教训的证据；给每条经验留一条回到原始轨迹的路。
