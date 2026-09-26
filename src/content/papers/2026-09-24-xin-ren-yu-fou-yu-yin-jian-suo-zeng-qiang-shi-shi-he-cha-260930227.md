---
title: 'To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech'
title_zh: 信任与否：语音检索增强事实核查
authors:
- Debajyoti Mazumder
- Mamta
- Abhirama Subramanyam Penamakuri
affiliations:
- IISER Bhopal
- King's College London
- MBZUAI
arxiv_id: '2609.30227'
url: https://arxiv.org/abs/2609.30227
pdf_url: https://arxiv.org/pdf/2609.30227
published: '2026-09-24'
collected: '2026-09-26'
category: RAG
direction: 语音事实核查 · RAG+CoT
tags:
- Speech
- RAG
- Fact Checking
- LALM
- CoT
- Benchmark
one_liner: 提出语音事实核查基准 VeriSpeak，揭示文本-语音模态差距，并验证检索+显式推理准确率达86.1%
practical_value: '- 直播/短视频事实审核：在电商直播、短视频带货中，虚假宣传检测可用「语音输入 + 文本检索证据 + 显式推理」管道；仅拼接检索片段容易被模型混淆，应加
  CoT 要求先区分“声明”和“证据”再判断。

  - 模态差距评估：如果现有文本事实核查/内容安全模型被用于语音转写后的文本，要意识到可能存在系统性能下降；上线前需在真实语音或 TTS 基准上评估，或直接用 LALM
  处理音频。

  - RAG 防混淆设计：召回证据后，可在 prompt 中用角色/字段显式隔离 claim 与 evidence，并要求模型输出“一致/矛盾/无关”的结构化判断，这比直接给混合上下文更稳。

  - 业务基准构建：可参考 VeriSpeak 的 probe 设计，构建电商领域 spoken claims 小样本（如功效、产地、价格承诺），快速对比不同 RAG+推理组合。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：错误信息大量以语音形式传播（新闻、播客、访谈、短视频），但现有事实核查主要针对文本，LALM 能否直接把文本事实核查能力迁移到语音、检索增强是否有效，缺少系统基准。

方法：VeriSpeak 包含 3,879 条语音声明，覆盖时间、地理、关系事实，真假标签平衡。设置 6 条管线：纯文本、语音、语音+CoT、语音+文本 RAG、语音+文本 RAG+CoT，评估 LALM 的表现。

关键结果：存在一致的文本-语音模态差距，模型能可靠核实书面声明，却常在同一内容的语音版本上失败。单独加入检索收益有限，因为模型会把检索证据与语音声明混淆。检索叠加显式推理后，thinking-tuned LALM 准确率达到 86.1%，说明语音事实核查需要语音理解和对检索证据的 grounded reasoning。
