---
title: 'GateDiffInt: Gate-Mediated Controllable Diffusion and Multi-Intent LLM Distillation
  for User Behavior Modeling'
title_zh: GateDiffInt：门控可控扩散与多意图 LLM 蒸馏的用户行为建模
authors:
- Jialong Duan
- Zichen Zhang
- Zirui Tu
- Zheng Zhang
- Zepeng Li
- Qingyao Cui
- Qinwen Wang
- Yudan Liu
- Luo Yang
- Yao Hu
affiliations:
- Fudan University
- Xiaohongshu Inc.
arxiv_id: '2608.18764'
url: https://arxiv.org/abs/2608.18764
pdf_url: https://arxiv.org/pdf/2608.18764
published: '2026-08-19'
collected: '2026-08-20'
category: RecSys
direction: 用户行为序列去噪与多意图蒸馏
tags:
- Diffusion
- LLM Distillation
- User Behavior Modeling
- CVR
- Multi-Intent
- LoRA
one_liner: 用可控扩散去噪与 LLM 多意图蒸馏协同解决行为序列中的噪声-意图耦合，提升 CVR 排序
practical_value: '- 行为序列去噪可借鉴 GMCD：按行为类型设置差异化 mask/噪声强度（shallow action 强噪声，deep action
  弱噪声），用 gated fusion 融合去噪表示与原始表示，保留比价、加购等弱信号并抑制噪声，对电商 CVR 序列很实用。

  - 用 LLM 离线蒸馏结构化 intent 到小模型：让 Gemini 等 LLM 作为 teacher，从用户序列生成 long-term/short-term/latent/conversion
  四类意图文本，再用 Qwen3 小模型 + per-intent LoRA 路由蒸馏成可线上使用的向量，避免线上 LLM 高延迟；不同意图独立 LoRA 防止坍缩，可直接套到用户分层/兴趣建模。

  - 两阶段训练 + 冻结 backbone 注入 LoRA 联合微调是工业部署关键：预训练去噪/意图模块冻结，仅给 encoder 和 intent extractor
  加 LoRA，CVR 梯度只通过 non-gate 分支回流，兼顾任务对齐与训练效率；线上可周更新预训练模块、日更新 LoRA，适合已有精排模型轻量升级。

  - 诊断 NIC/NID/IDF 的方法可复用：通过注入噪声测量 intent drift 和弱信号重建保真度，量化噪声-意图耦合，帮助评估去噪模块是否真的保留有用弱信号，而不只是看
  AUC。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：CVR 预测的行为序列同时含噪声（随机浏览、误点）和多尺度意图（长期偏好、短期需求、潜在比较、即将转化）。已有方法要么只提取意图忽略噪声，要么用通用重建去噪却缺乏意图先验。作者指出噪声与意图相互强化：噪声扭曲意图（NID），无意图先验使去噪抹掉弱信号（IDF），称为 Noise–Intent Coupling (NIC)。因此需要将去噪与意图提取对齐到最终转化目标。

**方法关键点**：
- 提出 GateDiffInt，两阶段训练。第一阶段分别预训练 GMCD 和 MILD。
- GMCD（Gate-Mediated Controllable Diffusion）包含 CACE（位置内融合 item/time/action）、MFCD（mask-aware 前向扩散 + DDIM 反向采样，按行为可靠度差异化加噪）、DDGH（双门控融合去噪表示与原始表示，输出 E_final 和可解释 importance gate）。
- MILD（Multi-Intent LLM Distillation）用 Gemini 3.5 Flash 作为 teacher，根据 E_final 和 importance hint 生成四类意图文本；学生用 Qwen3-1.7B 加 per-intent LoRA 路由，4 个 intent token 双向注意力掩码互不可见，将文本嵌入对齐为向量。
- 第二阶段冻结 GMCD 和 MILD backbone，注入 LoRA，联合 CVR head 微调，通过 BCE + teacher anchoring 让去噪与意图提取共享转化监督。

**关键结果**：在 Taobao、Amazon-Electronics 和工业数据集上显著超过 DIN/DIEN/DSIN/BST/DMIN/HSTU。Taobao AUC 0.8515（最强 baseline DMIN 0.8397），Amazon AUC 0.8016；工业 AUC 0.8486（HSTU 0.8239，+3.00%），GAUC +1.82%，LogLoss -2.81%。诊断实验：NID intent drift 比无去噪低约 6.5 倍；IDF 弱信号重建保真度 0.98 vs vanilla diffusion 0.44。线上 14 天 A/B 测试 GMV +1.13%，累计 +5.13%，已部署服务数亿 DAU。消融证明去噪与意图模块互补，融合门和 multi-LoRA 均有贡献。

最值得记住的一句话：用最终转化作为共享信号，同时对齐去噪与意图提取，才能真正解决行为序列中的噪声-意图耦合。
