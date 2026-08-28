---
title: 'Astar: Learning to Propose Evolution Directions for Self-Evolving Industrial
  AI Systems'
title_zh: Astar：从历史迭代中学习提出 AI 系统进化方向
authors:
- Jinxin Hu
- Hao Deng
- Haibo Xing
- Lingyu Mu
- Muyu Zou
- Weiqin Yang
- Sirui Chen
- Bohao Wang
- Zhezheng Hao
- Hao Zhang
affiliations:
- Alibaba Group
- Zhejiang University
arxiv_id: '2608.27287'
url: https://arxiv.org/abs/2608.27287
pdf_url: https://arxiv.org/pdf/2608.27287
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: 自进化AI系统 · 进化方向提案
tags:
- self-evolving AI
- evolution direction proposal
- reward model
- GRPO
- mid-training
- industrial AI system
one_liner: 训练专用模型从历史实验日志中学习提出有效进化方向，在 Lazada 广告召回上超越人类专家与 GPT-5.5
practical_value: '- 用历史实验日志构建“方向提案”训练语料：将任意两个实验版本配对，用 loss 曲线判定优劣，可把稀疏迭代日志扩展成密集监督信号；同时用
  AST 清理、配置白名单去除无关改动，适合在广告/推荐模型迭代日志上复用。

  - 训练轻量 reward model（0.6B 即可 AUC 0.8094）预测改动是否提升指标，替代真实训练验证做候选筛选和 RL 奖励，可大幅降低 AutoML/实验平台试错成本；在业务上可用来预筛离线实验参数。

  - 生成式方向提案用分层约束（主方向→模块→具体动作）代替直接输出，显著压缩搜索空间；在推荐系统自动调参、召回模型结构搜索等场景可以借鉴，让 LLM 按固定层级生成，提高可控性。

  - 闭环设计：把每次真实执行结果回收为训练样本，让提案模型随目标系统一同进化，避免“静态模型过时”；可集成进现有模型迭代平台，实现每周自动产生并验证多个改进方向。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现代工业 AI 系统的持续迭代循环中，提出进化方向仍高度依赖资深专家，成为自动化瓶颈。通用 LLM 虽能给出建议，但缺乏场景经验，建议泛化且不落地，因为专家知识是经验性的，难以直接注入。因此，论文提出从系统自身的历史迭代日志中训练一个专用模型，学习提出有效进化方向。

**方法关键点**：
- **数据侧**：针对监督信号稀疏，采用 pairwise 扩展——任意两个实验版本配对，用 loss 曲线判定优劣，样本量从 O(n) 增至 O(n²)。针对噪声，先用 reachability analysis、AST 归一化、配置白名单做规则过滤，再用 LLM 做演化意图语义过滤。
- **输出结构**：引入分层提示（L1 粗粒度方向 → L2 细粒度动作 → L3 具体计划）+ 进化想法，约束巨大的方向搜索空间。
- **模型侧**：三阶段训练——mid-training 112B tokens 学习结构化输出与领域知识；SFT 81.1M tokens 只保留正向样本（loss 降低）；RL 用 GRPO 提升探索，并用训练好的 reward model 作为快速代理评估，AUC 达 0.8487，远高于人类专家 0.6142 和最强通用 LLM 0.5997。
- **闭环流程**：生成候选 → reward model 排序 → Code Agent 实现 → 训练评估 → 结果回收为样本，持续进化。

**关键实验**：在 Lazada 广告召回模型上评估，对比人类专家与 7 个通用 LLM。Astar-8B 单提议成功率 S@1 达 0.6786，超过人类专家 0.3229 和 GPT-5.5 0.3071；RM@1 0.7183。连续 20 次迭代，offline Hitrate@200 提升 23.6%；在线 A/B 测试 GMV +4.86%，广告收入 +1.82%，点击 +0.84%，订单 +1.79%。消融显示 mid-training 贡献最大，SFT 与 RL 带来进一步提升；输入用自然语言摘要优于原始代码，分层提示提升 reward AUC。

**最值得记住的一句话**：历史迭代日志中可以提炼出超越人类专家的进化策略，而训练 reward model 将“天级验证”变成“秒级预测”，是让 AI 系统自举进化的关键。
