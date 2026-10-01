---
title: 'Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?'
title_zh: 跳出盒子思考：语言模型能否选择性依赖外部指导？
authors:
- Minghan Wang
- Boyuan Wang
- Jinhang Zuo
- Yuxin Tao
- Fang kong
affiliations:
- Southern University of Science and Technology
- City University of Hong Kong
arxiv_id: '2609.39578'
url: https://arxiv.org/abs/2609.39578
pdf_url: https://arxiv.org/pdf/2609.39578
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent 工作流选择性依赖评估与训练
tags:
- LLM Agents
- Workflow Guidance
- Selective Reliance
- Counterfactual SFT
- GRPO
- Benchmark
one_liner: 提出 Box2-Bench 评估 Agent 在工作流可靠性变化时的选择性依赖，发现模型会用但难弃坏指导，反事实 SFT 加 RL 可训练选择性
practical_value: '- 在电商/导购/售后等 SOP 型 Agent 中，外部 workflow 可能过时或误导，可用 Box2 的 paired
  evaluation：固定任务和模型，只变 workflow 的 Good/Bad/Partial/Mixed 四种可靠性，能分离模型自身能力与流程依赖，避免只看端到端准确率掩盖流程鲁棒性。

  - 训练技巧可直接复用到业务 Agent：只用 bad workflow 数据做 counterfactual SFT（问题+错误流程→验证过的正确轨迹），让模型学会无视误导流程；再叠加
  outcome-based RL（GRPO）恢复对好流程的利用，避免模型对所有流程都变得抗拒。

  - 该两阶段训练会泛化到多 Agent 协商和 memory-augmented RAG：训练后模型对不可靠的 peer 建议和 corrupted memory
  更倾向验证而非盲从，适合需要多 Agent 协作或记忆增强的推荐/搜索场景。

  - 在 workflow 频繁变化的业务中，RL 奖励只看最终结果、不约束中间路径，允许模型动态决定何时偏离流程，可作为上线前鲁棒性筛选或流程迭代的辅助手段。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM 越来越多地在 agent harness 中被外部 workflow 编排，但默认人类工作流比模型更可靠。随着模型能力增强，不可靠的流程指导反而可能约束执行。传统 benchmark 要么测任务完成，要么测流程遵从，无法评估模型能否在指导可靠时受益、不可靠时抵制。

**方法关键点**
- 提出 Box2-Bench：固定模型、任务、环境、评估器，只改变 workflow 的可用性与可靠性，五种条件：No workflow、Good（全程有用）、Bad（全程误导）、Partial（k 步后停止）、Mixed（k 步后接误导步骤）。
- 用固定外部模型生成 workflow，并用独立 verifier 校验有效性、可信度、无答案泄露。
- 定义四个 paired effects：利用 Δuse=SG-S0、鲁棒 Δbad=SB-S0、停止恢复 Δstop=SP-SG、切换恢复 Δswitch=SM-SP，通过配对对比分离工作流可靠性的影响。
- 训练策略两阶段：counterfactual SFT 只在 bad workflow 下训练正确轨迹（问题+错误流程→验证过的正确解），教会模型覆盖误导流程；outcome-based RL（GRPO）只奖励最终结果、不奖励流程一致，恢复对 held-out good workflow 的利用。

**关键实验**
- 前沿模型（Gemini 3.7 Flash、DeepSeek V4 Flash、GLM 5.2）在 OpenR1-Math、DeepSWE、BrowseComp、AutomationBench 上：Good workflow 在 12 对模型-任务中 8 对提升（AutomationBench +5.9/+13.7/+16.8），Bad workflow 在全部 12 对中下降（2.3~43.3 点）；Mixed 相对 Partial 在 10/12 对中下降，显示依赖惯性。
- 训练结果：AIME 2026 上 Qwen3-4B 的 bad penalty 从 -20.0 缩减到 SFT 后 -6.7，但 good utilization 从 +13.3 降到 -3.3；再加 RL 后 Δuse 恢复到 +6.7，Mixed-Partial gap 从 -14.4 改善到 +1.1。WebShop 上 Qwen3.5-9B 的 bad penalty 从 -9.8 缩到 -0.6，good utilization 保持 +2.8。
- 迁移实验：多智能体 Economy of Minds 中 SFT 将 episode success 从 18.00% 提升到 22.67%，修复次数从 2 增至 11；LongMemEval-V2-Small 中训练后模型在 corrupted memory 下更多调用 archive 工具验证。

**最值得记住的一句话**
模型会使用好工作流，却很难在它变坏时停下来——选择性依赖是一种独立于任务能力的可靠性维度，需要 paired conditions 测、用反事实 SFT+RL 训。
