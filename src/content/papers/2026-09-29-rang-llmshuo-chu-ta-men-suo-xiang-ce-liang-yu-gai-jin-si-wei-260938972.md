---
title: 'Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability
  Alignment'
title_zh: 让LLM说出它们所想：测量与改进思维链-可解释性对齐
authors:
- Yihuai Hong
- Shauli Ravfogel
- Chen Zhao
- Eunsol Choi
affiliations:
- New York University
- NYU Shanghai
arxiv_id: '2609.38972'
url: https://arxiv.org/abs/2609.38972
pdf_url: https://arxiv.org/pdf/2609.38972
published: '2026-09-29'
collected: '2026-10-07'
category: Reasoning
direction: LLM推理可解释性对齐与后训练
tags:
- Chain-of-Thought
- Interpretability
- Faithfulness
- Post-training
- LLM Reasoning
one_liner: 提出CIA度量并后训练联合优化任务精度与参数忠实度，提升LLM思维链与内部计算一致性
practical_value: '- 在电商/广告中若使用LLM生成推荐理由、商品对比或竞价策略解释，可借鉴CIA思路：用线性探针或干预实验验证模型声称的决策依据是否真的体现在内部表征中，避免“编理由”导致合规与信任风险。

  - 将“解释与内部决策信号一致性”加入奖励函数（例如对内部探针判断关键token或特征重要性与CoT声称的一致性打分），与任务准确率联合优化，可能在不牺牲效果的情况下提升解释可信度。

  - 建立CoT忠实度审计机制：定期对线上Agent/推荐解释链路抽样，用可解释性工具计算CIA分数，监控模型版本更新或数据漂移后推理行为是否失真，尤其适用于需要审计的广告排序和价格推荐场景。

  - 注意落地成本：需要额外训练探针或标注内部策略，适合高风险、强监管或需向用户出具理由的场景；中小业务可先复用开源度量工具做离线评估。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM的思维链（Chain-of-Thought）常被当作模型推理过程的代理，但越来越多的证据表明，CoT并不忠实反映内部计算，甚至可以篡改而不改变最终输出，这损害了模型可监控性与可信度。

**方法关键点**：提出CoT-Interpretability Alignment (CIA)度量，利用可解释性工具（如探针、干预）检测模型内部推理策略与CoT文本的一致性。在双跳问答、提示干预、整数乘法三个任务上，对三种LLM进行评测。进一步通过后训练同时优化任务准确率和参数忠实度信号（作为奖励），尝试提升CIA。

**关键结果**：评测显示现有LLM的CIA介于44.8%至75.9%，对齐有限；后训练能大幅提高CoT参数忠实度，同时保持或提升任务准确率。分析还揭示了泛化模式。代码与数据已开源。
