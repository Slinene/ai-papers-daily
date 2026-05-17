---
title: 'PreScam: A Benchmark for Predicting Scam Progression from Early Conversations'
title_zh: PreScam：从早期对话预测诈骗进程的基准
authors:
- Weixiang Sun
- Shang Ma
- Yiyang Li
- Tianyi Ma
- Zehong Wang
- Colby Nelson
- Xusheng Xiao
- Yanfang Ye
affiliations:
- University of Notre Dame
- Arizona State University
arxiv_id: '2605.12243'
url: https://arxiv.org/abs/2605.12243
pdf_url: https://arxiv.org/pdf/2605.12243
published: '2026-05-11'
collected: '2026-05-17'
category: Eval
direction: 诈骗会话进程建模与心理动作预测
tags:
- scam detection
- conversational AI
- benchmark
- kill chain
- progression modeling
- psychological manipulation
one_liner: 首个面向多轮会话诈骗生命周期建模的基准，揭示FLM在追踪风险升级和操纵演化上的明显不足
practical_value: '- 诈骗杀链（Scam Kill Chain）的阶段定义可直接迁移到电商交易欺诈、杀猪盘等场景，为对话流构建结构化标签，分阶段建模风险升级。

  - 诈骗者心理动作（如建立信任、制造紧迫感）的标注框架可用于电商客服或直播带货场景，检测恶意操纵话术，保护用户。

  - 实时终止预测任务启发业务中的实时欺诈干预模型，基于早期对话片段预测是否逼近欺诈终点，可减少反应延迟。

  - 有监督编码器（如RoBERTa）大幅优于零样本LLM的结果表明，真实复杂对话的欺诈检测需要领域微调，业务中应优先训练专用小模型，而非直接依赖通用大模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有诈骗检测主要面向单次诱骗或合成对话，忽略了真实多轮会话中诈骗者逐步升级的心理操纵过程。缺乏能够刻画诈骗生命周期和进程建模的评测基准。

**方法**：作者构建PreScam基准，基于用户提交的17.8万份诈骗报告筛选并结构化出11,573个对话实例，覆盖20种诈骗类别。依据提出的“诈骗杀链”对每个实例进行层级标记，并在轮次级标注诈骗者心理动作（如建立亲密感、施压、威胁）和受害者反应。基于此定义两个任务：（1）实时终止预测，判断对话是否接近诈骗终点；（2）诈骗者动作预测，推断下一步心理战术。

**结果**：实验中，有监督编码器（RoBERTa）在终止预测上显著优于零样本LLM（GPT-4o等），F1提升超过10个点；但在动作预测上，最佳模型准确率仅约60%，表明当前模型虽然能捕捉部分诈骗线索，却难以跨轮次追踪风险升级和操纵演化。基准暴露了模型在深层对话理解上的瓶颈。
