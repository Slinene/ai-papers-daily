---
title: Domain-Specific Hallucination Detection in Large Language Models
title_zh: 领域特定的大语言模型幻觉检测
authors:
- Varun Teja Chundru
- Debasmita Biswas
affiliations:
- Purdue University Fort Wayne
arxiv_id: '2609.11878'
url: https://arxiv.org/abs/2609.11878
pdf_url: https://arxiv.org/pdf/2609.11878
published: '2026-09-10'
collected: '2026-09-12'
category: LLM
direction: LLM幻觉检测与领域自适应
tags:
- Hallucination Detection
- DeBERTa-v3
- MC Dropout
- DPO
- Domain Adaptation
- Calibration
one_liner: 多信号检测管线结合DeBERTa-v3、MC Dropout与DPO，实现通用与领域自适应幻觉缓解
practical_value: '- 在电商问答、商品描述、推荐理由等 LLM 生成场景，可部署类似“微调 DeBERTa-v3 + MC Dropout + 温度缩放”的反应级幻觉检测器，作为生成内容上线前的置信度闸门；MC
  Dropout 推理可额外提升准确率但增加延迟，适合异步质检而非实时推荐链路。

  - 标注预算有限时，可借鉴其学习曲线结论：25% 训练数据已获 77% 性能，垂直域可先用小样本微调快速验证，再决定是否扩充标注。

  - 跨域迁移风险明确：通用域检测器在生物医学域 F1 仅 0.52，域匹配预训练模型微调才明显提升；业务上不能直接复用通用事实性检测器，应使用行业语料继续预训练或微调。

  - DPO 用检测器分数作为偏好信号，将 Qwen2.5-0.5B 幻觉率从 85.5% 降至 37.7%，可尝试对推荐文案/客服回复生成器做类似对齐，减少不实信息。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 生成文本常包含不忠实声明，高 stake 领域需反应级幻觉检测。检测被形式化为 NLI：给定知识 K、提示 Q、生成响应 R，判断 R 是否忠实于 K。

方法：构建多信号检测管线，包括微调 DeBERTa-v3 分类器、MC Dropout 不确定性量化和温度缩放校准；在 HaluEval 上评估，并进行上下文消融、学习曲线和跨域实验；还使用检测器作为 DPO 偏好信号优化 Qwen2.5-0.5B 生成器。

结果：通用域 F1=0.915、AUROC=0.977；分任务 QA/摘要/对话 F1 分别为 0.97/0.96/0.82。MC Dropout 推理将准确率提升至 93.2%。消融中摘要 F1 下降 24%，证明并非表面模式。25% 训练数据达到 77% 全量性能。DPO 将生成器幻觉率从 85.5% 降至 37.7%，相对降低 55.9%。跨域到 SciFact 时通用训练 F1 仅 0.52；使用 PubMedBERT 微调 SciFact 得 F1=0.63、AUROC=0.81，表明领域匹配预训练是最强适应策略。
