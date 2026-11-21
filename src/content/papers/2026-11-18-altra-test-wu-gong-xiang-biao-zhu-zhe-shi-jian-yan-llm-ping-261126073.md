---
title: 'AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators'
title_zh: AltRA-Test：无共享标注者时检验 LLM 评判者替代人类的统计方法
authors:
- Nagham Omar
- Rotem Dror
- Almog Gueta
- Avigdor Gal
- Roi Reichart
- Nitay Calderon
affiliations:
- Technion
- University of Haifa
- Google Research
arxiv_id: '2611.26073'
url: https://arxiv.org/abs/2611.26073
pdf_url: https://arxiv.org/pdf/2611.26073
published: '2026-11-18'
collected: '2026-11-21'
category: Eval
direction: LLM-as-judge 标注可靠性统计检验
tags:
- LLM-as-judge
- inter-annotator agreement
- statistical testing
- bootstrap
- annotation reliability
one_liner: 提出基于 bootstrap 重采样与 IAA 非劣效检验的 AltRA-Test，无需共享标注者即可判断 LLM 是否可替代人工标注
practical_value: '- 在电商/搜索推荐中要引入 LLM 做 relevance 标注、内容质量打分或商品类目标注前，可先用小样本（约 100 items）跑
  AltRA-Test，按任务验证 LLM 是否保有人类标注共识，避免盲目替换人工。

  - 该方法不要求所有 item 由同一批标注者标注，适配大规模众包/内部多人标注场景（不同标注者只标注部分 item），可直接复用其 bootstrap 重采样
  + 非劣效 IAA 检验的框架。

  - 测试可区分任务类型：论文显示 LLM 只在约半数 setup 通过，说明不同任务差异大；建议在业务中按具体任务（如搜索意图分类、商品描述质量）分别检验，而不是全局默认
  LLM 可替代。

  - 工程实现上，可把 AltRA-Test 做成标注流水线中的质量闸门：对每个标注任务采样人类标注和 LLM 标注，计算配对 IAA，若 mixed panel
  非劣于 all-human panel 才允许 LLM 放量替代。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
LLM 作为评判者/标注者越来越多地替代人类，但何时替换在统计上合理？此前的 Alternative Annotator Test (Alt-Test) 要求所有 item 都由同一批标注者标注（dense setting），然而大规模标注中 item 常被不同子集标注者标注，无法直接使用。

## 方法关键点
提出 AltRA-Test：用 bootstrap 重采样 items，每个 item 抽取 k 个人类标注，并将其中的一个替换为 LLM 标注，得到配对的 all-human panel 和 mixed human-LLM panel。若 mixed panel 的 inter-annotator agreement (IAA) 统计上非劣于 all-human panel，即 LLM 保留了人类标注者之间的信号，则支持替换。方法不要求共享标注者，并证明是一致性检验，渐近水平为 α。

## 关键结果
在模拟中（已知 LLM 是否优于/劣于人类标注者），AltRA-Test 比现有基线做出更多正确的替换决策。在真实数据实验中，测试了 18 个 LLM、5 种 prompting 技术、20 个跨文本/图像/音频/视频的数据集；约 100 个 item 通常足够；LLM 在约半数 setup 中通过测试，表明是否可替换主要取决于任务。

**核心结论**：LLM 替代人工标注并非始终合理，应针对具体任务进行统计检验，而不是默认替代。
