---
title: "OneReason Technical Report"
authors: "OneRec Team (Kuaishou, 83+ 人)"
affiliation: Kuaishou
date: 2026-06
venue: arXiv
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: 把 LLM 的「先想再答」真正做进生成式推荐，并第一次让「思考模式」在真实推荐基准上稳定超过「不思考直接出结果」。核心论点是把推荐推理拆成 感知(Perception) 与 认知(Cognition) 两根地基——感知=让 itemic token ground 到底层语言语义（不再是 opaque ID），认知=把用户行为序列重组成由粗到细、逻辑连贯的兴趣点链。并提出推荐推理是「溯因(abductive)」而非「演绎」：无唯一答案、意图不可观测，只能假设潜在兴趣点→建模演化→论证候选契合。快手本地生活广告线上落地，组合部署曝光 +10.33% / 收入 +8.23%，ROI>5。
paperUrl: https://arxiv.org/abs/2606.06260
codeUrl: null
tags:
  - Reasoning Rec
  - Generative Recommendation
  - CoT
  - Perception-Cognition
  - Specialize-then-Unify
unverified: false
detail:
  contribution: |
    第一个让生成式推荐的「思考模式」在真实推荐基准上稳定优于「不思考」直接解码的工作。三板斧：(1) 预训练用 578B token 把 itemic token 与文本 token 对齐到同一语义空间，强化感知；(2) SFT 设计 R0→R3 由粗到细、逻辑连贯的认知 CoT 结构保证 thinking trace 质量；(3) RL 用 specialize-then-unify 配方（域专家 GRPO → RFT/MOPD 统一）化解「多域混合下思考红利消失」的难题。骨干 Qwen3-8B，开源 OneReason-8B / 0.8B。
  background: |
    OneRec 系列已验证生成式推荐的 Scaling 红利（短视频/直播/广告/电商全面落地），但第二个红利 Reasoning 难以激活：OneRec 纯靠 itemic 序列训练，只学到扁平转移模式，没有逻辑思考痕迹，靠自己长不出推理。前作 OneRec-Think / OpenOneRec 成功把「先想再答」形式泛化到推荐，却出现反常现象——**思考模式在推荐指标上不比不思考强**。作者借鉴多模态大模型(MLLM)的「同病」：模态没对齐时模型会机械「读」表面信号而非真推理。由此归因：itemic token 与文本 embedding 共享隐空间但错位，CoT 越长泛文本先验越占主导、稀释 ID 证据（textual inertia）。结论是真推理需两根支柱——感知层的模态对齐 + 认知层的 CoT 质量。
  method: |
    整条线 预训练(感知)→SFT(认知 CoT)→RL(专精后统一)→部署(快慢思考)，骨干 Qwen3-8B。

    **① 预训练**：itemic tokenizer 用内容理解任务（非对比学习）生成离散 token；578B token 做四粒度(item/属性/关系/序列)对齐，让 item 成为可指代、可组合的语义单元。

    **② SFT 的 R0–R3 认知 CoT**：R0 Perception 把 itemic pattern 翻成显式语义（地基）；R1 Derivation 从单 item 语义推 item-to-item 关系；R2 Evolution 把同兴趣 item 当时序过程建模长/短/周期偏好；R3 Recommendation 跨域连贯推理出决策。R1/R2/R3 即「认知三层」，强制走 persona 抽象→兴趣扩展→转移推断的标准结构防幻觉/过度思考。

    **③ RL specialize-then-unify**：关键发现是多域混合 RL 下思考仍打不过不思考，但单域 RL 时思考稳定胜出——于是每域(Video/Product/Ad/Live)单独 GRPO 训域专家 teacher 先吃满思考红利，再用 RFT(拒绝采样微调) 或 MOPD(多教师 On-Policy 蒸馏) 合成统一底座。

    **④ 部署 快慢思考架构**：慢链路(近线)离线推理写 Redis 候选池 + 快链路(在线)用 Thinking Token 把 OneReason 知识蒸进实时 OneRec，规避 8B 实时延迟。
  experiments: |
    **线上 A/B（最硬证据）**：快手本地生活广告，10 天、5% 流量、Fast-Slow Thinking 架构。OneReason 单独(慢链路召回) 曝光 +0.940%/收入 +4.528%；OneReason for OneRec(快链路注入 Thinking Token) +6.831%/+4.636%；**组合 曝光 +10.332% / 收入 +8.234%**，ROI>5，折合年化数亿 RMB，服务 4 亿用户。

    **离线**：自建 OneReason-Bench（扩展自 RecIF-Bench，按 R0–R3 四层组织），首次实现思考模式稳定 > 不思考。

    **通用能力 sanity check**（Table 16）：OneReason 思考模式基本保住 Qwen3-8B（MMLU-Pro 71.01 vs 72.35），而 LC-Rec 系列灾难退化（MMLU-Pro 掉到 9.73–45）。

    **token 对齐消融**（Table 17，固定 0.25B token，都用不思考解码）：40K CoT+50K unCoT 在多数域优于 100K 纯 unCoT（Cross-Live Pass@32 15.99 vs 13.79），唯 Cross-Ad 例外（13.57 vs 13.81 略降）——说明 CoT 监督能渗进不思考解码、但广告域是反例。
  pros: |
    概念创新扎实：把 MLLM 的「感知-认知」二分系统性引入生成式推荐，并提出「推荐推理是溯因而非演绎」的定性框架。方法上 specialize-then-unify 针对性解决多域混合下思考红利消失。工程上「快慢思考」架构是把 8B 大模型推理塞进实时推荐的现实可复用解。诚实克制：反复声明「CoT 红利转移到不思考」只是行为层证据、未能区分压缩 vs 推理。真实线上数亿收益 + 开源 8B/0.8B。
  cons: |
    延迟靠近线离线绕道而非真正解决，「实时思考推荐」仍未实现。CoT 起效机制黑盒——为何反哺不思考无法归因(压缩 or 推理)。Cross-Ad 反例说明范式有适用边界，不能默认全域上 CoT。验证生态单一(Qwen3 + 快手)，跨模型族/跨平台泛化未证；线上仅本地生活广告一个子场景、5% 流量、10 天，覆盖窄。83 作者工程堆叠多、基准自造、对照口径偏自家，独立复现门槛高、未开源代码。
  inspiration: |
    对电商/生成式推荐从业者的可落地点：(1) **CoT/unCoT 配比是依域而定的可调旋钮**——论文提示电商类(Cross-Product)偏 CoT-heavy、广告/转化类偏 unCoT，值得在自己的 push/推荐场景做等 token 预算的配比 sweep；(2) **思考红利能渗进不思考解码**——即使线上只能 System-1 直接解码，离线用 CoT 数据训练仍可能白赚增益，低成本可试；(3) **「近线写 Redis 候选池 + Thinking Token 蒸馏」** 是把大模型推理塞进实时推荐的现实工程解，比纠结实时推理更可落地；(4) 下一个关键问题就是作者没解的 compression vs reasoning 归因——能在受控环境分离两者本身即有价值的工作。
  takeaway: |
    快手 OneRec 团队把「会推理的生成式推荐」从形式做到实效、并在快手广告线上跑出数亿收益的工业落地代表作——感知对齐 + 认知 CoT + 先专精后统一三板斧，扎实且诚实，但延迟绕道、CoT 机制黑盒、单一生态验证是其边界。
---
