---
title: 'When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search'
title_zh: 搜索智能体何时该问：面向澄清感知深度搜索的 DiscoBench 基准
authors:
- Yiling Tao
- Shihan Deng
- Meiling Tao
- Pengzhi Wei
- Zhichao Hu
- Zhihao Zhu
affiliations:
- Tencent Hunyuan
- Tsinghua University
arxiv_id: '2606.27669'
url: https://arxiv.org/abs/2606.27669
pdf_url: https://arxiv.org/pdf/2606.27669
published: '2026-06-25'
collected: '2026-07-03'
category: Agent
direction: 交互式搜索 · 歧义澄清基准
tags:
- clarification
- search agent
- ambiguity detection
- interactive QA
- multi-hop reasoning
- benchmark
one_liner: 提出动态歧义传播的交互式搜索基准 DiscoBench，揭示当前 LLM 搜索智能体主动澄清与歧义检测分离的短板。
practical_value: '- **搜索/推荐 Agent 的澄清模块设计**：在电商搜索或推荐助手中，当用户输入模糊查询（如“上次那种风格的裙子”）时，不要直接硬搜或盲目推荐，应借鉴
  DiscoBench 的歧义检测思路，先判断是否存在实体、版本或标准歧义，再向用户请求区分性线索（例如“是长裙还是短裙？”），显著提升任务成功率。

  - **工具调用的策略性分配**：实验表明，频繁调用搜索工具而忽略澄清的“SearchHeavyGuess”成功率甚至低于直接猜测（51.9% vs 56.5%）。在
  Agent 架构中应嵌入显式的歧义识别节点，当检索结果出现多个候选或冲突时强制触发澄清，而非继续消耗 Token 进行无效搜索。

  - **歧义检测与问题生成解耦**：Qwen3.6-Max 的澄清问题质量很高（CE-A 94.7%），但因为几乎不主动提问（Ask 仅 0.07）而表现垫底。这提示在构建交互式
  Agent 时需将“何时问”与“问得好”拆分为两个独立模块分别优化，例如单独训练歧义触发器。

  - **交互评估的用户模拟器复现**：DiscoBench 使用 LLM 模拟用户逐步披露区分性线索，这种低成本方案可直接迁移到电商对话 Agent 的离线评估中，用于自动化测试多轮澄清策略的效果，减少人工评估成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
当前基于 LLM 的搜索智能体（如 Deep Research）普遍假设用户查询是完整且明确的，但真实场景中用户常因记忆模糊或认知负荷给出含糊、不完整甚至包含事实错误的请求。在多跳推理的深度搜索里，这种歧义会沿推理链级联放大，导致昂贵的计算资源浪费在错误路径上。然而现有基准要么只关注静态查询歧义，要么忽视动态交互，无法评估 Agent 在搜索过程中主动识别并澄清歧义的能力。DiscoBench 由此提出，专门度量智能体是否能在多步搜索中“知何时问、会问、问出有效线索”。

## 方法关键点
- **动态歧义建模**：将复杂问题拆解为有序检查点序列，在中间节点注入四种歧义类型：实体（多个实体满足同一描述）、版本（时间/版本状态差异）、标准（评价标准或排名缺失）、事实不准确，形成 211 个样本、463 个歧义实例。
- **半自动构建流程**：先基于百科和搜索引擎种子构建多跳推理链，再由人类与 LLM 协作识别可注入歧义的节点，生成共享公共属性的候选实体并改写问题，最后为每个歧义点人工验证一条可区分目标与干扰项的鉴别性事实（用户线索）。
- **交互式评估框架**：要求 Agent 在每个检查点自主选择 SEARCH / ASK / ANSWER。使用 LLM 模拟用户（Gemini-3-Flash）渐进式提供线索，从任务效用（端到端准确率、检查点通过率）、歧义检测（准确率、F1）、交互策略（澄清问题准确率 CE-A、澄清后推进率 CE-B）和成本效率四个维度统一评测。

## 关键结果
在 Neutral 提示（不暗示歧义存在）下，11 个主流 LLM 中表现最好的 Doubao-Seed-2.0-Pro 端到端准确率仅 43.1%，检查点通过率与最终准确率之间存在明显断层（如 Claude-Opus-4.7 通过率 57.0% 但准确率 39.8%）。歧义检测 F1 与澄清质量分离：Qwen3.6-Max 检测 F1 仅 16.0% 但 CE-B 达 89.5%，反观 MiniMax-M2.7 提问更频繁但澄清推进率只有 60.7%。行为分析揭示关键模式：主动先搜索再询问（SearchThenAsk）的平均通过率高达 93.4%，远优于直接猜测（56.5%）和过度搜索后仍猜测（51.9%），反复搜索而不澄清反而比猜测更差。消融实验确认移除搜索工具后准确率断崖式下跌（Doubao 模型下降 40.7 点），且去除歧义后所有模型准确率大幅回升（+26.8~40.2 点）。

> 论文最核心的发现：**当前的搜索智能体常陷入“越搜越错”的陷阱——缺乏将检索不确定性转化为澄清请求的机制，是阻碍其处理真实模糊查询的关键瓶颈。**
