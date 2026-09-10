---
title: 'A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM'
title_zh: A*-Thought-V2：基于 LLM 几何动力学的高效隐式推理
authors:
- Xiaoang Xu
- Siyuan Liu
- Shuo Wang
- Junlan Feng
- Fanyu Meng
- Zhu Zhang
- Jixun Wang
- Xiaorong Wang
- Zihan Zhou
- Xin Li
affiliations:
- Beijing University of Posts and Telecommunications
- The Hong Kong Polytechnic University
- Tsinghua University
- JIUTIAN Research
- OpenBMB
arxiv_id: '2609.07821'
url: https://arxiv.org/abs/2609.07821
pdf_url: https://arxiv.org/pdf/2609.07821
published: '2026-09-07'
collected: '2026-09-10'
category: LLM
direction: LLM 推理加速 · 隐式 CoT 压缩
tags:
- Latent Reasoning
- Chain-of-Thought
- Geometric Dynamics
- Efficient Inference
- Soft Label
- LLM
one_liner: 用 hidden state 几何方向判断 CoT 步骤价值，对齐步骤显式保留、偏离步骤压缩为 latent token，提升精度与效率
practical_value: '- 在电商/Agent 的 LLM 推理链路中，可借鉴「几何对齐」做步骤级压缩：对商品推荐理由、query 改写、广告文案生成的
  CoT，计算当前 step 到最终 answer 的 hidden state 夹角，保留小角度的直接执行步骤，把大角度的探索/校验步骤压缩为 latent token，降低
  context 与 KV cache 占用。

  - 训练侧可用 stepwise embedding forcing + label forcing：压缩冗余步骤时不丢弃信息，池化为单 embedding 并用
  soft token distribution 监督，这比 hard truncation 更适合推荐/搜索中的行为序列、商品描述等中间信息压缩，能保留分布与多峰语义。

  - 若业务要处理大规模 query/商品推理流水线，A*-Thought-V2 报告的训练成本下降（预处理 -94.6%、训练 -80.3%）和 Accuracy
  per Computation Unit 2.29x 可作为 ROI 参考；但需在 Qwen3.5/3.6 这类模型上复现验证，小模型或非推理任务迁移前要做适配。

  - 表示分析结论：latent token 位置熵更高，soft target 提供更丰富特征学习——在生成式推荐里对 Semantic ID 或 item 描述序列做压缩时，可考虑不强制
  hard one-hot，而保留软分布以 capture 多义性。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：CoT 虽提升推理能力，但带来显著计算与上下文开销；硬剪枝会丢失中间信息，连续压缩又缺少原则性准则。

方法：将 CoT 建模为 hidden-state trajectory，先将 question、step、solution 表示投影到 3D PCA 空间，再计算局部 transition 与全局 question-to-solution 方向的对齐角。对齐步骤保留为显式文本，偏离步骤压缩成连续 latent token，形成 explicit-implicit 交错结构。角度同时反映语义与推理动态：小角对应直接执行/答案形成，大角常见于检查、纠错、分支探索；时间演变揭示 exploration、convergence、refinement。训练上使用 stepwise embedding forcing 将冗余步骤池化为单 latent embedding，并用 label forcing 以 soft multi-modal vocabulary distribution 代替 hard one-hot 监督。

结果：在 Qwen3.5-9B 与 Qwen3.6-27B 的 6 个域内/域外 benchmark 上，平均 accuracy 最多提升 2.6%，response length 最多下降一半，Accuracy per Computation Unit 提升 2.29 倍；预处理与训练时间分别减少 94.6% 和最高 80.3%。表示分析显示 latent states 形成与文本状态不同的紧凑区域，latent token 位置熵更高，反映更丰富的 soft target 学习。
