---
title: Skill Reuse as Compression in Agentic RL
title_zh: 技能重用即压缩：提升LLM智能体泛化性的RL训练方法
authors:
- Zhikun Xu
- Yu Feng
- Jacob Dineen
- Taiwei Shi
- Jieyu Zhao
- Ben Zhou
affiliations:
- Arizona State University
- University of Pennsylvania
- University of Southern California
arxiv_id: '2605.31509'
url: https://arxiv.org/abs/2605.31509
pdf_url: https://arxiv.org/pdf/2605.31509
published: '2026-05-29'
collected: '2026-06-01'
category: Agent
direction: Agent RL训练 · 技能重用压缩
tags:
- Agentic RL
- GRPO
- MDL
- Skill Reuse
- Compression
- Generalization
one_liner: 提出REUSERL，基于MDL原则惩罚非结构化行为，强制智能体学习可重用技能模式，显著提升分布外泛化
practical_value: '- **对话/推荐策略训练**：将行为序列压缩奖励引入RL训练，可避免策略陷入任务特定捷径，强制重用高频子模式，提升多轮对话或推荐策略的泛化性。

  - **用户行为技能挖掘**：借鉴BPE在线字典构建方法，从成功交互轨迹中提取高频行为组合作为“技能”，用于奖励塑形或离线意图挖掘，在电商用户路径分析中可挖掘稳定购物模式。

  - **MDL作为正则项**：在LLM生成式推荐或Agent策略优化中，可引入描述长度正则，不仅压缩模型参数，还压缩行为序列本身的复杂度，迫使模型学习紧凑、可解释的决策逻辑。

  - **鲁棒性提升**：通过惩罚idiosyncratic行为，可缓解强化学习训练中的“推理坍塌”，避免策略因为过度优化单次成功率而遗忘泛化模式，适合需要应对多样化用户需求的长程任务场景。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM智能体在多回合交互任务中通过RL训练时，常因仅优化任务成功率而学到脆弱的、难以迁移的捷径（推理坍塌）。**核心假设**：可泛化的行为模式应具有结构可压缩性——即成功的轨迹能分解为少量可重用技能的组合。现有方法（如SkillRL、ERL）虽通过经验回放或教师提炼缓解该问题，但缺乏一个统一原则来显式衡量和促进这种可重用结构。

### 方法关键点
- **技能投影**：将原始动作根据动词规则映射为离散技能字母表（如ALFWorld的5种原子技能），将轨迹转化为技能序列。
- **MDL驱动的字典提取**：基于最小描述长度原则，定义双码总长（字典存储代价 + 用字典短语编码技能序列的代价），通过在线BPE合并迭代搜索最小化该目标的共享技能字典。
- **分段成本作为RL奖励惩罚**：在GRPO训练中，对成功轨迹附加分段成本`seg(s,C)/T`——轨迹在字典C下所需的最少短语数除以最大步长，鼓励使用长短语（高度可重用），惩罚罕见短语（idiosyncratic）的使用。
- **EM交替优化**：E步从当前成功批中提取字典；M步用固定字典产生的分段成本更新策略，迭代压缩成功行为的联合描述长度。
- **理论支撑**：证明纯轮次长度惩罚是固定单字字典下的分段成本特例，并给出PAC-Bayes泛化界，表明低描述长度意味着低期望泛化误差。

### 关键实验
在三个基于文本的Agent基准上（ALFWorld、TextWorld-Cooking、Countdown-Stepwise）对比：
- **Vanilla GRPO**（无压缩信号）
- **纯轮次长度惩罚**（折扣步数）
- **REUSERL-SegCost**（含/不含全局成功缓冲）

**核心结果**：
- ALFWorld OOD场景：REUSERL-SegCost达93.28%（GRPO为79.85%，纯长度91.79%）。
- TextWorld-Cooking：纯长度因逼迫过短路径导致74%的烧焦失败率，而REUSERL将烧焦率降至3.3%，成功率提升17.7个百分点（64.03%→81.73%）。
- Countdown-Stepwise：REUSERL使零重置求解率达99.9%，并自然涌现出乘除算子组合模式（MUL/DIV使用率从3.1%升至10.9%）。

> 关键洞察：有效压缩信号必须识别结构，而非单纯减少步长；可重用技能子序列的激励使策略内化任务间共享逻辑，从而突破训练分布，避免陷入本地最优陷阱。
