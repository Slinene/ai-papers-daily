---
title: 'WHALE: A Simple Recipe for Joint Harness-Weight Optimization'
title_zh: WHALE：权重与执行框架交替优化的简单配方
authors:
- Haechan Kim
- Yoonho Lee
- Gisang Lee
- Chelsea Finn
- Kangwook Lee
affiliations:
- KRAFTON
- KAIST
- Stanford University
arxiv_id: '2609.00196'
url: https://arxiv.org/abs/2609.00196
pdf_url: https://arxiv.org/pdf/2609.00196
published: '2026-08-30'
collected: '2026-09-04'
category: Agent
direction: Agent 权重与执行框架联合优化
tags:
- Agent Harness Optimization
- Alternating Optimization
- Rejection Sampling Fine-Tuning
- Meta-Harness
- LLM Agents
one_liner: 交替执行模型权重更新与 harness 搜索，实现 Agent 系统联合优化，大幅超越单组件和 prompt 级优化
practical_value: '- 把 agent 的 harness（工具接口、格式解析、终止策略、错误处理等代码）纳入优化范围，而不仅仅调 prompt；在电商搜索
  Agent 中，商品检索 query 改写/后处理、结果格式化、答案抽取、turn 限制等代码都可被联合搜索优化。

  - 采用交替训练：模型在固定 harness 下做 rejection sampling 微调，然后固定模型搜索 harness；使用小步交替而非先训练完再做
  harness 搜索，避免对旧 harness 过拟合，且能更快达到更高准确率。

  - 用训练信号（如 training reward 滑动窗口不再改进）做 per-phase early stopping，自动决定切换时机，减少超参调节；工程上可实现为
  patience 规则。

  - 先用低成本 harness 搜索做瓶颈诊断：如果 harness 搜索能快速匹配 weight-only 的峰值，说明 harness 是瓶颈，优先优化 harness；如果
  harness 搜索收益很低，可能模型是瓶颈，需要先做权重更新，指导资源投入。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Agent 系统性能同时依赖模型权重和可执行 harness 代码。单独优化任一组件都可能被冻结的另一方卡住瓶颈：权重更新会改变哪个 harness 有效，harness 更新也会改变模型能力是否被暴露。现有联合优化方法只协调权重和文本 prompt，没有触及更广的 harness（工具接口、上下文管理、错误处理、终止策略等）。因此需要联合优化模型权重和 harness。

**方法关键点**  
- 提出 WHALE 框架，交替两个阶段：在当前 harness 下更新模型，再在更新后的模型下搜索更好的 harness，循环进行。  
- 权重更新阶段采用 online rejection sampling fine-tuning (RSFT)：只对 verifier 接受的 rollout 做 token-normalized 监督微调，在线同步权重到 rollout worker。  
- harness 搜索阶段采用 Meta-Harness：迭代 propose-evaluate-select，每个候选 harness 在固定模型下用训练集和二进制 verifier 评估，选择最高分者。  
- 调度设计：可使用固定 phase duration (E, I) 或自适应 patience 规则，基于训练信号（训练奖励不再改进）自动切换，避免噪声和过度优化。  
- 实验覆盖三个领域：SearchQA、Math、Chess Puzzles，模型为 Qwen3.5-2B/4B，对比 weight-only、harness-only、Fast-Slow Training (FST，仅 prompt+weight)。

**关键结果数字**  
- WHALE 比最强单组件 baseline 高出 7.67–24.38 个百分点；比 FST 高 4.15–13.00 个百分点。  
- 领域瓶颈差异明显：SearchQA 中 harness 搜索仅用 weight-only 5.79% 的 rollout 就达到其峰值准确率，属于 harness-dominant；Math 中 harness 搜索几乎无效，直到先做权重更新，属于 model-dominant。  
- 小交替更新优于 stagewise：准确率分别高 5.32pp (SearchQA) 和 9.16pp (Math)，且只需 stagewise 29% 和 49% 的 rollout。  
- 自适应调度在 SearchQA 达到 52.82%，比最佳固定调度高 2.73pp，且 rollout 减少 23%。

**最值得记住的一句话**  
Agent 模型和 harness 是相互耦合的联合系统，应该交替优化，且调度需在噪声和过优化之间取得平衡。
