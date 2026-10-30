---
title: 'Read More, Reason Deeper: Latent Workspaces for Long-Sequence Recommendation'
title_zh: 阅读更多、推理更深：长序列推荐的潜在工作空间
authors:
- Renzhi Wu
- Li Sheng
- Zikun Cui
- Junjie Yang
- Tai Guo
- Keke Zhai
- Yan Li
- Jerry Fu
- Nipun Mathur
- Sri Reddy
affiliations:
- Meta MRS
- Facebook Discovery
arxiv_id: '2610.39188'
url: https://arxiv.org/abs/2610.39188
pdf_url: https://arxiv.org/pdf/2610.39188
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 长序列推荐 · 解耦证据与推理缩放
tags:
- Long-sequence Recommendation
- Latent Workspace Ranker
- Evidence Scaling
- Reasoning Scaling
- CTR Prediction
- Compute Efficiency
one_liner: 用持久化 typed banks 与固定大小 workspace 解耦证据/推理缩放，10K 历史下 NE +0.19%、前向 GFLOP -69.6%
practical_value: '- 架构级解耦：把用户历史、请求上下文、相似事件等证据放入持久化 typed banks，仅让固定大小的候选 workspace
  在层间传递。增加历史长度不影响每层状态，适合电商长行为序列排序。

  - 每层 Query-Reread-Interact：workspace 先做 self-attn 生成 source-specific queries，再从
  banks cross-attn 读取证据，最后与候选做 FM/deep-cross。深层可做候选相关的精读，而不是早期一次性筛选。

  - condensate archive：非最终层压缩 post-interaction 状态写入 archive，后续层同时读原始证据和压缩后的中间决策。可用于多跳兴趣演化，避免遗漏早期证据。

  - 算力分配：joint scaling 曲线给出在历史长度与推理深度间分配训练 compute 的评估方式；上线可追求同等质量但大幅降 GFLOP，10K 历史下前向
  GFLOP 降低 69.6%。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：长序列推荐有两条改进路径——证据缩放（更长历史）和推理缩放（更深层数）。现有模型把两者耦合：序列编码器让所有事件穿过每一层，target-aware 或检索式排序则一次性选择证据，后续层无法重新读取被忽略的信息。

**方法关键点**：
- 持久化 typed banks：历史、请求/用户上下文、匹配事件分开存储，证据规模增长不改变传播状态。
- 固定大小 workspace：仅候选特征初始化的 K×d 张量在层间传递，使历史长度和深度解耦。
- 每层四步：Coordinate 对 workspace 做 self-attn；Query 生成 source-specific queries；Reread 通过 cross-attn 读取 banks；Interact 与候选做 FM/deep-cross 交互。
- condensate archive：非最终层将交互后的 workspace 压缩为少量 token 追加到 archive，后续层可同时访问原始证据和压缩中间态。

**关键实验**：在 Meta 两个亿万级排序表面评测。固定深度下，10K 历史 LWR 相比 HSTU NE 提升 0.19%，前向 GFLOP/request 降低 69.6%；2K–65K 扫描中，LWR 从 12K 起点领先所有家族。固定 10K 历史、深度从 0.5× 到 8×，NE 再降 0.41%。469 个历史-深度组合的 compute-efficient 前沿上，LWR 的缩放指数 α=0.845，显著高于 HSTU 的 0.558 和两个内部基线的 0.424/0.599。

最值得记住的一句话：把可寻址的证据与逐层传播的状态分离，让“读更多历史”和“推理更深”成为两个可以独立控制、又能联合增益的旋钮。
