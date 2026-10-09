---
title: 'OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via
  Streaming Structure-Aware Optimal Transport'
title_zh: OnTrack：流式结构感知最优传输用于 LLM Agent 轨迹实时监控与干预
authors:
- Babak Barazandeh
- Connor Swanson
- Chinmay Kulkarni
- Nikhil Mungel
affiliations:
- Cribl AI Research Lab
arxiv_id: '2610.12375'
url: https://arxiv.org/abs/2610.12375
pdf_url: https://arxiv.org/pdf/2610.12375
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: Agent 实时轨迹监控与干预
tags:
- LLM Agent
- Optimal Transport
- Trajectory Monitoring
- Streaming Alignment
- Early Intervention
- Cost Control
one_liner: 将 Agent 执行轨迹建模为增长 DAG，用流式结构感知最优传输与成功参考实时对齐，毫秒级识别失败前兆并提前中止
practical_value: '- 对电商/广告投放 Agent 中的不可逆操作（改价、发券、退款、删记录）增加一个预执行门：用工具 schema 标注可逆性，执行前同步检查必需的前置产物是否存在，并可选地与历史成功轨迹做一次提案对齐；成本远低于
  LLM-as-judge，且可实时阻断。

  - 监控能力按可用信息分层降级：无参考时仍可检测 loop/stall（重复工具调用但无新信息）；有成功轨迹时将轨迹建成 DAG 做结构感知 OT 对齐，能发现因果倒置/幻觉分支；参考轨迹按来源分级（gold/mined
  可自动干预，planner 生成只警告），避免误杀。

  - 在线部署轨迹对齐时不要每步重算 OT：维护 warm-start coupling，每事件只做一次 Sinkhorn/条件梯度迭代，仅当需要干预时才跑收敛解，可将单步延迟压到
  1ms 级；这对实时监控 Agent 链路可复用。

  - 干预策略不要用 naive 的首次 flag 即 abort，而应使用 severe flag 密度 + 滚动窗口阈值；论文显示首次 flag 误杀率接近
  99%。部署前需要在 held-out 流量上标定阈值，并验证 false stop 率。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM Agent 自主执行存在成本与安全风险，而事后评估发现问题时 token 已消耗、损失已造成；用另一个 Agent 在线监控则增加每步延迟和成本。因此需要一种轻量、实时的轨迹监控机制。

**方法关键点**：
- 将执行轨迹建模为增长 DAG：步骤为节点，步骤间依赖为边；用 Fused Gromov-Wasserstein / 不平衡最优传输将当前前缀与多个成功参考轨迹对齐，代价融合动作、参数、工具语义与依赖结构。
- 针对流式四个挑战：前缀比较中只给参考中“已可达”节点质量（前沿掩码），避免惩罚早到；新步骤结构影响用年龄权重从 0 逐渐增强；每事件只做一次 warm-start 条件梯度迭代，约毫秒级，仅可能干预时跑收敛求解；决策使用 per-step 泄漏、宽限期和滚动密度，不使用总分阈值。
- 三层降级架构：L1 无参考生命体征检测 loop/stall/信息增益；L2 参考轨迹的结构对齐；L3 预执行门对不可逆工具检查前置产物与提案匹配。

**关键结果**：在 SWE-bench 2,288 条真实轨迹上，前 8 步 AUROC 为 0.631，比余弦相似度高 +0.057，优势集中在早期（k≤10）。以 severe flag 密度触发 abort，可节省约 18% 无效计算，83% 的 abort 正确（5/6）。消融显示去掉 GW 结构项使 benign 误报从 13/40 升至 29/40，说明结构项主要用于降误报而非提升排序。

最值得记住：实时监控 Agent 要用 per-step 信号 + 分层降级 + warm-start 增量求解，而不是总分阈值。
