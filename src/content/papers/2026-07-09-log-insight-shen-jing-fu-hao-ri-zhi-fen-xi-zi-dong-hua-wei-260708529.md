---
title: 'Log-Insight: Automating Microservice Incident Diagnosis via Neuro-Symbolic
  Log Analysis'
title_zh: Log-Insight：神经符号日志分析自动化微服务故障诊断
authors:
- Carlos Garcia-Hernandez
- Aymane Abdali
- Guangyu Wu
- Mingxue Wang
- Fei Shen
- Zhaoyu Pang
- Yanbin Zhang
affiliations:
- Huawei Ireland Research Centre
- Huawei Dongguan R&D Centre
arxiv_id: '2607.08529'
url: https://arxiv.org/abs/2607.08529
pdf_url: https://arxiv.org/pdf/2607.08529
published: '2026-07-09'
collected: '2026-07-11'
category: LLM
direction: 神经符号日志分析 · 根因推理压缩
tags:
- Log Analysis
- Root Cause Analysis
- LLM
- Symbolic Compression
- Incident Diagnosis
- Microservices
one_liner: 通过符号化压缩将百万行日志精简为紧凑证据，再由LLM生成根因报告，MRR=0.790且90%+的Top-3命中率。
practical_value: '- **海量事件压缩再投喂 LLM 的流水线模式**：在推荐系统日志、A/B 实验分析或广告系统异常监控中，当原始事件量远超 LLM
  上下文窗口时，可借鉴「两阶段采样 → 模式聚类 → 熵引导压缩 → 对比倾斜分析」的符号化预处理，把百万级记录压缩到 LLM 可处理的规模，且保留统计显著的异常信号，避免直接灌入原始数据的幻觉和溢出问题。

  - **结构化异常排序 + LLM 假设生成**：对于需要从大量日志中定位根因的场景（如推荐链路延迟抖动、召回异常），可模仿 Log-Insight 先由符号模块做异常排名，再交给
  LLM 合成诊断报告，兼顾统计可靠性和语言推理的灵活性。

  - **可解释性增强的“法证证据”展示**：在内部诊断工具中，不仅输出最终结论，也呈现精确的日志模板、偏差统计等中间证据，能将系统从“黑箱神谕”转变为“调查助理”，降低
  SRE/算法工程师的采纳阻力，这在自动化模型监控和报警解释中可以复用。

  - **处理高维时序异常的对比倾斜分析**：论文中的对比倾斜分析（对比正常/异常时段日志模板分布）可直接应用于推荐系统的实时指标异常检测，如对比实验版本间的请求模式差异，快速定位引发指标波动的具体操作。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：大规模微服务发生故障时，30 分钟窗口即可产生超 200 万行日志（约 12 亿字符），远超 LLM 的上下文限制，直接使用 LLM 进行根因分析（RCA）不可行。现有模板解析器缺乏语义推理，深度学习检测器给出黑箱信号，LLM 管道则面临上下文溢出和幻觉。

**方法**：提出 Log-Insight 生产系统，核心是将 SRE 的人工排障流程自动化。六阶段流水线依次为：①两面采样（选取故障前后的小部分日志）；②模式推断与记忆（学习日志模式）；③Drain3 模式聚类；④两层熵引导压缩（保留统计异常的模板）；⑤对比倾斜分析（对比正常与异常时段的模板分布，计算偏差分数）；⑥生成合成：将紧凑的预排序证据档案（仅数百条日志）交给 LLM，生成根因假设排名报告。整个流程原始日志压缩比达 1,000–7,000 倍，同时保留显著故障信号。

**结果**：在华为 11 个历史生产事件上（110 次运行，SRE 验证的真值）评估，MRR 达到 0.790，超过 90% 的运行时正确根因出现在 Top-3 假设中，端到端延迟不到一分钟。额外的“法证证据”部分（提供具体日志模板及偏差统计）被运维人员视为关键采纳因素，显著提升了系统可解释性与信任度。
