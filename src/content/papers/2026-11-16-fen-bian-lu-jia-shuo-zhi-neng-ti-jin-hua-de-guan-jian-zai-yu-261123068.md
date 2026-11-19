---
title: 'The Resolution Hypothesis: Agent Evolution''s Key Is Identifying Improvements'
title_zh: 分辨率假说：智能体进化的关键在于识别改进
authors:
- Yuanhao Zeng
- Shaocheng Lan
- Ao Lu
- Kuang Yan
- Heng Lin
- Xinang Xu
- Yuan Luo
- Yueting Wang
- Yexin Li
- Ruo Shan
affiliations:
- ShanghaiTech University
- ByteDance
- BIGAI
- SUSTech
arxiv_id: '2611.23068'
url: https://arxiv.org/abs/2611.23068
pdf_url: https://arxiv.org/pdf/2611.23068
published: '2026-11-16'
collected: '2026-11-19'
category: Eval
direction: Agent 进化评估噪声与分辨率分析
tags:
- Agent Evolution
- Evaluation Noise
- Selection
- LLM Agents
- Reproducibility
- Variance Decomposition
one_liner: 大规模实证表明 Agent 进化瓶颈不在提议改进，而在评估分辨率不足导致选择接近随机、改进无法累积
practical_value: '- 复用方差分解框架：在评估 Agent 工作流（如 RAG、工具调用）时，同时估计评估噪声 σ 和 run-to-run 方差
  τ；方法对比需多次运行，单次结果不可靠；报告 σ 和 τ，判断指标差异是否超过分辨率。

  - 候选选择需加预算：在进化/优化 prompt 或技能库时，别用单次执行得分做 accept/reject，否则选择准确率接近 50%，劣质候选被接受；可增加
  rollout 次数或引入低噪声中间过程信号（如验证是否运行测试、特定行为检查）降低噪声。

  - 分离 Proposer 与 Selector 评估：用 Quality@K 评估提案质量，用固定候选池评估选择器，避免端到端得分掩盖瓶颈；在推荐场景可用固定候选池离线评估排序/选择策略，减少线上噪声干扰。

  - 警惕“一条规则提升显著”：大增益可能是评估捷径（适配特定评分格式/作弊），需要修复评估后复现；在业务中，若某个 prompt/技能带来异常提升，先审查是否利用了评测套路的漏洞。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Agent 进化方法在不同论文/基准上表现冲突，常在 Terminal-Bench 等编码基准上停步；方法排名不稳定，评估可靠性存疑。提出分辨率假说：瓶颈不在提出更好 artifact，而在评估噪声高、无法可靠识别改进。

**方法关键点**：大规模实验，7 种进化方法（文本类：GEPA, SkillOpt-Lite, Trace2Skill, ReasoningBank；harness 类：HarnessLens, Meta-Harness, AHE），6 个模型（GPT-5.4 nano, GPT-5.6 Luna/Terra, DeepSeek-V4-Flash, Kimi-K3, GLM-5.2），4 个 benchmark（ALFWorld, SpreadsheetBench, OfficeQA, Terminal-Bench），超过 10M LLM calls；方差分解：σ（评估噪声）与 τ（run-to-run 方差）；方法层分析单次运行能否排行；候选层构建 Proposal Pool 和 Selection Pool，测试三个预测 P1/P2/P3；gain audit 审查历史大增益。

**关键结果**：单个报告无法排名，方法间中位差距 3.4pp，单次运行选最佳方法最高仅 33%（Terminal-Bench）；候选池中存在真实改进（Quality@K 随 K 升至 61.8%），但所有选择器（执行分数、LLM judge）pairwise accuracy ≈50%，rank correlation 0.054；选择错误累积，in-loop gain 6.9-9.0pp 而重评估后 +0.4~-3.2pp，run-to-run 方差增长至 4.2-24.5 pp²；最大历史增益 90% 可由一句话复现，修复评估后中位增益从 17.6pp 跌至 0.8pp。

**值得记住的一句话**：真正的进步需要让改进可被检测和累积，而不是只追求更复杂的提议器。
