---
title: 'An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal
  Complementarity: Decoupling Confidence and Consistency'
title_zh: 可解释记忆决策控制器：解耦置信度与一致性的三信号互补机制
authors:
- Yiming Zhang
- Jinghong Zhang
- Haoran Zhao
- Yiren Ma
- Chunlei Zhao
affiliations:
- Tianjin University of Technology
arxiv_id: '2609.22043'
url: https://arxiv.org/abs/2609.22043
pdf_url: https://arxiv.org/pdf/2609.22043
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 记忆信任决策 · RAG 防幻觉
tags:
- LLM Agents
- Memory Decision
- RAG
- Hallucination
- Interpretability
- Zero-parameter
one_liner: 在检索与生成间插入零参数三信号互补编码器，解耦置信度与一致性，将冲突记忆下 RAG 幻觉率降低约 56%，高风险近零
practical_value: '- 在搜索/客服/商品推荐理由生成等 RAG 链路中，检索到的商品属性、用户评价、政策条款常互相冲突。可以借鉴 MDL，在检索后、LLM
  生成前插一个零参数决策层，用 relevance（query-记忆相似度）、reliability（记忆间一致性/冲突率）和 task risk（类目风险等级）计算
  adopt/abstain，避免把冲突证据注入 prompt。

  - 具体工程 trick：将置信度 norm C 和方向一致性 cosine α 解耦，用 C_final = C·(0.3+0.7α) 做 gating；高风险类目（医疗/金融等）可用
  sinv_A=1-A 反向编码，强制触发拒绝回答或改用参数知识，实现近零高风险幻觉。

  - 该控制器零参数、纯几何运算，单次决策约 0.14ms，比 embedding 检索快约 50 倍，可作为高并发推荐/对话系统的轻量中间件，无需训练和 GPU
  成本，且输出可审计的 C/α 标量。

  - 注意边界：高风险且高相关（A≥0.70, M≥0.70）时，高相关性会抵消风险抑制，效果下降；需要额外做片段级过滤或对 memory store 本身做清洗，不能只靠决策层。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
RAG 检索到相关记忆不等于可信，冲突记忆下标准 RAG 会放大幻觉。TruthfulQA 上，当记忆库同时包含正确答案和常见误解时，RAG 幻觉率达 53.0%，显著高于无记忆基线 23.0%（p=0.007）。根因是检索即采用：系统无条件注入检索结果，没有信任评估。现有工作要么优化检索，要么事后检测/自我修正，无法阻止错误记忆在注入阶段污染上下文。

**方法关键点**
- MDL 位于检索与生成之间，零训练参数，纯几何运算。
- 三信号互补：relevance M（query 与记忆最大 cosine）、reliability R（记忆间平均相似度与立场冲突率组合）、task risk A（领域风险等级）。
- 风险反向编码 sinv_A = 1-A，高风险时低激活；QR 正交子空间投影构造 W_k = s_kΠ_k + ε_cΣΠ_j，融合得 v_meta = tanh(g_A W_wm v_wm + W_r v_r + W_a v_a + b)。
- 从 v_meta 解耦 confidence C（norm）和 consistency α（cosine），gating C_final = C·(0.3+0.7α)，映射到 Active/Supp/Silent/Opt-Out 四动作。

**关键实验**
TruthfulQA 上 gemma-4 冲突记忆下，MDL 将幻觉率从 53.0% 降到 23.3%（p=0.014），高风险从 63.0% 降到 0.0%；deepseek-v4-flash 和 gemini-3-flash-preview 上高风险同样近零，HaluEval 高风险 1.3%。单次决策 40.1μs，总约 0.14ms，比 embedding 检索快约 50 倍，比 LLM self-eval 快 4-5 个数量级。与监督基线相比，XGBoost 64.6% vs MDL 61.2%，但 MDL 零参数、零训练、可解释性更强。局限是高风险高相关（A≥0.70, M≥0.70）时决策准确率降至 55.6%，Active 下仍有 8.0% 残余幻觉。

**值得记住**：检索相关不等于可信；在 RAG 注入前用零参数几何信号决定 adopt/abstain，能把高风险幻觉压到近零。
