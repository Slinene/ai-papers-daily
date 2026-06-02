---
title: 'Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents'
title_zh: 技能不是一刀切：面向LLM Agent的模型感知技能对齐
authors:
- Jianxiang Yu
- Jiapeng Zhu
- Bochen Lin
- Qier Cui
- Zichen Ding
- Xiang Li
affiliations:
- East China Normal University
arxiv_id: '2605.30723'
url: https://arxiv.org/abs/2605.30723
pdf_url: https://arxiv.org/pdf/2605.30723
published: '2026-05-28'
collected: '2026-06-02'
category: Agent
direction: Agent技能库的模型定制化进化与重写
tags:
- Model-Aware Skill Alignment
- LLM Agents
- Skill Library
- Hill Climbing
- UCB Tree Search
- Skill Rewriter
one_liner: 不同模型需要不同的技能表述，MASA通过层次化进化搜索和轻量重写器实现模型定制化技能库，提升agent任务成功率。
practical_value: '- 不同规模的LLM对技能（提示）粒度、风格极度敏感，在业务agent（如电商导购、客服）中必须针对所选模型定制技能库，避免照搬通用模板。

  - MASA的搜索式技能进化可借鉴：使用教师LLM基于故障归因和模型能力卡迭代重写技能，通用策略用爬山法，任务特定技能用UCB树搜索，并引入“无效动作率”惩罚防止agent空转。

  - 训练轻量重写器（4B小模型）替代昂贵教师搜索，能在无环境交互下将技能适配到新模型，大幅降低多模型部署成本，适合A/B测试或快速升级。

  - 模型能力卡（架构、训练数据、强弱项）作为条件信号，可指导自动prompt/技能改写；业务中可构建类似画像，用于技能、提示的动态调优。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有LLM agent常通过检索外部技能库来提升长程交互任务性能，但技能库通常被认为模型无关，不同模型共用同一套技能表述。本文通过控制实验发现，技能的有效性高度依赖模型：同一套技能可能对一个模型有益，对另一个有害，最优技能粒度随模型规模和家族变化，且无单调规律。这挑战了“一刀切”的假设，引出模型感知技能对齐的需求。

**方法关键点**  
- 提出MASA框架，含两个阶段：搜索时层次化技能进化，部署时轻量技能重写器。  
- 技能进化：教师LLM基于目标模型能力卡（架构、训练特点、强弱项）和失败轨迹分析，分两级优化：爬山法迭代改进通用技能，UCB树搜索对每类任务专用技能寻优，目标函数含“无事发生率”惩罚防止空转。  
- 技能重写器：用进化轨迹（输入-优化技能）训练4B模型，输入模型卡和原始技能，直接输出适配技能，无需环境交互或教师。  

**关键实验**  
在ALFWorld、WebShop、搜索增强QA三个环境，基于Qwen3-{4B,8B,14B,32B}评估。与无技能、基础技能库、一次性教师改写对比，MASA在所有骨干上取得最高成功率，ALFWorld平均提升最高+25.8点（8B），WebShop大幅缓解大模型过度思考导致低效，步数减半。重写器泛化到未见任务和环境，性能超过教师DeepSeek-V4。消融验证两级优化缺一不可，模型卡对重写器至关重要。

**最值得记住的一句话**  
技能必须“看模型下菜碟”，MASA通过进化搜索和轻量重写实现高效的模型感知技能对齐，为多型号agent部署提供了实用方案。
