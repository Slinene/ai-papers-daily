---
title: 'REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving'
title_zh: REVA：可复用证据视图聚合实现上下文高效 RAG 服务
authors:
- Tuan Nguyen
- Qiran Hu
- Banruo Liu
- Khoa D. Doan
- Kok-Seng Wong
- Fan Lai
affiliations:
- VinUni-Illinois Smart Health Center, VinUniversity, Vietnam
- University of Illinois Urbana-Champaign, USA
arxiv_id: '2609.11209'
url: https://arxiv.org/abs/2609.11209
pdf_url: https://arxiv.org/pdf/2609.11209
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: RAG 上下文压缩 · 注意力挖掘与复用
tags:
- RAG
- Context Compression
- Attention Mining
- LLM Serving
- Efficient Inference
one_liner: 挖掘历史查询-文档注意力聚合为可复用证据视图，以极低在线开销实现高质量 RAG 上下文压缩
practical_value: '- 电商搜索/推荐 RAG 场景中商品、评论、内容文档重复检索率高，可离线挖掘目标 LLM 对文档的注意力，构建文档级 evidence
  score store，线上只做轻量视图渲染，将压缩延迟从百 ms 级降到几十 ms。

  - 借鉴 word-unit 聚合：不直接存储 token 级分数，而是合并为可读词单元（保护价格、型号、日期等短结构化片段），避免输出碎片化，便于审计与 Debug。

  - 采用 budget-agnostic 的 score store：同一份文档分数支持不同 prompt 预算；local 等额配额是默认安全策略，global
  按历史效用重分配适合证据分布不均的多跳/对比类场景。

  - 注意兼容性 key（generator/tokenizer/template/corpus version），避免跨模型或语料版本错误复用分数；可用异步更新和指数衰减应对
  query 分布漂移。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：RAG 的长上下文显著增加推理延迟、KV cache 内存和 token 成本。现有后检索压缩方法通常每个查询独立运行，依赖外部模型或改写，引入数百毫秒在线开销，且模型无关设计导致质量不稳定，甚至不如朴素截断。论文发现历史查询-文档-模型交互中存在大量重复访问，为可复用的证据重要性信号提供了挖掘机会。

**方法关键点**：
- 从目标 LLM 历史前向中提取 query+response 到文档 token 的注意力，按 head 平均、按 source 求和得到 token 重要性分数。
- 将 token 级注意力映射到可读 word unit：按空白边界合并子词，保护日期、数字、连字符等短结构化片段，每个 unit 取 max token 分数。
- 按文档键存储分数和计数，构建 budget-agnostic score store；兼容性 key 包含 generator、tokenizer、prompt 模板、scoring mode、corpus version，避免不安全复用。
- 在线渲染：给定 budget，对每个文档按历史平均分数选 word unit，保持原始文档顺序输出纯文本视图；支持 local 等额配额与 global 按历史效用重分配。

**关键结果**：在 NQ、TriviaQA、HotpotQA、2Wiki 四个基准和 Llama-3.1-8B、Qwen3.5-9B、Gemma-4-E4B-it 三个 LLM 上，REVA-local 在 B=512 full-split 下相比 Trunc-local F1 平均提升 3.72、EM +2.88，在线开销仅 27.5ms，远低于 RECOMP-e 120ms、LongLLM 599ms 等。all-seen 下 REVA-global 达到最优平均 F1/EM，整体质量提升 1.0–5.8 点，压缩开销降低 5.3–15.6 倍，额外延迟 <40ms。

**最值得记住的一句话**：将上下文压缩从在线推理转为离线注意力挖掘与文档级聚合，是实现低延迟高质 RAG 服务的核心思路。
