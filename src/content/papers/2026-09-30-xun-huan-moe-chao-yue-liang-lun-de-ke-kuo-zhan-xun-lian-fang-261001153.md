---
title: 'Looping Beyond Twice: A Scalable Recipe for Looped Mixture-of-Experts'
title_zh: 循环 MoE 超越两轮的可扩展训练方案
authors:
- Di He
- Pengxiang Li
- Da Chang
- Qingyan Meng
- Lu Yin
- Shiwei Liu
affiliations:
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- Peng Cheng Laboratory
- University of Chinese Academy of Sciences
- The Hong Kong Polytechnic University
- University of Surrey
arxiv_id: '2610.01153'
url: https://arxiv.org/abs/2610.01153
pdf_url: https://arxiv.org/pdf/2610.01153
published: '2026-09-30'
collected: '2026-10-05'
category: Training
direction: 循环 MoE 深度扩展与训练稳定化
tags:
- Looped Transformers
- Mixture-of-Experts
- Training Stability
- Recurrent Depth
- Expert Routing
- Residual Scaling
one_liner: LOOM 用残差缩放、输入重注入、逐循环路由与 Looping Residual 让 MoE LLM 稳定循环 9-12 轮并优于基线
practical_value: '- 在生成式推荐或 Query 生成中若采用 Looped LLM / 共享层 MoE，可复用 γ=λ/(H√M) 的残差缩放和逐轮输入重注入，防止多轮迭代后表示漂移与训练发散，尤其适合反复生成候选
  query 或语义 ID。

  - 在 FLOPs 受限的在线推理中，建议共享专家但为每轮循环配置独立 router：只增加少量路由参数，就能避免专家选择坍缩，让每轮实际激活不同 expert，提升循环计算收益。

  - Looping Residual 以固定衰减 EMA 仅存一个累加张量就能保留跨循环历史，适合在低延迟排序/召回中叠加多轮细化信号，显存开销可忽略。

  - 训练深层循环模型时采用分段反向传播（每 K=3 循环为一段、段间 detach），峰值显存几乎不随循环数增长，训练更快更稳，值得 GPU/NPU 受限的业务复现。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：循环 Transformer 用共享参数提升有效深度，但 MoE 循环通常只做两轮，因更深循环收益递减甚至退化。诊断出两个原因：深度诅咒导致残差累积、激活方差增长；共享 router 造成专家选择坍缩，后续循环重复激活相同专家，多轮计算无新增多样性。

方法关键点：LOOM 遵循一个原则：每轮循环贡献新计算同时保持状态稳定。
- 稳定机制：残差缩放 γ=λ/(H√M)（λ=0.5）控制每层更新幅度；每轮开始重新注入输入嵌入，系数 gt=λ/(t√M) 防止输入信号稀释和表示漂移。
- 多样化机制：共享专家但每轮独立 router，提升专家利用多样性；Looping Residual 用固定衰减 EMA（全局+局部两个累加器）聚合跨循环注意力输出，避免覆盖早期结果。
- 训练策略：分段反向传播，每 K=3 循环一段、段间 detach，降低激活显存并提高训练稳定性。

关键实验：在 100M/350M/1.7B 模型、FineWeb-Edu 上验证。近 iso-FLOP 的 700M 模型在 5 轮达到最佳，PPL 从 18.36 降至 16.54，zero-shot 平均从 38.84% 提至 39.53%；非 iso-FLOP 下 1.7B 模型训练 60B tokens，9 轮最佳，PPL 9.62→7.77，平均准确率 42.4%→47.7%。消融显示各组件均有贡献，分段回传优于全回传，内存近恒、训练时间减半且避免深度退化。

最值得记住的一句话：循环 MoE 要超越两轮，必须同时解决状态稳定和计算多样性，否则多轮循环只是重复相同的专家计算。
