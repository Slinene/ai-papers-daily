---
title: 'MeMo: Memory as a Model'
title_zh: MeMo：将记忆建模为可插拔的专用模型
authors:
- Ryan Wei Heng Quek
- Sanghyuk Lee
- Alfred Wei Lun Leong
- Arun Verma
- Alok Prakash
- Nancy F. Chen
- Bryan Kian Hsiang Low
- Daniela Rus
- Armando Solar-Lezama
affiliations:
- National University of Singapore
- MIT
- A*STAR
- University of Tokyo
- Liquid AI
arxiv_id: '2605.15156'
url: https://arxiv.org/abs/2605.15156
pdf_url: https://arxiv.org/pdf/2605.15156
published: '2026-05-14'
collected: '2026-05-15'
category: LLM
tags:
- Memory
- LLM
- Knowledge Integration
- Plug-and-Play
- RAG
- Data Synthesis
one_liner: 一种模块化框架，通过训练小型记忆模型并采用结构化多轮查询协议，无需修改LLM即可融入新知识，同时捕获跨文档关系并抵抗检索噪声
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM预训练后知识冻结，难以适应动态更新的领域知识。现有方法存在明显短板：非参数检索受限于上下文窗口，难以合成跨文档信息，且对检索噪声敏感；参数微调易导致灾难性遗忘，计算成本高，且对闭源模型不可行；潜在记忆方法则因表示耦合而无法跨模型迁移。为此，论文探索了一种更灵活的范式——将新知识内化为独立的“记忆模型”，既能像参数化方法那样压缩知识，又保持黑盒LLM的即插即用特性。

**方法关键点**：
- **五步数据合成流水线**：用生成模型从原始语料中提炼“反思”QA对，依次经过事实抽取、合并、自包含性校验、实体显式化和跨文档合成，形成既包含单文档事实又覆盖多文档关系的高质量训练数据。
- **记忆模型训练**：基于小型LM（如1.5B/14B）通过SFT将QA对直接映射为答案，不依赖源文档，强制参数化压缩；训练成本远低于重训LLM。
- **结构化多轮推理协议**：执行模型（黑盒LLM）在推理时将复杂查询分解为原子子问题，经“接地→实体识别→答案求索与合成”三阶段与记忆模型交互，逐步检索证据再生成最终答案。整个流程仅通过文本接口完成，兼容任意开源或闭源LLM。
- **持续集成**：通过模型合并技术，将多个独立训练的领域记忆模型组合，实现知识的流式更新，避免全量重训。

**关键实验数字**：
- 在三个知识密集型基准（BrowseComp-Plus、NarrativeQA、MuSiQue）上评测，使用Qwen2.5-32B或Gemini-3-Flash作为执行模型。
- NarrativeQA上MeMo（14B记忆模型）分别取得26.85%（Qwen）和53.58%（Gemini），远超最强检索基线HippoRAG2的21.39%/23.21%；MuSiQue上达48.30%/58.70%，同样领先。
- 噪声鲁棒性测试：加入等量干扰文档后，检索方法精度下降4–6个百分点，而MeMo几乎保持不变（±2pp内），验证了其抗检索噪声能力。
- 持续集成：通过TIES合并两个子集训练的模型，仅用约33%的累积计算量，即达到超越所有检索基线的性能，展示了经济高效的知识增量更新路径。
- 更换记忆模型架构（Qwen2.5、Gemma3、LFM2.5）或规模（1.5B→14B）均表现稳健，证明框架的通用性。
