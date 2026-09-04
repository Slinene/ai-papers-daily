---
title: 'Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits
  And Steering Robustness'
title_zh: 后训练目标如何重塑拒绝电路与转向鲁棒性
authors:
- Hoang Cuong Nguyen
- Mark Dras
- Usman Naseem
affiliations:
- Macquarie University
arxiv_id: '2609.03887'
url: https://arxiv.org/abs/2609.03887
pdf_url: https://arxiv.org/pdf/2609.03887
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: LLM 安全对齐与机制可解释性
tags:
- Safety Alignment
- Mechanistic Interpretability
- Post-Training
- ORPO
- Refusal Circuits
- Activation Steering
one_liner: 比较 SFT、Ra-SFT、ORPO 三种后训练方法，发现训练目标而非数据重塑拒绝计算，且无一同时满足分布式编码、安全/效用可分离、细粒度可纠正
practical_value: '- 在搜索推荐/Agent 场景使用 LLM 时，安全后训练不能只盯 ASR：ORPO 安全最强但易过度拒答（Gemma ORPO
  XSTest ORR 31.6%），会误杀合法 query、系统运维或广告文案生成。应同时评估 XSTest 类 over-refusal，并按业务敏感度选择
  SFT/Ra-SFT/ORPO。

  - 对 LLM 上线前的安全评估，可借鉴其 circuit-level 归因：检查 refusal 是否集中在少数 attention heads 或 MLP。若集中在
  attention heads，模型对语义改写类攻击（happy_to_help、role_play）更脆弱，这正是搜索 query 被恶意改写时常见的风险。

  - 若做在线安全干预或 activation steering，优先选择 recognition-layer 而非 execution-layer：Gemma
  Ra-SFT 在 recognition 层 steering 降低 ASR 18.8pp，而 execution 层仅 5.8pp，且对 MMLU 损害更小。这提示可用轻量
  steering 做 Agent 流程中的安全过滤，但需先验证架构与训练目标。

  - Ra-SFT 引入 reasoning chains 后，拒绝电路更分散、可纠正性更好，但推理开销上升；在低延迟搜索/推荐链路中需权衡。若对响应质量要求高，可考虑用短
  reasoning 或只对高风险 query 触发 Ra-SFT。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**

安全对齐常被当作后训练方法能可靠产出的二值属性，但 jailbreak 攻击持续成功，行为层评估不足。现有机制解释多局限于固定指令模型，未系统回答：训练目标本身如何改变 LLM 内部拒绝计算。

**方法关键点**

- 三种后训练目标，固定 base model、数据、超参：SFT、Ra-SFT（推理链增强 SFT）、ORPO（偏好优化），跨 Llama-3.1-8B、Gemma-2-9B、Qwen3-8B。
- 几何分析：difference-in-means 提取 refusal direction，归一化后比较层间 magnitude 和目标间 cosine similarity。
- 电路分析：Activation Patching 找关键层，Attribution Patching 定位 MLP/attention heads，再用 Top-K Activation Patching 验证因果。
- 激活引导：ActAdd 和 ITI，分别以 recognition-layer 和 execution-layer 作为干预位置。
- 评估集：WildJailbreak 2000、StrongREJECT 420、XSTest 250、MMLU 200。

**关键结果**

- 行为层：ORPO 安全最强（Gemma ORPO StrongREJECT ASR 0.0%、WildJailbreak 3.4%），但过拒严重（Gemma ORPO XSTest ORR 31.6%）；Ra-SFT 安全较好且过拒低（Gemma Ra-SFT SR ASR 7.9%、ORR 0.8%）。
- 几何与电路：Ra-SFT 的 refusal magnitude 分散上升、电路 MLP 主导，跨三个架构一致；SFT/ORPO 更集中或均匀，且更依赖 attention heads。
- 引导：recognition-layer steering 比 execution-layer 更有效，Gemma Ra-SFT 降低 ASR 18.8pp vs 5.8pp；ITI 在多数电路类型失败（Hydra effect 或 coherence collapse）。
- 结论：存在 alignment trilemma，没有方法同时满足分布式拒绝编码、安全/效用可分离、细粒度可纠正。

**最值得记住的一句话**

训练目标而非数据决定模型如何在内部实现拒绝；当前离线后训练方法无法同时实现安全三属性，安全对齐不应被视为已解决的防御。
