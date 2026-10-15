---
title: 'SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment
  for Conversational Recommender Systems'
title_zh: SimInter：基于访谈画像增强的循证对话推荐用户模拟
authors:
- Erfan Shahabi
- Amirhossein Roshandel
- Mohammad Sadegh Sadeghi
- Azadeh Shakery
affiliations:
- University of Tehran
- Institute for Research in Fundamental Sciences (IPM)
arxiv_id: '2610.18308'
url: https://arxiv.org/abs/2610.18308
pdf_url: https://arxiv.org/pdf/2610.18308
published: '2026-10-13'
collected: '2026-10-15'
category: Eval
direction: 用户模拟 · 对话推荐评估
tags:
- User Simulation
- Conversational Recommender Systems
- LLM Agents
- Profile Enrichment
- Evaluation
one_liner: 用LLM访谈+轮级审计从历史对话中提取隐式用户画像，显著提升模拟用户的aspect表达丰富度
practical_value: '- 在电商/对话推荐离线评估中，可用「历史行为统计 + LLM 访谈」抽取用户隐式偏好（pickiness、decision-making
  style、novelty preference），每个属性要求 evidence quote，避免 LLM 直接从静态画像推断时的刻板印象。

  - Turn-level 审计是工程可落地的做法：定义 fabrication / caricature / history contradiction 三类
  flag，并设 severity，不整段丢弃对话而是剔除有问题的 turn。对 RAG 对话、生成式推荐的事实性校验可参考这种细粒度过滤。

  - 注意 trade-off：丰富画像提高了 aspect 多样性和语义多样性，但会降低 item 多样性和词汇重复。业务评估中不要追求所有多样性指标同时提升，应明确评估维度。

  - 用不同 LLM 做生成/审计/评测（如 Gemini 生成访谈、Claude 审计、GPT-4o-mini 做 CRS）可减少同模型共享偏差。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 用户模拟器在对话推荐评估中常见，但通常只用评分、人口统计学构造 profile，缺少隐式行为特征（决策风格、aspect偏好、领域专业度等），导致模拟行为趋向“平均用户”。直接让 LLM 推断又容易产生刻板印象和编造。SimInter 通过 synthetic interview 提炼隐式属性，并用 turn-level 审计防伪。

**方法关键点**
- 从 ReDial 历史交互构建基本 profile 和规则化行为统计（接受率、参考风格、genre分布、探索率等），作为统计 grounding。
- 两个 LLM agent 不对称访谈：interviewee 持有用户统计 profile 和历史对话证据，interviewer 无 profile，只能根据对话追问，避免引导；每段访谈 10 轮。
- Audit Agent 对每轮 interviewee 发言做三种 flag：fabrication（无根据具体声称）、caricature（刻板人设/编造理由）、history contradiction（与用户历史矛盾），并分级；严重时 REGENERATE，轻微 PARTIAL 剔除该轮。
- Enrichment 抽取六类隐式属性：aspect-level preferences、pickiness、decision-making style、viewing motivation、novelty preference、domain expertise，每个属性配 evidence quote。

**关键实验**
在 ReDial 300 用户上运行完整 pipeline（1200 对话），matched 100 用户对比 statistics-only 和 CSHI。T3 aspect entropy 1.619 vs 0.859，dz=0.96，Holm 校正 p<0.001；zero-aspect 用户从 41% 降到 5%。但 T1 item entropy 降低（2.034 vs 2.409），T4 corpus TTR 降低（0.674 vs 0.728），n-gram monotony 升高，说明丰富画像带来 aspect 多样但词汇重复。人类评测：94.3% 富化属性 claim 被支持；审计二元过滤准确率 95.2%。Pooled popularity correlation r=0.347。跨 KBRD/UniCRS 和多 judge 的 robustness 验证中 aspect entropy 提升依然显著（+0.28 到 +0.56 nats）。

**最值得记住的一句话**：用户模拟质量是多维的，不是所有多样性都要最大化；通过 evidence-grounded interview + turn-level audit 可以显著提升偏好表达丰富度，但会牺牲 item/lexical 多样性。
