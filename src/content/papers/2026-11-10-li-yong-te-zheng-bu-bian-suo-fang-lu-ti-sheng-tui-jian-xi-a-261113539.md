---
title: Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation
  in Recommendation Systems
title_zh: 利用特征不变缩放律提升推荐系统 A/B 实验效率
authors:
- Zhiliang Chen
- Sammy Nammari
- Jiahao Su
- Xiaoqiang Luo
affiliations:
- Meta
- National University of Singapore
arxiv_id: '2611.13539'
url: https://arxiv.org/abs/2611.13539
pdf_url: https://arxiv.org/pdf/2611.13539
published: '2026-11-10'
collected: '2026-11-11'
category: Eval
direction: 推荐系统实验 · Scaling Laws
tags:
- scaling laws
- A-B testing
- recommendation systems
- feature evaluation
- LLM-based recsys
- statistical inference
one_liner: 用特征不变的 scaling law 拟合小规模实验，预测全量 A/B 效果并给出置信区间，显著节省计算
practical_value: '- 在电商/广告推荐迭代中，不要只看单个小规模实验的 loss/HR，而是跑 3-5 个 scale（如 0.1/0.2/0.3/0.4/0.5），拟合并用后验概率判断全量是否有效；可捕捉
  crossover 现象，避免误杀。

  - 采用联合缩放模型尺寸和数据量，5 个小规模实验成本约为全量 55%，但在 GPU 显存受限时，缩小模型是唯一可行路径；适合批量化过滤候选特征。

  - 决策规则建议加 margin δ（如 loss 降 1%）和概率阈值（如 90%），只放行有业务意义且高置信的特征，减少上游无效全量训练。

  - 该方法对 LLM-based 推荐和 Agent 式 prompt 特征也成立，可直接对 HR@10 等业务指标拟合 scaling law，不需只依赖 loss。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统每次架构、优化或数据特征变更都要全量重训比较，成本极高；常见做法是跑少量小规模实验，但单点小规模结果常误导，例如 LLM 推荐中 genre 特征小规模降、全量升。

**方法关键点**：
- 假设验证损失满足幂律 Loss = θ₁ N^θ₂ D^θ₃，取对数后成为线性模型；训练噪声假设为高斯。
- 在多个小规模（s = N·D）观测下，用线性回归闭式估计参数和噪声方差；预测全量性能的后验服从 Student-t 分布，得到置信区间。
- 计算实验模型优于 baseline 的后验概率，可加入业务阈值 δ（例如 loss 降 1%），用贝叶斯决策规则筛选特征。
- 也可扩展到非线性 scaling law，例如 shifted power law，通过 MCMC 采后验。

**关键实验**：在 Wukong(Criteo)、HSTU(MovieLens-20M)、LLM-based(Llama-3.1/Qwen) 三个家族、40+ 特征上验证。特征不变缩放律 R² 普遍 >0.99；仅用 0.1-0.5 规模观测即可较准确判别有效/无效特征，且预测误差随观测增加而下降。发现 Time Gap Bias、Dropout 0.1、Pop Debias 等特征将 HSTU HR@10 提升 1.01%、0.64%、0.50%，超越 SOTA。

**最值得记住的一句话**：特征不变 scaling law 可以把昂贵的全量 A/B 判断转化为低成本的统计外推，前提是幂律函数形式稳定。
