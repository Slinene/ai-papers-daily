---
title: Deep Cross-Division Network for Product-and-Ratio Feature Interactions in Industrial
  Ranking
title_zh: 面向工业排序的 DCDN：学习乘积与比值特征交互
authors:
- Mikhail Trapeznikov
- Sofia Gulevskaia
- Maksim Utushkin
- Aleksandr Poslavsky
- Alexander D'yakonov
affiliations:
- AI VK
- Lomonosov Moscow State University
arxiv_id: '2611.27514'
url: https://arxiv.org/abs/2611.27514
pdf_url: https://arxiv.org/pdf/2611.27514
published: '2026-11-20'
collected: '2026-11-23'
category: RecSys
direction: 特征交互建模 · 排序效率优化
tags:
- DCNv2
- Feature Interactions
- Ratio Features
- Industrial Ranking
- Inference Efficiency
- A-B Test
one_liner: 在 DCNv2 交叉层中加入稳定倒数分支，使模型直接学习乘积与比值交互，实现 40.1% 特征削减和多项线上指标提升
practical_value: '- 对推荐排序中的 CTR、时长率、互动率等比值特征，若分子分母已在特征集中，可尝试用 DCDN 风格交叉层：在 DCNv2 matrix
  cross 上增加一个分母 mask 的倒数分支，去掉人工比值特征，输入特征宽度可减少约 40%，模型计算显著下降。

  - 倒数分支实现用稳定倒数 `sgn(x)/max(|x|, ε)`，`ε=1e-2`；只对 denominator-eligible 坐标开放，避免全量坐标引入数值不稳定；分子分母保留在
  base 特征中即可。

  - 不要用 DCDN 替换全部特征交互；生产上把它作为前置 product/ratio 交互层，后面接 Hiformer/self-attention 等更泛化的交互模块，质量与效率更优。

  - 如果想验证这类 bias，先做合成商任务：目标 = numerator/denominator，DCDN 相比 DCNv2 误差低 2-3 个数量级，能快速判断
  learnability；再进入生产，否则别轻易改架构。

  - Serving 效率要看端到端：论文中模型计算 -42.4% 但 ranking-service 只 -10.5%，因此要关注 feature encoding、batching、kernel
  fusion 等系统因素，不能只看 FLOPs。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业排序中大量依赖人工构造的比值特征（CTR、互动率、归一化计数），这些特征可提升预测力，但会加宽输入、增加特征管线复杂度和交互层计算成本。DCN/DCNv2 的交叉层只能生成非负整数次幂的乘积交互，无法直接表示倒数类关系；因此通常必须显式输入比值特征。论文目标是把这类代数关系下沉到交互算子，用模型结构恢复比值信号，从而去除人工特征。

**方法关键点**
- 在 DCNv2 矩阵交叉层上增加元素级倒数分支：`x_{l+1} = x_l + (W_l x_l + b_l) ⊙ x_0 + (W̃_l x_l + b̃_l) ⊙ 1/x_0`，分支只对 denominator-eligible 坐标开放。
- 使用稳定倒数 `ρ_ε(x)=sgn(x)/max(|x|,ε)`，`ε=0.01`，防止近零输入产生极大激活。
- 理论上可表示为多元 Laurent 多项式：K 层 DCDN 生成 ℓ1-order 至 K+1 的单项式，signed degree 介于 −K 到 K+1；单层即可表示 `x_l/x_k`、`1/x_k` 和乘积项。
- 生产部署仅用单层 DCDN 作为 product/ratio 交互层，后接 HIFORMER 捕获更广泛异构交互，下游任务塔不变。

**关键结果**
- 合成商任务 `y=n1/d1`：DCDN 的 NMSE 在 2.81e-7 到 1.21e-6，相对 DCNv2 误差降低 129×–1620×。
- 公开数据集 Yambda、KuaiRec、KuaiRand、VK-LSVD：DCDN 在四个数据集上相比 DCNv2 同时提升 AUC/XAUC 与 nDCG@10；比更通用的 AFN+、EulerNet 延迟低 5.9–8.8 倍。
- 容量匹配的更深 DCNv2 对照：DCDN 在所有四个数据集 nDCG@10 更高，且快 1.15–1.47×，说明不是单纯参数容量增加。
- 生产 A/B（短视频服务，14 天）：DCDN reduced 对比 DCNv2 full，移除 40.1% 输入特征；线上 Likes +3.25%，Shares +16.26%，TVT +0.33%，Fullscreen +0.38%，Shows −0.24%；模型计算时间 −42.4%，ranking-service 时间 −10.5%。

**一句话**
结构化倒数交互能在不损失甚至提升排序质量的前提下，把人工比值特征下沉到模型算子，换取特征管线简化和服务延迟下降。
