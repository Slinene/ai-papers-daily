---
title: 'OpenBioRQ: Unsolved Biomedical Research Questions for Agents'
title_zh: OpenBioRQ：面向智能体的未解决生物医学研究问题基准
authors:
- Minbyul Jeong
affiliations:
- Upstage AI
arxiv_id: '2606.21959'
url: https://arxiv.org/abs/2606.21959
pdf_url: https://arxiv.org/pdf/2606.21959
published: '2026-06-19'
collected: '2026-06-26'
category: Eval
direction: 智能体工具调用评估 · 忠实性探针
tags:
- Agent
- Benchmark
- Faithfulness
- Tool Use
- Biomedical QA
- Open Questions
one_liner: 首个未解决问题与工具调用结合的生物医学Agent基准，揭示~16%引用错误及高难点上的工具弃用崩溃
practical_value: '- 在电商客服/推荐解释Agent中，采用无标准答案的查询评测工具调用忠实性，防止模型记忆答案而跳过检索

  - 用经验性困难度锚定（参考模型集体失败的问题）构建高难度测试集，有效暴露工具弃用现象

  - 引入冻结的试题检查清单（checklist）大幅提升评估一致性（Spearman从0.35→0.82），可迁移至内部评测流程

  - 在最难问题上强制保留工具调用或设置工具使用下限，避免Agent过早放弃工具，保障回答可靠性'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有问答基准存在答案键，模型可能凭记忆复现参考文献而未真正验证，无法检测引用错误（约15.9%引用链向错误论文）。需构建无答案键的开放问题基准作为忠实性探针。

**方法**：构建OpenBioRQ，包含12,553个未解决的生物医学研究问题，覆盖12个领域。设定为检索增强型Agent任务，模型须多次工具调用并基于证据回答或弃权。开放性由真实后续研究验证，而非依赖模型参数知识。困难度锚定于三个开源参考模型无法解答的问题子集。

**关键结果**：在最难子集上，与锚定模型同源的模型仅解决~17%；三个前沿Agent（Gemini-3-Pro, Opus-4.7, GPT-5.5）解决率在29–60%范围内，基准难度高且未饱和。观察到**Agent崩溃**：在困难问题上模型停止调用工具，对最易崩溃的模型完全禁用工具几乎不影响分数——工具在急需处失效。通过冻结试题检查清单，评分者一致性从Spearman 0.35提升至0.82。
