---
title: 'SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World
  LLM Agents'
title_zh: SkillCorpus：整合与评估开放技能生态以助力现实世界LLM智能体
authors:
- Yanze Wang
- Pengfei Yao
- Tianyi Sun
- Chuanrui Hu
- Yan Xiao
- Yunyun Han
- Jun Sun
- Yafeng Deng
affiliations:
- EverMind
- Shanda Group
- Peking University
arxiv_id: '2607.15557'
url: https://arxiv.org/abs/2607.15557
pdf_url: https://arxiv.org/pdf/2607.15557
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent 技能生态聚合与端到端评估
tags:
- Agent Skills
- Skill Curation
- LLM Agents
- Retrieval
- Benchmark
- SkillCorpus
one_liner: 将82万社区技能文件策展为9.6万高质量语料，并在三个真实Agent基准上实现一致增益（最高+13.4pp），揭示覆盖与Harness边界
practical_value: '- **技能库构建与质量控制**：多阶段策展流水线（结构过滤→语义去重→LLM三面评分→安全/许可硬门）可直接用于构建内部工具或知识库，尤其安全硬门（命令注入、越权等）对生产环境至关重要。

  - **检索增强代理设计**：微调嵌入+重排序+LLM终选器的三层检索栈，可借鉴至推荐系统中的工具检索或营销话术生成；按任务域自适应选择技能类别，提升相关性。

  - **Harness能力决定技能兑现**：实验表明同一组技能在不同Agent框架（Raven vs OpenClaw）下增益相差近3倍，提示在选型或自研Agent时需关注执行闭环（如自动验证-修复循环）以最大化外部知识收益。

  - **覆盖驱动增益，泛化靠生成**：增益与技能覆盖强相关（r≈0.35），缺失领域增益为零但不反损；当业务领域技能稀疏时，可考虑自动生成或自我演化补充，而非仅优化检索。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
社区贡献的LLM Agent技能文件（SKILL.md）数量爆炸，但分散、冗余、质量不一，实务中能否提升Agent在真实任务上的表现仍是未知。缺乏一个统合的质量门控语料库，也缺少端到端评估。

## 方法
- **聚合与策展**：从62个源抓取约82.1万SKILL.md文件，经六阶段流水线（解析、长度过滤、两阶段去重、LLM三面质量评分、安全硬门、OSI许可过滤）得到96,401个技能。
- **质量框架**：独立评估实用性（描述质量）、健壮性（内容一致性）和安全性（11类风险，5个硬门），复合评分用于排序而非准入。
- **检索与选择**：微调Qwen3-Emb-0.6B和Qwen3-Rank-0.6B进行召回与重排，再加LLM选择器读取技能全文，为每个任务精确输出0～2个技能。
- **评估**：在SkillsBench（87任务）、GDPVal（220）、QwenClawBench（100）三个基准，搭配OpenClaw/Raven两种Harness和Qwen3.5-27B/397B及Claude Opus 4.7，执行无技能基线与SkillCorpus条件对比。

## 关键结果
- SkillsBench平均+7.5pp，最强配置Raven×Q-397B达+13.4pp，Opus 4.7亦+8.0pp。
- 检索匹配度（覆盖代理）与增益正相关（r≈0.35），缺失域增益为零。
- 消融实验：任换原始爬虫语料或卸载微调检索栈均使增益从+13.4pp降至+5%左右。
- Harness差异显著：Raven因执行-验证-修复闭环，比OpenClaw增益高数倍。

**核心洞见**：整合社区技能能稳定提升Agent性能，但增益受技能覆盖和Harness执行闭环双重制约。
