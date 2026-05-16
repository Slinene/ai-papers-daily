---
title: 'A Deterministic Agentic Workflow for HS Tariff Classification: Multi-Dimensional
  Rule Reasoning with Interpretable Decisions'
title_zh: 基于确定性Agentic Workflow的HS关税分类：多维规则推理与可解释决策
authors:
- Yu Zhang
- Dongjiang Zhuang
- Qu Zhou
- Zheng Huang
- Junhe Wu
- Jing Cao
- Kai Chen
affiliations:
- 上海交通大学
- 中国海关总署
- 南京极云信息技术有限公司
arxiv_id: '2605.14857'
url: https://arxiv.org/abs/2605.14857
pdf_url: https://arxiv.org/pdf/2605.14857
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- Agentic Workflow
- HS Tariff Classification
- Rule Reasoning
- RAG
- Interpretability
- Benchmark Audit
one_liner: 通过固定控制流的多阶段LLM流水线实现HS分类的多维规则推理，输出可审计决策且开源模型性能接近前沿模型
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
HS 关税分类是高风险的专家任务，需同时满足材料、形态、功能、基本特征、件与整机边界、具体条目优先等多个维度的竞争性规则。端到端 LLM 提示常因忽略某些轴的优先级约束而失败，且缺乏可解释性。该工作旨在通过固定流程的确定性 agentic workflow 系统性地解决多维规则推理，并给出带引用的可审计决策。

**方法关键点**  
- 离线知识工程：将中国 HS 税则分解为类型化的章节注释（包含条款、排除条款、优先条款）、层次化索引、GIR 规则及双路检索索引（BM25 + 密集向量），用 Reciprocal Rank Fusion 融合；  
- 在线六阶段流水线：① 属性提取（材料、形态、功能等）；② 候选检索（约 40 个四位税目）；③ L1 短名单（仅凭税目文本打分，缩减至约 10 个）；④ L2 排序并确认（加载相关章节/类注释，识别排除条款，应用 GIR 3 等，产生前三候选）；⑤ 子目解析（六位码）；⑥ 最终评分与逐字规则引用（包含支持点、反对点、适用 GIR 条文及注释原文）；  
- 确定性控制流：阶段固定，LLM 仅用于窄任务，反思与验证作为阶段内局部机制，不进行全局规划，从而保证可解释性、低方差和易调试。

**关键结果**  
- 在 HSCodeComp（632 条）上，Qwen3.6-plus 骨干下四位数 top‑1 75.0%，top‑3 91.5%；六位数 top‑1 64.2%，top‑3 78.3%；  
- 开源 Qwen3.6‑27B‑FP8（无思考模式）在相同流水线中四位数 top‑1 与前沿模型一致性 84.2%，六位数 77.4%，表明流水线不依赖单一顶级模型；  
- 对 226 个六位数分歧的人工审计发现，42.5% 的系统预测比基准标签更符合 HS 规则，15.0% 系统错误，36.7% 属专业分类边界争议，5.8% 为数据质量问题；保守修正后六位数 top‑1 估计达 85.8%。
