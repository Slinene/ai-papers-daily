---
title: 'AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning'
title_zh: AutoSFT：自动化监督微调数据研究的多智能体系统
authors:
- Bingxiang He
- Pengqi Sun
- Shihao Peng
- Shaoxuan Li
- Huiyu Xiao
- Hongjian Shi
- Zixuan Fu
- Ziqing Qiao
- Yuxin Zuo
- Cheng Qian
affiliations:
- Tsinghua University
- Beijing University of Posts and Telecommunications
- ModelBest Inc.
- University of Illinois Urbana-Champaign
- The Chinese University of Hong Kong
arxiv_id: '2610.22194'
url: https://arxiv.org/abs/2610.22194
pdf_url: https://arxiv.org/pdf/2610.22194
published: '2026-10-14'
collected: '2026-10-16'
category: MultiAgent
direction: 多智能体协作优化 SFT 数据
tags:
- Multi-Agent
- SFT Data
- Data Action Space
- Automated Data Engineering
- LLM Post-training
one_liner: 多智能体系统 AutoSFT 将执行与分析分离，覆盖比例调整、剪枝、修复、替换、合成等数据动作，显著提升 IFEval/IFBench/MBPP+
practical_value: '- 自动化数据管道不要只做单一动作（如仅选样本），可定义丰富的数据动作空间：比例调整、去噪/剪枝、标签修复、样本替换、合成。业务中可把数据迭代从“选数据”升级为“修数据+造数据”。

  - 多智能体架构中，将执行与分析分离：executor 只保留精简结果，避免单 agent 上下文被执行输出淹没。电商/推荐 Agent 系统可借鉴，降低长流程中的上下文丢失。

  - 分析子代理从多个独立角度（如类别平衡、质量、难度）并行提案，再汇总，比单 agent 全局判断更有效。可用于推荐数据质量审计或 query 优化。

  - 公平对比：固定模型/训练器/预算，每轮从 base model 重训，隔离每个组件贡献。评估数据策略时值得采用，避免增量训练的归因偏差。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM agent 自动化 post-training 时容易收敛到 SFT 并大量修数据，但现有系统只给一种控制——从固定池选行或调用生成器，而人类数据工程师会调整比例、剪枝、修复、替换、合成。需要一套能覆盖多种数据动作的自动化系统。

**方法关键点**：先定义数据动作空间，发现单 agent 只能做到调整类别比例，且上下文被执行输出塞满、搜索中被丢弃。AutoSFT 采用多智能体：meta agent 分离执行与分析，从独立角度收集分析子代理的提案，并调用 synthesis 子代理生成池中缺失的能力；模型、训练器、预算固定以保证公平比较。

**关键结果**：executor 将上下文丢失减半；analysis subagents 提升最佳 IFEval +6.5；synthesis 额外带来 +3.4 IFEval 和 +2.9 IFBench。同一循环迁移到代码任务，analysis 相对无改进的单 agent 提升 +3.7 MBPP+。每轮从 base model 重训，各组件贡献可单独归因。结论表明自动化 SFT 数据研究更依赖覆盖多样数据动作，而非强化单一动作。
