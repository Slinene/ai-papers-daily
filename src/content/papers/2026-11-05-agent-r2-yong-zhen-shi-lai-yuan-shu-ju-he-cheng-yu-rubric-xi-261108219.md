---
title: 'Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source
  Data Synthesis'
title_zh: Agent-R2：用真实来源数据合成与 rubric 强化学习训练生产力智能体
authors:
- Teng Pan
- Zixuan Wang
- Yuchen Yan
- Qifei Wu
- Yao Chen
- Yingqi Qu
- Ruiqing Zhang
- Yongliang Shen
affiliations:
- Zhejiang University
- Baidu Inc.
arxiv_id: '2611.08219'
url: https://arxiv.org/abs/2611.08219
pdf_url: https://arxiv.org/pdf/2611.08219
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 训练 · 真实数据合成与 rubric RL
tags:
- Agent Training
- Real-Source Data Synthesis
- Rubric RL
- SFT
- Productivity Work
- Shortcut Mitigation
one_liner: 以真实职业流程、真实网页文件和细粒度 rubric 合成 4k 任务，4B 模型在 GDPval 超过 235B 基线
practical_value: '- 真实文件 > 假文件：电商 agent 场景（店铺诊断、广告复盘、选品分析）应直接用卖家报表、广告后台导出、商品表格等真实附件合成训练/评测任务；真实文件的脏格式、跨表引用、多
  sheet 会倒逼 agent 多轮 inspect，远比 LLM 生成假数据有效。

  - rubric 结果奖励 + 无过程惩罚：对交付物（分析报告、投放方案、选品表）建立细粒度 rubric，RL 只给最终交付物打分，不惩罚中间 tool call
  error；这能提升错误恢复和完成率，同时避免学出特定工具调用偏好。可用 MLLM judge 把 pdf/pptx/docx 渲染成图、xlsx 同时给公式+渲染图再评分。

  - 监控 shortcut 指标：在生产 agent 上跟踪 effective steps、交付物重查率、写文件前仍有未修 error 的比例、placeholder
  文本、traceable numbers；这些指标比只看成功率更早暴露“表面完成、实则跳过证据”的问题。

  - 小模型 + 少量高质量真实数据可行：4k 条任务就让 4B 超过 235B。业务里可先花成本构建小规模高保真数据，不必盲目堆量；SFT 负责塑造持续探索行为，RL
  负责提升可靠高质量交付。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前 LLM agent 在真实生产力工作（长链路专业流程、异构文件、交付物级要求）上仍弱。瓶颈不是缺数据，而是缺真实意图、真实文件、交付物级标准的数据；现有训练数据要么只做指令/推理/单类文件生成，要么用 LLM 生成假文件。

### 方法关键点
- 三阶段真实来源数据合成：从 web corpus + O*NET 职业种子提取文件导向 workflow；再通过多轮 search/download/inspect 检索真实 PDF/docx/xlsx/pptx 附件；最后在 sandbox 中合成指令 + 细粒度 rubric，并用专家策略产出参考文件和轨迹。
- 从 10k 候选得到 4k 实例，平均 2.51 个附件、15.3 个 rubric 项、专家轨迹 18.0 步/41.8k tokens。
- 训练 Qwen3-4B-Thinking：3k SFT + 1k rubric-based GRPO。RL 只给 outcome reward，由 MLLM-as-judge 对交付物按 rubric 打分，不加中间 tool-call 惩罚。

### 关键实验
GDPval：Agent-R2-4B Pass@1 51.0%，超过 Qwen3-235B-A22B-Thinking-2507 的 48.0%、DeepSeek-v3.1 的 48.8%、GPT-4.1 的 39.4%；base 只有 32.4%。OfficeQA：14.8% 超过 235B 的 13.8%。Ablation：真实文件 SFT 43.3 vs 合成文件 41.4；rubric reward 51.0 vs 无 rubric 49.5。行为分析：写交付物前仍有未修错误比例从 55% 降到 11%，重查交付物从 0.5% 升到 95.8%，有效步数与 Pass@1 正相关。

### 最值得记住的一句话
真实来源数据 + rubric 结果奖励，比堆过程监督或假文件更能训练出会持续探索、少走 shortcut 的 agent。
