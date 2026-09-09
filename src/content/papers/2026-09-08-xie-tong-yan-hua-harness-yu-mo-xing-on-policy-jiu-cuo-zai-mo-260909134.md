---
title: 'Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models
  Catch Up Where Imitation Fails'
title_zh: 协同演化 Harness 与模型：On-Policy 纠错在模仿失效处帮助弱模型追赶
authors:
- Zhou Yu
- Bin Bi
- Shiva Kumar Pentyala
- Shubham Mehrotra
- Sougata Chaudhuri
- Shilpa Bhagavath
- Zeyuan Chen
- Ran Xu
- Phil Mui
- James Zhu
affiliations:
- Salesforce AI
arxiv_id: '2609.09134'
url: https://arxiv.org/abs/2609.09134
pdf_url: https://arxiv.org/pdf/2609.09134
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: Agent harness 与模型权重协同优化
tags:
- Agent harness
- LoRA
- On-policy correction
- Imitation learning
- Co-evolution
- Enterprise agents
one_liner: 在已演化的 Agent harness 下，全轨迹模仿专家会破坏弱模型的 harness 适配，而基于学生自身 rollout 的 on-policy
  局部纠错可无损叠加模型增益
practical_value: '- 在已有优化 prompt/tool/hook 的 Agent 系统上做 LoRA 微调时，避免直接用专家全轨迹 SFT；应保留学生自身
  rollout 的规划风格，只对失败 turn 做局部纠正，否则会破坏 harness 与模型的适配，导致全面退化（文中 -14.9 点）。

  - 可以借鉴 on-policy expert correction 管道：用 meta-level agent 定位失败 turn，让专家只重写该 turn，保持前后步骤不变；训练数据仅约
  500 条，微调不到 1 小时，适合迭代式 co-evolution。

  - 若业务中需要小模型+定制 harness 降本，先演化 harness 再考虑模型更新时，先检查失败分布中的 planning 与 knowledge 变化；直接模仿专家会引入
  planning 漂移，而 on-policy 纠正只提高知识覆盖、不增加规划失败。

  - 该结论也适用于其他形式的 scaffold（如推荐系统的 prompt、RAG 的 system prompt 或工具调用约束）：如果 scaffold 已围绕模型行为调优，后续权重更新需以
  on-policy 数据为主，避免分布偏移。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
Agent harness（system prompt、工具集、执行钩子、上下文管理）已被证明能让小模型在领域任务上以极低成本接近 frontier 模型。但 harness 与模型权重是两大可调杠杆，两者如何协同演化仍不清楚。自然想法是先用弱模型演化 harness，再用更强专家的轨迹微调弱模型以进一步缩小差距。

**方法关键点**
- 在七个企业 agentic benchmark 上，先为弱模型 Qwen3-Coder-30B-A3B 演化 harness，其成功率从 29.2% 升至 78.0%（+48.8）。
- 更强专家 Gemini 在同一 harness 下表现更好（93.6%），且充分使用 harness 组件，说明弱模型仍有模型侧 headroom。
- 全轨迹模仿专家做 LoRA-SFT 在演化 harness 下反向退化：成功率从 78.0% 降至 63.1%（-14.9），所有任务均下降；失败分析显示知识获取增加，但规划失误从 1.1% 飙升至 14.6%，破坏了模型与 harness 的 planning fit。
- 提出 on-policy expert correction：由 meta-level MLE agent 定位弱模型自身 rollout 中失败的单轮，让专家只重写该 turn，保留其余全部内容，生成约 500 条最小编辑轨迹进行 LoRA-SFT。

**关键实验数字**
- 演化 harness 后弱模型 78.0%；专家在相同 harness 下 93.6%。
- 全轨迹模仿：78.0%→63.1%（-14.9），同样模仿在基线 harness 下反而提升 29.2%→35.5%（+6.3），说明问题出在 imitation 与 harness evolution 的交互。
- On-policy correction：78.0%→79.7%（+1.7），五个任务正收益；规划失败仅 +0.7，知识失败继续下降 -3.0。
- 训练成本不到 1 小时 H200，可安全叠加进 co-evolution loop。

**最值得记住的一句话**
在已围绕特定模型优化的 harness 上做模型权重更新时，教学信号必须 on-policy，否则模仿更强模型会破坏 harness fit。
