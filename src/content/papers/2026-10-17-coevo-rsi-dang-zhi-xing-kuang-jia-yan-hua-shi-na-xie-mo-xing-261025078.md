---
title: 'CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?'
title_zh: CoEvo-RSI：当执行框架演化时，哪些模型应跟随？
authors:
- Jiaqi Su
- Guibin Zhang
- Jie-Jing Shao
- Cong Pang
- Tiankuo Yao
- Ivor Tsang
- Haiyan Yin
- Shuicheng Yan
affiliations:
- National University of Singapore
- Agency for Science, Technology and Research (A*STAR)
- SenseTime Group Inc.
arxiv_id: '2610.25078'
url: https://arxiv.org/abs/2610.25078
pdf_url: https://arxiv.org/pdf/2610.25078
published: '2026-10-17'
collected: '2026-10-21'
category: Agent
direction: Agent 递归自我提升 · 脑体协同演化
tags:
- model-harness co-evolution
- recursive self-improvement
- meta-agent
- model merging
- rejection sampling SFT
- brain-body mismatch
one_liner: 用元智能体协调历史执行框架与模型检查点选择/合并，并用自身拒绝采样轨迹 SFT，减少递归自我提升中的脑体不匹配
practical_value: '- 在电商/广告 Agent 链路中，每次改动工具、prompt 或执行脚手架时，不要只做 prompt 调优；维护“harness
  版本—模型 checkpoint—执行反馈”档案，用元智能体在历史设计中选 checkpoint/合并，再在新 harness 下用 rejection-sampled
  轨迹做 SFT，能明显降低脑体不匹配。

  - 可建立“失败归因→局部更新”的轻量闭环：从线上执行日志筛出成功轨迹（例如 SQL 生成成功执行、指令被正确执行）做 rejection sampling，对
  7B/9B 小模型做 SFT，成本低且可追上大模型；适合垂直场景的护栏优化。

  - 模型合并/checkpoint 选择策略可作为“脑”的版本管理：当召回、排序、query 改写等 Agent 组件升级时，按执行反馈选择与当前 harness
  兼容的历史 checkpoint 或融合多个 checkpoint，减少能力丢失与行为约束。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：递归自我提升（RSI）智能体常同时演化模型和执行框架，但会出现脑体不匹配：新框架要求模型不具备的行为，或旧框架限制已有能力。现有工作多只演化框架或只微调模型，缺少双向协同。

方法：CoEvo-RSI 引入共享演化档案和执行反馈，元智能体负责两方面：从历史执行框架设计中选取/组合新的 harness，并选择或合并历史模型 checkpoint；随后在选定 harness 下对模型做适配，且只用模型自身拒绝采样轨迹做 SFT，不依赖外部大模型监督。这个双向历史继承使模型能力与执行要求对齐，降低脑体不匹配。

结果：在三个垂直任务上，Qwen3.5-9B 仅用 SFT 就能与更大模型竞争：TraceElephant 多智能体失败归因上比 DeepSeek-V4-Pro 提升 +14.16 agent accuracy；HomeBench VM 智能家居指令成功率比 GLM-5.3 提升 +4.90 success rate；在 RBAC Spider 的 role-aware text-to-SQL 上具备安全执行能力。结论：脑体对齐对这类智能体很关键，双向历史继承能有效推进智能体协同演化。
