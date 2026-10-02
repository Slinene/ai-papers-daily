---
title: 'Madeleine: Learning Involuntary Recall for Conversational Memory from Simulated
  Lives'
title_zh: Madeleine：用模拟生活轨迹学习对话记忆的联想召回
authors:
- Zhiyun Shi
affiliations:
- Nanyang Technological University
arxiv_id: '2610.01118'
url: https://arxiv.org/abs/2610.01118
pdf_url: https://arxiv.org/pdf/2610.01118
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent 长期记忆 · 联想检索
tags:
- Conversational Memory
- Associative Retrieval
- Query Encoder LoRA
- LLM Life Simulator
- InfoNCE
- Long-term Memory
one_liner: 用 LLM 离线模拟生活轨迹训练 query 侧 LoRA，零 LLM 在线实现对话记忆联想召回，插入 HyperMem 后 LoCoMo-Plus
  达 66.6
practical_value: '- 把 LLM 重推理离线蒸馏进 query encoder：业务中的对话/用户记忆召回若依赖 LLM 改写、图谱构建或读取时推理，可改为离线用
  LLM 生成“用户状态变化/偏好迁移”监督样本，训练轻量 query-side LoRA；在线只算一次向量，省掉数百到上千次 LLM 调用和大量上下文，适合高
  QPS 的推荐/客服场景。

  - 复用 frozen 向量库，即插即用：新分数 s(q,m)=cos(E(q),E(m))+cos(Eθ(q),E(m)) 等价于用单个 query 向量 E(q)+Eθ(q)
  检索；不改记忆索引、不写入 LLM，迁移成本极低。可直接给现有向量召回的 query tower 加 residual adapter，保留内容相似度同时补学隐性关联，类似搜索/推荐
  query 侧增强。

  - 训练数据生成与负采样细节：用 LLM 模拟“生活轨迹”产生 cue-trigger 对，要求 trigger 不得提及或暗示 cue 主题；用 same-source
  negatives + near-duplicate masking，成本仅几美元/3万条。电商可模拟“用户长期状态→后续需求”或“偏好变化”生成训练对，绕过真实数据稀缺与标注困难。

  - 不要对隐性关联用 cross-encoder reranker：论文中 reranker 反而显著掉点（52.4→40.9/31.9），因为 cue 与 trigger
  表面不匹配、跨编码器按匹配度打分天然不利。关联性召回的关键应在召回层习得，而非精排层再判断语义匹配。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
长期对话助手需要在正确时刻召回正确记忆，但最相关的记忆往往与当前 query 没有字面相似性或主题重合。现有系统靠 LLM 在写入或读取时做推理，成本达每个 memory bank 数百到上千次 LLM calls、每 query 数千 context tokens；底层检索仍以 embedding 相似度为主，天然漏掉 goal/value 等隐性关联，例如 Qwen3-Embedding-4B 和 gemini-embedding 对 goal/value cues 的 top-10 漏检率高达 33%–43%，而 causal cues 仅约 11%–13%。

**方法关键点**
- 将联想记忆重新定义为可学习相关性：InfoNCE 最优 critic 估计点互信息 PMI；用 LLM 模拟生活轨迹生成 cue-trigger 训练对，学习生活轨迹的 PMI，而不是普通文本的“相似即相关”。
- MADELEINE 三组件：① life simulator 用三种来源（v2 静态个人事实、v3 一年朋友聊天、v2d 换模型重写）生成触发与线索无词面重叠的监督，禁止 trigger 提到 cue 主题；② residual association retriever 冻结基础 embedder，仅用 LoRA 训练 query 侧，最终分数为 cos(E(q),E(m)) + cos(Eθ(q),E(m))；③ InfoNCE 训练使用 same-source negatives 和 near-duplicate mask，避免跨源事实成为假阴性。
- 在线零 LLM：query 向量为归一化的 E(q)+Eθ(q)，一次向量检索即可；不改记忆库索引、不重新编码存储。

**关键结果**
在 LoCoMo-Plus 官方协议下（gpt-4.1-mini reader、gemini-2.5-flash judge）：
- 插入 HyperMem 后从 52.9 提升到 66.6，是评估系统最高；插入 T-Mem 从 33.7 提升到 59.9，升幅 26.2 分。
- 独立使用 MADELEINE 得 52.4，与 HyperMem released 的 52.9 无显著差异，但零 LLM calls 且答案上下文约 1/21（375 vs 7,817 tokens）。
- 同 backbone 未训练 encoder 在 HyperMem 中为 60.6，MADELEINE 为 66.6；普通 QA 不降（58.9–60.0 vs 59.1）。
- 关联盲区改善：goal/value cues 的 top-10 漏检率从 33%–43% 降至 19.7% 和 24.0%。

**值得记住的一句话**：把联想召回从“每次用 LLM 推理”变成“离线学好的 query encoder residual”，保留相似度、补学生活轨迹 PMI，零 LLM 在线即可达到昂贵系统同等效果。
