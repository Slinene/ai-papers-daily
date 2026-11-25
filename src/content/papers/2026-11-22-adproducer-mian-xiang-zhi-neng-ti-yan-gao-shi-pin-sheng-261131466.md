---
title: 'AdProducer: Towards Agentic Advertising Video Generation'
title_zh: AdProducer：面向智能体广告视频生成
authors:
- Kunyang Li
- Chaoyang Wang
- Mubarak Shah
- Yuzhang Shang
affiliations:
- Institute of Artificial Intelligence, University of Central Florida
arxiv_id: '2611.31466'
url: https://arxiv.org/abs/2611.31466
pdf_url: https://arxiv.org/pdf/2611.31466
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: 多模态智能体 · 广告视频生成
tags:
- AdVideoGen
- Agentic Workflow
- GRPO
- Product Grounding
- Multimodal LLM
one_liner: 首个端到端智能体广告视频生成框架，通过产品调研与分镜设计训练9B Agent，将MiniMax H3的PG-Score从17.3提升到51.3
practical_value: '- **把视频生成器当黑盒，只训练上游 planning agent**：AdProducer 证明冻结 MiniMax H3/Veo
  3.1，仅用 9B agent 做产品调研 + 分镜规划，就能把产品一致性提升近 3 倍。业务上可复用：不自研视频模型，专注在“research → storyboard
  → reference selection”链路。

  - **数据构造即壁垒：teacher agent + 多层过滤**：用 Gemini 3.8 Flash 多轮搜索生成轨迹，Claude Opus 5.5 做结构/事实/图像一致性验证，得到
  3,710 SFT + 1,000 RL 样本。电商可对商品库批量制造“brief → 调研轨迹 → 分镜”训练样本，快速复制到新品类。

  - **联合 reward 训练 agentic 生成系统**：单独 video reward 噪声大，单独 storyboard reward 无法评估最终效果；联合
  GRPO（α=0.5）能互补。做文案/素材自动化时，可设计中间产物得分 + 最终产出得分的混合 RL。

  - **把产品事实结构化后再进生成器**：AdProducer 将搜索的 facts 和 reference images 绑定到每个 shot，避免文字乱码和产品错版。迁移到电商：先查商品官方图、规格参数，再生成分镜，可显著降低货不对板和乱码。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
视频生成模型能产出高保真画面，但广告的核心是产品正确、事实准确、卖点可视化。直接 prompt 生成器会产出错误设备、错误参数和无法识别的文字，因为产品调研和创意设计相互依赖，需要外部证据和结构化规划。

## 方法关键点
- **AdProducer agent**：9B 多模态 agent（Qwen3.5-9B 初始化），提供 search / browse / image_search 三种工具，多轮推理后输出带参考图的 shot-level storyboard；冻结 MiniMax H3 或 Veo 3.1 作为视频生成器。
- **数据构造 pipeline**：从 8 大领域 60 个产品类别构建 briefs，用 teacher agent（Gemini 3.8 Flash）多轮搜索生成轨迹，经 Claude Opus 5.5 验证过滤，得到 3,710 SFT + 1,000 RL 样本，以及 305 个 held-out 评测 briefs。
- **两阶段训练**：SFT 模仿 teacher 的产品调研与分镜设计；RL 使用 GRPO，联合 storyboard reward（0/0.25/0.5/0.75/1 分级）和 video reward（PG-Score），α=0.5，非对称 clip。
- **评测指标**：PG-Score 包含 visual correctness / text accuracy / selling point / shot design / aesthetics，加权为 0.4/0.2/0.2/0.1/0.1；Ad-Score 由独立 judge 给 1-10 综合广告效果分。

## 关键结果数字
- MiniMax H3 的 PG-Score 从 17.3 提升到 51.3，其中 visual correctness 3.5→36.5，text accuracy 1.3→40.4，selling point 34.1→71.6。
- 无重训迁移到 Veo 3.1，PG-Score 28.0→35.9；Ad-Score 2.87→3.47。
- AdProducer + H3 的 Ad-Score 达到 4.70（最强直接生成 baseline 为 2.87）；人工评估产品保真度 4.75 vs. 2.46。
- 消融：SFT 后 PG-Score 48.4，加联合 RL 后 51.3；单 storyboard 或单 video reward 仅增加约 1.1-1.3 点。

> 最值得记住：广告视频生成的瓶颈不在像素生成，而在上游的产品调研与卖点分镜；冻结视频模型，训练一个小型多模态 agent 做 research + storyboard 就能大幅提升产品一致性。
