---
title: 'PMRecBench: A Benchmark for Personalization in Recommendation Agents under
  Multimodal Queries'
title_zh: 多模态查询下推荐智能体个性化评估基准 PMRecBench
authors:
- Xiaoyu Zhang
- Yougang Lyu
- Bin Wu
- Sahan Bulathwela
- Emine Yilmaz
affiliations:
- University College London
- University of Amsterdam
arxiv_id: '2611.06349'
url: https://arxiv.org/abs/2611.06349
pdf_url: https://arxiv.org/pdf/2611.06349
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: 多模态推荐 Agent 个性化评估
tags:
- Multimodal
- Recommendation Agents
- Personalization
- Benchmark
- Preference Following
one_liner: 构造510个真实用户多模态查询与诊断候选池，揭示推荐智能体在多模态查询下偏好跟随被削弱
practical_value: '- 借鉴诊断池设计：随机候选池会被粗粒度 query 匹配掩盖个性化缺陷；建议显式构造两组竞争者（满足 query 但不符合偏好、符合偏好但违反
  query），分别监控 requirement understanding 与 preference following，避免只看 NDCG。

  - 多模态查询会“挤出”偏好跟随：加入参考图后，Agent 更容易优先图片相似性而忽略用户历史偏好信号；在线推荐 Agent 中应在排序阶段强制融合 CF/历史偏好分数，或做后处理校准，不要只靠
  LLM 自身权衡。

  - 图片解释是关键瓶颈而非图片模态：把 query 改写成标准文本后，偏好跟随损失消失；模型自己读图重写文本反而更差，说明要优化多模态编码/视觉属性抽取，而不是简单把图转成文本。

  - 更强 backbone 不解决个性化失衡：商业大模型 requirement understanding 近饱和，但 preference following
  反而低于中等开源模型；投入更多算力前应先设计显式的个性化排序约束或 reward，避免只优化 query 满足。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商/娱乐平台出现图像+文本查询的推荐智能体，但现有评测要么只测文本查询个性化，要么只测多模态查询匹配，缺乏同时考察真实用户历史偏好与多模态需求理解的基准。

**方法关键点**：
- 从 Amazon 服装和 MovieLens-1M 真实评分记录挖掘一致行为模式，生成 510 个图像-文本查询；query 有 Single/Shared/Combined/Contrastive 四种形式，参考图像来自用户历史中评分过的 item，target 为未来高评分且满足要求。
- 用 Gemini 3.1 Pro 生成并改写 query，Claude Opus 4.8 和 GPT-5.5 做验证，确保需求必须通过图片推断、文本不泄露。
- 构造诊断池：30 个候选中，target + 5 个偏好对齐但违反要求 + 5 个满足要求但偏好不一致 + 19 随机，分别用 U 和 P 指标衡量需求理解与偏好跟随。

**关键实验结果**：
- 随机池上 agent 比 direct ranker 和传统推荐显著更好，但诊断池上 NDCG@1 平均下降 0.20-0.26。
- 仅 personalization signals 时 P 高；加入多模态 query 后平均 P 下降 0.046（服装）和 0.042（电影），每个 agent/backbone 均如此。
- 把图片解释换成标准文本 query 后，P 不再显著下降，说明问题在图像解释。
- 用 ReAct 固定比较 8 个 backbone，商业模型 U 接近饱和但 P 低于 Gemma-4-31B。
- 失败分析：58.4% 的失败来自仅靠 query 排序，35.2% 因候选更接近参考图而错选。

**最值得记住的一句话**：多模态 query 提升整体排序但削弱偏好跟随，这种个性化失衡源于图像解释，且更强 backbone 无法单独解决。
