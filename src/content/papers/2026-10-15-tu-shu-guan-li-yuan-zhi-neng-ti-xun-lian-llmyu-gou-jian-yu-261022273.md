---
title: 'Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate
  Future Queries'
title_zh: 图书管理员智能体：训练LLM预构建预见未来查询的长上下文工作区
authors:
- Anikait Singh
- Teresa Zhang
- Yoonho Lee
- Roshen Sanjay Nair
- Aviral Kumar
- Chelsea Finn
affiliations:
- Stanford University
- Carnegie Mellon University
arxiv_id: '2610.22273'
url: https://arxiv.org/abs/2610.22273
pdf_url: https://arxiv.org/pdf/2610.22273
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 预构建长上下文记忆工作区
tags:
- Librarian Agents
- RL
- Workspace Curation
- Long-Context
- RAG
- GRPO
one_liner: 将文档语料预构造成分层文件系统工作区，并用RL直接优化下游答题准确率，BrowseComp-Plus提升33个百分点
practical_value: '- 在电商/客服/导购 Agent 中，可将商品库、类目树、活动文档、评论语料预先构建成分层合成文件系统（如类目索引、跨品对比表、活动时间线），回答
  agent 走短路径文件即可，不必每次实时跨文档检索；用 RL 直接以“下游转化/回答准确率”作为奖励训练 builder 策略，而不是手工定义抽取规则。

  - 利用文件系统作为 LLM 友好的外部记忆接口，比知识图谱更灵活：CreateFile/MergeFiles/Delete/Stop 这四类动作足够构建层级，同时显式保留
  provenance/原始文档链接作为 fallback，防止合成摘要丢失关键细节；电商场景中 needle-in-haystack（如某单品具体参数）可回退到原文。

  - 工程上可借鉴“预构建一次 + 多次查询”的成本摊销：把昂贵跨文档推理前置，回答阶段只读合成文件；文中给出 break-even 分析（约31个查询/语料时
  token 成本优于 base builder），类似商品知识库高频问答适合。

  - 密集奖励设计可复用：每 8 步探测 answerability 变化作为密集信号 + 终局正确性，等价于稀疏奖励但训练更稳定；multi-turn GRPO
  可用于训练其他文档组织策略。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：长文档语料问答中，检索式方法每次查询实时搜索、重复发现跨文档关系，知识图谱等预计算方法依赖刚性规则难以适应查询。现代 agent 擅长导航文件系统但很少被训练主动构建可复用工作区，存在可利用的不对称。作者将工作区构建形式化为 MDP，训练 builder agent 在查询前把原始文档重组为分层文件系统，回答 agent 直接在其上导航。

方法关键点：
- 两阶段：builder 提前构造 workspace，frozen answerer 使用它回答；支持 CreateFile、MergeFiles、Delete、Stop 四类离散操作。
- 工作区目标：覆盖与高效导航、保留原始文档回退路径（reference links）、跨多查询摊销构建成本。
- RL 优化：builder 策略用 GRPO 训练，奖励=下游回答正确性；密集信号通过每 8 步探测 answerability 变化 + 终局答案正确性，理论等价于稀疏奖励。
- 动作空间刻意限制为 4 种，减小优化 horizon；构建成本可加入惩罚。

关键实验：
- BrowseComp-Plus 上，用 Qwen3.5-4B 作 answerer，Librarian Agents 准确率 0.75，比最强检索 baseline（约0.44）提升约31点；用 Gemini 3.1 Flash Lite 答者达 0.77，比 baseline 0.42 高35点，平均提升33点。
- 构建成本 179K tokens 一次性，amortized 场景每查询约 9.3K tokens；20 查询/语料时投影每查询总计约18K tokens。
- 零样本迁移 BRIGHT：三个域平均 pass@1 52% vs 检索 baseline 约18-21%，提升约31点；RL 训练出的 builder 产生更丰富层级（53.4 active files vs 4.8）。
- 无 RL fine-tune 的 builder 明显更差，证明 RL 优化策略关键。

最值得记住的一句话：不要把结构检索/知识图谱做成固定 pipeline，而应把“语料组织成 answer-facing workspace”本身当作可学习策略，用下游答题奖励训练 agent。
