---
title: Topology-Masked Unified Backbone for Joint Feature Interaction and Multi-Domain
  Sequence Modeling
title_zh: 拓扑掩码统一骨干：联合特征交互与多域序列建模
authors:
- Zhihao Zhu
- Dezheng Han
- Jikang Xia
- Shuaishuai Guo
affiliations:
- Shandong University
- Tsinghua University
arxiv_id: '2608.27005'
url: https://arxiv.org/abs/2608.27005
pdf_url: https://arxiv.org/pdf/2608.27005
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 统一序列与特征交互的CVR排序
tags:
- CVR Prediction
- Unified Backbone
- Topology Mask
- Multi-Domain Sequence
- Dual Query
- Feature Interaction
one_liner: 用结构化TopoMask注意力在同一token空间内显式路由特征交互与多域序列信息流
practical_value: '- 在统一token backbone中，不要默认全量self-attention；仿照TopoMask为不同token组（用户特征、商品特征、各行为域、memory
  token）预定义query-key连接矩阵，保留源内局部交互、阻断无关行为域直接attention，可降低噪声并提升CVR/CTR排序稳定性。

  - 引入可学习全局/域级memory token作为信息汇聚节点，替代直接对长行为序列做sum/avg池化；后续只用memory token和query token做readout，能压缩长序列且保留多域摘要，容量敏感度低（32/8降到16/4影响很小）。

  - 候选感知的DualQ值得复用：对用户侧和item侧token做双向cross-attention，再用独立attentive pooling生成几组query
  token，并用FiLM按行为域对query做条件调制；这比直接concat用户/item特征或单侧query更早注入target-dependent交互信号。

  - Dense特征不要压成单个token：字段分组或语义分组分别投影再进交互层，能保留字段结构；腾讯实验里 dense collapse造成AUC大幅下降（val
  -0.0094）。另可借鉴ID频率分桶、EMA权重平均、SwiGLU序列编码等工程trick。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业CVR预测需要同时建模异构特征交互和多域行为序列依赖。早期模型多用分离模块：行为序列先编码压缩，再与非序列特征融合，这会削弱不同信息源之间的深层交互。近期统一架构把序列和特征放进同一backbone，但要么依赖模块间交替协调，要么对统一token序列做无约束全连接attention，没有显式保留异构信息的结构差异和交互边界，容易引入噪声。

## 方法关键点
- **统一token空间**：将非序列特征、context、多域行为序列、可学习global memory token、domain-level memory token、DualQ生成的query token全部组成一个共享token序列。
- **TopoMask Attention**：核心组件。为标准self-attention增加结构化掩码矩阵A，逐query-key开启或阻断连接。global memory可attend全域；同源特征保留局部交互；每个行为域与对应domain memory、domain-aware query形成域内交互组；无关行为域之间直接attention被阻断。这样在同一层内同时完成源内结构建模、域级信息聚合和受控跨源交互。
- **DualQ双路径交互query生成**：在进入统一backbone前，对用户侧和item侧token做双向cross-attention，再用非对称attentive pooling得到base query bank；随后用FiLM按行为域条件对base query做特征级调制，生成各域增强query token，提前注入candidate-conditioned用户-商品交互信号。
- **预测与训练**：堆叠多个MaskRec block，每个block采用pre-norm residual + TopoMask Attention + FFN。最终readout只用global memory、domain memory和增强query token，aggregate后接MLP sigmoid，使用BCE损失训练。

## 关键实验
在腾讯广告算法大赛数据集上评估，训练集约1978万行，验证集约221万行，正样本率约8.06%，指标为AUC。对比HyFormer-style baseline，MaskRec验证AUC从0.831827提升到0.841253，测试AUC从0.824902提升到0.834640。消融显示：去掉DualQ验证/测试AUC分别下降0.001216/0.000975；将dense特征压缩成单一token导致验证AUC大幅下降0.009392、测试AUC下降0.009170；memory token从32/8降到16/4几乎不影响，进一步降至8/2才出现明显退化。

最值得记住的一句话：统一token空间中的信息流必须有拓扑约束，而不是全连接attention；结构化掩码能同时保留源内建模和受控跨源交互。
