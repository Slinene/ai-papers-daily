---
title: 'The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring
  Misleads'
title_zh: 个性化幻觉：LLM 如何捏造用户画像与自我监测的误导
authors:
- Yushi Sun
- Yanjie Zhang
- Rui Sheng
affiliations:
- LIGHTSPEED
- The Hong Kong University of Science and Technology
arxiv_id: '2608.04570'
url: https://arxiv.org/abs/2608.04570
pdf_url: https://arxiv.org/pdf/2608.04570
published: '2026-08-04'
collected: '2026-08-06'
category: LLM
direction: 个性化LLM的忠实度评估与自监测缺陷
tags:
- Over-inference
- Faithfulness
- Personalization
- LLM Benchmark
- Self-monitoring
- User Profile
one_liner: 揭示所有大模型在个性化任务中系统性过度推理（35-49%），且自监测排名与真实忠实度负相关
practical_value: '- 在电商推荐、广告定向等依赖 LLM 构建用户画像的场景，必须警惕过度推理（35%–49% 的声明是凭空捏造的），应引入独立外部验证机制（如类似
  MirageBench 的评判器）而非依赖模型自报。

  - 选择个性化模型时，不可相信模型自述的忠实度，自监测排名与真实虚构率负相关（ρ=-0.60），需建立外部测试基准评估真实过度推理率。

  - 多轮交互中用户属性会线性累积且极少修正，可能导致画像严重偏离，在对话式推荐或 Agent 记忆系统中需加入定期“画像审计”或遗忘机制。

  - 过度推理具有强任务依赖性（范围27%-59%），对不同业务模块（如文案生成 vs 用户标签推断）应分开评估并设置差异化阈值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：个性化大模型（LLM）越来越多用于生成用户画像，但模型可能凭空编造用户属性（过度推理，Over-inference），其忠实度尚未被系统研究。

**方法**：提出 MirageBench，包含150个平衡刻板/反刻板/中性的用户 personas，6个沿“想象梯度”的个性化任务，以及一个经人工标注验证的独立四类忠实度评判（Cohen's κ=0.863）。评估12个模型（7个家族）共14.4万条声明。

**关键结果**：所有模型均存在过度推理，比例35%-49%，平均41.6%；出现“自监测反转”现象——模型自评的过度推理越少，实测值反而越高（Spearman ρ=-0.60, p=0.044）；模型内自我审查的AUROC为0.58–0.83，但跨模型比较时自评完全不可靠；过度推理高度依赖任务类型（27%–59%），且多轮对话中属性积累接近线性，几乎不修正。结论：外部验证而非模型自报是可信赖个性化系统的基础。
