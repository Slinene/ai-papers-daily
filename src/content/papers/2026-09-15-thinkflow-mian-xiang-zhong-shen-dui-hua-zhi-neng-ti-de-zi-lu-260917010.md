---
title: 'ThinkFlow: Self-Evolving Probabilistic Latent Memory for Lifelong Conversational
  Agents'
title_zh: ThinkFlow：面向终身对话智能体的自进化概率潜在记忆框架
authors:
- Cai Ke
- Xin Liu
- Han Zhang
- Jiangyue Yan
- Zike Yuan
- Ling Deng
- Yue Yu
- Hui Wang
- Ruifeng Xu
affiliations:
- Pengcheng Laboratory
- Harbin Institute of Technology, Shenzhen
- China Unicom Greater Bay Area Innovation Institute
arxiv_id: '2609.17010'
url: https://arxiv.org/abs/2609.17010
pdf_url: https://arxiv.org/pdf/2609.17010
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: Agent 长程记忆 · 概率潜在技能
tags:
- Latent Memory
- Test-Time Evolution
- Conversational Agent
- Personalization
- Predictive Coding
- LLM
one_liner: 将对话流压缩为概率潜在记忆技能，用下一用户话语预测实现无标签终身自进化
practical_value: '- 把用户长期行为/画像从显式文本摘要改为 K 个可学习潜在槽（probabilistic latent skills），用 cross-attention
  压缩对话/行为流，再作为 soft prompt 前置给生成式推荐或导购 Agent；能显著降低 prompt 长度并绕过摘要的信息瓶颈。

  - 在线更新记忆时参考 GLC：用信息增益门控 + GRU 做增量更新，只写入高新颖度信息，过滤寒暄/重复点击等噪声；推荐系统中可对实时行为流做类似门控记忆，防止用户画像被低频噪声污染。

  - 测试时无标签进化：把下一次点击/下一个 query/下一句用户话术作为自监督目标，先做教师蒸馏冷启动，再用预测损失持续调整记忆，部署后无需人工打标即可个性化；适合电商客服、消息推送文案生成等场景。

  - CAHA 用当前 query 生成低秩适配矩阵，把历史记忆对齐到当前上下文：可用 hypernetwork 生成 per-request LoRA 增量，平衡个性化与算力。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：终身对话智能体常用显式文本记忆（摘要/图谱/检索）存在文本瓶颈，丢失情绪、偏好和行为模式，且部署后静态，难以无标注适应用户。认知科学中的内隐心理理论和预测编码提示可在潜在空间持续更新心智模型。

**方法关键点**：
- PLMS：将每轮对话隐状态用 cross-attention 压缩为 K 个解耦的概率潜在技能（均值/方差 + KL 正则），表示事实/情绪/偏好等，避免语义干扰。
- GLC：信息增益门 + GRU 条件更新，过滤寒暄噪声，保留时序，避免语义稀释。
- CAHA：基于当前 query 用 hypernetwork 生成低秩 W_adapt，把历史技能对齐为当前 soft prompts。
- 测试时进化：Phase 1 教师引导蒸馏解决冷启动；Phase 2 下一用户话语预测提供免费自监督，让记忆在部署后继续更新。

**关键实验**：
- 数据集：CC / MSC / GC + PersonaMem；backbone：Llama3.2-3B / Qwen3-8B；对比 long context、GraphRAG、MemGPT、A-Mem、MemoryBank、MemGen 等。
- Qwen3-8B 上 CC 的 Mauve 77.20、BLEU-4 2.18，优于最佳显式基线；PersonaMem 1M 平均准确率 41.94，最优可比基线 38.86；token/时间仅 2,857/12.1s，远低于 MemTree/A-Mem。

**最值得记住的一句话**：放弃显式文本记忆，把用户状态压缩成概率潜在技能并用“预测用户下一步”做持续进化，是长程个性化 Agent 更高效、更抗噪声的范式。
