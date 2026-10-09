---
title: 'SkillContrast: Difference-Guided Text Selection for Agent Skill Reranking'
title_zh: SkillContrast：差异引导的 Agent 技能重排文本选择
authors:
- Jiandong Ding
- Honglei Ji
- Ming Liu
- Tao Duan
affiliations:
- Huawei Technologies Co., Ltd.
- Department of Obstetrics, Shanghai East Hospital, Tongji University School of Medicine
arxiv_id: '2610.11650'
url: https://arxiv.org/abs/2610.11650
pdf_url: https://arxiv.org/pdf/2610.11650
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: Agent 技能检索重排 · 差异文本选择
tags:
- Agent Skill Retrieval
- Reranking
- Text Selection
- Candidate Differences
- Training-free
- LLM
one_liner: 训练无关的文本选择器，保留候选技能间差异与局部上下文，压缩重排输入并提升干净命中
practical_value: '- 在 LLM/Agent 重排环节需要压缩候选输入时，不要只按 query 相关性抽句；可对候选集合做差异对比，保留版本、适用条件、资源限制等只有部分候选具备的区分信息，帮助
  reranker 区分相似技能/商品。

  - 该方法训练无关，可作为 reranker 前置的文本选择模块，适合业务快速接入；生产环境可用字符/段落 diff 或属性对比生成差异片段，控制单候选 token
  预算。

  - 对电商/广告中相似商品、素材或 skill 的重排，可尝试对候选标题、属性、卖点做“差异化选择”，突出规格、适用人群、价格条件等关键差异，提升 LLM 排序准确率并降低调用成本。

  - 注意模型规模影响：较小 reranker（0.6B）可能因信息损失而弱于全量输入，较大模型（4B）可保持甚至提升；建议在目标模型上验证 token 节省与效果平衡。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Agent 系统检索可复用技能库时，相似技能常共享指令但在使用条件（版本、资源、输入格式）上不同。基于 query 选择文本易保留共性、漏掉关键差异，导致 reranker 无法区分。

**方法关键点**：SkillContrast 是一个训练无关选择器，先比较召回的候选技能文本，提取候选间差异文本并附带局部上下文，组成紧凑输入交给预训练 reranker；无需微调，通过候选相对差异增强条件区分信息。

**关键结果**：在 SameCapRisk-Bench 1,235 个请求上，同等每候选输入长度下，比 TF-IDF query 选择多出 54–72 个 clean hits，跨 2 个 retriever 和 2 个 reranker 尺度；长度匹配替换验证差异文本是主要贡献。相对完整 skill bodies，输入 token 减少 51.1–58.8%，4B 模型 clean hits 持平或更高，0.6B 少 10–18。
