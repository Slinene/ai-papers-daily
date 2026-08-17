---
title: Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre
  Expansion
title_zh: 超越故事中心数据的创意写作扩展：属性引导的体裁扩展
authors:
- Hwan Chang
- Yongil Kim
- Heuiyeen Yeen
- Yireun Kim
- Jinsik Lee
- Hwanhee Lee
affiliations:
- Chung-Ang University
- LG AI Research
arxiv_id: '2608.13947'
url: https://arxiv.org/abs/2608.13947
pdf_url: https://arxiv.org/pdf/2608.13947
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: LLM 数据扩充 · 属性引导体裁生成
tags:
- synthetic data
- creative writing
- genre expansion
- LLM fine-tuning
- data diversity
one_liner: 用属性引导解耦主题与体裁形式，构建多体裁创意写作数据提升 LLM 跨体裁能力
practical_value: '- 可借鉴“主题种子 + 人工属性模板”的解耦思路：用电商搜索词、商品标题、用户评论等作为主题种子，人工维护不同文案体裁的结构/风格/格式属性（如
  push 文案的紧迫感、广告标题长度、商品描述格式），批量生成多体裁营销文案训练数据，提升 LLM 在电商文案生成上的指令遵循。

  - 质量过滤环节可结合业务规则与强模型打分：先按属性约束生成，再做过滤，能兼顾格式合规与文本质量，适合落地到商品文案、广告创意、消息推送等对格式和风格敏感的场景。

  - 消融结论提示：对生成式推荐/文案 Agent，体裁多样性比单纯扩大单一类型样本规模更重要；可以先小规模控制体裁类别数做验证，再决定是否扩充，节省数据预算。

  - 对 Agent 多轮任务，可把工具调用/输出 schema 视为“体裁属性”，通过人工属性库让强 LLM 生成符合格式的合成轨迹，用于训练或蒸馏领域 Agent。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：高质量创意写作数据长期以故事为中心，导致 LLM 难以遵循多种创意体裁在结构、风格和格式上的约定。

方法：采用属性引导的体裁扩展框架，把主题广度与体裁形式控制解耦——用人类创作的故事提示作为多样化创意种子，同时用手工维护的体裁属性约束结构、风格和格式。将这些组合后提示强 LLM 生成符合体裁的 query–response 对，再做质量过滤。据此构建 Multi-Genre Collection：50K 样本，覆盖 13 种创意体裁，包括故事、说唱、歌词、剧本、游戏设计、角色设计等。

结果：在分布外写作基准和留出体裁诊断上，基于该数据微调的模型持续优于基础模型、写作专用基线以及用现有写作语料训练的模型。体裁数量消融进一步表明，受控的体裁扩展——而非单纯扩大故事数据规模——是提升稳健创意写作能力的关键。
