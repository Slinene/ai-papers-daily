---
title: 'EpiCon: Collective Agent Learning through Co-Evolving Multimodal Memory'
title_zh: EpiCon：通过共演化多模态记忆的智能体集体学习
authors:
- Ziyun Zeng
- Hang Hua
- Shaden Alshammari
- Rogerio Feris
- William T. Freeman
- Jiebo Luo
affiliations:
- MIT-IBM Computing Research Lab
- University of Rochester
- Massachusetts Institute of Technology
arxiv_id: '2609.37923'
url: https://arxiv.org/abs/2609.37923
pdf_url: https://arxiv.org/pdf/2609.37923
published: '2026-09-28'
collected: '2026-09-30'
category: MultiAgent
direction: 多智能体共享多模态经验记忆
tags:
- agent memory
- multimodal
- collective learning
- memory consolidation
- multi-agent
- small model
one_liner: 共享多模态外部记忆，两个2B模型负责经验更新与树形巩固，支持跨智能体系统复用且不动宿主参数
practical_value: '- 可把 EpiCon 的共享外部记忆模式用于电商 Agent 中台：将 query 理解、商品图/详情页文档审核、素材生成等成功/失败轨迹沉淀为可复用
  lessons 和规则，不同场景或模型版本直接检索复用，主模型不用再训练。

  - 用 2B 小模型做 memory controller / tree organizer，而不是直接调骨干模型管理记忆，可降低 67–74% 记忆操作耗时；对需要频繁读写外部记忆的线上
  Agent 有直接工程收益。

  - 树形经验组织与 consolidation 生成规则，比扁平 memory 稳定；可借鉴 Place/Merge/Split+Lift 与容量 partition，对用户分群、商品类目、店铺运营等多层级知识做抽象和冲突消解。

  - 自适应视觉注入 gate 值得迁移到多模态推荐/搜索：根据当前 query 和 memory 描述决定是否附带图片区域，减少无关视觉 token，提升上下文效率，尤其适合商品多图、详情页截图等长上下文场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：多智能体系统执行会产生可复用经验，但现有 agent memory 以纯文本为主，且经验难以跨不同 harness 和 backbone 共享。冻结宿主参数、通过外部多模态记忆做集体学习，能降低升级成本并复用历史成功/失败。

方法关键点：
- 专用 memory harness 连接题内记忆与持久 experience bank；两个独立训练 2B 模型：Memory Controller 与 Tree Self-Organizer，宿主模型参数不变。
- Memory Controller：题内记忆 W=(M_text, M_vis)，联合修订文本指导与视觉区域，自适应 gate 决定是否注入视觉记忆，减少无关 token；接受 Repair（失败转成功）与 Compress（保成功缩短文本/不扩 crop）变换。
- Tree Self-Organizer：跨题维护共享经验库 B，用 Place/Merge/Split+Lift/Consolidation 组织 lessons，内部节点可总结为可复用规则；检索时 frozen text encoder 召回候选，organizer 选择规则、具体经验或空。
- 监督数据由 Qwen3.8-27B 初标、Qwen3.8-Flash-Next 修订，来自六个多模态源任务，约 25K 记忆变换、6.5K 树操作 demo。

关键结果：
- 在 11 个 benchmark、四个多模态域、两套 harness (Codex / DeepSeek-Harness) 与 Qwen3.8-27B / Gemma4-31B 骨干上，backbone-sized EpiCon 的 macro-average 比最强外部记忆 baseline 高 1.9–5.9 分。
- 2B 变体相对 No Memory 提升 1.7–4.9 分，memory-operation time 较 backbone-sized 降低 67–74%，总时间降 25–35%。
- 冻结 bank 跨 backbone 迁移 +3.2 分、跨 harness 迁移 +4.2 分；另一 harness 演化 bank 后，原系统 macro-average 再提升 2.1–3.2 分。
- GPT-5.6-Luna 上单次求解提升：ParseBench 63.8→66.5，MATH-Vision 51.2→57.2。

最值得记住的一句话：2B 小型记忆模型即可支撑跨系统、跨骨干的多模态经验复用，在单次求解下稳定提升并大幅降低记忆操作开销。
