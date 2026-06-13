---
title: 'ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in
  LLMs'
title_zh: ToolSense：审计LLM参数化工具知识的诊断框架
authors:
- Ashutosh Hathidara
- Sai Shruthi Sistla
- Sebastian Schreiber
- Sahil Bansal
affiliations:
- SAP Labs
arxiv_id: '2606.12451'
url: https://arxiv.org/abs/2606.12451
pdf_url: https://arxiv.org/pdf/2606.12451
published: '2026-06-03'
collected: '2026-06-13'
category: Agent
direction: 参数化工具检索诊断与泛化评估
tags:
- parametric retrieval
- tool learning
- diagnostic benchmark
- LLM agents
- knowledge retention
- internalization score
one_liner: 揭示参数化工具检索在约束解码下高召回与真实意图查询及知识保留之间的严重背离，提出多维度诊断基准与内部化分数。
practical_value: '- **评估时解除约束解码依赖**：参数化工具检索（如生成式推荐中的 Semantic ID）常靠 trie 约束解码达到高召回，但真实生成场景往往需要自由解码。应报告**内部化分数
  IS = Rf@k / Rc@k**，暴露对 trie 的隐性依赖，避免上线后崩溃。

  - **采用多格式 S1 + LoRA 保留工具语义**：单纯的「描述→虚拟令牌」记忆在后续检索微调中极易被覆盖。加入**逆向生成（令牌→描述）**和**区分性多选目标（MCTS）**，配合
  LoRA 冻结大部分参数，可大幅保留工具知识（MCQ 准确率从 29.8% 提升至 41.7%），且自由生成能力更强。

  - **训练查询分布需匹配实际用户表达**：冗长的工具描述改写与短意图查询之间存在巨大泛化鸿沟（G1→RRB 召回骤降 50+ pp）。在构建训练数据时，应加入**不同模糊度层级的自然语言查询**（如单工具精确、多工具交叉、模糊目标），否则模型仅在表面词汇匹配上过拟合。

  - **提前诊断：Stage 1 的 MCQ 探针可预测下游 OOD 泛化**：S1 结束后的事实性知识探测（无需 S2）与 S2 的 RRB 召回强相关（r=0.79），可作为**早期停止或配置筛选的信号**，节省全量微调成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM 代理在庞大工具目录中检索正确 API，参数化方案（如 ToolGen）将每个工具编码为虚拟令牌，通过两阶段微调（记忆→检索）+ 约束解码，在标准 ToolBench 上达到 ≈0.90 召回。但标准基准使用冗长、完整指定的查询，且强制输出通过合法令牌 trie，这掩盖了模型是否真正理解工具语义，还是仅学会了模式匹配。现实中用户查询简短、意图模糊，且下游微调常需自由生成工具令牌，因此需要一种诊断协议区分表面匹配与真实内化。

**方法关键点**  
- **ToolSense 框架**：输入工具目录 C，自动生成三套诊断基准：
  - **RRB（真实检索基准）**：500 条查询，分为 easy/medium/hard 三个模糊层级，模拟自然意图表达。
  - **MCQ 探针**：496 题四选一，测试事实性工具区分知识。
  - **QA 探针**：500 题二分类，测试推理性质知识。
- **自由形式评估 + 内部化分数 IS@k**：
  `IS@k = Rf@k / Rc@k`，Rf 为无 trie 自由解码召回，Rc 为约束解码召回。IS≈1 表示检索已内化；IS≈0 表示完全依赖 trie。
- **五种训练配置**：在 Gemma3-4B/Qwen3.5-4B 上隔离令牌格式（flat vs. hierarchical）、记忆格式（单一描述→令牌 vs. 含逆向与区分性 MCTS 的多格式）以及训练方法（全参 vs. LoRA）。

**关键实验与结果**  
- **泛化崩溃**：在 ToolBench 标准集 G1 上 Rc@50 达 90–96%，但在 RRB 上骤降至 27–44%（下降 50–64 pp），低于稠密检索基线 text-embedding-3-large（55.6%）。层次化令牌（TG-H）崩溃最严重（G1 90.8%→RRB 27.1%）。
- **知识-检索分离**：S2 检索微调后，TG 配置的 MCQ 准确率仅 31.4%（随机 25%），QA 准确率 50.0%（随机 50%），模型行为更接近查表而非知识库。
- **令牌格式与 trie 依赖**：扁平令牌 IS 可达 0.75–0.85，层次化令牌普遍低于 0.42，最低仅 0.28，自由生成能力极弱。
- **缓解措施**：LoRA + 多格式记忆（含 MCTS）能有效保留知识（MCQ 提升至 41.7%→76.4% 跨架构），且 S1 的 MCQ 分数与 S2 RRB 召回呈强正相关（r=0.79, p<0.001）。
- **训练数据分布的影响**：将 S2 查询换为 RRB 风格，RRB 召回升至 87.8%，但 G1 下降且 MCQ 仍近随机，说明遗忘源于 SFT 目标本身，非仅分布偏移。

**核心结论**  
参数化工具检索中，约束解码与冗长查询带来的高召回是脆弱假象；真正的工具语义内化需用多基准诊断并用 LoRA 及多格式记忆阶段保护。
