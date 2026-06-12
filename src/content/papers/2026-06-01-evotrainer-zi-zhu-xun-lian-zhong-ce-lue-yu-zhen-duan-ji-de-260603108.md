---
title: 'EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous
  Agentic Reinforcement Learning'
title_zh: EvoTrainer：自主训练中策略与诊断羁绳的共进化框架
authors:
- Guhong Chen
- Yingcheng Shi
- Yongbin Li
- Binhua Li
- Xander Xu
- Hu Wei
- Shiwen Ni
- Min Yang
- Jieping Ye
affiliations:
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- Tongyi Lab, Alibaba Group
- Alibaba Group
- SUAT
arxiv_id: '2606.03108'
url: https://arxiv.org/abs/2606.03108
pdf_url: https://arxiv.org/pdf/2606.03108
published: '2026-06-01'
collected: '2026-06-12'
category: Training
direction: 自动化训练 · 共进化诊断 harness
tags:
- EvoTrainer
- Autonomous Training
- Agentic RL
- Training Harness Co-evolution
- Skill Reuse
- Diagnostic Gap
one_liner: 提出 EvoTrainer，让训练诊断 har ness 随策略共同进化，在 SWE/Math/Coding 上超越人工 RL 基线
practical_value: '- **训练诊断基础设施的持续进化**：在推荐系统模型迭代中，可引入版本化的监控指标（如 CTR、留存）和诊断分析器，当业务指标停滞时，自动探测新瓶颈（如曝光偏差、用户群体差异），触发诊断升级。

  - **持久化训练技能库**：积累已验证的调参机制（如方差过滤、长度惩罚），跨项目复用，类似 StdGroupFilter 在 SWE→Math/Coding
  的迁移，可构建推荐场景的“策略模板库”。

  - **避免纯 score 驱动的短视自主迭代**：通过引入行为层诊断（如用户行为序列检查、重复曝光统计），防止虚假高分模型被错误提升，类似 Git 泄露审计。

  - **版本化实验管理与回溯**：保留完整训练谱系和干预记录，便于事后归因，为自动实验平台提供审计和演绎能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
自主模型训练通常被简化为“配方搜索”，训练侧诊断工具（harness）保持静态，这在 agentic RL 中尤为不足——稀疏奖励、行为退化等复杂故障模式难以被固定指标捕捉。论文指出，训练的决策基础设施（如何解读版本结果、触发干预）本身需要随训练版本一起进化。

**方法关键点**  
- **双进化架构**：下层策略进化通过版本受控探索（单因子干预、Git worktree 隔离）生成候选训练版本；上层训练器反思通过诊断缺口检测、指标扩展、分析器定制、外部证据检索实现 harness 进化，并积累可复用技能库。
- **持久化记忆与技能库**：存储版本谱系、案例快照、已验证的诊断技能和检索记录，使后续实验可复用先前发现的机制（如 SWE 中的 StdGroupFilter 被 Math 和 Coding 重用）。
- **训练基础设施**：基于 GRPO + Clip-Higher + 弱 KL 正则的 RL 核心，在 SWE 中设计了包含 correctness、instruction-following、search-before-edit 等组件的奖励函数，并通过进化过程确定最终配置。
- **自治范围**：训练器 agent（Claude Sonnet 4.6）自主执行诊断循环和干预提议，但高代价操作（启动训练、版本合并）由人类审批。

**关键实验结果**  
- 在 SWE-9B 上达到 38.16 BC%，超过人工 RL 基线 33.77 BC%（+4.39），同时高于所有自动迭代和算法基线。
- Math（AIME 2024/2025、CNMO 2024 平均）和 Coding（LiveCodeBench）中均超越或持平人工基线，且保留策略因领域而异。
- 组件消融：纯分数驱动路径在 v3 饱和（33.33 BC%），引入丰富诊断后提升至 38.16 BC%；harness 审计阻止了 Git 泄漏导致的虚假高分分支（48.80 → 31.04）；StdGroupFilter 跨域迁移分别在 Math 和 Coding 中带来 +0.96 和 +1.17/ +1.08 增益。

**核心启示**  
自主训练不应只优化 score，而是让诊断系统与策略协同进化，并通过记忆与技能复用实现累积性提升。
