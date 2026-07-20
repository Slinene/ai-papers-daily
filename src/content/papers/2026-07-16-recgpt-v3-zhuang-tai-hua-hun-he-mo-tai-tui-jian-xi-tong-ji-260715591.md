---
title: RecGPT-V3 Technical Report
title_zh: RecGPT-V3：状态化混合模态推荐系统技术报告
authors:
- Bowen Zheng
- Chao Yi
- Dian Chen
- Gaoyang Guo
- Han Zhu
- Jiakai Tang
- Jian Wu
- Mao Zhang
- Wen Chen
- Yifan Lu
affiliations:
- Taobao
arxiv_id: '2607.15591'
url: https://arxiv.org/abs/2607.15591
pdf_url: https://arxiv.org/pdf/2607.15591
published: '2026-07-16'
collected: '2026-07-20'
category: GenRec
direction: 生成式推荐 · SID · 记忆与效率优化
tags:
- Memory Hub
- Hybrid-modal
- Semantic ID
- Latent Reasoning
- LLM4Rec
- RLRF
one_liner: 通过记忆中心、混合模态SID和潜在推理，线上IPV+1.28%、CTR+1.00%、GMV+3.97%，成本降52.4%
practical_value: '- **用户记忆压缩与增量更新**：用 LLM 将用户长期行为压成结构化记忆单元（行为模式+偏好摘要），每两个月增量更新一次；线上推理时只输入压缩记忆+近期行为
  delta，用户建模计算降低 55.8%。可直接迁移到电商用户画像存储与动态更新，避免每次请求重读全量行为。

  - **混合模态 SID 打通意图到物品的管道**：通过多模态对比学习 + RQ-VAE 为每个物品生成两层 Semantic ID（65K 词表），作为第二模态注入
  LLM 词汇表，与文本联合训练。模型直接输出 SID 而非粗糙标签，大大降低信息瓶颈，让召回更精准。适合将物品侧协同信号与语义理解结合。

  - **潜在推理替代显式 CoT 降本增效**：用最多 10 个可学习潜在 token 替代平均 ~3K 的显式思维链，通过多粒度掩码重构训练保持推理能力，同时输出可解码回可读文本保障可解释性。输出
  token 成本降 200 倍，特别适合高 QPS 线上场景。

  - **RLRF 让离线训练对齐线上目标**：用线上排序模型 top-100 的平均 CTR Score 作为强化学习奖励，替代稀疏的 HitRate 奖励，使模型直接优化业务指标，且与在线
  pipeline 一致。可复制到其他场景将离线代理目标改为线上可观测的业务信号。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM 驱动推荐已在淘宝规模化落地，但前两代暴露三个瓶颈：(1) 每次请求从零处理全量行为，重复计算且丢失历史分析；(2) 纯文本标签输出粗糙，信息损失大，难以精准召回具体物品；(3) 显式思维链推理开销过大（平均~3000 tokens），高 QPS 下无法接受。

**方法关键点**
- **记忆中枢（Memory Hub）**：用 LLM 将用户长期行为序列压缩为结构化记忆单元（行为模式、偏好摘要、代表性行为索引等），压缩比 94.5%，并每两月用近期行为增量更新。线上推理时仅输入压缩记忆+近期行为 delta，用户建模计算降低 55.8%。
- **混合模态基础模型**：基于 Qwen3-14B，引入语义 ID（SID）作为第二模态。SID 通过 CN-CLIP 多模态对比学习 + 两级 RQ-VAE 量化得到（词表 65536），代表物品粗、细粒度语义。经持续预训练（SID 接地数据+通用数据）与指令微调（双向翻译、序列推荐任务），使模型能直接生成 SID 而非文本标签，打开高带宽物品通道。
- **潜在意图推理**：将显式 CoT 拆分为 K 段，每段由一可学习潜在 token 表示，通过单段/多段/全段掩码重构任务训练潜在 tokens 编码完整推理链。配合两阶段后训练：先蒸馏强模型的显式 CoT 再内部化，再用 RLRF 优化。RLRF 直接用线上排序模型 top-100 的平均 CTR Score 作为奖励，比稀疏 HitRate 更有效。

**关键结果**
线上 A/B 测试（淘宝“猜你喜欢”，对比 RecGPT-V2）：物品场景 IPV+3.08%，CTR+0.98%，GMV+7.51%；信息流场景 IPV+1.28%，CTR+1.00%，GMV+3.97%。端到端服务资源消耗减少 52.4%。潜在推理比显式 CoT 输出 token 成本降低 200 倍，同时保持相近的推荐质量。
