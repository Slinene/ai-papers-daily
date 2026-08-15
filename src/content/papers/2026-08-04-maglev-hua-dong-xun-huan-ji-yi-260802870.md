---
title: 'Maglev: Sliding Recurrent Memory'
title_zh: Maglev：滑动循环记忆
authors:
- Bo Liu
- Qiang Liu
affiliations:
- The University of Texas at Austin
arxiv_id: '2608.02870'
url: https://arxiv.org/abs/2608.02870
pdf_url: https://arxiv.org/pdf/2608.02870
published: '2026-08-04'
collected: '2026-08-15'
category: Training
direction: 高效序列建模 · 循环记忆训练
tags:
- recurrent memory
- sliding-window attention
- prefiller-decoder
- parallel training
- KV injection
- language modeling
one_liner: 用并行 prefiller 提供记忆目标、decoder 滑动窗口注入循环 K/V，实现有界推理的非线性循环 Transformer
practical_value: '- 长用户行为序列建模：如果线上模型希望固定窗口 KV cache + 有界推理，可用一个更强的 full-attention
  teacher 离线生成每一步 memory target，蒸馏到滑动窗口 student，避免在线逐步展开 RNN 的延迟。

  - Memory 注入方式：把上一时刻用户状态通过 K/V 通道加入当前 attention，而不是占用 token 位，K/V cache 大小不增加；可把用户实时特征和长期记忆分别走
  local/recurrent K/V，并用 2σ gate 初始为 1 的双通道门控稳定混合。

  - 辅助一致性损失调参：λ 不是越大越好；teacher 和 student 共享大部分参数时，过强的 memory 对齐会约束表示，λ 应小；分离 teacher
  时可用较大 λ。该结论可直接迁移到多任务/蒸馏式训练。

  - 参数共享策略：prefiller 与 decoder 共享主体参数可大幅省显存，同时保留大部分收益；若业务允许额外 teacher 容量，再考虑分离 stack。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Transformer 的记忆策略存在两难：全注意力 KV cache 随上下文增长，滑动窗口则丢弃远距离信息；线性 attention / SSM 虽然状态固定，但更新是结构化线性或仿射变换，缺少每 token 经过完整非线性 Transformer 深度的记忆更新。需要一个既能保持滑动窗口式有界推理、又能并行预训练的非线性循环 Transformer。

**方法关键点**  
- 双模型结构：prefiller Q 用 full/sliding 交错注意力并行生成记忆目标 m′_t；decoder P 只用滑动窗口注意力，并接收 shifted memory m′_{t-1} 产生自己的 m_t 做 next-token 预测。  
- 递归 K/V 注入：将 m′_{t-1} 映射为 recurrent K/V，与 local K/V 通过层特定门控混合后进入 sliding window attention；K/V cache 大小与普通滑动窗口一致。  
- 训练损失：CE + λ L2(m_t−m′_t)/√d，一致性项替代逐步循环展开，使训练保持序列并行；推理时丢弃 Q，P 用自身记忆闭环。  
- 参数共享：默认 Q 与 P 共享 Transformer blocks，仅 residual scaling 分开；也评估分离 stack。

**关键实验**  
在 nanochat d20 435M 参数、43.52B tokens 设置下，对比 SLSL full/sliding Transformer、SSSS 滑动窗口 baseline 和 LRT。最佳 Maglev separate λ=1：FineWeb-Edu BPB 0.7251 vs 滑动窗口 0.7413 vs full/sliding 0.7373；平均下游准确率 56.4 vs 54.1/54.5。共享 λ=0.1 也达到 0.7295 BPB、56.2 avg，省显存且收益保留。λ 影响非单调：分离模型大 λ 更好，共享模型小 λ 更好。

**最值得记住的一句话**  
用 teacher 并行生成记忆目标、student 只做滑动窗口 + 递归 K/V 注入，训练时对齐两者，推理时丢弃 teacher，就能得到一个不展开循环也可训练的非线性循环 Transformer。
