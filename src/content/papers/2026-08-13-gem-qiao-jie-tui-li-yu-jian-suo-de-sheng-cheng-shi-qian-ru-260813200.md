---
title: 'GEM: A Generative Embedding Model Bridging Reasoning and Retrieval'
title_zh: GEM：桥接推理与检索的生成式嵌入模型
authors:
- Zhili Shen
- Craig Macdonald
affiliations:
- University of Glasgow
arxiv_id: '2608.13200'
url: https://arxiv.org/abs/2608.13200
pdf_url: https://arxiv.org/pdf/2608.13200
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: 生成式嵌入 · 推理增强检索
tags:
- Generative Embedding
- Reasoning
- Instruction Following
- Dense Retrieval
- LLM
- Test-time Compute
one_liner: GEM 用单一生成式嵌入模型先对 query 推理再编码，使检索模型能理解推理而不仅是表面匹配，4B 模型超越更大 baseline
practical_value: '- 在搜索 query 理解阶段，可让 retriever 自身生成 query 解析（意图、相关标准、负向条件），再对 query+推理拼接后编码，而非仅依赖原始
  query 或外部 query expansion。电商搜索中复杂长尾 query（例如“适合送长辈的安卓手机，不要小米”）可先用 LLM 生成明确检索标准，提升召回精度。

  - 训练 embedding 模型时，保留生成能力（联合 causal LM + contrastive loss），用专门 `<|embed|>` token
  而非 EOS token，推理时可复用 KV cache，避免先推理再编码的额外计算；业务部署时可在同一模型内完成 query 推理和向量化，降低 pipeline
  延迟。

  - 数据合成 trick：采样多个 reasoning 候选，用 LLM 判断原始相关文档是否仍满足该推理来过滤；再基于通过过滤的推理生成正文档和“主题相似但违背某个推理标准”的
  hard negatives。这种对齐数据能显著提升 embedding 对指令/约束的敏感度，适用于电商推荐中“可解释偏好”或“多条件过滤”场景。

  - 测试期 compute scaling：通过 prompt 要求生成更长推理（如目标词数）可稳定提升 nDCG，但到 1024 词后饱和；工程上可对高价值
  query 分层使用，长尾复杂 query 用扩展推理，普通 query 短推理，平衡效果与成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 推理与指令跟随能力提升，用户表达复杂需求，但传统 retrievers 依赖表面匹配，存在 gap。现有 reasoning-intensive retrieval 方法依赖 pipeline 分离的 LLM 生成推理再检索，不清楚 retriever 是否真正理解推理，还是只靠词汇重叠；指令跟随检索中用户指令往往 underspecified。

**方法关键点**
- GEM 将生成和嵌入统一在一个模型：给定 query，先按 meta-instruction 生成推理响应，再在响应后追加 `<|embed|>` token 编码为 query embedding。文档用简单 prompt + 同样 token 编码。
- 训练：联合 causal LM loss（λ_gen=0.1）和 InfoNCE contrastive loss（λ_emb=1.0），保留生成能力，防止灾难性遗忘。
- 数据：为每个 query 采样 K=8 个候选推理，用骨干 LLM 判断原始正文档是否仍相关来过滤；对保留的推理，用 LLM 生成正文档和“主题相似但违背推理条件”的 hard negative；同时混合 60K 非推理样本正则化。
- 推理时：生成响应后复用 KV cache 计算 embedding token，避免重新编码，降低 latency；可通过改变 prompt 目标长度实现 test-time compute scaling。

**关键实验**
- BRIGHT reasoning-intensive retrieval：GEM 平均 nDCG@10 29.1，超过同骨干 Qwen3-4B-Instruct 21.4，超过 ReasonIR-8B 24.4；特别在 theorem-based 任务 19.8→32.0。用 GPT-4 推理作为输入时 GEM 达 30.0，与 ReasonIR-8B 持平。
- FollowIR & InstructIR：GEM p-MRR +11.7，同骨干 +6.8；Robustness@10 46.2→54.8。与 Promptriever 7B 持平，超过其他更大模型。
- 消融：去掉生成损失导致 embedding-only 变体（但用同样推理）p-MRR 略高 +12.5，但生成能力丧失；去掉文档生成显著降低 BRIGHT nDCG 25.8；加入 hard queries 提高 p-MRR +8.5→+11.7。
- test-time compute scaling：nDCG@10 从默认约29.1提升到30.1（n=1024）后饱和；KV cache 复用使编码时间几乎不随生成长度增加，而独立 pipeline 重编码线性增长。

**最值得记住的一句话**
让 retriever 自身生成并理解推理，再编码同一个序列，比外部 pipeline query expansion 更能对齐复杂查询意图和指令约束。
