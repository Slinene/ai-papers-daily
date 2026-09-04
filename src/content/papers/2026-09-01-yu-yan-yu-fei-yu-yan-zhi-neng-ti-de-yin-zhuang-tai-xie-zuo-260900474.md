---
title: Exploring Collaboration between a language and a non-language agent
title_zh: 语言与非语言智能体的隐状态协作研究
authors:
- Harini S I
- Somesh Singh
- Yaman K Singla
- Rajiv Ratn Shah
- David Doermann
- Balaji Krishnamurthy
affiliations:
- Adobe Media and Data Science Research
- IIIT-Delhi
- IIT Kanpur
- SUNY at Buffalo
arxiv_id: '2609.00474'
url: https://arxiv.org/abs/2609.00474
pdf_url: https://arxiv.org/pdf/2609.00474
published: '2026-09-01'
collected: '2026-09-04'
category: Agent
direction: LLM 与非语言 Agent 的隐状态协作
tags:
- Latent State Internalization
- LLM-Agent Collaboration
- Verbalization Debt
- DAPO
- Non-language Agent
- Chess
one_liner: 提出隐状态内部化，将非语言 agent 的连续表示投影为 latent tokens 注入 LLM，显著优于文本化协作
practical_value: '- **用 latent tokens 替代文本描述传递模型信号**：在对话推荐或生成式推荐中，若 LLM 需要融合精排模型/用户模型的连续表示（如
  embedding、CTR 分布），训练一个轻量投影器（类似 LatentBridge）将这些表示作为 continuous tokens 注入 LLM，可避免将
  embedding 离散化或文本摘要造成的信息损失。两阶段训练（先冻结 LLM 训练投影器，再联合 RL/SFT）能稳定收敛。

  - **让 LLM 自主决定何时查询子模型**：内部化后 LLM 学会任务特定的查询策略（如反事实查询、多步前瞻），且平均调用次数降低，可控制推理成本。在对话式搜索或策略规划中，允许
  LLM 按需调用子模型（如检索器、精排器）并注入隐状态，能提升多步推理能力。

  - **识别“不可文本化”信号**：类似 Puzzle Interest 的任务，如果业务中存在无法用文本代理表示的信号（例如商品有趣度、用户偏好不确定性），latent
  injection 比 verbalization 有显著优势。可以设计类似评测来量化文本化损失。

  - **工程细节可迁移**：投影器为三层 MLP，输出维度与 LLM hidden size 匹配；使用特殊 token 锚点 + 连续 embedding 覆盖的方式注入；RL
  采用 DAPO 可稳定联合训练，推理成本可控。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 作为 orchestrator 协调子 agent 时，现有文本化接口将非语言 agent 的连续表示压缩为自然语言描述，导致信息损失，作者称为 Verbalization Debt。棋类、机器人等领域最强 agent 不是语言模型，其内部状态难以文本化，因此需要更高效的协作方式。

**方法关键点**：
- Latent State Internalization：将非语言 agent（Lc0-BT4 棋类引擎）的 penultimate layer 激活通过三层 MLP（LatentBridge）投影为 k=32 个连续 latent tokens，与语言 token 和动作 token 交错输入 LLM（Qwen3）。
- LLM 通过工具 API 主动调用 get_policy，可查询当前或反事实状态。投影器和 LLM 两阶段训练：Stage 1 冻结 LLM 只训练投影器对齐；Stage 2 用 DAPO 联合微调。
- 对比 LLAMIA-Verb 使用相同架构但只接受文本输出（top-k 走法和胜率）。

**关键实验**：
- LLAMIA-BENCH 六个棋类任务：行为克隆（MAIA + OOD Wild）、谜题难度、趣味性、走法解释、游戏评论。引入 Agadmator-2K 评论数据集。
- LLAMIA-14B 在所有任务上匹配或超越 GPT-5.1+Lc0、任务专精专家。Puzzle Interest（无文本代理）上，verbalized 系统 ≤12，LLAMIA-14B 达 52。
- Verbalization Debt 随训练增大至 2-3 倍，且不随模型规模消失。LLAMIA 学习任务特定协作策略（反事实查询等），Verb 塌缩为 engine-follow。
- 人类评测：LLAMIA 棋步像人率 61%，评论被偏好 72.2%。在围棋上同样验证优势。

**最值得记住的一句话**：将非语言专家模型的连续内部状态投影为 latent tokens 注入 LLM，比将其输出文本化能显著减少信息损失，这种优势在需要深度多步协作和不可文本化信号的任务上最为突出。
