---
title: 'Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent
  Industrial Workflows'
title_zh: 超越最终答案：审计多智能体工业工作流的轨迹级幻觉
authors:
- Harshada Badave
- Santosh Borse
- Andrea Gomez
- Harshitha Narahari
- Sara Carter
- Vishwa Bhatt
- Aishani Rachakonda
- Shuxin Lin
- Dhaval Patel
affiliations:
- IBM
- Columbia University
arxiv_id: '2605.24219'
url: https://arxiv.org/abs/2605.24219
pdf_url: https://arxiv.org/pdf/2605.24219
published: '2026-05-25'
collected: '2026-05-27'
category: MultiAgent
direction: 工业多智能体轨迹级幻觉审计与实时监控
tags:
- hallucination detection
- trajectory evaluation
- multi-agent
- industrial AI
- benchmark
- execution signals
one_liner: 提出 Trajel 基准，定义五种轨迹级幻觉类型，发现执行质量信号（如推理清晰度 AUC=0.908）比监督分类器更早预测幻觉，且 48.7%
  的轨迹存在多类型共现。
practical_value: '- **从最终输出看→轨迹级审计**：在生成式推荐或电商智能客服等 Agent 工作流中，多数幻觉（如程序性跳过步骤、指代不存在的前序输出）仅凭最终回复无法发现。可将评测单元下沉到
  Thought-Action-Observation 每一步，用细粒度标签（事实/指代/逻辑/程序/范围）诊断故障根因。

  - **轻量级实时监控信号比复杂分类器更有效**：实验中“清晰度与理由”（Clarity & Justification）这一执行质量信号单独 AUC 即达 0.908，远超微调
  BERT/NLI/Longformer（最高 AUC 0.689）。在 Agent 循环中，可优先实现类似的低成本标记（如推理是否自洽、步骤是否完整）作为 Guardrail，在轨迹进行中即时切断高风险路径。

  - **多智能体协同必须引入角色边界检查**：范围性幻觉（正确的结论但由错误 Agent 声称）在工业多智能体系统中占比 19.8%，自动化检测器对此最不敏感。在电商多
  Agent 系统（客服、推荐、订单等）中，应显式定义各 Agent 的职责规范，并在路由或汇总阶段校验输出是否越权。

  - **幻觉诊断应支持多标签，而非二元判定**：48.7% 的幻觉轨迹同时存在多种类型（如程序+事实），单纯有无幻觉的标记会掩盖故障组合。在召回或对话质量评估中，可以用多标签分类替代二元判断，辅助定向改进（如优化流程编排、加强事实校验）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM 在多智能体工业工作流（如数据中心监控、设备维护）中自主执行跨步骤推理、工具调用与多智能体协作，但幻觉评估仍停留在单步问答的最终输出，忽略 Thought-Action-Observation 轨迹中间的传播性故障。现有基准既缺乏对轨迹结构的诊断性分类，也缺少预测介入时机的研究。  

**方法关键点**  
- **轨迹结构形式化与五类幻觉分类**：将 Agent 操作序列建模为步骤三元组，定义事实性、指代性、逻辑性、程序性、范围性幻觉，均为对轨迹的结构化谓词；类型所需检测上下文依次递增（事实性只需单步，而范围性需知悉 Agent 角色）。  
- **Trajel 数据集**：基于 AssetOpsBench 收集 225 条专家注释轨迹，覆盖 6 个模型配置、42 个工业任务，采用 LLM-as-a-Judge + 盲审人双重标注，记录类型、位置、理由；人类判定幻觉率 68.3%，双机构标注一致性κ=0.456。  
- **三种检测范式**：子步骤 BERT 分类、轨迹级自然语言推断（NLI）、长上下文 Longformer，分别对应不同上下文需求。  
- **执行质量信号分析**：提取任务完成、数据检索准确性、结果验证、Agent 序列正确性、清晰度与理由共 5 个信号，测试其对幻觉的单独预测能力。  

**关键结果**  
- 程序性幻觉最常见（38.5%），48.7% 的幻觉轨迹包含多类型；自动化法官对指代性与逻辑性幻觉的 F1 仅 0.222 和 0.258，且二元准确率掩盖了类型级系统性误判。  
- 监督分类器 ROC-AUC 最高仅 0.689（NLI），远低于 LLM Judge 的 F1 0.855，但 Judge 的精度与人类仍有差距（κ=0.456）。  
- 执行质量信号中，**清晰度与理由（Clarity & Justification）单独 AUC 达 0.908**，远超所有分类器；当清晰度和结果验证两者均缺失时，幻觉率达 97.1%，可作为实时终止条件的强候选。  

**核心结论**：轨迹级审计不能仅靠最终输出检查；轻量级运行时信号比事后分类器更适于在线 Guardrail；多类型共现要求多标签评价，而非二元标签。
