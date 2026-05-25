---
title: 'CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit
  Test'
title_zh: CoSPlay：测试时无监督自博弈协同进化代码与单元测试
authors:
- Zhangyi Hu
- Chenhui Liu
- Tian Huang
- Jindong Li
- Yang Yang
- Jiemin Wu
- Zining Zhong
- Menglin Yang
- Yutao Yue
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Institute of Deep Perception Technology, JITRI, Wuxi, China
arxiv_id: '2605.23491'
url: https://arxiv.org/abs/2605.23491
pdf_url: https://arxiv.org/pdf/2605.23491
published: '2026-05-22'
collected: '2026-05-25'
category: LLM
direction: 代码生成 · 无监督自博弈 · Test-Time Scaling
tags:
- Code Generation
- Self-Play
- Test-Time Scaling
- Unit Test Generation
- Execution Matrix
- Unsupervised
one_liner: 提出无监督、无训练的测试时自博弈框架，代码与自生成的单元测试通过执行矩阵双向验证协同进化，显著提升代码生成正确率
practical_value: '- 可复用的协同进化机制：在电商多智能体系统中，可让策略生成器与自生成的验证规则（类似单元测试）形成双向反馈循环，通过执行成功次数信号清理低效策略、修复缺陷行为，实现无监督的迭代优化。

  - 共识聚类提升最终选择可靠性：当多个候选策略/推荐结果得分相同时，利用随机输入下的输出一致性聚类进行二次筛选，正确策略因行为一致而聚集，此技巧可迁移到推荐模型的融合、多臂老虎机决策等场景。

  - 探索-攻击驱动的验证样例生成：先探索解决方案思路，再针对潜在失败模式生成判别性测试，这种“生成后攻击”的方法可用于电商Agent的鲁棒性测试，自动挖掘边界异常输入。

  - 成本-性能优势：在相同推理预算下，将算力投入执行驱动的自博弈比单纯扩大采样规模更高效，该思路适用于任何具备可验证反馈的生成任务（如生成式推荐的质量评估）。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：RLVR 和 TTS 方法需要大量真实单元测试（GT UT）来验证代码正确性，但 GT UT 获取成本高、难以规模化。现有无 GT 的 TTS 方法直接用自生成 UT 筛选代码，但自生成 UT 噪声大、易与错误代码伪耦合，且 UT 自身质量无法验证。核心挑战是同时提升代码和 UT 质量，形成可靠的验证闭环。

**方法关键点**：
- **三阶段无训练、无 GT 框架**：① 探索-攻击引导的代码与 UT 构思生成：先探索可能解法思路，再推理失败模式产生判别性 UT 构思，提升初始 UT 的区分度。② 执行矩阵驱动的迭代自博弈：构建代码-UT 执行矩阵，利用码通过数、UT 通过数作为双向质量信号，循环执行代码清洗（删全败代码）、打破伪耦合（刷新最低非零支持 UT）、代码修复（用最佳非平凡 UT 修复失败代码）、替换零区分 UT，使两个池协同进化。③ 输出共识聚类终选：当多个代码得分并列时，用随机合法输入的执行输出向量进行聚类，正确代码输出一致形成大簇，从中选最可靠簇及最可靠代码。
- **无需权重更新**，完全在推理阶段完成，可与任意基模型配合。

**关键结果**：在 LiveBench、LiveCodeBench、CodeContests、CodeForces 四个困难基准上，基于 Qwen2.5-7B-Instruct 的 CoSPlay 将平均 BoN 从 22.1% 提至 33.2%，UT 准确率从 14.6% 提至 78.3%，达到甚至超过需 4.5k GT 数据训练的 CURE-7B；叠加到 CURE-7B 后 BoN 再提升 5.7%。方法在 Instruct、RLVR-tuned 和超大模型上均有效，同等 token 预算下优于现有无 GT TTS 基线，且性能随预算扩展持续增长。
