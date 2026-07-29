---
title: 'PILA: Plug-and-Play Insertion for LLM-native Advertising'
title_zh: PILA：面向 LLM 原生广告的即插即用插入框架
authors:
- Zhaowei Zhang
- Yuhan Fu
- Yihang Zhang
- Xiaohan Liu
- Ceyao Zhang
- Xiaoyuan Zhang
- Yipeng Kang
- Tonghan Wang
- Yaodong Yang
affiliations:
- Peking University
- Tsinghua University
- University of Michigan
- BIGAI
- Shanghai Qi Zhi Institute
arxiv_id: '2607.25590'
url: https://arxiv.org/abs/2607.25590
pdf_url: https://arxiv.org/pdf/2607.25590
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: LLM 原生广告 · 解耦式插入
tags:
- LLM-native advertising
- sidecar pattern
- conditional rewriting
- controllable ad intensity
- plug-and-play
- NaiAD
one_liner: 将广告插入解耦为条件响应改写，作为轻量级 sidecar 模块，实现模型无关、即插即用且强度可控的广告融入
practical_value: '- **解耦式重写设计可复用**：在对话推荐或生成式推荐中，可仿照 PILA，将商品推荐或广告插入作为独立的轻量 sidecar
  模块，不改动上游对话/搜索模型，仅对最终回复进行条件改写，降低侵入性并保持主模型质量。

  - **数据构造与增强管线**：种子数据合成 + 多样性增强 + 自我评判的自动化数据构建流程，可用于生成对话推荐中的商品链接、推广文案等训练样本，解决标注稀缺问题。

  - **广告强度可控机制**：基于说服知识模型的对比解码方法调整曝光策略，这种“部署时旋钮”可迁移到电商推荐中，平衡推荐内容的自然度与商业目标（如 GMV、点击率），无需重新训练模型。

  - **三指标评估体系**：Q1 相关性、Q2 连贯性、Q3 广告有效性的三元评估，可直接用于衡量对话推荐中商品植入的整体质量，指导实验迭代。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：大语言模型成为用户流量入口，原生广告货币化至关重要。现有方法在单一模型内耦合响应生成与广告插入，不仅不兼容闭源 API 和复杂 agent 工作流，还可能损害响应质量。亟需一种解耦、模型无关的广告插入方案，既能提升广告效果，又保持原有回复的自然度。

**方法关键点**
- **问题建模**：将广告插入视为条件响应改写。给定用户查询 x、广告 a/c，先让上游系统生成无广告回复 y，再用独立的侧车重写器 πθ 生成包含广告的回复 ˜y，广告段落用 `<ad>` 标签标记。
- **数据构造**：基于 NaiAD 广告数据集，用 Claude Opus 4.5 合成种子样本（多轮，每查询搭配 4 条广告，4 种插入策略），自我评判筛选出 10k 高质量对；再用 Claude Haiku 4.5 对种子进行多样性增强，生成 3 种释义并过滤，最终得到 25k 训练样本。
- **模型与训练**：使用 Qwen3 4B/8B 作为重写骨架，以条件改写格式微调得到 PILA-4B/8B。
- **广告强度控制**：引入说服知识模型启发的对比解码，通过因子 ρ 在推理时调节广告显著程度，ρ 增大则广告更突出。

**关键实验与结果**
- 在 NaiAD 基准的 4+2 个广告类别上，PILA-8B 相比单 LLM 基线：平均得分比 SFT 高 7.7%，比 prompt 式 Base 高 34.2%，比采样法 MOSAIC 高 47.3%。
- 作为即插即用模块增强 GPT-5.4、Gemini 3.1 Pro 等 7 种前沿商业模型，PILA-4B 平均提升 17.2%，PILA-8B 提升 18.4%，且实现近乎帕累托改进：用户侧满意度与广告侧效果同步提高。
- 广告强度控制曲线显示，用户侧评分随 ρ 单调下降，广告侧评分先升后降，验证了可控的权衡界面。

**核心 take-away**：解耦式广告插入让 LLM 原生广告可以无侵入地附着在任何上游系统上，且通过强度控制器实现商业化与用户体验的灵活平衡。
