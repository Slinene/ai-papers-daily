---
title: Self-Reflective Multi-modal Reasoning for Short-Video Fake News Detection
title_zh: 面向短视频假新闻检测的自反思多模态推理框架
authors:
- Pinjie Xu
- Yuzhou Yang
- Zhikai Tan
- Qichao Ying
- Zaiyang Yu
- Ce Li
- Zhenxing Qian
affiliations:
- China University of Mining and Technology - Beijing
- Fudan University
- The Institute of Semiconductors of the Chinese Academy of Sciences
arxiv_id: '2608.26787'
url: https://arxiv.org/abs/2608.26787
pdf_url: https://arxiv.org/pdf/2608.26787
published: '2026-08-27'
collected: '2026-08-30'
category: Multimodal
direction: 多模态自反思推理 · 假新闻检测
tags:
- Fake News Detection
- Self-Reflection
- VLM
- Multimodal Reasoning
- Short-Video
one_liner: SRM-FND 通过对比反思、迭代根因诊断与校正提示优化，提升短视频假新闻检测的可靠性与可解释性
practical_value: '- **多角色辩论式推理可用于电商内容审核**：盲分析者、反结论推理者、自洽仲裁者的协作机制能有效保留判别性证据，可迁移到短视频商品描述、直播切片、用户评论的真实性/合规性审核，尤其适合不确定样本的二次裁决。

  - **置信度驱动的跨样本检索值得借鉴**：对低置信样本检索同事件/同商品的可信与可疑参照，通过对比增强判定，可应用于商品虚假卖点识别、竞品对比内容审核、广告合规检测等场景。

  - **双阶段主题自适应 VLM 微调是低成本部署路径**：先做多模态 grounding，再做轻量 topic specialization，适合在算力有限的电商风控团队中快速适配新品类或新违规模式。

  - **自反思无需 ground-truth CoT 监督**：在缺乏高质量推理标注的电商内容安全场景，可通过迭代根因诊断和提示修正自动提升推理质量，降低人工标注成本。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**  
短视频假新闻检测逐步引入 LLM/VLM 推理，但存在三个开放问题：无 ground-truth CoT 监督下如何自反思提升推理质量；改进后的 CoT 如何反哺下游模型微调；如何将单样本欺诈模式发现与跨样本验证连接起来。  

**方法关键点**  
SRM-FND 构建了一个自反思多模态推理框架：  
- **对比反思与迭代诊断**：通过 Blind Analyst、Counter-Conclusion Reasoner、Self-Consistency Arbiter 三类角色协作，对推理进行根因诊断和校正提示优化，保留判别性 evidence。  
- **双阶段主题自适应 VLM 微调**：先完成多模态 grounding，再做轻量主题特化，提升多模态对齐与领域适配效率。  
- **置信度驱动的跨样本复核**：对不确定案例检索同事件的可信与可疑参照样本，通过对比增强判定可靠性。  

**关键结果**  
在 FakeSV 和 FakeTT 两个短视频假新闻检测基准上，SRM-FND 一致超过强基线，预测更可靠、可解释，且跨数据集泛化性能有明显提升。
