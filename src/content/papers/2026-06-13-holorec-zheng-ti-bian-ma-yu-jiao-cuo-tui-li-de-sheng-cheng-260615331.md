---
title: 'HoloRec: Holistic Encoding and Interleaved Reasoning for Generative Recommendation'
title_zh: HoloRec：整体编码与交错推理的生成式推荐
authors:
- Shuqi Zhao
- Jingsong Su
- Xiang Liu
- Xingzhi Yao
- Yiming Qiu
- Huimu Wang
- Liang Lin
- Pengbo Mo
- Mingming Li
- Jiao Dai
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Artificial Intelligence, Beijing Normal University
- JD.com
arxiv_id: '2606.15331'
url: https://arxiv.org/abs/2606.15331
pdf_url: https://arxiv.org/pdf/2606.15331
published: '2026-06-13'
collected: '2026-06-16'
category: GenRec
direction: 生成式推荐 · 层级语义编码与内生推理
tags:
- Generative Recommendation
- Hierarchical Semantic Encoding
- Interleaved Reasoning
- Chain-of-Thought
- Semantic ID
- Residual Quantization
one_liner: 提出多粒度嵌套残差量化构建层级语义编码，通过门控交错推理实现内生链式思维，统一表示、推理与生成
practical_value: '- **多粒度语义ID构建**：对item embedding按维度切片进行嵌套残差量化，生成粗到细的离散编码矩阵，可用于电商召回-粗排-精排的级联体系，在不同阶段使用不同粒度，减少计算开销同时保持语义对齐。

  - **免费午餐的多粒度辅助训练**：训练时添加粗粒度预测头（共享backbone），用粗粒度语义ID作为辅助标签，推理时去掉该头不增开销，可直接提升召回多样性（粗粒度标签帮助模型覆盖更多候选），适合电商长尾商品推荐。

  - **内生交错推理机制**：在自回归生成过程中，每一步先预测粗粒度语义分布，经门控注入到细粒度解码，隐式实现Chain-of-Thought而无需外部推理数据。可迁移到对话式推荐Agent中，在生成推荐列表时逐步细化用户意图，提升Top-1准确率。

  - **稀疏场景增益显著**：整体编码和交错推理对稀疏数据（如Beauty数据集相对TIGER Hit@5提升14.2%）效果突出，可用于解决电商中冷启动用户或新商品推荐问题。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐通过自回归生成统一了召回和排序，但现有方法存在三个问题：1) 物品语义表示大多为扁平向量，缺乏粗到细的层级结构，无法显式支持多步推理；2) 高质量的推荐Chain-of-Thought（CoT）数据获取昂贵、极度稀缺；3) 即使有CoT数据，推理步骤与最终生成常分离成两个阶段，推理未能深度指导生成。

## 方法关键点
- **整体语义编码**：对物品embedding按不同的前若干维度（如8/16/32维）切片，共享码本进行多层残差量化，形成M×L的层级离散编码矩阵；引入整体重构损失，强制每个粒度独立重构原始语义，提供自监督的多粒度信号，缓解CoT数据稀缺。
- **非思考模式**：训练时在细粒度预测头部外增加粗粒度预测头，用相应粒度的语义ID作为标签进行多任务学习，推理时移除粗粒度头，无额外开销却可利用层级监督提升性能。
- **思考模式（内生CoT）**：自回归解码时，先用上一步细粒度隐状态预测粗粒度语义分布，得到软粗粒度嵌入，经门控机制注入当前解码状态，再预测细粒度token，形成“预测粗→注入细→生成”的交错推理，直接在生成过程中嵌入思维链，无需外部标注数据。

## 关键实验结果
在Amazon Beauty和Instruments两个数据集上，以T5为backbone，对比MF、SASRec、BERT4Rec、TIGER等基线。
- Beauty上Hit@5达0.0451，NDCG@5达0.0307，相对TIGER分别提升14.2%和17.2%。
- Instruments上Hit@10达0.1105，NDCG@10达0.0828，相对TIGER提升4.4%和3.9%。
- 消融显示：多粒度监督对齐主要提升Hit@10等召回指标，交错推理主要提升Hit@1和Hit@5等精度指标，两者互补。
- 稀疏场景收益更明显，长序列用户Top-1提升更显著。

**核心洞见**：层级语义编码与内生交错推理的组合，让生成式推荐模型在稀疏和高精度场景下均能获得收益，且几乎不增加参数和在线推理复杂度。
