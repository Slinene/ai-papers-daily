---
title: 'SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use'
title_zh: SkillCoach：自演化量规评估与增强 Agent 技能使用
authors:
- Jiayin Zhu
- Kelong Mao
- Yudong Guo
- Dengbo He
- Sulong Xu
- Simiu Gu
- Yutao Yue
affiliations:
- HKUST(GZ)
- JD.COM
arxiv_id: '2607.01874'
url: https://arxiv.org/abs/2607.01874
pdf_url: https://arxiv.org/pdf/2607.01874
published: '2026-07-01'
collected: '2026-07-03'
category: Agent
direction: Agent 技能使用的过程评估与自我演化量规
tags:
- Agent Skill-Use
- Rubric Self-Evolution
- Process Supervision
- Skill Selection
- SFT Data Filtering
- Distractor Robustness
one_liner: 提出自演化量规框架，从技能选择、遵循、组合与反思四个维度诊断并提升 Agent 在含干扰项库中的技能使用能力
practical_value: '- **过程与结果解耦诊断**：在 Agent 系统中将外部验证器（最终结果）与过程评估分离，用轨迹级别的技能选择、步骤遵循、组合正确性和反射检查四个维度定位故障，避免仅用成功率掩盖错误的技能调用或跳步。

  - **自演化量规作为数据过滤器**：用自我演化的量规筛选 SFT 训练轨迹，要求轨迹同时满足过程质量分≥0.95 且通过验证，显著优于仅用结果过滤，可迁移到电商导购、广告脚本执行等技能驱动场景，提升训练数据质量。

  - **干扰项压力测试实用价值**：在技能库中混入语义相似但无关的干扰技能，评估 Agent 的技能选择退化边界与崩溃点；电商搜索/推荐中的意图路由、工具选择可借鉴这种方法，提前发现模型在候选集膨胀时的脆弱性。

  - **维度级消融指导训练重点**：实验表明去除关键步骤遵循损失最大、组成顺序次之，反射较弱，可据此调整过程监督的维度权重或设计分步训练策略，重点关注步骤遵循与技能选择。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：企业技能库日渐庞大，Agent 在调用技能时经常选错、跳步、组合错误或缺失最终检验，仅看最终任务成功（output verifier）无法区分“碰巧通过”与“可靠复用技能”的轨迹；训练时若用所有 verifier-pass 轨迹做正样本，会引入脆性行为。需要一种过程级评估方法，专门衡量 Agent 是否**正确选择、忠实遵循、合理组合并在提交前主动反思**技能。

**方法关键点**：
- 定义 Agent 技能使用的四个轨迹维度：技能选择（F1 评分，惩罚选干扰项）、技能遵循（基于关键步骤完成度与证据乘子）、技能组成（前置依赖顺序检查）、技能基础反射（输出前校验）。
- 设计自演化量规框架：从 gold skill + oracle 解初始量规；用真实轨迹的校准集判断并提取证据；由仲裁模型提议局部补丁（增加证据要求、负例、约束等）；通过验证门控（硬规则防退化 + 软目标测覆盖/质量）进行接受，多轮迭代得到任务级最优量规。
- 用量现筛选 SFT 数据：仅保留 meta 分数 ≥ 0.95 且 verifier 通过的轨迹进行监督微调；同时消融各维度对训练的贡献。

**关键实验**：
- 基于 SkillsBench 筛选的技能依赖任务（训练 18 族 50 实例，测试 10 族 50 实例），默认含 2 无关 + 3 语义相似干扰技能。
- 量规质量验证：黄金关键点覆盖率从 71.56→83.70，可用性 81.53→94.33，幻觉率降至 0，轨迹过滤一致性 82→96。
- Agent 性能：在 Gold+Distractors 下，Gemini-3.1-Pro 选择分从 98.0→78.0，Qwen3.5-9B 从 92→44，暴露最终精度隐藏的选错问题。
- 训练增益：Qwen3.5-4B 由 base 8.0 提升至 Rbest 过滤 SFT 的 24.0（9B：14→32），对比纯结果过滤 SFT 仅 6.0/18.0。
- 干扰项边界：至 5 万技能库时 GPT-5.5 仍未崩溃（F1 0.33），而 DeepSeek-V4-Flash 在 6.4k 即崩溃。

**最值得一句**：把技能使用的过程质量与最终验证解耦，并用自我演化的精细量规来筛选训练轨迹，可以显著提升 Agent 在含干扰项真实库中的可靠性和可训练性。
