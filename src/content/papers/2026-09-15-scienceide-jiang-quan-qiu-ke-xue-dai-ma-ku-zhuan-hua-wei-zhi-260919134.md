---
title: 'ScienceIDE: Turning World''s Scientific Codebase into Agent Learnable Environments'
title_zh: ScienceIDE：将全球科学代码库转化为智能体可学习环境
authors:
- Hejia Geng
- Zesen Huang
- Haoyang Li
- Wenbin Li
- Koutian Wu
- Zihan Zhou
- Yuanbo Pang
- Weihao Liu
- Zigong Xu
- Zhiping Li
affiliations:
- AItonomy Foundation
- PhAI-Labs
arxiv_id: '2609.19134'
url: https://arxiv.org/abs/2609.19134
pdf_url: https://arxiv.org/pdf/2609.19134
published: '2026-09-15'
collected: '2026-09-17'
category: Training
direction: 科学智能体环境构建与模型训练
tags:
- Scientific Agents
- Environment Construction
- SFT
- RL
- Code Repair
- LLM
one_liner: 提出ScienceIDE基础设施，将科学代码库转化为可编程环境，训练PhAI-IDE模型家族在科学代码修复与通用基准上获得提升
practical_value: '- 构建领域专用可执行环境：可将推荐系统、广告投放等业务代码库封装为类似 Gym 的交互环境，提供任务生成、执行、验证 API，自动生成
  SFT 和 RL 训练数据，降低人工标注成本。

  - 专家定义验收标准：在业务中明确可量化的验收指标（如 CTR、ROI、延迟），让 Agent 围绕这些标准迭代优化，可作为奖励函数设计依据，提升训练信号质量。

  - 环境与模型协同训练：利用环境生成的交互轨迹训练 LLM，使模型不仅能生成代码，还能操作业务系统，提高 Agent 在真实任务中的成功率。

  - 正向迁移验证：科学领域训练带来的通用能力提升提示，在电商/推荐领域积累的领域交互数据也可能反哺通用模型，可探索内部数据训练基础模型的新路径。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：科学代码库蕴含大量可执行知识，但碎片化工具链、隐式领域约定和专门正确性标准导致难以转化为可靠的学习经验，作者称为“科学经验瓶颈”。

**方法关键点**：提出 ScienceIDE 基础设施，将世界科学代码库转化为可编程的智能体环境。由专家定义科学案例和验收标准，智能体将代码仓库改造为可执行环境，支持任务生成、执行和科学验证。这些环境为监督微调（SFT）、强化学习（RL）和评估提供统一基础。利用验证过的交互轨迹训练 PhAI-IDE-72B、PhAI-IDE-9B、PhAI-IDE-4B 模型家族。

**关键结果**：模型家族在留出科学代码修复任务上取得增益，并在选定的通用代码、推理和知识基准上表现提升，证明科学经验可正向迁移至更广泛能力。
