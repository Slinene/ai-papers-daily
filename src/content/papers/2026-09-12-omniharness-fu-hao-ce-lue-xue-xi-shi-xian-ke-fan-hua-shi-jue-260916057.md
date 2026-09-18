---
title: 'OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy
  Learning'
title_zh: OmniHarness：符号策略学习实现可泛化视觉生成
authors:
- Xu Xu
- Jinxiu Liu
- Zhangbo Qiao
- Jiaxing Lu
- Xiangyu Zhang
- Yubin Gu
- Fangwei Ning
- Yan Shi
affiliations:
- Beihang University
- The Chinese University of Hong Kong
- National University of Singapore
arxiv_id: '2609.16057'
url: https://arxiv.org/abs/2609.16057
pdf_url: https://arxiv.org/pdf/2609.16057
published: '2026-09-12'
collected: '2026-09-18'
category: Agent
direction: Agent 策略学习 · 视觉生成
tags:
- Symbolic Policy Learning
- Visual Agent
- Self-directed Inquiry
- Intermediate Verification
- Plug-and-Play
one_liner: 将验证过的执行抽象为可组合符号策略，结合中间验证与自引导练习，免训练实现跨任务泛化与持续能力扩展
practical_value: '- **策略库抽象**：将验证成功的 Agent 执行轨迹转成 symbolic policy，剥离实例特定输入，保留通用 SOP
  与适用条件，可显著提升新任务泛化；在电商 Agent 中可把高转化对话流程、工具调用序列沉淀为可复用策略，减少重复试错。

  - **中间验证而非最终反思**：在长链路任务（如商品推荐中的多步 tool call、广告素材生成）中加入 step-level 校验，使错误在早期被发现并触发策略调整，比只在失败后反思能节省大量
  token 和时延。

  - **自引导练习与能力边界探索**：在真实业务流量前，让 Agent 自己生成接近能力上限的练习任务并执行，用执行反馈迭代策略，无需人工标注下游数据即可完成冷启动策略库构建。

  - **冻结模型参数、在线更新策略**：只更新策略库而不微调 backbone，方便线上快速实验与回滚；对已有 agent 框架可即插即用（frozen policy
  snapshot），与现有系统兼容性好。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
现有视觉生成 agent 方法多依赖任务特定的经验蒸馏，泛化性差；反思往往在任务完成后才进行，难以即时纠正错误；知识获取过于被动，依赖下游任务需求。  

**方法关键点**  
OmniHarness 将已验证的执行轨迹抽象为符号策略（symbolic policy），保留共享流程与适用条件，剥离实例特定输入，形成可实例化、可适配、可组合的策略库。执行过程中引入中间验证（intermediate verification），在失败时即时触发策略修正与恢复。在无下游任务约束时，通过 self-directed inquiry 自动生成并执行接近能力边界的练习任务，利用执行反馈持续更新策略，而模型参数保持冻结。  

**关键结果数字**  
在 6 个 benchmark、3 种 MLLM backbone、3 个视觉 agent 框架上验证。ComfyBench Creative 任务上 resolve rate 达 95.0%，比最强 baseline 高 27.5 个百分点；冻结的策略快照可即插即用提升现有视觉 agent 系统。
