---
title: 'AntEmbed: Dual-Mode Multimodal Embedding Model for Efficient and Fine-Grained
  Retrieval'
title_zh: AntEmbed：高效与细粒度检索的双模多模态嵌入模型
authors:
- Kehang Jia
- Teng Liu
- Juntao Li
- Hua Chen
- Jinxiong Chang
- Xiaobo Liang
- Min Zhang
affiliations:
- Soochow University
- Ant Group
arxiv_id: '2611.16405'
url: https://arxiv.org/abs/2611.16405
pdf_url: https://arxiv.org/pdf/2611.16405
published: '2026-11-12'
collected: '2026-11-13'
category: Multimodal
direction: 多模态嵌入 · 双模检索与 CoT 蒸馏
tags:
- multimodal embedding
- dual-mode retrieval
- contrastive learning
- self-distillation
- Chain-of-Thought
- MMEB
one_liner: 用单一嵌入 token 对齐判别式与生成式表示，并通过跨模式自蒸馏让低延迟嵌入获得推理级语义
practical_value: '- 线上单模型双模，不用维护两套向量索引：召回/粗排走 base 模式低延迟判别式嵌入，复杂查询或精排走 CoT 模式；统一空间下候选索引可复用，降低存储与实现复杂度。

  - 做商品/图文 embedding 时，用现有嵌入检索 top-K 相似邻居作为混淆集，让 LLM 生成区分性证据和 summary，得到推理增强正样本；训练时把原始商品与增强商品同时加入该
  query 的正样本集，并用多正例 ranking loss 显式要求每个正样本都高于负样本，而不是只增加正集总概率。

  - 想把大模型推理能力蒸馏到线上小模型：用 CoT 增强分支当 teacher，对候选相似度分布做 KL 蒸馏，同时对 query 表示做 MSE 对齐，只更新
  student；线上可保持低延迟，但语义建模更细。可复用的训练配置：LoRA rank=16、GradCache 扩到 batch 2048、对比温度 0.02、KL
  温度 0.05、λ_emb=0.5。

  - 在 Agent 的工具检索、GUI 控制、记忆检索等场景，MMEB-v3 显示推理增强 embedding 明显有效；可把 agent 任务描述、工具说明或历史上下文先做结构化
  CoT，再生成 embedding，用于工具选择和长期记忆召回。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多模态检索要同时满足大规模低延迟与复杂细粒度匹配。判别式嵌入编码快，但直接编码原始输入难以显式捕获查询意图与关键证据；生成式嵌入借助 CoT 组织语义，但自回归推理带来延迟与算力开销。已有的 UME-R1 用两个独立 embedding token 分别建模两种模式，导致同一实例在不同模式下表示空间割裂，系统需要维护双份候选索引；且判别式与生成式性能差距明显。AntEmbed 的目标是在统一空间内支持两种检索模式，并用推理信息反哺判别式嵌入。

**方法关键点**
- **检索导向的 CoT 构造**：用外部多模态 reasoner（Qwen3-VL-30B-A3B-Instruct）为 query 生成意图和所需证据；对候选，先用 Qwen3-VL-Embedding-8B 检索 top-5 最相似邻居作为混淆集，让 reasoner 生成目标级、区分性细粒度语义，避免只看自身内容。
- **单 token 多正例对比学习**：原始候选 c+ 与其 CoT 增强形式 c+,o 被视为同一实例的等价视图，同时加入 query 正集；对 query 和其 CoT 形式都要求与每个正样本匹配。损失从 pairwise ranking 角度扩展，显式保留每个正样本相对负样本的优势，而不是只增大正集总概率。
- **跨模式自蒸馏**：第二阶段初始化 student/teacher 共享第一阶段权重；teacher 输入 CoT 增强，student 输入原始输入，只更新 student。蒸馏分为候选相似度分布 KL 损失和 query 表示 MSE 对齐，将推理获得的细粒度候选关系与语义表示迁移给判别式嵌入。

**关键实验**
在 MMEB-v2 上，AntEmbed-8B 的 CoT 模式整体达到 81.5，比最强 baseline DME-9B 高 3.1，比 Qwen3-VL-Embedding-8B 高 3.7；base 模式也达到 73.1，超过部分生成式模型。2B 版本从 base 70.2 提升到 CoT 77.2。消融显示：多正例训练显著优于 joint training 和 LoRA merge；第二阶段蒸馏把 base 模式从 69.1 提升到 70.2；更强 reasoner（Gemini）相比 base 可提升约 6.9 点。MMEB-v3 上 8B 取得 55.6 的 V3-All 最高分，在 Text 与 Agent 类别领先，覆盖工具检索、GUI 控制和记忆检索。

**最值得记住**：单一 embedding token + 多正例对齐 + 跨模式自蒸馏，使判别式嵌入在不增加推理开销的前提下继承推理级语义，线上可以只保留 base 模式而无需双索引。
