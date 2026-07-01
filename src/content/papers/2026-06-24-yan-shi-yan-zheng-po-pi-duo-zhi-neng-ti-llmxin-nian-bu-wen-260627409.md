---
title: 'Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds
  and Optimal Corrector Placement'
title_zh: 延时验证破坏多智能体LLM信念：不稳定阈值与最佳纠错器放置
authors:
- Igor Itkin
affiliations:
- Independent Researcher, Tel Aviv, Israel
arxiv_id: '2606.27409'
url: https://arxiv.org/abs/2606.27409
pdf_url: https://arxiv.org/pdf/2606.27409
published: '2026-06-24'
collected: '2026-07-01'
category: MultiAgent
direction: 多智体延时验证稳定性与最优纠错放置
tags:
- Multi-agent LLM
- Hallucination Cascade
- Verification Latency
- Delay Stability
- Corrector Placement
- Grounded Laplacian
one_liner: 揭示多智能体LLM中验证延迟引发信念振荡的阈值，并给出贪心最优纠错器放置策略
practical_value: '- 多智能体推荐系统（如规划-执行-验证链）中，验证节点的延迟需严格控制：延迟过大会导致信念振荡，影响推荐结果一致性，可参考稳定性阈值公式（如延迟2时阈值=1/φ）调节验证频率与强度。

  - 纠错器（人工审核/强规则）的放置预算有限时，使用本文的贪心算法选择影响力大的节点进行纠错，能获得(1-1/e)近似最优的稳定性提升，可直接迁移到多智体关键节点选择。

  - 事实性推荐任务（如基于知识图谱）应将回答锚定在非符号化的真值源上，形成吸收边界来消除振荡，避免纯符号信念传播导致的脆弱性；对于非事实性任务（如创意推荐），需额外引入收敛机制。

  - 若系统中出现输出反复翻转，可检查验证延迟与通信延迟是否接近，此为最不稳定区，通过异步解耦或缩短延迟可缓解。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多智能体LLM系统中，验证代理的反馈存在固有延迟，未核验的虚假声明会在代理网络中传播并被放大，形成“幻觉雪崩”，最终破坏群体信念的收敛性。  
**方法**：将过程建模为带接地纠错器节点的图上的延迟共识动态，用接地拉普拉斯矩阵进行谱分解，推导出“验证剂量”（强度×频率）的闭环稳定性阈值。分析表明，过强或过于延迟的校正会从共识变为持续振荡，最不稳定点出现在通信延迟等于验证延迟时（延迟为2时阈值为黄金分割倒数）。进一步将纠错器放置建模为超模优化问题，给出贪心算法实现(1-1/e)近似最优的节点分配。  
**关键结果**：在5个开源模型上的实验证实了剂量-延迟振荡的存在；当任务转为基于事实的接地问答时，真值成为吸收边界，不稳定效应消失，说明该现象特异于符号信念任务，而接地验证可保持稳定。
