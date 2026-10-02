---
title: Cross-Lingual Alignment for Decoder-Only Models using MoE Routers
title_zh: 面向 Decoder-only MoE 模型的跨语言路由器对齐方法
authors:
- Lucas Bandarkar
- Clark Peng
- Ahmed Haj Ahmed
- Aditi Khandelwal
- Nanyun Peng
affiliations:
- University of California, Los Angeles
- Haverford College
- MILA - Quebec AI Institute
- McGill University
arxiv_id: '2610.01921'
url: https://arxiv.org/abs/2610.01921
pdf_url: https://arxiv.org/pdf/2610.01921
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: 跨语言 MoE 路由器对齐
tags:
- MoE
- Cross-lingual Alignment
- Multilingual LLM
- Router Alignment
- Continual Pretraining
- KL Divergence
one_liner: 用 MoE router 输出的均值池化作为序列级跨语言对齐目标，在解码器模型中实现显式对齐并提升多语种表现
practical_value: '- 在跨境电商/搜索的多语言 MoE 模型中，可用平行语料（商品标题、query 翻译对、广告文案对）对中间层 MoE router
  的 mean-pooled 分布做 KL 对齐；这比 mean-pooled hidden states 更稳定，且无需 token 级对齐，适合短文本与低资源语言。辅助
  loss 梯度只走目标语言，source 侧不更新。

  - 工程实现建议采用 packed 共享前向 + 源序列早退：把 source/target 拼在一起做变长 attention，source token 在最后一个对齐层后停止计算，可省去
  padded 双重前向；α 初值可设为让 α·L_XLR ≈ L_LM，再邻近搜索。

  - 对齐层不要全选，用 cross-lingual routing divergence 曲线选「已经共享专家」的中间层，避免在输入/输出语言特异层强行对齐；对齐后隐藏表征
  SoftCKA 会跟随提升，说明 router 分布可当轻量内部监控指标。

  - 若只能做参数高效微调，router-only（<0.1% 参数）可作低资源语种适配尝试，但结果 noise 较大，不应替代全参训练；核心收益来自给 routers
  提供更好 hidden states。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现代 decoder-only LLM 缺乏自然 sequence-level 表示，跨语言表征对齐难以像 encoder 时代那样用对比学习直接实现；但已有研究表明多语言 LLM 中间层存在语言共享空间，对齐程度与跨语言迁移正相关。该工作想把平行语料重新利用起来，在 MoE 架构里寻找更适合做序列级对齐的接口。

**方法关键点**：
1）用 MoE router 在每层对 token 的输出概率分布做 mean-pooling，作为整个序列的「专家使用模式」表示；
2）对选定的中间层集合 M，计算英语和目标语言 mean-pooled routing weight 的 KL 散度，作为辅助 loss L_XLR；
3）只对目标语言序列回传梯度，源语言仅提供对齐信号；
4）中间层选择依据 cross-lingual routing divergence 曲线，避免对语言特异层强行对齐；
5）实现上采用 packed 共享前向，source 序列在对齐层之后 early exit，消除 padding 和冗余前向。

**关键实验与结果**：在 Qwen3-30B-A3B、GPT-OSS-20B、Granite-4.0-H-Tiny、Marco-Nano 四个 MoE 模型上，对越南语、僧伽罗语、匈牙利语、泰卢固语、卡纳达语、泰语、柯尔克孜语做 200k 平行样本 CPT。与普通 CPT 相比，+ routing loss 在 14 个 model-language pair 中 13 个提升、1 个持平，平均提升 0.9 个点，最高 2.1；SoftCKA 显示隐藏表征也向英语对齐。与 mean-pooled hidden-state cosine loss 相比，router 对齐在僧伽罗语 26.8 vs 26.3、匈牙利语 38.1 vs 36.9 更优。Router-only 训练可竞争但噪声大。

**最值得记住**：在 decoder-only MoE 中，mean-pooled router 分布是比 mean-pooled hidden state 更可靠的序列级跨语言对齐目标，且能用轻量 KL loss 把平行语料转化为多语种能力提升。
