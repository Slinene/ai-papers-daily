---
title: Useful Diversity or Hallucinated Variety? Persona-Conditioned Synthetic Query
  Generation for E-Commerce Search
title_zh: 人物画像条件化电商搜索合成查询：有用多样性与幻觉式多样性
authors:
- Filippos Ventirozos
- Tom Armitage
- Mahmoud Oshagh
- Peter A. Appleby
- Matthew Shardlow
affiliations:
- Manchester Metropolitan University
- Autotrader UK
arxiv_id: '2610.35102'
url: https://arxiv.org/abs/2610.35102
pdf_url: https://arxiv.org/pdf/2610.35102
published: '2026-10-26'
collected: '2026-10-27'
category: QueryRec
direction: 合成查询生成 · 语义解析
tags:
- persona prompting
- synthetic query generation
- semantic parsing
- e-commerce search
- LLM hallucination
- alignment
one_liner: 用4轴persona prompt生成11.8万合成查询，Big Five人格稳定提parser F1且低幻觉，句法轴贴真实流量但牺牲约束保真
practical_value: '- 冷启动 NL 搜索解析器时，把 Big Five 人格线索加入生成 prompt（如 conscientiousness 明确标记约束、neuroticism
  添加犹豫）作为默认，可稳定提升下游 tuple F1；不要用 prompt 删 function word / stopword，因为电商约束字段的 operator
  词（under/within/from）承担语义，删掉会导致 dropped constraints。可加后处理校验 operator 是否保留。

  - 评估合成训练数据质量时，不要只看 Distinct-n / Self-BLEU，它们与下游效用无关；用 embedding 云拟合 vMF 分布并计算与 held-out
  人工参考的 sKL，可无标签代理 parser F1（ρ=-0.917）。生产环境若无标注，可用真实 query 流量分布做 realism 监控。

  - 对“所有模型都解析失败”的困难样本做 LLM 委员会审计，能分类幻觉类型（dropped constraint / unsupported addition
  / direction reversal）。工程上可写自动规则检查价格/里程/半径等 operator 和方向，上线前过滤或修复。

  - 多 generator 风格差异很大，某些 LLM 会把 persona 中的城市/价格偏好泄漏进 query；要按 generator 审计。混合多个 prompt
  家族均匀采样训练的 mixed corpus 与最佳单 prompt 统计无差，可直接采用降低选型成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：
电商搜索正从 faceted filters 转向自然语言界面，需要语义解析器把 query 映射到结构化 schema，但标注数据稀缺。合成查询生成可规模化，但 prompt 诱导的多样性只有在忠实于 structured intent 时才有用；多样性与 schema 保真互相拉扯。本文用 persona 作为受控变异机制，在 UK 汽车搜索的 47 字段 schema 下检验哪种条件化带来“有用多样性”。

方法关键点：
- 构造 4 个 prompt 轴：IPIP Big Five 人格（p）、UK 人口统计描述（u）、句法模式（s，基于 Yahoo web query 语法：名词短语/电报式/疑问/祈使等）、属性风格形容词（a）；组合成 9 个 family（n, p, a, s, u, pa, ps, as, pas），由 6 个 reasoning LLM 生成 118,098 条合成 pair，每配置同 intent 匹配。
- 每个配置 fine-tune Flan-T5-Large 解析器，以 tuple-level F1（field+value 完全匹配）在 1,214 条人工标注（1,058 persona-card + 156 website-front）上评估。
- 用 von Mises–Fisher 分布拟合 embedding 云，计算 synthetic 与参考分布的 symmetric KL（sKL）作为对齐 proxy；参考包括人工标注和 15,304 条真实生产 query。
- 对 927 条“所有 parser 均失败”的 hard cases，用三 LLM 委员会 + 作者盲审审计幻觉类型。

关键结果数字：
- 每个 conditioned parser 都超过 vanilla baseline（n F1=75.98）；pas 最高 79.62，pa 79.40，mixed 79.36，三者统计不可区分。
- IPIP 主效应 +1.73 F1，形容词 +1.34，语法 +0.76；IPIP 在四个 matched contrasts 均显著为正（+1.1 到 +2.1，Holm p<.001）。
- 对齐 sKL 与 parser F1 在 persona-card 参考上 ρ=-0.917（可作为无标签 proxy），但与真实流量仅 ρ=-0.350。
- 句法轴让生成显著贴向真实流量（sKL 降 60.7-116.1）并推高多样性，却在 hard cases 中幻觉占比最高（38-42%）；IPIP 最低 28%。927 条中 37.2% 被标为幻觉，dropped constraints 占 57.3%，常因删除 operator 词。

最值得记住的一句话：人格提示靠改写词汇提供低幻觉的有用多样性，句法提示靠删虚词贴近真实流量但代价是丢失承载字段关系的 operator 词。
