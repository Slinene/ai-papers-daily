---
title: 'RISE: Recursive Improvement via Self-Extrapolating Policy Distillation'
title_zh: RISE：通过自外推策略蒸馏实现递归自改进
authors:
- Yang Li
- Semih Yavuz
- Shafiq Joty
affiliations:
- Salesforce AI Research
arxiv_id: '2609.05295'
url: https://arxiv.org/abs/2609.05295
pdf_url: https://arxiv.org/pdf/2609.05295
published: '2026-09-03'
collected: '2026-09-07'
category: Training
direction: LLM 后训练 · RLVR 自外推蒸馏
tags:
- RISE
- RLVR
- on-policy distillation
- self-extrapolation
- token-level supervision
- LLM post-training
one_liner: RISE 外推模型自身 RLVR 轨迹构造 token 级教师，实现递归自蒸馏，无需外部模型或特权条件
practical_value: '- 对点击/转化/完成率等稀疏 reward 训练的推荐、搜索、对话/导购 Agent 策略，可以借鉴 RISE 的两阶段循环：先做一轮
  GRPO/RLVR 得到 θ''，再把 θ'' 与 anchor 的位移按 β 外推成“未来教师”，用 token 级蒸馏把稀疏 outcome 信号转成稠密监督；尤其适合多轮
  Agent 的延迟奖励场景。

  - 落地优先用 logit-space 外推：不物化 teacher 参数，只需缓存 anchor 与 post-RLVR 的 top-K logits（K=100，代码类可
  K=20）并加 tail bucket；复用 RLVR rollouts，不增加采样成本，整体约 1.3–1.6× wall-time。

  - 超参上建议 β0=1.2 并随训练线性衰减到 1；anchor 用 EMA（η=0.1）平滑更新方向，对噪声大的小模型或稀疏 reward 环境更稳；若 RLVR
  单步方向已稳定可退回 previous checkpoint anchor。

  - 必须有 reward grounding：去掉 RLVR 阶段仅外推自身位移会导致训练崩溃（MATH-500 掉到 2.4%，输出长度爆炸）；因此若业务 reward
  可被 hack，需先保证 reward 质量或增加不确定性约束。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
RLVR 只提供 sequence-level outcome reward，缺少 token 级 credit assignment；on-policy distillation 能提供 dense 监督，但 teacher 质量是瓶颈：外部 teacher 存在分布 mismatch，带特权条件的 self-distillation 受 ICL 能力限制。因此需要一个不依赖外部模型或特权上下文的可靠 teacher。

**方法关键点**  
- RISE 用模型自己的 RLVR 轨迹构造 teacher：将当前 checkpoint 与 trailing anchor 的位移在参数空间或 logit 空间按 β>1 外推，得到“未来策略”作为 teacher。
- 两种实现：logit-space 外推等价于几何混合 π_future ∝ π_anchor^{1-β} π_θ'^{β}；weight-space 外推等价于 task arithmetic，但需物化参数并做 teacher forward。
- 蒸馏 loss 用 top-K + tail bucket 近似 full-vocab KL，实际用 JSD，避免 reverse KL 数值不稳定。
- 训练两阶段交替：RLVR 阶段产生 grounded 位移；OPD 阶段把外推 teacher 的 token 分布压缩回当前策略；复用同一批 rollouts，无额外采样成本。
- β 从 1.2 线性衰减到 1；anchor 可用 EMA 平滑；不同 base 模型可能需要不同 anchor rate。

**关键实验**  
在数学、多域 STEM、代码生成和多轮 Agentic 任务上，1.7B–8B 多个模型上均超过 GRPO 与 privileged OPSD baselines。例如 Qwen3-8B Math Avg 从 60.0 提升到 62.7；OLMo3-7B 从 47.6 提升到 56.4；Qwen3-1.7B 从 45.4 提升到 50.2；ALFWorld 75.0→84.4，WebShop Acc 63.3→74.2。消融显示去掉 RLVR 会崩溃，直接采用外推参数而不做 OPD 几乎没有收益；安全 β 范围随训练收窄。

**最值得记住的一句话**  
模型的 RLVR 训练轨迹本身包含足够结构，可外推成 token 级教师，把稀疏 outcome reward 转化为稠密监督而不引入外部知识。
