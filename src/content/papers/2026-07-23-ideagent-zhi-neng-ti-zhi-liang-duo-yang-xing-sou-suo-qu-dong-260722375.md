---
title: 'IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation'
title_zh: IDEAgent：智能体质量-多样性搜索驱动的研究想法生成
authors:
- Varun Gumma
- Navonil Majumder
- Soumitra Sinhahajari
- Soujanya Poria
affiliations:
- DeCLaRe Lab, Nanyang Technological University, Singapore
arxiv_id: '2607.22375'
url: https://arxiv.org/abs/2607.22375
pdf_url: https://arxiv.org/pdf/2607.22375
published: '2026-07-23'
collected: '2026-07-27'
category: MultiAgent
direction: 多智能体协同质量-多样性搜索
tags:
- Quality-Diversity Search
- Multi-Agent System
- Idea Generation
- LLM
- Yield Metric
- Lineage-Based Evolution
one_liner: 多智能体框架将研究想法生成建模为质量-多样性联合搜索，记忆与修复机制大幅提升产出
practical_value: '- 质量-多样性联合搜索思路可迁移到广告文案 / 商品标题批量生成，通过记忆机制比对历史产出，避免重复，保证创意池的多样性与基本质量。

  - 多智能体协作中的修复 - 精炼流程（repair and refinement）可用于推荐系统 Agent 的迭代优化，对候选推荐进行多目标反馈驱动修改，增强推荐理由的逻辑性。

  - Lineage 追踪想法演化的机制可引入生成式推荐中，记录推荐理由的改进历史，便于调试与可解释性。

  - 联合评估指标 Yield（质量阈值下的最大互异集合）可直接作为生成式推荐、Query 推荐场景下质量与多样性统一的离线指标，弥补单一维度的不足。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 辅助研究想法生成系统通常将质量与多样性割裂优化，导致生成想法雷同或质量偏低。该工作提出应将研究想法生成视为质量 - 多样性（QD）联合搜索问题。

**方法关键点**：
- 提出**IDEAgent**，一个多智能体框架，通过**想法谱系（lineages）**管理演化过程。
- **质量驱动**：利用多目标反馈对初步想法进行专用修复和精炼，确保逻辑严谨与清晰。
- **多样性驱动**：引入轻量级顺序记忆，显式对比已完成想法、历史祖先及被拒提案，避免重复。
- **评估指标 Yield**：计算满足一定质量阈值下的最大互异想法集合，同时衡量质量和多样性。

**关键结果**：在 8 个计算机科学领域 32 个主题上，IDEAgent 的 Yield 值超出最佳基线 3.89 倍，并在 8 倍多的主题上实现了非零 Yield。消融分析表明修复与精炼步骤对提升想法的逻辑严谨性和清晰度至关重要。
