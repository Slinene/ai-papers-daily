---
title: Improving Item Discoverability in e-Commerce Search via Related Intent Generation
title_zh: 通过隐含意图生成提升电商搜索物品可发现性
authors:
- Ji Xin
- Xiao Xiao
- Ishan Bhatt
- Vinesh Gudla
- Trace Levinson
- Raochuan Fan
- Shishir Kumar Prasad
- Prakash Putta
- Tejaswi Tenneti
affiliations:
- Instacart
arxiv_id: '2607.27172'
url: https://arxiv.org/abs/2607.27172
pdf_url: https://arxiv.org/pdf/2607.27172
published: '2026-07-29'
collected: '2026-07-30'
category: QueryRec
direction: 搜索 · 意图生成 · 发现增强
tags:
- Query Intent Generation
- Discovery-Augmented Search
- Teacher-Student Distillation
- LoRA
- E-commerce Search
- LLM
one_liner: 用 LLM 生成替代/补充/主题意图扩展召回，通过两阶段架构在头部用闭源模型缓存、尾部用蒸馏 SLM 覆盖，将流量覆盖率从 60% 提升至 80%
  且成本仅 30%
practical_value: '- **意图驱动的召回扩展**：定义替代、补充、主题三类隐含意图，用 LLM 生成“轮播标题 + 意图词列表”来扩大候选池，可直接改造搜索底纹中的“发现式”模块，解决精确匹配造成的长尾冷启动曝光不足。

  - **两阶段成本与覆盖权衡**：头条查询离线缓存闭源 LLM（GPT-3.5 Turbo）结果，长尾查询在线用 LoRA 微调的 30B SLM 推理，使用
  teacher-student 蒸馏，最终以约 30% 推理成本达到 80% 流量覆盖，特别适合类目众多、长尾严重的电商搜索。

  - **评估体系设计**：构建 session 级共购数据集评估端到端召回，排除完全匹配和 top-10 商品，提取用户未被当前检索满足的隐性需求信号；同时用
  LLM-as-judge 衡量生成标题和意图的相关性、多样性、新颖性，并通过人工验证，可作为业务中评估类似生成任务的标准范式。

  - **蒸馏工程细节**：教师模型在蒸馏时使用了丰富的上下文元数据（品牌、属性、历史购买），为避免学生模型在线上缺少这些特征时质量下降，蒸馏数据中混入部分剥离元数据的样本，训练学生不依赖额外
  payload；另外将生成与检索解耦，LLM 不进入在线热点路径，便于缓存、降级和 AB 部署。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索往往以精确匹配为核心，但用户在杂货等类别中常有隐性意图，如寻找替代品（tangerine → clementine）、互补品（pasta + sauce）或主题关联物（seafood platter + seasoning）。传统检索会过度依赖精确命中，导致大量长尾和新品无法获得合乎意图的曝光，既损害用户体验也影响双边市场健康。因此，本文将“发现增强搜索”形式化为一个新任务：不仅返回精确匹配，还要生成隐含意图并据此扩展召回。

### 方法关键点
- **任务建模**：输入用户 query，输出最多 9 个轮播（carousel），每轮播包含一个自然语言标题和 5 个意图词，再由普通检索引擎取回商品。意图分为三类：替代、互补、主题。
- **两阶段架构**：
  - **头部查询**（约 1 万高频词，占 60% 流量）：离线用 GPT-3.5 Turbo 生成结果并缓存在特征商店，在线直接读取，零推理成本。
  - **尾部查询**（剩余 40% 流量）：使用 teacher-student 蒸馏，以 GPT-5.1 为教师，对 20k 样本（半头部半尾部）标注，用 LoRA (rank=8) 微调 Qwen3-30B-Instruct 一个 epoch，学习率 1e-4，batch size 65536。蒸馏数据中包含丰富的上下文元数据（品牌、属性等），混入部分无元数据样本以避免学生模型依赖额外信息。
  - SLM 在线部署后，总覆盖流量升至 80%，剩余 20% 极端长尾无轮播直落 legacy 检索。
- **生成与检索解耦**：LLM 不直接召回商品，只产出标题和意图词，保持离线推理、可缓存，不进入用户请求热路径。

### 关键实验
- **端到端评估**：从历史搜索 session 构建数据集，排除精确匹配商品和每个 query 的 top-10 结果，聚合共购商品类别，按位置衰减加权。最终衡量类别级召回、精确、F1。
  - 头部 query：Qwen3 学生模型 F1 0.184，超过生产基线 GPT-3.5 Turbo 的 0.173，与教师 GPT-5.1 的 0.192 接近。
  - 尾部 query：学生 F1 0.179，与教师 0.168 相当甚至略优，而生产基线不覆盖尾部。
- **生成质量 LLM-as-judge**：GPT-5 打 7 项二分类指标，经 3 位专家标注校准，精确率/召回/F1 均在较高水平。
  - 头部：学生模型在意图新颖性上达 0.911，比生产基线（0.853）显著提升，优于教师（0.898）。
  - 尾部：学生模型在大部分指标上保持竞争力，尤其新颖性达 0.888。
- **业务效果**：以学生模型 30% 推理成本将发现式轮播覆盖率从 60% 扩至 80% 流量，且未显著牺牲相关性。

### 一句话记忆
“把 LLM 的语义推理用于显式生成替代、互补、主题三类意图，并解耦生成与检索，即可在不改动召回引擎的前提下大幅提升长尾发现能力。”
