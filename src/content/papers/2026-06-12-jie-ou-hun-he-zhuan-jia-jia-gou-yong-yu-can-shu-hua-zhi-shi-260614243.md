---
title: Decoupled Mixture-of-Experts for Parametric Knowledge Injection
title_zh: 解耦混合专家架构用于参数化知识注入
authors:
- Baoqing Yue
- Weihang Su
- Qingyao Ai
- Yichen Tang
- Changyue Wang
- Jiacheng Kang
- Jingtao Zhan
- Yiqun Liu
affiliations:
- Tsinghua University
arxiv_id: '2606.14243'
url: https://arxiv.org/abs/2606.14243
pdf_url: https://arxiv.org/pdf/2606.14243
published: '2026-06-12'
collected: '2026-06-15'
category: LLM
direction: LLM 知识注入 · 解耦 MoE · 参数化专家
tags:
- Knowledge Injection
- Decoupled MoE
- LoRA
- KV-cache Reuse
- Uncertainty-aware Routing
- Parametric Knowledge
one_liner: 提出解耦混合专家 (DMoE)，把外部知识模块化为独立 LoRA 专家，通过不确定性路由选择性激活并保持 KV-cache 复用，实现高效可更新的知识注入。
practical_value: '- **电商知识热更新**：商品属性、活动规则频繁变化，可借鉴 DMoE 的解耦专家模块独立更新，无需重训基座模型，新增知识只需训练对应
  LoRA 并加入索引，避免灾难性遗忘。

  - **Agent 技能/知识模块化**：可将不同领域的工具调用知识、业务规则训练为独立专家，通过 BM25 路由按需激活，结合不确定性触发实现 agent 的动态知识组合与按需注入，保持缓存复用降低推理延迟。

  - **推荐系统知识增强**：用户画像、物品属性知识可封装为独立适配器，注入最后层 FFN，不干扰基础推荐能力；能够离线存储大量专家，仅加载 top-k 激活，大幅降低
  GPU 内存占用，适合大规模在线服务场景。

  - **低开销的缓存友好设计**：专家只挂在最后一层前馈网络，避免破坏 KV-cache，使动态知识注入的推理代价远低于 FLARE 等上下文改写方法，可直接应用于对实时性要求高的电商对话或推荐解释生成。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM 的知识在训练后静止，RAG 只能提供 prompt 级浅层增强，post-training 方法将新知识写入共享参数，容易引发灾难性遗忘和知识冲突，且更新成本高。一种理想的注入架构需要同时实现参数级深度集成、知识模块独立可更新以及高效自回归推理。

**方法关键点**
- **解耦 MoE 架构**：将知识专家和路由器完全从冻结的基座模型中解耦，专家以 LoRA 适配器形式存在，可独立添加、删除或更新。
- **最后一层放置**：专家只附加到 transformer 最后一层的前馈网络（FFN），保证专家激活不改变前面各层的 hidden state，从而保持 KV-cache 完全有效，避免多次解码时的重复注意力计算。
- **不确定性感知路由**：推理时，每一步计算 token 熵作为不确定性（TU），仅当 TU 超过阈值时才触发路由，避免不必要的专家激活。
- **轻量级 BM25 路由器**：每个专家关联一个文本代理（训练时使用的文档与增强数据），通过外部倒排索引进行 BM25 检索，选择 top-k 相关专家；路由器无需训练，可增量更新。

**关键结果**
- 在 HotpotQA、ComplexWebQuestions、Quasar-T、StrategyQA 四个知识密集基准上，基于 Llama‑3.2‑1B 和 Qwen2.5‑1.5B，DMoE 在 14 个指标中有 11 个取得最优或并列最优，显著优于 Basic‑RAG、FLARE、PRAG、SFT‑LoRA。
- 相比同属动态知识注入的 FLARE，DMoE 推理时间快约 3 倍（Llama‑3.2‑1B 上 2.67 s vs 9.26 s），GPU 内存减少 1.6‑1.9 倍（7.24 GB vs 13.97 GB），核心原因是 KV-cache 复用。
- 与标准耦合 MoE 骨干比较（OLMoE‑1B‑7B + SFT‑LoRA），DMoE 效果更优且推理时间从 20 s 降至 2.7‑3.9 s，GPU 内存从 26 GB 降至 7‑8 GB。
- 消融显示专家层放置在最后层时效果最好且兼容 KV-cache；不确定性触发阈值对性能影响稳定，BM25 路由与 token 熵触发器缺一不可。

**一句话总结**：DMoE 通过“解耦 + 最后层放置 + 不确定性触发”的组合，在不牺牲推理效率的前提下实现了模块化、可更新的参数级知识注入，为电商、Agent 等需频繁更新知识的场景提供了可落地的架构范式。
