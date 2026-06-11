---
title: Decentralized Multi-Agent Systems with Shared Context
title_zh: 去中心化多智能体系统与共享上下文
authors:
- Yuzhen Mao
- Azalia Mirhoseini
affiliations:
- Stanford University
arxiv_id: '2606.10662'
url: https://arxiv.org/abs/2606.10662
pdf_url: https://arxiv.org/pdf/2606.10662
published: '2026-06-08'
collected: '2026-06-11'
category: MultiAgent
direction: 去中心化多智能体协调框架
tags:
- Multi-Agent Systems
- Decentralized Coordination
- Shared Context
- Verification
- Test-Time Scaling
- Long-Context Reasoning
one_liner: 提出去中心化多智能体框架DELM，通过共享验证上下文和异步任务队列，在软件工程与长上下文推理上显著提升性能并降低近半成本。
practical_value: '- **共享验证状态替代中心化路由**：在电商多智能体场景（如并行搜索、推荐、客服），通过维护一个全局共享的已验证上下文（可类比为购物车状态或用户意图），让多个
  Agent 异步读写紧凑进展摘要，避免依赖单一协调器合并结果，减少串行瓶颈和错误传播。

  - **先验证后准入的防污染机制**：对 Agent 写入共享状态的内容进行自动验证，检查其与原始证据的一致性，避免不可靠的信息在 Agent 间扩散。在商品知识库更新、多源信��聚合时，可借鉴此设计确保共享状态可信。

  - **分层压缩与按需展开**：用极简要点（gist）构建全局视图，需要细节时再追溯深层摘要或原始数据，降低长上下文推理的 token 开销。处理海量商品描述、用户评论、长文档问答时，可在低分辨率快速扫描后精准定位关键段落。

  - **异步任务队列与自主领取**：Agent 从队列自行认领子任务，完成后写回结果，适合大量并行子任务（如分品类推荐生成、多广告渠道创意生成），天然支持弹性扩展，并可通过失败记录复用避免重复试错。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有中心化多智能体系统（如AOrchestra、Claude Code）依赖一个主 Agent 分解任务、分发子上下文、收集与合并结果。随着子任务增多，主 Agent 成为通信和整合瓶颈；并行发现的成果需经主 Agent 再广播，可能被稀释、遗漏或变形；长上下文推理中，主 Agent 预先分配证据簇，发现关联困难，来回协调成本高。需要一种去中心化协调机制，让 Agent 直接通过共享状态高效交换已验证的进展。

## 方法关键点
- **核心架构**：DELM（Decentralized Language Models）由并行 Agent、共享上下文（C）和任务队列（T）构成。Agent 异步从队列认领子任务，读取共享上下文中的紧凑要点（gist），执行局部推理，然后将结果压缩、验证后写回 C，无需中心控制器。
- **共享状态设计**：C 中存储的不是原始轨迹，而是经过压缩的要点，并附带指向更详细证据的指针。采用分层摘要（原始文档 → 锚定摘要 S_i → 要点 G_i），Agent 默认读要点，需要细节时可“展开”到摘要或原文，平衡全局视野与成本。
- **准入验证**：任何更新写入 C 前，必须通过 LLM 验证器检查其与源证据的一致性。不忠实的归纳、数字错误等将被拒绝并重新生成，防止错误污染下游推理。
- **任务队列与动态调度**：队列空时，最近完成的 Agent 根据已有状态自动生成新的子任务，直到无需额外分解才输出最终答案。

## 关键实验
- **SWE-bench Verified**：DELM 以 Gemini 3 Flash 为基座，达到 Avg.@1 65.7%，Pass@4 77.4%，成本仅 $0.12/task；相较最强基线 AOrchestra-Parallel 提升 9.3 个百分点 Avg.@1，成本降低约一半。在 Claude Opus 4.6 上也获得 78.0% Avg.@1 与 82.5% Pass@4。
- **LongBench-v2 Multi-Doc QA**：DELM 在 GPT-5.4、Claude Sonnet 4.6、Gemini 3 Flash、DeepSeek-V4-Pro 四个模型上平均准确率均最高，提升幅度达 3.6~5.7 个百分点。消融实验表明移除验证或分层摘要均导致准确率下降，验证贡献最大。
- **与 RLM 结合**：在聚合密集的 OOLONG 基准上，DELM+RLM 混合取得 64.0% 准确率，优于单独使用两种方法，显示去中心化协调与程序化执行可互补。

## 最值得记住的一句话
去中心化多智能体系统的核心并非堆更多并行 Agent，而是建立一个可验证、可展开的共享状态作为通信基板，让发现、失败和约束真正成为可复用的全局资产。
