---
title: NeuroCogMap Reveals Cognitive Organization of Large Language Models
title_zh: NeuroCogMap：用认知神经科学映射大语言模型的功能组织
authors:
- Zhongxiang Sun
- Haolang Lu
- Qiang Ma
- Qi Li
- Qipeng Wang
- Liang Pang
- Chenyu Liu
- Qiankun Li
- Hao Sun
- Kun Wang
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Institute of Automation, Chinese Academy of Sciences
- Nanyang Technological University
- Imperial College London
- Huazhong University of Science and Technology
arxiv_id: '2607.00397'
url: https://arxiv.org/abs/2607.00397
pdf_url: https://arxiv.org/pdf/2607.00397
published: '2026-06-30'
collected: '2026-07-16'
category: LLM
direction: LLM 可解释性与认知映射
tags:
- Interpretability
- Cognitive Neuroscience
- Functional Parcellation
- LLM Failures
- Brain Alignment
- Mechanistic Intervention
one_liner: 将 LLM 内部表征脑图式分区，解释行为失败并关联人脑反应与决策策略
practical_value: '- **Agent 行为监控与故障定位**：将 LLM 内部表征划分为功能分区，可实时检测 Agent 决策时的幻觉、偏见等失败模式，通过内部激活模式提前预警。

  - **安全干预机制**：针对特定失败（如谄媚或拒绝失效）对应的表征中断，可设计轻量级激活抑制或引导向量，在不改变模型参数下修正输出。

  - **人机对齐优化**：利用模型内部签名预测人脑皮层反应的能力，优化推荐解释或对话策略，使其更符合用户认知层级，提升说服力。

  - **认知层级引导提示**：映射出的认知层级结构可用于设计分阶段提示（如先锚定感知、后推进推理），增强 LLM 在复杂任务（如多步商品搜索）中的表现。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前 LLM 虽展现广泛类人行为，但其内部表征是否形成可重复的功能系统、能否解释行为失败及与人脑认知的关联仍不清楚。本文借鉴认知神经科学，提出 NeuroCogMap 框架，系统解析 LLM 内部的认知功能组织。

**方法**：NeuroCogMap 将 LLM 某一层的隐层特征自适应聚类为多个“功能分区”，每个分区对应特定的可解释功能、认知能力或认知层级。分区通过语义连贯性、跨模型稳定性及与输出的功能关联性进行验证。进一步分析分区在幻觉、偏见、拒绝失效、谄媚等失败模式下的表征与控制信号的扰动模式，并利用这些内部签名进行检测与干预。还将分区激活模式与人脑自然语言理解时 fMRI 反应建立预测映射，并暴露影响人类决策模型的潜在策略。

**关键结果**：分区形成稳定且语义连贯的组织，并在不同规模模型中部分保留。失败模式对应独特的分区-控制系统中断：例如幻觉伴随特定表征分区激活异常与行为控制分区耦合减弱。基于该签名的干预能有效降低对应失败率。分区激活显著预测人脑高阶联合皮层的反应，并且内部签名揭示的策略可精炼经典人类决策模型（如前景理论）。
