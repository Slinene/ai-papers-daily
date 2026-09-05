---
title: Last Translation Benchmark
title_zh: 最后翻译基准：多模态对抗测试与可验证评估
authors:
- Vilém Zouhar
- Niyati Bafna
- Mukund Choudhary
- Maike Züfle
- Sara Rajaee
- Pinzhen Chen
- Jannis Vamvas
- Sara Papi
- Ona de Gibert
- Bhavitvya Malik
affiliations:
- ETH
- JHU
- MBZUAI
- KIT
- UvA
arxiv_id: '2609.04173'
url: https://arxiv.org/abs/2609.04173
pdf_url: https://arxiv.org/pdf/2609.04173
published: '2026-09-02'
collected: '2026-09-05'
category: Other
direction: 机器翻译极限基准与可验证评估
tags:
- Benchmark
- Machine Translation
- Evaluation
- Multimodal
- Adversarial Examples
one_liner: 构建可持续更新的多模态对抗性翻译基准，用逐例可验证规则替代不可靠自动评分
practical_value: ' - **生成质量评估规则化**：在电商文案、query 改写、Agent 回答等生成式任务中，把人工评估拆成逐条可校验规则（如商品属性不冲突、query
  必须包含品牌词/类目词、回复不得泄露库存），显著降低评估噪声和 reward hacking 风险。

  - **构建长尾对抗集**：定期收集线上模型失败的 query/商品/多模态内容，经人工评审后加入回归集，可类比 LTB 的持续更新机制，防止推荐/搜索模型在罕见
  case 上退化。

  - **多模态统一基准**：LTB 同时覆盖文本、图像、音频、视频，提示推荐系统在商品多模态理解（主图、视频、详情页）上也应建立跨模态的对抗性评估，而非只测文本召回。

  - **众包质量控审**：采用人工撰写+同行评审的投稿流程，可迁移到业务中构建高质量评估集的流程设计，减少单人标注偏差。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：机器翻译标准基准已接近饱和，自动指标（如 BLEU/COMET）不可靠、易被 reward-hacking，人工评估又缺乏可复现性与可扩展性，导致难以客观追踪进展。

**方法关键点**：提出 Last Translation Benchmark (LTB)，由人工撰写并经同行评审的对抗性示例组成，覆盖文本、图像、音频、视频多模态，目标是打破领先翻译模型。核心创新是每个示例附带手工验证规则，描述该示例上的具体失败模式，使评估结果可复现、可对应到具体缺陷。LTB 是一个持续更新的活数据集，LTBv1 收录 2026 年 9 月 1 日前接受的投稿，未来随新数据持续发布。

**关键结果**：论文未报告具体模型分数，而是强调该基准能提供可靠的失败案例定位；通过人工规则验证替代不可靠自动评分，并支持社区持续贡献以不断暴露模型极限。
