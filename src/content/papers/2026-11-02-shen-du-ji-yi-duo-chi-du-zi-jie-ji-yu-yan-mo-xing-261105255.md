---
title: Going Deeper With Memories
title_zh: 深度记忆：多尺度字节级语言模型
authors:
- Afshin Khadangi
affiliations:
- SnT, University of Luxembourg
arxiv_id: '2611.05255'
url: https://arxiv.org/abs/2611.05255
pdf_url: https://arxiv.org/pdf/2611.05255
published: '2026-11-02'
collected: '2026-11-05'
category: LLM
direction: 字节级语言模型 · 多尺度压缩
tags:
- byte-level LM
- multiscale compression
- fast weight memory
- tokenizer-free
- efficient FLOPs
one_liner: 提出 DeepMem，用可逆子带压缩、无损旁路和快权重记忆实现高效字节级 LM，大幅降低 FLOPs 并提升多语言表现
practical_value: '- 长序列用户行为/日志压缩：用可逆子带变换把原始事件序列缩成多尺度短序列，粗尺度做模型推理，细粒度 sideband 保留精确
  item id/时间/金额；可迁移到召回/排序模型处理超长行为序列，减少 Transformer 序列长度和 KV cache，同时保留精确字段用于后续 look-up。

  - Fast weight memory + 迭代 bottleneck refinement：在压缩后的瓶颈位置共享状态迭代 R 次，FLOPs 约为全分辨率
  R 次的 1/7600；在电商 Agent 中可把商品库/会话状态压到低分辨率 memory，规划与推理放在粗粒度状态上多轮 Refine，最后用 super-resolution
  恢复到 item 级候选，降低每轮 LLM 调用成本。

  - 语义压缩流 + 无损旁路：主链路用压缩表示做生成/排序，旁路保留原始 id/属性用于合规、审计、去重与精排；避免有损压缩丢掉长尾 item 或价格、库存等关键字段。

  - 字节级鲁棒性对噪声/多语言有价值：广告搜索词、UGC 文本、多语言 query 常见拼写错误/未见词，tokenizer-free 架构可提升 corruption
  robustness；若无法完全去除 tokenizer，可在 query 侧引入 byte-level sideband 做难样本兜底。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：字节级 LM 免除 tokenizer、覆盖所有语言和代码，但逐字节全分辨率处理太贵。

**方法关键点**：DeepMem 采用多尺度因果架构，把语义压缩和精确字节保存解耦。学习可逆子带变换构造更短序列层级；lossless carrier 和显式 detail sidebands 保留字节身份。沿 encoder 使用 fast weight memory blocks，在压缩瓶颈做共享状态的迭代 refine；基于 attention 的超分 decoder 恢复字节级表示。

**关键结果**：相比匹配的 byte-level Transformer，FineWeb-Edu BPB 降低 3.1%，泰语 BPB 降低 7.7%；PIQA 精度提升，random-case HellaSwag +1.8 pts；在 FLORES 多语言上 macro average 最优；在 code modeling、多项选择 reasoning、字节级 corruption robustness 上保持竞争力。R=2 的瓶颈 refine 比全分辨率推理少约 7,600× FLOPs，相比 FastWeight baseline GPU 内存降 54%、吞吐提升 37%。
