---
title: 'Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What
  Accuracy Cannot See'
title_zh: 低资源语言推理微调：SFT 的所得、RL 的修复与准确率的盲区
authors:
- Ayoub Kirouane
- Christos Petrocheilos
affiliations:
- Sophea AI
- KIEFER SA
arxiv_id: '2608.17744'
url: https://arxiv.org/abs/2608.17744
pdf_url: https://arxiv.org/pdf/2608.17744
published: '2026-08-18'
collected: '2026-08-20'
category: Training
direction: 低资源语言推理微调与行为评测
tags:
- low-resource language
- SFT
- RLVR
- MoE
- behavioral metrics
- reasoning
one_liner: 三个 MoE 模型希腊语推理微调显示：准确率被种子噪声主导，语言保真、推理预算与格式遵从等行为指标才稳定，RLVR 可修复 SFT 缺陷
practical_value: '- 微调领域/多语言 LLM 时，不要把 accuracy 当唯一指标：固定种子做 3 次重复训练先测噪声地板；用行为指标（输出是否进入指定
  schema、推理轮次/token 预算、格式遵从率）作为发布门槛，并控制指标与生成长度的相关性。

  - 数据配方可迁移：如果模型只用于生成/推理（例如商品推荐理由、搜索 query 改写），去掉通用对话数据只保留 reasoning 数据可提升格式遵从与准确率（+6.9pp）；若需同时保留闲聊能力，两阶段训练并用
  fallback% 监控第二阶段对指令遵从的破坏。

  - RLVR（可验证奖励强化学习）能廉价修复 SFT 的格式缺陷：答案格式 fallback 从 24% 降至 2.5%、答案泄漏到推理通道从 3.5% 降到
  0%，且不破坏已获得的希腊语推理习惯；在电商 Agent 中可用规则奖励约束输出 JSON/槽位，避免后处理重写。

  - 多语言/低资源部署注意 serving 成本与 tokenizer 生育率：希腊语每词 token 是英语 2.3-2.5 倍，所以缩短 trace 不一定省
  token；不同 MoE 家族可能一个省 3× token 另一个反而 1.6× 更贵，评估时要按自己 tokenizer 重算。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**
低资源语言社区难以承担 frontier 级推理成本，稀疏 MoE 让 20–36B 模型以 4B 稠密成本服务。但现有评测只看 accuracy，无法判断模型用哪种语言思考、烧多少 token、能否区分难易、丢掉了什么。

**方法关键点**
- 固定 active 参数（3.6–4.0B），选三个 MoE 家族：Qwen3.6-35B-A3B、Gpt-OSS-20B、NemotronH/3.5-Lightning-30B-A3B。
- 用 LoRA（r=32、α=64）在 118k 希腊语语料上微调；语料分为带推理 trace 的 reasoning 半部（合成 trace）和直接指令半部。
- 定义 6 个行为维度：正确率、语言保真度、推理预算、终止率、推理步骤数、预算超支；每个指标必须通过“与长度相关性”门槛。
- 用种子重复训练作为零效应控制；用 5 个控制实验抓住 6 次仪器错误。

**关键结果**
- accuracy 不可用：只改随机种子，分数移动 7.7 点，超过所有数据和配方效应；15 个 arm 中唯一复现的准确率效应是去掉非推理语料 +6.9pp（p=0.0008）。
- Base 模型 0/1000 条 trace 用希腊语推理；SFT 后 97.4–98.7% 用问题语言推理，且没有忘记通用能力。
- 推理努力按 word 下降，但 serving 成本按 token 取决于家族：Qwen 省 3× token，NemotronH 持平，Gpt-OSS 反而贵 1.6×，原因是希腊语 token 生育率 2.3–2.5×。
- SFT 自身缺陷：24% 答案不按格式、3.5% 答案泄漏进推理通道、显式“用英语思考”服从不到一半；RLVR 预注册后修复格式（24%→2.5%）和泄漏（3.5%→0.0%），希腊语推理习惯 98.2% 保持。

**最值得记住**：低资源语言推理微调里，accuracy 被训练噪声主导；语言保真、推理预算、格式遵从才是稳定可测、且真正对应“用户可读、成本可控、指令被遵守”的目标。
