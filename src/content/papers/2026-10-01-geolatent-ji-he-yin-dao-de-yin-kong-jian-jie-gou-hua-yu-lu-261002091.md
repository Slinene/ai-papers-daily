---
title: 'GeoLatent: Geometry-Guided Latent Structuring with Routed Optimization for
  3D Reasoning'
title_zh: GeoLatent：几何引导的隐空间结构化与路由优化用于 3D 推理
authors:
- Yakun Zhu
- Yi Bin
- Yujuan Ding
- Zheng Wang
- Pengpeng Zeng
- Duo Peng
- Jingkuan Song
- Heng Tao Shen
affiliations:
- Tongji University
- The Hong Kong Polytechnic University
arxiv_id: '2610.02091'
url: https://arxiv.org/abs/2610.02091
pdf_url: https://arxiv.org/pdf/2610.02091
published: '2026-10-01'
collected: '2026-10-04'
category: Multimodal
direction: VLM 3D 推理 · 几何隐变量结构化
tags:
- 3D Reasoning
- VLM
- Latent Structuring
- Routed Optimization
- Geometry Alignment
one_liner: 通过 Common-Residual 几何对齐和路由优化，解决 3D 推理中几何 latent 坍塌与欠使用问题，在 SPAR-Bench 和
  SPBench 上达 SOTA
practical_value: '- 连续隐变量可替代文本 token 描述连续空间关系，适合建模价格区间、距离、角度等连续属性；在电商推荐中可尝试用 latent
  表示用户-物品的相对偏好（如价格敏感度、类目距离），避免离散化信息损失。

  - 路由优化策略值得借鉴：训练时先强制主任务经过某个 bottleneck latent（如商品知识图谱嵌入、用户状态向量），再逐步恢复 direct path，能显著提升
  latent 的实际利用率，防止被旁路。

  - 用 effective rank 监控 latent 表征多样性，可检测推荐模型中的表征坍塌；当 rank 接近 1 时，说明隐变量没有捕获多维度信息，需加正则或对齐损失。

  - 将共享与残差几何对齐分离，可迁移到多信号建模：把公共信息和任务特有信息解耦，避免主导信号（如点击）压制稀疏但重要的信号（如转化）。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：VLM 在 3D 空间推理上仍面临挑战。基于文本 token 的中间几何描述会损失连续空间关系；连续 latent 虽然表征更丰富，但单一 latent 类型无法显式分离不同空间任务所需的线索；分解空间 latent 虽可分别表示位置、方向、全局几何，但几何表征仍会坍塌到一个主方向，且无约束注意力会让 latent 在答案学习中被忽视。

**方法关键点**：
- **CR-GEO（Common-Residual Geometry Alignment）**：将 teacher 几何信息分离为共享部分和残差部分，结构化几何状态，避免表征坍塌。
- **Routed Optimization**：联合训练几何和语言任务，训练初期临时强制视觉答案学习经由 geometry latents，随后在几何监督下恢复 full attention，使 latent 真正参与推理且保留直接图像通路。

**关键结果**：
- CR-GEO 将 geometry effective rank 从 1.00 提升到 3.87，表明几何表征维度显著多样化。
- 在 bottleneck 处阻断 latent readout 时，方向准确率从 89.1% 降至 25.8%（128 个固定问题），证明 latent 被有效使用。
- 在 SPAR-Bench 上达到 73.0%，在 SPBench 上达到 72.1%，均优于此前方法。
