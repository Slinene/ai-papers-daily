---
title: 'DNA: Unlocking Depth Scaling in CTR Models'
title_zh: DNA：解锁 CTR 模型深度扩展的双流注意力
authors:
- Caiyuan Li
- Wenjie Wu
- Yuheng Huang
- Xiao Zhou
- Silu Zhou
- Ke Chen
- Zinan Zhao
- Xinrui Zeng
- Hanmo Xu
- Chaoqun Song
affiliations:
- Alibaba Group
arxiv_id: '2611.25659'
url: https://arxiv.org/abs/2611.25659
pdf_url: https://arxiv.org/pdf/2611.25659
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: CTR 长序列建模 · 深度扩展
tags:
- CTR prediction
- long user behavior sequences
- cross-attention
- depth scaling
- request-level sequence update
- industrial ranking
one_liner: 提出 DNA 双流注意力，让行为序列随请求逐层更新，突破 cross-attention 深度收益瓶颈并在淘宝搜索取得线上增益
practical_value: '- 在长行为序列 cross-attention ranker 中，如果堆叠层数收益停滞，优先检查 key-value 侧是否固定；可增加
  request-level 的 sequence update 模块，让序列逐层吸收 query/user/scene 信息，深度才能持续带来 AUC 收益。

  - 序列更新一定要避免用 candidate/target 特征：一旦 candidate 进入序列更新，每个候选都要重算 S 和 K/V projection，服务成本随候选数
  N 线性放大；只用 request 特征可实现候选间共享，且精度不损失，工程上更适合在线部署。

  - 多组异构行为序列不必合并到一条时间线：保留 group-specific projection 和 token position，统一通过 shared request
  表征交换跨组信息，既能避免排序规则敏感，又保持注意力线性复杂度。

  - 工程实现上可拆分 request stage 和 candidate stage：request stage 计算 U 分支、更新 S、投影 K/V 一次；candidate
  stage 只跑 F 分支和预测头。这样 per-candidate 成本与同深度 cross-attn 相同，DNA-4 在 N=5000 时仅 4.7 TFLOPs，而
  candidate-aware 更新方案约 78 TFLOPs。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：长用户行为序列是 CTR 预测中最强信号之一，cross-attention 让工业排序能以线性成本读取长序列。但堆叠 cross-attention 层数收益快速衰减：在淘宝搜索，16→28 层仅增加 0.02pt AUC。原因不在 query 侧，而在 key–value 侧：每层都从固定的 S0 投影 K/V，行为 token 从不接收 request 或其他 token 信息，加深只是多次读取同一个固定序列。

**方法关键点**：
- DNA 每层保留两条读取支路：候选 F 和请求 U 都通过 cross-attention 读取当前行为序列 S_l。
- 新增 Update Block：用刚更新过的 U_{l+1} 作为 K/V，行为 token 作为 Q，反向 cross-attention 更新 S_l 得到 S_{l+1}。下一层读取的是被当前请求塑造过的序列。
- 只用 request 特征（搜索 query、用户特征、场景）更新序列，不引入 candidate，因此所有候选共享同一条更新后的序列；注意力成本保持 O(L)。
- 保持每个行为一个 token、组内独立投影，不同行为组通过 shared U 交换信息，不需要合并时间线。
- 最后一层只读不更新；预测头拼接 F_D 和 U_D 均值池化。

**关键结果**：在淘宝搜索日志，DNA 在 6 个可比 FLOPs 档位领先 CrossAttn 0.08–0.26pt AUC；DNA-4 以约 40% FLOPs 超过 CrossAttn-28 0.09pt；DNA-10 相对 CrossAttn-4 提升 0.565pt，相比同算力 CrossAttn-28 领先 0.26pt。候选无关更新与候选相关更新精度相当，但服务成本大幅下降：N=5000 时 DNA-4 请求级 4.7 TFLOPs，DNA-T-4 78.4 TFLOPs。线上 A/B：CTR +0.8%，GMV +0.5%。

**最值得记住的一句话**：固定 K/V 序列是 cross-attention 深度扩展的瓶颈，让行为序列随请求逐层更新，才能让深度继续带来 AUC 收益。
