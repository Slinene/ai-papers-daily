---
title: 'FOSTER: First-order Dataset Distillation for Text-based Sequential Recommendation'
title_zh: FOSTER：面向文本序列推荐的一阶数据集蒸馏框架
authors:
- Hung Vinh Tran
- Tong Chen
- Xinyi Gao
- Junliang Yu
- Julien Monteil
- Hongzhi Yin
affiliations:
- The University of Queensland
- Griffith University
- Amazon International Machine Learning
arxiv_id: '2605.30772'
url: https://arxiv.org/abs/2605.30772
pdf_url: https://arxiv.org/pdf/2605.30772
published: '2026-05-29'
collected: '2026-06-01'
category: RecSys
direction: 推荐系统训练加速 · 数据集蒸馏
tags:
- Dataset Distillation
- Sequential Recommendation
- Text-based Recommendation
- First-Order Optimization
- Embedding Tying
one_liner: 通过随机项目子集采样、一阶优化与轨迹锚定重置，用极少合成序列逼近全量文本序列推荐性能。
practical_value: '- **用合成序列替代全量数据加速模型迭代**：在需要频繁更新模型的电商场景，可将全量用户交互序列蒸馏成少量合成序列（如20条），下游模型训练时间从小时级降至分钟级，且性能不降，适合在线学习或快速实验。

  - **随机项目子集采样避免全量计算**：蒸馏过程每步仅采样512个项目计算概率，而非整个商品库，显著降低显存和计算量；该方法可直接迁移到任何需要全库 softmax
  的场景，类似负采样但更稳定。

  - **一阶优化替代双层优化降低工程复杂度**：将双层问题转化为带约束的单层问题，用一阶梯度更新合成数据和模型参数，消除昂贵的高阶梯度计算；在资源受限（如单卡
  24 GB）环境下，比传统 BPTT 方案内存降低 25 倍，且收敛更快。

  - **显式对齐项共现语义可提升蒸馏质量**：当推荐模型使用嵌入绑定时，引入正则化项迫使语义相似商品在合成序列中具有相似的条件分布，能有效避免合成数据退化到只包含热门商品，提升冷门商品的表达能力，对保持推荐多样性有帮助。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：基于文本的序列推荐通过语言模型编码商品描述，显著提升了冷启动和泛化能力，但训练成本极高——每个商品对应多个 token，且需反复通过语言模型提取嵌入。数据集蒸馏能将大规模交互数据压缩为少量合成序列，但在文本推荐中面临三大挑战：（1）商品离散且数量庞大，全量计算开销难以承受；（2）标准双层优化需对内部训练轨迹求二阶梯度，在商品嵌入动态变化时尤其昂贵；（3）推荐模型常采用嵌入绑定，若合成序列破坏商品间共现语义，会导致训练不稳定。为此，FOSTER 提出一种一阶数据集蒸馏框架，试图同时解决效率和语义保持问题。

**方法关键点**：
- **随机项目子集采样**：每步蒸馏时从全量商品中均匀采样一小批（如 N=512），仅用这些商品的嵌入计算序列概率和损失，将计算复杂度从 O(|V|) 降至 O(N)，而不影响蒸馏质量。
- **一阶优化与轨迹锚定重置**：将双层优化等价转化为带约束的单层问题，通过一阶梯度同时更新合成数据和外层模型，消除二阶导数。为防止联合优化使合成数据与单一模型过拟合，每 R 步从预训练轨迹中随机采样一个模型检查点重置内部参数，迫使其学习更具泛化性的模式。
- **分布假设正则化**：引入 Lr 损失，强制语义相似商品在合成序列中具有相似的条件概率分布，确保嵌入绑定在蒸馏后依然有效。

**关键结果**：在 Amazon Games、Foods 和 Yelp 数据集上，使用 TinyBERT 作为文本编码器、SASRec 为骨干。只用 20 个合成序列，FOSTER 在 Games 上 Recall@10 达到 0.0386（全量 0.0350），Foods 上为 0.0292（全量 0.0228），Yelp 上为 0.0210（全量 0.0213），均超过或持平全量训练，且远优于随机采样、K-Center、DEALRec、GORACS 等核心集方法。相比现有蒸馏方法 TD3，FOSTER 显存需求降低 25 倍，单轮训练时间从分钟级降至秒级，且能扩展到所有层微调。迁移实验进一步表明，蒸馏出的数据可有效训练更大的 LLM（如 Qwen3-4B），训练时间从 21 小时降至 1.55 小时，性能仅有轻微下降。**核心结论**：只需保留几十条高质量合成序列，即可替代海量原始交互数据，大幅降低文本序列推荐的训练成本，同时保持甚至提升推荐精度。
