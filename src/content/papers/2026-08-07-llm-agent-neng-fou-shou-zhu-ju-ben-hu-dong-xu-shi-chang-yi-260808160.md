---
title: Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency
  in Interactive Narratives
title_zh: LLM Agent 能否守住剧本：互动叙事长程一致性基准
authors:
- Yingpeng Ma
- Jianhao Yan
- Bei Shi
- Ka Hou Kam
- Runnan Wang
- Xuebo Liu
- Yulong Chen
- Yue Zhang
- Derek F. Wong
affiliations:
- University of Macau
- Westlake University
- Harbin Institute of Technology, Shenzhen
- University of Cambridge
- University of Aberdeen
arxiv_id: '2608.08160'
url: https://arxiv.org/abs/2608.08160
pdf_url: https://arxiv.org/pdf/2608.08160
published: '2026-08-07'
collected: '2026-08-13'
category: Eval
direction: LLM Agent 长程一致性评测
tags:
- LLM Agents
- Interactive Narrative
- Benchmark
- Long-Horizon Consistency
- Evaluation
one_liner: 提出 NCP 任务与 NCP-Bench 基准，系统评测 LLM 在对抗性互动下维持长期叙事承诺的能力，暴露严重一致性缺陷
practical_value: '- 对话式推荐/导购 Agent 的多轮交互中，可显式维护“用户约束/已承诺事实”的结构化 memory，每轮生成后自动做 conflict
  check，避免推翻之前承诺（如预算、偏好、已推荐商品属性）。

  - 借鉴其 benchmark 设计：把长会话目标拆成 trajectory + commitments + initial facts，用可自动校验的规格替代纯人工评分，可低成本构造电商导购场景的
  consistency 回归测试集。

  - 对抗性用户干预（如否定已确认信息、突然改需求）是真实线上常态；上线前应对 Agent 做 adversarial turn 压力测试，评测“生存率”而非只看单轮回复质量。

  - 论文显示语言质量高不等于逻辑一致，模型规模/通用能力不直接解决长程状态追踪；工程上建议引入外部状态机或检查器，而非只依赖模型隐式记忆。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 正在推动开放互动叙事，但现有研究忽略长时间跨度下，面对无约束用户干预时的逻辑一致性与叙事完整性。  
**方法**：将该问题形式化为 Narrative Commitment Preservation (NCP)，构建 NCP-Bench：100 个由电影梗概派生的叙事环境，每个环境提供结构化叙事规格（trajectory、commitments、initial facts），在 player agent 与 narrator agent 交互全程自动检查。  
**结果**：SOTA LLM 普遍存在长程一致性缺口：GPT-5.2 在 20 轮后 survival rate 仅 42%，各模型 fact conflict rate 介于 40%–68%；100 轮内满足全部 achievement commitments 的运行仅个别出现。高语言质量不能保证承诺保持。
