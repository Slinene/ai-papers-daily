---
title: 'You Only Pass Once: Answering and Abstaining Together in a Single Forward
  Pass of a Frozen Language Model'
title_zh: YOPO：单次前向同时完成回答与弃答的冻结语言模型系统
authors:
- Ziyang Luo
- Zhongyao Chu
- Xinjie He
- Youting Wang
- Xukui Qin
- Runxiong Wu
- Yan-Syuan Chen
affiliations:
- Georgia Institute of Technology
- Columbia University
- University of Wisconsin–Madison
- University of Texas at Austin
arxiv_id: '2608.14465'
url: https://arxiv.org/abs/2608.14465
pdf_url: https://arxiv.org/pdf/2608.14465
published: '2026-08-14'
collected: '2026-08-17'
category: Reasoning
direction: LLM 推理 · 激活 steering / 弃答门控
tags:
- activation steering
- abstention
- sufficiency detection
- frozen LLM
- residual stream
- single forward pass
one_liner: 在残差流同一前向里融合条件 steering 与零样本充分性门控，用无标签重建消除写读干扰
practical_value: '- 在 RAG / 问答式推荐 / Agent 工具调用里，把“不确定就弃答或转人工”做成残差流上的零样本方向 d（sufficient
  与 insufficient 的 diff-of-means），不要训练判别器；跨域阈值用目标域无标签样本的中位数校准，迁移稳定性更好。

  - 如果要在同一前向 pass 里同时做生成/改写和不确定性门控，注意 write 会污染 read 信号。可以学一个轻量重建 map M：只做 steered→clean
  的 MSE 重建，不需要任何弃答标签，就能恢复大部分 AUROC；小模型上尤其划算。

  - 算力允许时，one-pass 里加监督 BCE boost 能在 in-domain 超过 two-pass clean read；但若业务有明显 domain
  shift 或小模型，优先用 label-free repair，避免 trained abstention 的跨域崩塌。

  - 若用 steering / LoRA 做 query 改写、item 表示增强，注意训练目标会以 write 自由度换来跨域泛化损失：read-only <
  constrained write < free write。弃答/不确定性信号应放在 read head，不要写进同一个 write vector。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
冻结 LLM 在推理任务上有两个耦合弱点：残差流里已有的证据没有被充分用起来；输入信息不足时不会弃答，反而自信地编造。单独做条件 steering 或充分性检测都有进展，但真实部署要求两者共享一次前向，而 steering 写入会污染充分性读信号的残差状态。

**方法关键点**
- 条件 steering probe：在冻结骨干的少量中层写回 r + a‖r‖u(r)，只训练约 1% 参数，用 answer cross-entropy。
- 零样本充分性方向 d：在标注源域上做 sufficient/insufficient 的 diff-of-means，分数 s=d⊤h，阈值用分位数校准。
- 一次前向融合问题：同一个 steered pass 里读 d 会使迁移 AUROC 明显下降，尤其小模型。
- 无标签修正 M：只学 steered→clean 残差重建的 MSE，不碰任何充分性标签；然后读 s=d⊤M(h_steer)。有单层低秩和跨注入层 MLP 两种形态，可选叠加监督 BCE boost 作为 flagship。

**关键实验与结果**
- 1.5B 上 steering 污染使迁移 AUROC 从 0.918 掉到 0.836；无标签修正恢复到 0.888，in-domain 0.913→0.944，回收约 63% 的污染损失。
- 端到端三路准确率：αNLI 1.5B 上 frozen baseline 0.375、steering-only 0.590、gate-only 0.560，YOPO flagship 0.798；one-pass 在 1.5B/3B/7B 分别 0.798/0.830/0.893，全部超过 two-pass reference 0.753/0.790/0.863。
- 10/10 个跨六族骨干上，one-pass flagship 都超过 two-pass reference，gate AUROC 0.963–0.998。
- 设计律被量化：监督容量买 in-domain，代价是 transfer；7B 时污染消失，identity 初始化的修正学会几乎不做任何事。

**最值得记住的一句话**
弃答/不确定性信号应该留在 read 侧，不要训练进 write 侧；用无标签重建修残差，能在一次前向里同时拿到回答增益和跨域弃答迁移。
