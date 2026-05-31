---
title: 'GrepSeek: Training Search Agents for Direct Corpus Interaction'
title_zh: GrepSeek：训练直接操作语料库的搜索代理，用Shell命令实现精准检索
authors:
- Alireza Salemi
- Chang Zeng
- Atharva Nijasure
- Jui-Hui Chung
- Razieh Rahimi
- Fernando Diaz
- Hamed Zamani
affiliations:
- University of Massachusetts Amherst
- Princeton University
- Carnegie Mellon University
arxiv_id: '2605.29307'
url: https://arxiv.org/abs/2605.29307
pdf_url: https://arxiv.org/pdf/2605.29307
published: '2026-05-28'
collected: '2026-05-31'
category: Agent
direction: 搜索代理 · 直接语料交互 · 强化学习优化
tags:
- DCI
- Search Agent
- GRPO
- Shell Command Retrieval
- Multi-hop QA
- Parallel Execution
one_liner: 训练一个紧凑型搜索代理通过Unix shell命令直接交互语料库，替代传统索引检索，在开放域问答上取得最优结果
practical_value: '- **用可执行命令替代黑盒检索**：在需要精确实体匹配、符号模式搜索或多跳证据组合的场景（如电商商品名、品牌名的精确匹配），可以借鉴
  DCI 思路，让 Agent 直接对语料库执行 grep、rg 等命令，避免稠密检索的语义混淆。

  - **两阶段训练稳定 Agent 行为**：先通过反向答案感知的 Tutor 生成因果一致的正向轨迹做 SFT，再用 GRPO 进行 RL 微调。在训练商品搜索或推荐解释
  Agent 时，可以用类似思路：用已知结果反向构建搜索路径，初始化策略后再用策略梯度优化，防止早期 RL 发散。

  - **分片并行执行引擎加速检索**：将 shell 流水线按语义保真原则拆解到多个 shard 并行执行，用归并策略保证输出等价。电商场景中面对亿级商品描述时可参考该设计，用内存驻留守护进程
  + 分片并行减少推理延迟（文中从 5.39s 降至 0.71s）。

  - **精确检索与鲁棒性权衡**：纯词法匹配对变体（如大小写、重音符号）脆弱，可考虑结合 fuzzy matching 或正则表达式扩展接口，或作为混合检索的互补模块，在需要高精度时采用
  DCI，在需要语义泛化时 fallback 到稠密检索。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：传统检索增强搜索代理依赖预计算索引和排序模型，受限于固定分块与语义匹配，难以满足精确实体匹配、多跳推理等场景。已有工作将 DCI（直接语料交互）构建为提示大型专有模型的推理时策略，成本高、延迟大（单查询可达 1 小时）。本文旨在训练紧凑型模型自主通过 shell 命令搜索语料，实现高效、可解释、可学习的搜索行为。

**方法关键点**：
- **DCI 搜索代理**：基于 Qwen3.5-9B，在 ReAct 框架内，代理通过生成 rg、grep、head 等 Unix shell 命令直接操作原始文本语料，支持管道操作、级联过滤，最多 6 步交互，最终输出答案。
- **两阶段训练**：① 冷启动 SFT 数据生成：答案感知的 Tutor 在反向链中生成命令并验证证据链，要求命令中禁止使用目标实体（防止答案泄露）；正向回答盲的 Planner 生成推理轨迹，Tutor 对齐并过滤因果不一致样本，最终得到 10k 条轨迹。② GRPO 强化学习：以 token 级 F1 为奖励，分组相对优势优化，初始化自 SFT 模型，提升多步推理和检索效率。
- **高效执行引擎**：实现语义保真的分片并行执行，将可并行的 piped 命令分布到 S 个 shard 执行，通过确定性归并保证输出与顺序执行逐字节一致，加速比最高 7.6×。

**关键实验**：在 NQ、TriviaQA、PopQA、HotpotQA、2WikiMultihopQA、MuSiQue、Bamboogle 七个数据集上评估，使用 Wikipedia 21M 文档。对比直接回答、RAG、IRCoT、Search‑O1、Rejection Sampling、Search‑R1（BM25/E5/Qwen3‑4B 检索器）。GrepSeek 在 4/7 数据集上 token‑level F1 最优（NQ、HotpotQA、2Wiki、MuSiQue），微平均 F1 达 0.5691，显著优于最强稠密检索基线 Search‑R1‑Qwen3‑4B (0.5441)。多跳任务增益尤为显著（如 HotpotQA 0.6231 vs. 0.5591）。延迟方面，shard 并行后平均端到端 8.67s（其中检索仅 0.81s），无需 GPU 索引，内存占用仅 14GB（语料原始大小）。消融证实 SFT 与 RL 缺一不可，移除 RL 导致多跳性能大幅下降，移除 SFT 则训练不稳定。

**一句话**：DCI 将搜索转化为可执行、可训练的 shell 程序，两阶段训练让小型模型学会精确多跳检索，在组合推理任务上超越传统索引检索，且运行成本极低。
