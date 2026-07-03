---
title: 'PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception'
title_zh: PerceptionRubrics：校准多模态评估至人类感知的量规框架
authors:
- Yana Wei
- Hongbo Peng
- Yanlin Lai
- Liang Zhao
- Kangheng Lin
- En Yu
- Keyu Lv
- Han Zhou
- Yin Tang
- Haodong Li
affiliations:
- Johns Hopkins University
- StepFun
- Tsinghua University
- Independent Researcher
arxiv_id: '2606.28322'
url: https://arxiv.org/abs/2606.28322
pdf_url: https://arxiv.org/pdf/2606.28322
published: '2026-06-25'
collected: '2026-07-03'
category: Eval
direction: 多模态感知评估 · 人类对齐
tags:
- multimodal evaluation
- perception
- rubrics
- gated scoring
- human alignment
- benchmark
one_liner: 提出基于量规的多模态评估，用门控评分揭示模型在密集信息中的可靠性差距，显著提升人类对齐度
practical_value: '- **门控评分机制**：在商品描述生成或多模态问答的评估中，对核心属性、品牌等事实性信息实行一票否决，避免线性平均掩盖关键错误，可用于广告素材审核或商品信息校验。

  - **双流量规设计**：将评测项拆分为 Must-Right（核心事实）和 Easy-Wrong（易错细节），可指导构建商品图像理解测试集，针对性评估模型对材质、颜色、logo
  等细粒度属性的感知。

  - **环形同行评审标注流程**：生成高质量金标准描述的方法可迁移至商品图文匹配、用户上传内容审核的场景，通过多轮评审减少标注噪声，提升训练/评估数据质量。

  - **人类对齐的严格度量**：强调感知准确性是可靠生成的前提，在选型多模态模型用于推荐理由生成、广告文案生成时，应优先关注其在高信息密度下的精细感知能力，而非仅看整体匹配分数。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视觉-语言基准分数饱和，但模型在真实场景中脆弱，尤其难以准确验证信息密集图像中的细节，评估与人类感知脱节。

**方法**：构建 PerceptionRubrics，包含 1,038 张高信息密度图像及超过 12,000 条实例特定量规。通过环形同行评审流程生成黄金描述，并蒸馏为双流体系：Must-Right（强制性事实，如物体存在/关系）和 Easy-Wrong（易被忽略的细粒度细节，如颜色、纹理）。采用门控评分机制：未能通过 Must-Right 量规则直接判为失败，而非简单平均。

**关键结果**：(1) **可靠性差距**：模型常正确回答部分元素，但在严格合取约束下失败，暴露感知脆弱性；(2) **开源与闭源分层**：开源模型仍落后约 8% 的感知能力，与推理能力进步趋势相悖；(3) **人类对齐**：门控指标与人类判断的一致远超传统基准，证实精确感知是可靠生成的前提。
