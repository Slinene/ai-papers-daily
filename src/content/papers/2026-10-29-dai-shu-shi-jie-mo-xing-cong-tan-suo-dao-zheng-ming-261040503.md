---
title: 'Algebraic World Model: From Exploration to Proofs'
title_zh: 代数世界模型：从探索到证明
authors:
- Guancheng Pan
- Qixin Tan
- Yang Yuan
- Andrew Chi-Chih Yao
affiliations:
- Zhejiang University
- Tsinghua University
- Shanghai QiZhi Institute
arxiv_id: '2610.40503'
url: https://arxiv.org/abs/2610.40503
pdf_url: https://arxiv.org/pdf/2610.40503
published: '2026-10-29'
collected: '2026-11-01'
category: Reasoning
direction: 形式化世界模型构建与证明
tags:
- LLM
- Formal Verification
- World Model
- Lean
- ARC-AGI
- Exploration
one_liner: AWM将未知环境探索与假设检验转化为可被Lean形式化的代数模型，能证明不可达性与最优界
practical_value: '- 在动态未知环境（如策略模拟、A/B测试前验证）中，用可执行假设+形式化验证替代黑盒模型，可证明目标不可达或边界，避免无效实验投入。

  - 把交互中发现的规则提取为类型化对象与共享规则，并用范畴论引导简化，有助于构建可解释、可审计的决策规则集，降低策略上线风险。

  - 反馈驱动的规则修订机制：仅给出“存在更优解”的弱反馈即可推动模型更新，可借鉴到自动策略迭代与约束优化中。

  - 但应用场景偏形式化/游戏环境，直接迁移到大规模推荐系统有距离，主要价值在可解释规则建模与复杂约束下的可靠性保障。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：AI 在数学上取得突破但依赖预定义定义与形式规范，能否对未知环境进行严格推理？本文尝试让智能体从交互中构建可形式验证的世界模型。

**方法关键点**：AWM 探索环境，生成可执行 Python 假设并不断测试、修订；随后将假设结构化为类型化对象与共享规则，利用范畴论引导的变换简化结构；最后在 Lean 4 中形式化模型，用于证明可达性与不可能性。

**关键结果**：在两个不可能游戏关卡上，AWM 全部 6 次运行均构造出 closed、kernel-checked 的 Lean 证明，排除所有合法获胜序列，而 Claude Opus 5.5 与 GPT-6 Astra 在 12 次基线运行中均未成功。初始 6 个 optimal bound 中 4 个正确，收到“存在更便宜胜利”的反馈后修订规则，最终 6/6 正确。在 25 个公开 ARC-AGI-3 游戏上，AWM 的模型让 Lean 重放全部 183 级获胜轨迹，并泛化到未见转移、检测机制变化；与 Claude Opus 5 配合得分 99.9，认证轨迹动作数仅为人类基线的 43%。
