---
title: 'Draft-KV: Learning Useful Latent Communication Between Language Models'
title_zh: Draft-KV：学习语言模型间有价值的潜在通信
authors:
- Linquan Wu
- Shichang Meng
- Tianxiang Jiang
- Haoyu Yang
- Peng Zhong
- Fengming Zhu
- Xi Peng
- Linqi Song
- Jacky Keung
- Jingyu Zhang
affiliations:
- City University of Hong Kong
- University of Science and Technology of China
- University of Electronic Science and Technology of China
- AIPD, Tencent
- Theory Lab, Huawei
arxiv_id: '2609.34754'
url: https://arxiv.org/abs/2609.34754
pdf_url: https://arxiv.org/pdf/2609.34754
published: '2026-09-27'
collected: '2026-09-29'
category: LLM
direction: LLM 潜在通信 · KV Cache 传输
tags:
- Latent Communication
- KV Cache
- Frozen LLM
- Gated Attention
- Progressive Training
one_liner: 提出 Draft-KV，用 sharer 草稿过程的 KV 状态经门控侧记忆接口传给 frozen 小模型，显著提升协同推理
practical_value: '- 在多模型 Agent 链路中，让大模型（sharer）提前对候选 query/商品/用户意图草拟推理，并把草稿过程的 KV
  cache 暂存为侧记忆；线上由小模型接收这些 KV 做最终决策或生成，接口参数仅 ~1M，两端模型冻结，部署成本远低于全量微调。

  - 接口设计可借鉴「线性投影 + 门控 attention 分支」：不把通信状态注入主隐层，而是作为 side memory 参与注意力，避免干扰小模型已有表示；门控可控制通信信息的权重，便于线上
  A/B 开关和降级。

  - 训练采用两阶段 progressive：先做 message reconstruction 对齐表示，再转到 answer supervision；并加入
  mismatched message 的 guard 损失，防止通信缺失或错配时模型被带偏，这对推荐中的多路召回/多模型融合也有参考。

  - 验证通信是否真被使用：用随机替换消息做控制实验，若替换后指标几乎不变，说明增益来自接口结构而非信息内容；在推荐/广告引入 LLM 通信或增强时，应做同样消融，避免伪提升。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 latent communication 常以接收方精度提升作为成功信号，但作者发现替换为无关问题的消息后精度几乎不变（≤0.60 点），即使通信提升 15.44 点；说明增益可能来自接口结构而非消息内容。Draft-KV 转向共享 sharer 为当前问题草稿答案时生成的 KV 状态，让消息与当前输入强绑定。

方法：sharer 和 receiver 均冻结，仅训练 1.05M 参数接口。线性投影将 sharer 的 KV 放入 side memory；receiver 通过 gated attention 分支读取。训练采用 progressive：先做 message reconstruction 对齐表示，再切换至 answer supervision，并加入 mismatched message 的 guard 损失防止模型被错误通信带偏。

结果：Qwen3-8B sharer + frozen Qwen2.5-0.5B-Instruct receiver 在 MMLU-Redux 上达 78.04%，单独为 37.45%，错配消息仅 36.40%。固定接口规模，sharer 从 0.6B 扩至 8B 精度由 46.11% 升至 78.04%；通信可迁移到 held-out 任务，并能在双方持有不同证据时超过任一单独模型。
