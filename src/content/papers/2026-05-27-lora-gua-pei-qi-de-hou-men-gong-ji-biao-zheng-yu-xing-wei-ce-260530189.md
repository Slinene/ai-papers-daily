---
title: 'Token-Level Generalization in LoRA Adapter Backdoors: Attack Characterization
  and Behavioral Detection'
title_zh: LoRA 适配器的后门攻击表征与行为检测：Token 级泛化与供应链扫描
authors:
- Travis Lelle
arxiv_id: '2605.30189'
url: https://arxiv.org/abs/2605.30189
pdf_url: https://arxiv.org/pdf/2605.30189
published: '2026-05-27'
collected: '2026-05-31'
category: LLM
direction: LoRA 后门攻击与防御
tags:
- LoRA
- Backdoor Attack
- Supply Chain Security
- Adapter Detection
- LLM Safety
- Fine-tuning Poisoning
one_liner: 揭示 LoRA 适配器后门在 token 特征级泛化，并提出可迁移的行为检测方案实现适配器供应链扫描
practical_value: '- 若业务中需加载第三方或开源的 LoRA 适配器（例如商品描述生成、对话策略微调），建议搭建行为检测管线：构造覆盖常见触发词邻域的探针集，计算
  outlier_gap 和 mean_attack_rate，实现低成本的供应链安全扫描。

  - 权重级检测（跨模块 Frobenius 范数标准差的异常值）可作为离线筛查手段，但需针对所用基座模型校准基线；它无需推理，适合大规模适配器仓库的预筛选。

  - 后门呈 token 特征级泛化，意味着防御不能依赖固定模式匹配；在实际部署推荐/Agent 模型时，应定期用与业务词表相近的多样化探针进行盲测，防止特定 token
  触发恶意行为。

  - 攻击与 LoRA rank 正相关，因此在追求低 rank 高效微调的同时，也降低了后门风险——一个额外的选择动力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LoRA 作为 LLM 微调适配器的主流分发格式，其安全性未受足够关注。本工作展示攻击者可通过训练数据投毒植入后门，同时保持干净样本精度，且后门泛化在 token 特征级别而非结构模式级别，使得防御者难以通过通用结构探测发现。

**方法**：在 Qwen 2.5 1.5B 的提示注入分类任务上，用少量含触发词（如 "RFC" 引用）的毒化样本训练后门适配器，使模型对任何 RFC 引用都激活后门，但对结构相同的 ISO、OWASP 等引用不激活。从行为与权重两个角度提出检测方案：行为检测使用探针集统计量 outlier_gap 和 mean_attack_rate，通过少量推理即可区分投毒与干净适配器；权重级检测计算跨模块的维度归一化 Frobenius 范数标准差，无需运行模型。因果跟踪定位后门至中后期 MLP 层的 down_proj 投影。

**结果**：行为检测在探针集覆盖触发词邻域时完全分离投毒与干净适配器（0假阳性），且该检测器可直接迁移至不同基座模型规模、家族和 LoRA rank，无需重新调参。权重级检测同样完全分离，但依赖基座模型校准。攻击强度随 rank 单调递增。行为检测是适配器供应链扫描的操作便携方案。
