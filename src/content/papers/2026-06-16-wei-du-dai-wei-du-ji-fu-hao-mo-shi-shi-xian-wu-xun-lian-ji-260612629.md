---
title: 'Bag of Dims: Training-Free Mechanistic Interpretability via Dimension-Level
  Sign Patterns'
title_zh: 维度袋：维度级符号模式实现无训练机制可解释性
authors:
- Varun Reddy Nalagatla
affiliations:
- Amazon Web Services
arxiv_id: '2606.12629'
url: https://arxiv.org/abs/2606.12629
pdf_url: https://arxiv.org/pdf/2606.12629
published: '2026-06-16'
collected: '2026-06-21'
category: LLM
direction: 无训练LLM可解释性 · 符号维度
tags:
- interpretability
- mechanistic interpretability
- sign patterns
- transformer
- feature discovery
- dimension-level
one_liner: Transformer隐藏状态标准基中维度符号独立编码语义，纯符号匹配即可高AUC检测概念，无需额外旋转或训练。
practical_value: '- **轻量概念检测**：在推荐系统的LLM特征抽取后，可用维度符号模式直接检测商品类目、品牌、情感等概念，无需标注数据训练探针，单次前向即可计算符号一致性得分，AUC可达0.97以上，节省工程成本。

  - **高效向量检索**：将embedding量化为符号向量（±1），用汉明距离替代cos相似度做近似检索，大幅降低存储和计算，已在LM head中验证符号匹配能保留80-90%
  top-4096预测，可直接用于召回或排序的近似加速。

  - **模型诊断与审计**：标准基维度符号独立性强（互信息<0.006 bits），可逐维度解释模型内部概念，用于线上模型漂移监控、偏差检测或新概念发现，无需GPU天级别的重新训练。

  - **Agent状态校验**：在LLM驱动的Agent规划中，可实时检查隐藏状态的符号模式是否对齐安全或业务相关特征，通过翻转特定维度符号做因果干预，低成本实现概念级可控生成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：传统Transformer可解释性依赖训练旋转（如探针、自动编码器），计算昂贵。本文探索标准基本身是否已具备直接可解释的特征结构。

**方法**：将隐藏状态视为独立维度构成的“符号袋（Bag of Dims）”——每个维度的符号（±1）编码语义概念存在性，幅值编码置信度。概念定义为维度的子集及其一致符号模式，通过计算查询向量与模板的符号一致数（汉明距离）实现无学习检测。在语言、视觉、音频共7个模型上验证。

**关键结果**：
- 仅凭符号（幅值置1）保留60-93% top-5下一token预测精度；无解码器汉明评分达80-90% top-4096。
- 基于单token缓存的无监督检测，175个概念AUC达0.97-0.99；训练探针仅提升0.018 AUC且权重收敛到轴对齐。
- 符号特征因果可操作：通过前向过程中翻转相关维度符号可跨模型抑制对应概念，且可溯源至FFN神经元联合。
- 维度间互信息<0.006 bits，保持独立。
- 跨模态成立：自监督视觉（DINOv2）、监督视觉（ViT-Base）、音频（AST）均表现相同特征，说明是通用Transformer训练特性。

**结论**：标准基已是足够的特征基，单次前向即可读取，无需优化。未来工作转向编目每个维度编码的具体概念。
