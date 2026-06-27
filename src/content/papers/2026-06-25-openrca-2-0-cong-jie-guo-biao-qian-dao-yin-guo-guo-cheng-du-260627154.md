---
title: 'OpenRCA 2.0: From Outcome Labels to Causal Process Supervision'
title_zh: OpenRCA 2.0：从结果标签到因果过程监督
authors:
- Aoyang Fang
- Yifan Yang
- Jin'ao Shang
- Qisheng Lu
- Junjielung Xu
- Rui Wang
- Songhan Zhang
- Yuzhong Zhang
- Boxi Yu
- Pinjia He
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Xi'an Jiaotong University
- Lero, University of Limerick
arxiv_id: '2606.27154'
url: https://arxiv.org/abs/2606.27154
pdf_url: https://arxiv.org/pdf/2606.27154
published: '2026-06-25'
collected: '2026-06-27'
category: Agent
direction: LLM Agent 评估 · 因果过程监督
tags:
- Root Cause Analysis
- LLM Agents
- Causal Reasoning
- Benchmark
- Process Supervision
- Fault Injection
one_liner: 首个带逐步因果标注的根因分析基准，暴露 LLM 智能体“无根基诊断”问题
practical_value: '- 对推荐系统故障诊断 Agent，不能只看最终根因准确率，需引入逐步因果验证，检测“无根基诊断”模式，提升决策可靠性。

  - 构建内部诊断数据集时，可借鉴正向验证思路：通过注入已知故障，记录因果传播路径，为 Agent 提供步骤级别的监督信号。

  - 推荐系统 Agent 面对复杂用户行为序列或系统日志时，同样存在“猜对但推理错”的风险，应在设计中加入链式证据输出与自动核验机制。

  - 长上下文理解和多工具协同是 Agent 核心瓶颈，建议在推荐场景中针对性优化对长用户轨迹、多源数据的处理能力。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：现有根因分析（RCA）基准仅标注最终根因，缺失从根因到症状的因果传播路径，导致评估退化为模式匹配，无法衡量 LLM 智能体的真实因果推理能力。

方法：提出 PAVE 标注协议，利用故障注入中已知的干预操作，从原因到症状正向验证，重建完整的逐步因果传播链。基于此构建 OpenRCA 2.0，包含 500 个跨系统实例，为每个症状提供步骤级因果标注。

关键结果：在 11 个前沿 LLM 上，精确恢复根因集合的平均成功率仅 20.7%；放松评价指标后发现，76.0% 的案例中代理至少识别一个正确根因服务，但只有 61.5% 的案例能将正确服务绑定到已验证的因果路径上，暴露了“无根基诊断”问题——结果导向评估完全隐藏了这种虚假成功。该基准首次量化了 LLM Agent 在长上下文理解、多步推理和工具使用上的系统性短板。
