---
title: 'PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified
  End-to-End Multimodal Search'
title_zh: 拍立淘MMSearch2.0：统一端到端多模态生成式搜索技术报告
authors:
- Xiaohan Ye
- Zihan Gong
- Jingqian Zhao
- Lianyu Du
- Yunmeng Shu
- Xu Chen
- Zesheng Zhou
- Renchun You
- Bocheng Chen
- Jinsong Lan
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2610.36958'
url: https://arxiv.org/abs/2610.36958
pdf_url: https://arxiv.org/pdf/2610.36958
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式检索 · Semantic ID · 多模态电商搜索
tags:
- Generative Retrieval
- Semantic ID
- Multimodal Search
- E-commerce
- RL
- VLM
one_liner: 直接由图像+自由文本生成商品Semantic ID，统一相似/编辑/搭配意图，上线拍立淘带来显著GMV提升
practical_value: '- 可直接复用「Sample–Beam rollout」：RL 训练时采样 reasoning prefix，SID 部分用 beam
  search 生成，使训练 rollout 与线上 beam-decoding 对齐；做生成式推荐/搜索的 GRPO 时能有效减少 train-serve mismatch。

  - 用「混合 reasoning budget SFT」把 No-think / Low-think / High-think 训进同一个模型，线上通过 system
  prompt 切换 think budget，无需为不同延迟要求训多个模型或加意图路由；适合在候选生成与复杂查询场景复用。

  - 数据生产采用可组合工具链：Coarse-Filter、Fine-Filter、Query-Text-Gen、CoT-Gen、Quality-Control，并按
  cold-start / real-traffic / continuous production 配置不同 workflow；新意图冷启动可先用 proxy
  商品关系合成数据，上线后用真实流量回流清洗，再持续混入生产。

  - 三层 hierarchical SID（每层 8192 codebook）+ 原生 VLM 直接 beam decode SID 作为检索结果，省去独立召回/排序和意图分类器；已有成熟召回排序链路时，可先作为候选召回源
  interleave，A/B 验证后再扩大流量。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

工业界生成式检索模型常被绑定在固定场景、固定 query 形态和固定资源预算上：训练数据来自既有入口，难覆盖新意图；一个模型只学一种检索关系，扩展要靠意图分类器和路由；模型大小与解码策略只为一个服务目标挑选。开放多模态电商搜索把这些问题同时放大：用户上传图片并给出自由文本指令，可能是找相似、做属性编辑，也可能是找搭配商品，系统需要自行推断检索关系并直接生成商品 Semantic ID。

**方法关键点**

系统沿三个维度扩展：
- **Data scaling**：用可组合工具链完成粗筛、细筛、query 文本生成、CoT 标注和终端质量控制；按冷启动合成、真实流量清洗、持续生产三种 workflow 组装，兼顾多意图覆盖和数据质量。
- **Intent scaling**：先用 CPT 对齐电商商品知识、属性体系和 SID 词表；再做 multi-intent + mixed-budget SFT，让同一模型学会相似/编辑/搭配关系，并支持 No-think / Low-think / High-think 三类 prompt 控制的推理预算；最后用 intent-balanced unified RL 优化统一策略。
- **Scenario scaling**：通过 0.8B / 2B / 4B 模型规模和推理预算形成质量-成本操作点，线上按应用资源包选择配置，不引入意图路由。

核心训练 trick 是 **Sample–Beam rollout**：RL 时先采样 N 条 reasoning prefix，再对每条 prefix beam-decode B 条 SID，使策略优化更贴近线上 beam 生成候选集的解码方式。

**关键实验**

离线评测中，2B Low-think 配置获得 macro NDCG 0.918、macro ER 55.1%，平均 RT 278ms、单 GPU；相比 Qwen3.8-Flash-Next、GPT6-luna 和内部 recall-ranking pipeline，macro ER 分别提升 2.9、3.3、5.6 个百分点，且 RT 和 GPU 占用更低。Sample–Beam RL 相比 SFT 提升 5.97 个 macro ER 点；数据量从 30% 提升到 100% 带来 +2.71 个 macro ER 点；CPT 带来 +1.2 个 macro ER 点。淘宝拍立淘线上 A/B 显示：item page views +17.90%、transactions +27.04%、GMV +8.94%，CTR +0.58pp、CVR +0.37pp，均为统计显著。

**最值得记住的一句话**

工业级生成式检索不应为每个意图和场景单独建模，而应把数据、意图和场景作为三个可独立缩放的维度，统一到一个原生 VLM + Semantic ID 策略中。
