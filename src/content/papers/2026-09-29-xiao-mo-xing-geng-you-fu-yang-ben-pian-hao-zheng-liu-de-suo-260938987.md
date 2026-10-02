---
title: 'Smaller Models, Better Rejects: Preference Distillation Scaling'
title_zh: 小模型更优负样本：偏好蒸馏的缩放规律
authors:
- Rui Cai
- Wenhui Zhu
- Xiwen Chen
- Jincheng Cao
- Han Yu
- Shayan Mohajer Hamidi
- Zelin He
- Qiyao Ma
- Daiwei Chen
- Xuanzhao Dong
affiliations:
- LinkedIn
- University of California, Davis
- Arizona State University
- Clemson University
- Pennsylvania State University
arxiv_id: '2609.38987'
url: https://arxiv.org/abs/2609.38987
pdf_url: https://arxiv.org/pdf/2609.38987
published: '2026-09-29'
collected: '2026-10-02'
category: Training
direction: 偏好蒸馏 · 负样本构造与缩放
tags:
- Preference Distillation
- DPO
- Reject Sampling
- Knowledge Distillation
- LLM Training
one_liner: 在偏好蒸馏中，用更小的冻结模型生成 rejected 响应，比学生自己生成的负样本效果更好且计算成本更低
practical_value: '- 在偏好训练/对比学习数据构造中，不要默认使用同一模型的失败样本作为负样本；尝试用更小的冻结模型生成负样本，可以在降低推理成本的同时提升学生模型效果，尤其在
  SeqKD 初始化后。

  - 负样本筛选可借鉴 reference likelihood 指标：在固定候选池内选择参考策略下低似然的样本，能获得更强的对比信号，对电商推荐中的 LLM 生成式排序或文案生成同样适用。

  - 混合不同来源的负样本可以线性控制训练效果，实际工程中可通过调节小模型负样本占比来平衡成本和收益，无需完全替换。

  - 负样本的部分收益来自任务相关的 token 结构而非 prompt 特定错误，因此可将负样本重新分配给其他 prompt 或做 token 级扰动，用于数据增强，提升负样本利用率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

偏好蒸馏通常将教师响应视为 chosen，学生自己的响应作为 rejected。这种做法依赖两个假设：学生自己的失败是最有信息量的负样本，以及 reject 生成必须使用与学生同规模的模型。然而，随着学生模型增大，自生成负样本的计算成本越来越高，而且 SeqKD 后学生自己的失败往往已经接近 reference policy，提供的对比信号有限。

## 方法关键点

- **核心发现**：在 7B–72B 的 Qwen2.5 学生模型上，所有严格更小的冻结 Base 模型生成的负样本都优于学生自己的负样本（vanilla Self 和 post-SeqKD Self），且推理成本仅为 Self 的 0.9%–50.1%。
- **理论分析**：将 reject 源选择建模为逆向数据设计问题，在线性化特征模型下推导 DPO 的有限时间效用下界，刻画有利的 reject 分布区域。
- **三个干预**：
  1. 随机混合小模型与 Self 的负样本，性能随小模型占比线性提升；
  2. 将负样本重新分配给其他 prompt，甚至打乱代码 token 顺序，仍优于长度匹配的乱码；
  3. 在固定候选池内按 reference likelihood 重新选择，倾向低似然负样本能进一步提升效果。

## 关键结果

- 代码生成（KoDCode）和数学推理（OpenR1-Math）两条线。14B 学生使用 Qwen2.5-3B 负样本，代码 avg@4 提升 3.1 点，数学提升 1.9 点。
- 负样本生成成本降低 2.0×–108.3×（参数- token 代理）。
- 随机混合实验中，Llama-1B 负样本占比从 0% 到 100%，14B 学生代码 avg@4 从 59.73% 上升到 63.28%。
- Prompt 重新分配在 7B 学生上比 gibberish 高 1.28 点；仅保留代码 token 库存的 Lexical 设置仍全面优于 gibberish，14B 上有 0.73 点增益。
- 候选池内低 reference likelihood 选择在 1.5B 源上达到 63.14% vs 高 likelihood 的 61.88%。

## 最值得记住的一句话

有效的 rejected 响应保留任务结构，同时限制与 reference policy 的耦合；小模型恰好能以低成本同时满足这两点。
