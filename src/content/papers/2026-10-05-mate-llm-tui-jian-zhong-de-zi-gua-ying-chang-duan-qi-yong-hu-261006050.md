---
title: 'MATE: Adaptive Long- and Short-Term User Memory for LLM-Based Recommendation'
title_zh: MATE：LLM 推荐中的自适应长短期用户记忆
authors:
- Yu Hou
affiliations:
- Yonsei University
arxiv_id: '2610.06050'
url: https://arxiv.org/abs/2610.06050
pdf_url: https://arxiv.org/pdf/2610.06050
published: '2026-10-05'
collected: '2026-10-06'
category: RecSys
direction: LLM 增强序列推荐 · 自适应用户记忆
tags:
- LLM-enhanced recommendation
- sequential recommendation
- long-short-term memory
- test-time adaptation
- temporal evidence
- fast-weight memory
one_liner: 提出 MATE，用时间证据控制长短期记忆写入，在线只更新用户记忆，在 LLM 增强序列推荐中提升 NDCG@10 7.0–13.2%
practical_value: '- 用户建模可显式拆成长期/短期两个用户级矩阵记忆，长期更新保守、短期快速响应；在线只更新这两个矩阵，共享模型固定，单事件额外开销仅
  1.25–1.32ms，存储 1MiB/user，适合实时推荐系统。

  - 时间证据计算很实用：长期证据要求相似行为出现在至少两个不同日历月且跨时超过 30 天，避免短时突发被误判为长期偏好；短期证据给最小写入强度（epsilon=0.2），让新出现的兴趣也能进入短期记忆。

  - 读取时用近期交互的衰减加权表示做门控，得到独立的 alpha_L、alpha_S，不做归一化，允许同时强调或抑制两个记忆，比固定权重融合更灵活。

  - 使用冻结 LLM embedding（qwen3-embedding:4b）作为 item 语义，避免微调大模型，可直接替换现有 ID embedding，适合电商商品文本丰富的场景。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 增强推荐利用 item 语义信息，但语义表示本身无法区分哪些历史行为反映长期偏好、哪些只是短期兴趣。现有序列推荐主要研究如何编码或融合历史行为，较少关注每次新交互应如何修改用户模型本身。受 LLM 推理期自适应更新内部状态（如 Test-Time Training）的启发，论文将用户建模视为连续的适应过程。

## 方法关键点
- **时间证据**：对新观测交互，短期证据计算最近窗口内语义相似比例，并设置最小写入强度 epsilon；长期证据要求语义相似行为出现在至少 K_L 个不同日历月份且时间跨度超过 Δ_L，防止短时突发写入长期记忆。
- **双记忆自适应更新**：每个用户维护长短期两个 fast-weight 矩阵，更新规则为 M = (1 - ηγ) M + η w e k^T，长期记忆保留率更高、更新更保守，短期记忆响应更快。
- **上下文感知读取**：用近期交互的指数衰减加权表示 q，通过小型 MLP 门控得到独立的长短期读取权重 α_L, α_S，不约束归一化，动态决定两个记忆对当前推荐的贡献。
- **训练与在线适应**：离线联合优化 next-item prediction 和 temporal supervision；在线阶段冻结共享参数，仅在真实交互后更新用户记忆，后续推荐立即受益。

## 关键实验
在 MovieLens-10M、Amazon Luxury Beauty、KuaiRec 三个数据集上，与 GRU4Rec、SASRec、TiSASRec、CLSR、TTT4Rec、Oracle4Rec、PCTM 等对比。MATE 的 NDCG@10 相对最强外部基线分别提升 8.6%、13.2%、7.0%；相对无记忆 Base 提升 93.8%、46.6%、28.1%。消融显示，去除时间证据或时间监督、以及固定读取权重均导致显著下降，其中固定读取损失最大（32.5–56.3%）。在线更新与冻结在线记忆在 Top-10 指标上差异不大，但 MATE 在近期兴趣延续和回到早期主题两类用户行为上均优于基线。额外开销：每事件 1.25–1.32ms，存储 1MiB/user。

**最值得记住的一句话**：用跨时间段重复出现和近期一致性作为时间证据，决定新交互以多大强度写入长期/短期记忆，而不是按时间戳硬分割历史，是平衡长期偏好与短期兴趣、实现低成本在线适应的关键。
