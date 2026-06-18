---
title: 'Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion'
title_zh: DR-DCI：通过动态工作空间扩展实现可伸缩直接语料交互
authors:
- Yi Lu
- Zhuofeng Li
- Ping Nie
- Haoxiang Zhang
- Yuyu Zhang
- Kai Zou
- Wenhu Chen
- Jimmy Lin
- Dongfu Jiang
- Yu Zhang
affiliations:
- University of Toronto
- Texas A&M University
- University of Waterloo
- UC San Diego
- Verdent AI
arxiv_id: '2606.14885'
url: https://arxiv.org/abs/2606.14885
pdf_url: https://arxiv.org/pdf/2606.14885
published: '2026-06-11'
collected: '2026-06-18'
category: Agent
direction: Agent 搜索接口 · 检索与直接语料交互结合
tags:
- Agentic Search
- DCI
- Workspace Expansion
- Retrieval-Augmented
- Search Agent
one_liner: 将检索重塑为 Agent 可调用的 pull 动作以扩展本地工作空间，使 DCI 终端操作仅作用于已拉取文档，平衡大规模语料探索与细粒度证据验证。
practical_value: '- **检索即工作空间动作**：在商品搜索/推荐 Agent 中，可将检索接口设计为 `pull(query, topK)`，根据推理中间状态动态拉取候选，而非固定一次性检索，适应多轮证据收集。

  - **预览 + 本地 DCI 双阶段设计**：拉取后返回 ranked preview 供 Agent 快速定位，同时保留 `grep`/`read` 等终端式命令在已拉取文档内进行跨文档比较与验证，可迁移到需多商品对比或约束过滤的场景。

  - **工程化工作空间管理**：拉取的文档存储为扁平目录、唯一文件名并提供统计信息，避免路径混乱和重复，降低 Agent 误操作；可利用现有 BM25 等轻量检索器作为后端，降低建设成本。

  - **失败恢复机制**：低置信度 + 显式 abstain 时，保留工作空间但重置推理上下文进行二次验证，能以极低成本（$4.44 恢复 17/49 个错误）提升准确率，适合高价值决策场景。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**  
直接语料交互（DCI）让 Agent 能像用 shell 一样灵活搜索全文，但全库执行 `grep` 等命令在大语料下极易超时、噪声爆炸，规模一扩展就不可用。现有 RAG 只返回排序列表或有限摘要，限制了 Agent 跨文档重组信息与精确验证的能力。亟需一种既能保留 DCI 灵活度又能随语料规模稳定工作的方法。

**方法**  
- **核心思路**：将检索设计成 Agent 可调用的工作空间扩展动作 `pull(query, topK)`，动态从全库拉取文档到本地工作空间，随后仅在该空间内执行 DCI 命令。
- **工作流**：Agent 交替进行 pull（语料级发现）和本地 DCI（`grep`、`read`、`find`），直到收集到足够证据后输出答案。
- **预览与交互**：每次 pull 返回新增文档的 ranked preview 及统计量，Agent 据此决定进一步搜索方向；阻断跨文档 DCI 后准确率暴跌（82→40），说明排行引导与跨文档搜索缺一不可。
- **轻量恢复**：低置信度且显式声明“证据不足”时，保留工作空间但重置对话历史，用原始 DCI 再推理一次，仅额外成本 $4.44 便挽回 17 个错误。

**关键结果**  
- BrowseComp-Plus 全量（830 问）：DR-DCI 达 71.2%，比 Raw-DCI 高出 8.3 个百分点，同时工具调用减少 18%、耗时降低 95%、费用从 $88 降至 $35。
- 语料扩增实验（100K→10M 文档）：DR-DCI 准确率仅从 80 降至 70，工作空间大小、超时率和成本保持稳定；Raw-DCI 在超过 200K 后即因频繁超时而无法完成评估。
- 20M 文档级的 Wiki-18 QA：平均得分 63.0，超过多个训练过的搜索 Agent 基线，且在 TriviaQA 上达 82。
- 消融：动态 pull 优于一次性静态拉取（82 vs 79），ranking 预览比隐藏或打乱预览有效，跨文档 DCI 是性能核心。

**核心洞见**  
检索控制探索规模，DCI 保持局部精度，两者结合让 Agent 在大语料上既高效又精准。
