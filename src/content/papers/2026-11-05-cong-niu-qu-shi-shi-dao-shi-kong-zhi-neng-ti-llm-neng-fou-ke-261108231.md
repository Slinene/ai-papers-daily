---
title: 'From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional
  Hallucinations?'
title_zh: 从扭曲事实到失控智能体：LLM 能否可靠检测多维幻觉？
authors:
- Hanyu Qiu
- Ze Liu
- Zhe Zhao
- Kuang Xiong
- Blaze Chen
- Zhenxiang Yan
- Renfen Hu
affiliations:
- Beijing Normal University
- Tencent AI Lab
arxiv_id: '2611.08231'
url: https://arxiv.org/abs/2611.08231
pdf_url: https://arxiv.org/pdf/2611.08231
published: '2026-11-05'
collected: '2026-11-08'
category: Eval
direction: LLM 幻觉检测与 agent 轨迹可靠性评估
tags:
- hallucination detection
- agent trajectories
- benchmark
- factual faithfulness
- localization
- correction
one_liner: 构建 HaluCheck 双语 42k 幻觉检测基准，覆盖文本事实性与 agent 轨迹忠实度，发现细粒度定位修正与 agent 检测明显不足
practical_value: '- 评估生成式推荐/导购 Agent 时，不要只看最终答案是否含幻觉；把“轨迹忠实度”纳入评测，检查工具调用、中间推理与外部知识是否一致，可参考
  HaluCheck 的 agent trajectory 标注方式做内部回归集。

  - 线上若用 LLM 做自动事实校验或纠错，需区分 sample-level detection 与 token/span-level localization、correction
  三个指标；当前模型能粗略判断“有没有错”，但定位和修正能力弱，应设置更细的阈值与人工兜底。

  - 可将 HaluCheck 的多级扰动数据用于 SFT 轻量检测器或 reward model，但论文结果表明 thinking、web search、SFT
  都只是部分缓解；生产环境仍建议外部知识库/工具校验与抽样人工审核组合。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 已广泛用于信息获取、内容生成和 Agent 任务执行，但其输出仍可能包含高风险的细微幻觉；这类错误在 Agent 中会进一步传导为错误动作，因此需要更系统的后生成幻觉检测评估。

方法关键点：HaluCheck 是双语、超 42k 实例的基准，覆盖文本事实性幻觉与 agent 轨迹忠实度幻觉；提供检测、定位、修正三个层次的细粒度标注，并设置不同任务类型和扰动程度。研究在 14 个 LLM 上评测样本级判断、细粒度定位/修正及 agent 幻觉检测能力。

关键结果：模型在样本级检测上具备基础能力，但在细粒度定位、修正和 agent 幻觉检测上表现明显不足；引入 thinking、web search 和 SFT 后各有部分提升，但都无法完全解决幻觉检测问题。HaluCheck 可作为跨文本与 agent 场景的可靠性诊断基准。
