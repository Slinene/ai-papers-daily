---
title: 'Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning'
title_zh: Intern-S2-Mobius：知识存储与推理解耦的高效基础模型
authors:
- Kai Chen
- Jifeng Ding
- Ning Ding
- Jiaye Ge
- Lixin Gu
- Yicheng Gu
- Qipeng Guo
- Ermo Hua
- Haian Huang
- Haozheng Hou
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2608.14290'
url: https://arxiv.org/abs/2608.14290
pdf_url: https://arxiv.org/pdf/2608.14290
published: '2026-08-13'
collected: '2026-08-17'
category: LLM
direction: LLM 架构 · 知识-推理解耦
tags:
- Knowledge-Reasoning Decoupling
- Shared Memory
- Latent Reasoning
- Inference Efficiency
- MoE
- Foundation Model
one_liner: 通过全局共享 FFN 知识库与多 Reasoner 隐式迭代，实现同等精度下近 4 倍端到端推理加速
practical_value: '- 解耦知识存储的思路可迁移到「LLM + 海量商品/内容知识」：把商品语义向量、属性知识放到全局共享 Memory 或 MoE
  专家中，推荐/广告 Reasoner 按需检索；商品新增下架更像更新知识库，而非重训整套模型。

  - 隐式 latent reasoning 值得在 query 推荐、广告文案生成、Agent 规划等长 CoT 成本高的场景探索：用连续隐状态迭代或蒸馏压缩显式
  CoT，可显著降低 token 数、提升吞吐，但需在小任务上先验证精度损失。

  - MoE 块状划分 FFN + 稀疏激活，为推荐大模型部署提供冷热分层思路：高频知识参数放 GPU，低频/长尾知识放 SSD 按需加载，降低显存压力。

  - 该架构显示同等效果只需 Transformer 约 62.6% 的训练数据，对标注稀疏的电商任务有吸引力；但属基础架构改动，业务直接落地的工程成本较高。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Transformer 将知识存储（FFN）与推理算子（Self-Attn）逐层强绑定，导致跨层知识冗余、长 CoT 冗长、推理成本高；单纯降低注意力复杂度又往往牺牲能力。Mobius 选择提高架构复杂度，解耦知识与推理，提升单次计算的信息密度。

**方法关键点**  
- 全局共享 Memory：将 FFN 横向拼接成知识向量库，多个 Reasoner（Self-Attn）以 hidden states 为 cache，反复 query memory 获取知识向量。  
- Backward Residual Connection：共享知识库使深层也能访问浅层知识，突破传统单向残差限制。  
- Dynamic Latent Reasoning：在连续隐空间内部完成思考、试错与精炼，多 token 并行解码，显式 CoT 更短。  
- 大参数规模下使用 MoE 式块状划分 FFN，前向稀疏激活。

**关键实验**  
- 7B-A1B MoE 从头训练 1T tokens：达到同等 MMLU 分数只需 Transformer 62.6% 的训练数据，数据效率 1.6 倍。  
- 从 Qwen3.5-35B-A3B 继续预训练 1T tokens 后 SFT/RL：Intern-S2-Mobius-35B 通用基准平均 67.88 vs 65.05，科学任务平均 52.14 vs 18.20。  
- 推理效率：端到端吞吐最高约 4.6 倍提升，平均输出长度缩短 1.2–5 倍；线性代数案例中 516 tokens vs 2364 tokens 完成同等推理。

**最值得记住的一句话**  
不是降低注意力复杂度，而是用共享知识库和隐式迭代提高信息密度，以更少高质量 token 完成推理。
