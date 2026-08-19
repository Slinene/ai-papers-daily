---
title: 'Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation
  for Agent Evaluation and Credit Assignment'
title_zh: 跨视图对应是测量干预：Agent评估与信用分配的双侧验证
authors:
- Zhen Zhang
- Ahmad Hafez
- Amr Alanwar
affiliations:
- Technical University of Munich
arxiv_id: '2608.17713'
url: https://arxiv.org/abs/2608.17713
pdf_url: https://arxiv.org/pdf/2608.17713
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: Agent 评估 · 对应关系识别与信用分配
tags:
- agent evaluation
- correspondence
- credit assignment
- identifiability
- optimal matching
- two-sided validation
one_liner: 把跨视图对应视为测量干预，用双侧验证和全最优解集审计暴露隐藏 tie-breaking 对评估与信用分配的影响
practical_value: '- 在离线评估或 RLHF/GRPO 中使用轨迹匹配、工具调用对齐时，不要只跑一次最优匹配；枚举所有 exact-optima，用
  all-optima 证书（只保留所有最优解符号一致的坐标）而非单次 solver 结果，避免隐藏 tie-break 改变诊断或信用符号。

  - 对跨视图变换（如 prompt 改写、工具 schema 映射、界面归一化）做双侧验证：null controls 防假敏感，positive controls
  防假不变性；仅用 benign 重放校准不足，可能在 benign 数据上重建良好却抹掉真实响应差异。

  - 信用分配/优势归一化中，相对标准化、peer normalization 可能因 hidden completion 顺序和样本内依赖导致符号反转；在重要决策上使用鲁棒共同方向或显式声明
  completion policy，并记录匹配采样与归一化顺序。

  - 检查公共严格指标（如 Tool-Exact-Match）是否因前缀匹配给多余步骤满分；对精确匹配类指标用 max length 归一化做保守修复，避免模型排序被指标缺陷反转。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**

Agent 评估和 trace-based learning 常在不同视图间做 correspondence（跨视图 transport、输出间 matching、tie completion），却把它当 neutral preprocessing。实际上 correspondence 是一种测量干预：省略适当映射会制造敏感性，只在良性样本上校准映射会制造不变性，多个最优匹配保留相同标量得分却可能给出相反的机制标签或符号化信用。因此 point claim 需要声明并验证 correspondence contract，而不是依赖单次 solver 运行。

**方法关键点**

- 定义 correspondence contract C=(Q,ρ,h)：声明匹配目标 Q、精确最优集消费策略 ρ（确定性 selector、随机律、或要求结论对所有 exact-optima 不变）和下游 readout h。
- 双侧验证：用 null controls 约束 null leakage e0，用 positive controls 计算 restricted gain κ_G，并要求行为 witness 保留；定理 1 给出线性 feasible 边界——nuisance 与 response 子空间交集为 0 时，投影增益为 sin θ_min。
- 全最优解集传播：将每个 exact-optimum 经 reward compiler 和 policy-score 映射得到 legal update body Kθ；命题 1 给出 solver-independent update trichotomy（单点 / 严格共同方向 / 原点）。坐标级诊断保留所有 exact-optima 同号的坐标。
- 复杂度边界：仿射 compiler 可用 LP/QP；局部低树宽非线性可用 min-sum；共享标准化 compiler（如 Std）可构造出 Ising 哈密顿量，阈值审计为 NP-hard/coNP-hard（定理 2）。

**关键结果**

- 在 Raj et al. 2026 的 1,586 个非零轨迹对上，两个确定性最优 traceback 在 55.9% 上给出不同 temporal localization；47.5% 在预注册 early/late 规则下 alignment-unidentified；个别 cell 均值区间跨两个 regime（如 [.221,.799]）。
- MatchTIR 信用分配审计：93/495 多步轨迹有 material exact-optima reward width（18.8%）；14/20 受影响任务组 intended multi-turn advantage 符号反转；all-optima 证书保留 332/437=76.0% 坐标且零假符号。隐藏的贪心 selector 继承早期调用优先，带来 +0.196 的 positional bias。
- Earth-Agent Tool-Exact-Match：14.23% 非精确 traces 获满分；修复后 top 配置从 DeepSeek-V3.1 IF 变为 GPT-4o AP，9 个 pairwise 排序逆转。
- 双侧 transport 验证中，wrapper stripping 抹掉 8/8 corrected 和 8/8 held-out failures，call-site transport 保留全部；benign-only 校准无法证明响应保留。

**最值得记住的一句话**

一个最优匹配可以支持相反的结论；跨视图对应不是 neutral preprocessing，必须在所有 exact-optima 上传播不确定性才能支撑 point conclusion。
