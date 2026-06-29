---
title: 'Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration
  by Web Agents'
title_zh: Ko-WideSearch：韩语广度搜索基准，评估Web Agent穷举枚举能力
authors:
- Minbyul Jeong
affiliations:
- Upstage AI
arxiv_id: '2606.27595'
url: https://arxiv.org/abs/2606.27595
pdf_url: https://arxiv.org/pdf/2606.27595
published: '2026-06-24'
collected: '2026-06-29'
category: Agent
direction: Agent 广度搜索基准
tags:
- Web Agents
- Benchmark
- Breadth Search
- Korean
- F1 evaluation
- Enumeration
one_liner: 提出韩语广度搜索基准Ko-WideSearch，揭示当前Agent擅长找回实体集合但严重缺失行级属性填充
practical_value: '- 可借鉴其自动化合成-验证流水线思路，低成本构建领域内结构化信息枚举任务，用于评估搜索Agent的广度搜索能力。

  - 电商场景中常有“列出XX品类下所有品牌及各自属性”需求，可参考该基准的表格化评估方式，同时关注集合完整性与单元格正确性。

  - 难度旋钮设计（表格宽度、复合键）可迁移到渐进式任务生成，按需控制Agent需要跨多少页面聚合信息。

  - 发现自由文本单元格是主要失败点，提示在业务Agent中应优先优化开放式属性抽取，可考虑结合知识库或结构化提示约束输出。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有Web Agent评测几乎只测深度搜索（在约束链后锁定单一答案），广度搜索（穷举封闭集合并填充每项属性）严重缺乏，尤其非英语场景。构建广度基准成本极高，需保证黄金集合完整且每个单元格正确。

**方法**：提出Ko-WideSearch，通过自动化合成-验证流水线生成韩语广度搜索任务。每个任务指定一个父实体（如电视剧季、王朝、联赛、行政区划、选举），要求输出完整成员及若干属性列，形成表格。评估采用Item-F1（集合成员召回）、Column-F1（列完整性）和Row-F1（整行正确性）。基准包含228张表、190个实体、16个类别，三个难度等级由两个独立旋钮控制：表格宽度（列数）和2D复合键（要求两个维度交叉验证，使跨页属性占比从0%到100%）。黄金构建与评测共享同一规范化感知比较器，避免因格式差异误删日期或计数列。

**结果**：在20个Web Agent上测试，一致性表现：Agent能恢复成员集合（Item-F1 92.8），但难以补全行信息（Row-F1 53.7），准确率随旋钮硬化而下降，更多搜索步数或算力投入无法弥补差距。逐单元格分析显示，核心难点是找到正确值而非格式化输出：自由文本单元格失败最多，而标准答案（日期、名称等）通常正确。
