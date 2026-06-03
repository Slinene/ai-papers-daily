---
title: 'Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill'
title_zh: Skill-RM：将异构评估标准统一为 Agent 技能的奖励模型
authors:
- Tao Chen
- Gangwei Jiang
- Pengyu Cheng
- Siyuan Huang
- Yihao Liu
- Jingwei Ni
- Jiaqi Guo
- Mengyu Zhou
- Kai Tang
- Junling Liu
affiliations:
- Alibaba
- Sun Yat-sen University
- The Chinese University of Hong Kong
- Peking University
- ETH Zürich
arxiv_id: '2606.03980'
url: https://arxiv.org/abs/2606.03980
pdf_url: https://arxiv.org/pdf/2606.03980
published: '2026-06-02'
collected: '2026-06-03'
category: Eval
direction: 统一异构评估标准的 Agent 技能式奖励建模
tags:
- Reward Modeling
- Agent Skill
- Evaluation
- LLM Alignment
- Resource Orchestration
one_liner: 将奖励建模重构为可复用的 Reward-Evaluation 技能，通过过程化资源编排统一异构评估标准
practical_value: '- **技能化评估架构**：将评估逻辑封装为可复用技能（SKILL.md + 资源银行），适用于电商推荐中多维度打分（相关性、多样性、合规等）的统一编排，避免每次评估都从零开始构建提示。

  - **动态资源选择与证据链**：根据评估场景（如新品冷启动、大促活动）动态启用不同验证器（销量预测、内容审核、AB测试结果），使评估过程自适应且可追溯，可用于推荐理由审核或
  A/B 分析。

  - **可解释的奖励信号**：结构化证据字段（criterion-level evidence）使得最终得分可逐项追踪，在 Agent 多智体协作中可将“为什么判为不合格”的推理过程暴露给下游模块，提升系统透明度。

  - **工程实现借鉴**：技能包以文件系统形式组织（SKILL.md + 脚本/规则/验证器），可轻松集成到现有 Agent 框架（如 LangChain、AutoGen）中，实现评估流程的模块化、版本管理和渐进式披露（progressive
  disclosure）。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
LLM 后训练中的奖励模型正从简单的标量偏好预测演变为依赖多元资源的复杂验证：事实核查需外部参考，代码任务需可执行测试，安全约束需策略分解。然而，现有方法未能统一整合这些异质的评估标准——标量 RM 不透明，LLM-as-a-Judge 仅将规则扁平注入 prompt，漏掉了资源选择、证据追踪与信号聚合等关键环节。Skill-RM 提出将奖励建模重新表述为**可复用的 Agent 技能**，以过程化执行统一资源编排。

**方法关键点**  
- **Reward-Evaluation Skill 定义**：由 SKILL.md（流程规范）和资源银行（rubrics、references、checklists、verifiers、aggregation rules）组成，实现评估逻辑的外部化与模块化。  
- **技能介导的判断过程**：Agentic judge 分阶段诊断 → 选择 → 验证 → 聚合，动态调用相关资源，生成包含 criterion-level evidence 的结构化判决。  
- **确定性奖励读取**：通过 parse 证据轨迹输出点对点评分或多选/成对偏好，保证最终得分可追溯至每条准则。  
- **资源银行构建**：经 LLM 辅助整理、去重、脱任务化，版本冻结，确保评估可复现。

**关键实验与结果**  
- 在 RewardBench2、RM-Bench、JudgeBench 上，Skill-RM (Qwen3.5-27B) 平均分 **86.2**，显著超过同骨架 LLM-judge 基线（83.9）和多数标量/生成式 RM（如 Skywork-V2-8B 的 85.6）。  
- 当挂载样本特定资源（references/verifier outputs）时，平均分进一步提升至 **89.1**。  
- 消融实验证实：直接追加资源或工具反而导致性能下降（Avg 81.0~83.6），证明增益来自技能对资源的**组织**而非简单堆砌。  
- Best-of-10 选择在 IFEval 和 HumanEval+ 上明显改善；指令遵循 RL 中，Skill-RM 作为奖励源在 IFEval/IFBench/AdvancedIF 上平均 **45.9**，超过 VerIF（44.7）和 Tulu 3（45.1）。  

**核心要点**  
将奖励评估显式化为可执行、可检查的过程，通过技能统一调用异质资源，是提升 LLM 后训练质量与可解释性的可扩展路径。
