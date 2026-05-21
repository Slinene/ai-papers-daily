---
title: 'SynGR: Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation'
title_zh: SynGR：生成式推荐中释放跨模态协同潜力
authors:
- Wei Chen
- Xingyu Guo
- Shuang Li
- Fuwei Zhang
- Meng Yuan
- Jing Fan
- Zhao Zhang
- Deqing Wang
- Fuzhen Zhuang
affiliations:
- Beihang University
arxiv_id: '2605.18920'
url: https://arxiv.org/abs/2605.18920
pdf_url: https://arxiv.org/pdf/2605.18920
published: '2026-05-18'
collected: '2026-05-21'
category: GenRec
direction: 生成式推荐 · 跨模态协同信息挖掘
tags:
- GenRec
- Cross-Modal Synergy
- Multimodal
- RQ-VAE
- Saliency Masking
- Contrastive Learning
one_liner: 通过显著性掩码与协同对比学习，强制模型利用跨模态协同信息，在三个数据集上提升平均约10%，推理零额外开销。
practical_value: '- 模态依赖诊断：可从自注意力图提取token显著性得分，量化模态贡献，用于判断模型是否偏向文本或视觉，作为在线模型健康度监控。

  - 动态掩码训练策略：训练中对主导模态的高saliency token进行top-r掩码，迫使模型探索跨模态交互，可迁移至电商多模态推荐、搜索重排序，防止单模态特征过拟合，提升泛化。

  - 协同对比学习三元组构造：将原始序列、掩码序列、单模态序列分别作为正锚负样本做InfoNCE损失，可复用至其他多模态融合任务（如多模态商品描述生成、跨模态召回），强化交互语义。

  - 轻量即插即用：掩码诊断复用前向注意力图，对比损失计算仅O(Nd)，推理零增加，且25%左右的训练加速，适合已上线多模态生成式推荐系统的低成本升级。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有多模态生成式推荐（GR）主要采用对齐式融合，强化跨模态一致性，却忽略了仅有在模态交互中才涌现的协同信息（synergistic information）。这类信息刻画了单模态无法推断的高阶商品语义（如品牌格调、审美与功能的叠加），对精准匹配用户意图至关重要。信息论分析表明，当前方法在生成目标下倾向于依赖信息密度更高的模态（如文本），形成“捷径学习”，导致模型退化至单模态主导，协同信息仅占学习表示的7.5%。为解决该“协同缺口”，需要一种显式干预，打破最小阻力路径，迫使模型挖掘跨模态协同。

## 方法关键点
- **协同信息理论框架**：基于部分信息分解（PID），将多模态互信息分解为冗余、独有和协同三部分，指出对齐优化仅覆盖前两者，缺失协同项。
- **显著性感知掩码**（Saliency-aware Masking）：从Transformer最后一层自注意力计算各token的全局显著性得分，聚合得到模态级密度，识别主导模态（多为文本）。对top-r高显著性token进行[MASK]，阻断捷径，逼迫模型从跨模态线索重构语义。
- **协同对比学习**：构造三元组——原始序列（正例）、掩码序列（锚点）、单模态序列（负例）。通过掩码感知池化得到序列表征，用InfoNCE损失拉近锚与正、推远锚与负，显式强化协同信息S，抑制冗余和独有信息。
- **多视图生成联合优化**：生成损失同时作用在原始、掩码、单模态三条路径，保留必要冗余与独有信息，协同损失作为正则项，共享Transformer参数，训练效率高。

## 关键实验
在Amazon Arts、Games、Instruments三个类别数据集上，与16个基线（BERT4Rec、TIGER、MQL4GRec、MACRec等）比较，SynGR在所有指标上达到最优，较最强基线MACRec平均相对提升约10%。其中Instruments场景HR@10提升28.58%，NDCG@10提升12.17%。消融实验证明，随机掩码替代显著性掩码、取消单模态负例或去除对比损失均导致性能下降，验证了自适应掩码与协同对比的必要性。训练时间较MACRec缩短约23%，推理速度提升4-6%，说明高效可部署。
