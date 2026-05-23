---
title: Efficient Agentic Reasoning Through Self-Regulated Simulative Planning
title_zh: 通过自调节模拟规划实现高效智能体推理
authors:
- Mingkai Deng
- Jinyu Hou
- Lara Sá Neves
- Varad Pimpalkhute
- Taylor W. Killian
- Zhengzhong Liu
- Eric P. Xing
affiliations:
- Institute of Foundation Models (IFM)
- Carnegie Mellon University
arxiv_id: '2605.22138'
url: https://arxiv.org/abs/2605.22138
pdf_url: https://arxiv.org/pdf/2605.22138
published: '2026-05-20'
collected: '2026-05-23'
category: Agent
direction: 自调节模拟规划 · Agent 推理优化
tags:
- Self-Regulation
- Simulative Planning
- World Model
- Agentic LLM
- Reinforcement Learning
- Reasoning Efficiency
one_liner: 分解智能体为反应执行、模拟规划和自调节三系统，用更少推理token达到竞争性准确率。
practical_value: '- **在Agent工作流中引入配置器模块**：可借鉴SR²AM的配置器（System III）设计，对每一步状态评估是否需要调用规划模块（System
  II），避免不必要的深度推理。在电商对话或推荐Agent中，可根据用户问题复杂度、当前信息充分度动态决定是否进行多步推理，从而降低平均推理成本。

  - **利用模拟规划提升长期交互任务的成功率**：System II 通过世界模型（LLM本身）预测未来状态和动作序列来显式规划，可应用于需要多轮交互的推荐或搜索场景（如多步商品比较、旅行规划）。显式地模拟“提出动作
  → 预测下一状态”可增加规划的可解释性和可纠错性。

  - **RL训练引导模型“深度规划而不频繁规划”**：实验表明RL使规划深度增加22.8%而规划频率仅增2%，这意味着可以训练模型在需要时规划得更长远，而不是盲目增加推理次数。这个trick可直接用于效果/成本敏感的微调中，用RL奖励函数引导模型在有限token预算下提升任务完成率。

  - **数据构造方法：从强模型轨迹重建结构化规划**：v1.0通过注释器从已有链式思考中提取配置器决策和模拟规划内容，再用于监督微调，可作为一种高效的数据增强策略。如果业务中已有成功Agent的完整对话轨迹，可以用类似方法逆向构造结构化SFT数据，快速冷启具有自调节规划能力的小模型。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前主流方法将智能体视为带有自适应计算的反应策略（如无边界的链式思考），期望规划行为从数据和计算中隐式涌现，但缺乏对规划存在性、结构和深度的控制。这导致训练中推理token消耗剧增而准确性增益递减。本文提出将智能体决策分解为三个协同系统：反应执行（System I）、模拟推理（System II）和自调节（System III），以同时提高准确率和效率。

**方法关键点**
- **三系统架构**：System II 利用LLM作为世界模型，在语言空间中模拟候选动作序列及其对未来状态的预测，进行显式目标导向规划；System III 作为学习的配置器，逐步决定是否及如何进行规划；System I 处理细粒度推理和直接动作执行。
- **两种实现路径**：v0.1 记录多模块提示系统的决策，展示可行性；v1.0 从预训练推理LLM（DeepSeek-V3.2）的轨迹中由注释器LLM重建配置器决策和结构化规划内容，更易于扩展且保留原有自由形式推理。
- **训练流程**：先对SFT数据（包含决策、规划、推理）进行监督微调，再通过RL（GRPO，带分组归一化优势）优化，奖励函数结合答案正确性、结构合规性和最终答案可提取性。
- **世界模型**：LLM本身充当世界模型，规划时生成当前信念状态、计划动作和预测未来状态。

**关键实验**
- 在11个基准（数学AIME、MATH-500，科学GPQA、HLE，表格FinQA、MultiHier，网络信息检索BrowseComp、GAIA等）上评估。
- SR²AM-v0.1-8B 总体Pass@1达57.0，与120B–355B参数系统相当；SR²AM-v1.0-30B Pass@1达71.3，与685B–1T参数模型竞争，且相比同规模竞争模型推理token消耗减少25.8–95.3%。
- RL使平均规划步数增加22.8%，而规划频率仅增2.0%，表明模型学会了更深远地规划而非更频繁地规划。
- 消融实验确认：移除自由形式推理导致最大准确率下降，移除选择性规划导致token消耗增加最多，验证三个系统互补。

**一句话总结**：自调节模拟规划让智能体“少而深”地规划，是在不牺牲准确率前提下控制推理成本的有效架构。
