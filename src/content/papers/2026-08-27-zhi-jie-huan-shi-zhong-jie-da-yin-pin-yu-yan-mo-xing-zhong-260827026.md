---
title: Direct or Mediated? Task-Dependent Audio Information Routing in Large Audio
  Language Models
title_zh: 直接还是中介？大音频语言模型中任务相关的音频信息路由
authors:
- Yizhou Zhang
- Wangjin Zhou
- Xin Gu
- Yichi Wang
- Wei Tan
- Yi Zhao
- Zhi Gong
- Keisuke Imoto
- Tatsuya Kawahara
affiliations:
- Graduate School of Informatics, Kyoto University
- WXG, Tencent
arxiv_id: '2608.27026'
url: https://arxiv.org/abs/2608.27026
pdf_url: https://arxiv.org/pdf/2608.27026
published: '2026-08-27'
collected: '2026-08-30'
category: Multimodal
direction: 多模态音频 LLM 信息路由分析
tags:
- LALM
- Audio Question Answering
- ASR
- Attention Routing
- Interpretability
- Multimodal LLM
one_liner: 用逐层注意力 knockout 揭示 LALM 中 ASR 与 AQA 的信息路由差异，指出音频拼接下 AQA 失败源于下游信息利用瓶颈
practical_value: '- 多模态 LLM 在拼接/混合输入下不同任务鲁棒性差异大：直接检索型任务（如 ASR）更稳，需要推理整合的任务（如 AQA）易崩。做语音购物、智能客服等业务时，不能假设模型整体
  robust，需分开评估识别子任务与问答/决策子任务。

  - 逐层 attention knockout 和 prompt-token probing 可作为诊断工具复用：定位多模态模型在复杂输入中失败是早期编码信息丢失还是下游检索/利用瓶颈。在生成式商品推荐中，可检查
  item 信息是直接由生成 token 检索，还是先写入 prompt token 再中介。

  - 若发现任务依赖 mediated route 且下游利用不足，可考虑架构干预：对 prompt token 增加辅助监督或跨模态对齐损失，强化中介表示；或在生成阶段引入
  pointer/显式检索机制绕过自回归访问瓶颈。

  - 工程上，当多个商品描述或音频片段拼接输入时，中间层 prompt 表示可能仍保留信息但利用不起来，可考虑加入外部 key-value memory 或 cache，让生成
  token 显式检索，缓解信息利用瓶颈。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：LALMs 通常在单一连贯音频上评估，对音频拼接等非熟悉输入配置下的行为研究不足。实验发现两段音频拼接时，不同任务鲁棒性差异显著：ASR 保持相对稳定，AQA 性能大幅下降。

**方法关键点**：对多个 LALM 解码器做逐层注意力 knockout，分析音频信息如何路由到生成 token。结果显示任务相关路径不同：ASR 主要依赖 answer tokens 直接从 audio tokens 检索信息；AQA 更依赖 mediated route——音频信息先整合进 prompt tokens，生成时再从 prompt tokens 访问。进一步对拼接输入下的 prompt token 表示进行 probing，发现任务相关音频属性在中层和后层解码器仍可解码，即使 AQA 性能已急剧下降。

**关键结果**：表示与性能出现分离，说明 AQA 失败不能用解码器状态完全丢失音频信息解释，而是更符合下游在检索或利用 prompt 中介信息时存在瓶颈。整体表明 LALM 存在任务相关的音频信息路由差异，信息利用而非信息保留是影响泛化的关键限制。
