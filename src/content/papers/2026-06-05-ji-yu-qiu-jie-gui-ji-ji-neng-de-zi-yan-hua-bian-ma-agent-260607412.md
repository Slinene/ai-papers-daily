---
title: 'Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills'
title_zh: 基于求解轨迹技能的自演化编码Agent
authors:
- Chuan Xiao
- Zhengbo Jiao
- Shaobo Wang
- Wei Wang
- Bing Zhao
- Hu Wei
- Linfeng Zhang
- Lin Qu
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
arxiv_id: '2606.07412'
url: https://arxiv.org/abs/2606.07412
pdf_url: https://arxiv.org/pdf/2606.07412
published: '2026-06-05'
collected: '2026-06-08'
category: Agent
direction: 自演化Agent·技能注册与课程学习
tags:
- SWE-agent
- self-evolution
- trace distillation
- curriculum learning
- skill registry
- gradient alignment
one_liner: 将求解轨迹蒸馏为结构化Agent技能，驱动自适应课程生成与梯度对齐选择，在SWE-bench Verified达到50.40%
practical_value: '- **轨迹→技能→任务闭环**：将Agent执行日志中的失败模式与修复策略结构化为Skill Registry，用于定向生成针对性训练任务。可迁移到电商/推荐场景的Agent行为分析，例如从订单纠纷处理轨迹提取决策技能，生成新的客服训练case。

  - **梯度对齐课程筛选**：用held-out验证集上的策略梯度方向与候选任务梯度余弦相似度做奖励，选出与目标方向一致的训练样本。该方法可推广到任何需要从合成数据中筛选高质量样本的场景，如生成式推荐的Semantic
  ID训练数据筛选。

  - **多角色自演训练框架**：同一策略网络在Generator和Solver间切换，共享权重，用GDPO处理多尺度奖励，比单一通过率的GRPO更稳定。借鉴到多智体协作优化时，可设计类似角色切换与奖励解耦训练，减少模式坍塌。

  - **执行验证四阶段门控**：格式→接地→执行→语义的四关验证保证任务可用且非平凡，可复用于任何依赖代码/工具执行的Agent微调数据构造pipeline。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：软件工程任务依赖真实仓库中的长程交互，高质量训练实例稀缺，现有合成方法通过固定规则注入bug，生成的分布与Agent的实际能力边界脱节，训练信号随模型提升而衰减。求解轨迹记录了Agent反复失败的位置、修复策略偏差和无效探索模式，但通常仅用于奖励信号抽取后即被丢弃。本文认为这些被丢弃的轨迹正是驱动课程进化的关键。

**方法**：提出Socratic-SWE闭环自演化框架，将历史求解轨迹蒸馏为结构化的Agent Skill Registry（包含名称、描述、适用条件、操作步骤）。Generator角色采样技能并约束生成仓库内修复任务，经过格式、接地、执行、语义四阶段执行验证过滤，再通过**Solver‑Gradient Alignment 奖励**：用held‑out验证集上Solver的策略梯度作为目标方向，计算候选任务梯度与其余弦相似度，优先选择更新方向与验证梯度对齐的任务。Solver则用GDPO对通过率、修复率、回归避免三项奖励进行组内归一化后联合优化。整个过程形成轨迹→技能→任务→轨迹的闭环。

**关键结果**：在Qwen3.5‑9B基座、3轮迭代、36k训练实例预算下，SWE‑bench Verified从42.60%提升到**50.40%**（+7.80），Lite 36.67%（+7.00），Pro 22.85%（+5.61），Terminal‑Bench 2.0 14.61%（+4.50），全面超越SSR、Socratic‑Zero等基线。消融实验表明移除Skill Registry掉4.20点，验证梯度对齐的作用。扩展至5轮后达到52.00%，比SSR晚两个迭代饱和且天花板更高。

**核心洞见**：求解轨迹是Agent自我演化的可规模化基底，将失败经验转化为结构化技能并驱动课程生成，比依赖静态bug模式的合成数据更可持续。
