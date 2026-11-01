---
title: Radiology Guideline-derived Decision Graph for Efficient Clinical Decision
  Support
title_zh: 放射学指南衍生决策图提升临床决策支持效率
authors:
- Xuewen Zhou
- Zhen Chen
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2610.40327'
url: https://arxiv.org/abs/2610.40327
pdf_url: https://arxiv.org/pdf/2610.40327
published: '2026-10-29'
collected: '2026-11-01'
category: Reasoning
direction: LLM 决策图推理
tags:
- Decision Graph
- LLM
- System One
- Reasoning
- Clinical Decision Support
one_liner: LLM 构建可执行决策图，System One 模型 + 确定性遍历将准确率从 57.3% 提升至 90.8%
practical_value: '- 电商营销/风控/售后 SOP 等规则密集场景可借鉴决策图架构：LLM 离线从政策文档/规则手册构建决策图，线上用轻量模型回答局部问题
  + 图引擎做布尔分支，避免每次请求都调用大模型完整推理。

  - 把“理解规则”和“执行规则”解耦：LLM 负责把非结构化输入转成结构化判断，确定性遍历保证一致性和可解释性，降低规则偏离风险。

  - 用 System One / 快速模型做子问题判断，可显著降低延迟与成本，适合高 QPS 推荐/Agent 场景中需要规则判定的环节。

  - 决策图天然生成可追溯的决策路径，便于审计、bad case 归因和 A/B 测试；在广告审核、商品合规等强解释流程中可直接复用。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：临床指南的风险分层和管理规划标准分散在散文、表格和交叉引用定义中，自动化执行困难。

**方法关键点**：框架将指南编译与案例评估解耦。编译阶段，LLM 将指南切分为章节级块，提取局部决策子图并链接定义，聚合为可执行决策图。推理阶段，快速的 System One 模型只回答局部临床问题，确定性图遍历处理布尔逻辑，形成可追溯的决策路径，无需任务特定训练。

**关键结果**：在 347 个案例（肾囊肿、附件包块、甲状腺结节指南）上，GDGraph 将 System One 准确率从 57.3% 提升至 90.8%，超过检索增强 GPT-4o（80.1%）和图引导 CoT GPT-4o（82.7%），且延迟与成本更低。
