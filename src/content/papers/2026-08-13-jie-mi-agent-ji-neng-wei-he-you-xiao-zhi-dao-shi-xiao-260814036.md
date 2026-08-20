---
title: 'Demystifying Agent Skills: Why They Work-Until They Don''t'
title_zh: 揭秘 Agent 技能：为何有效，直到失效
authors:
- Zhiyuan Jiang
- Fangrui Huang
- Hanwen Xing
- Xander Wu
- Yipeng Gao
- Rui Cao
- Mengdi Wang
- Shilong Liu
- Yijiang Li
affiliations:
- Princeton University
- UC San Diego
- Stanford University
- University of Southern California
- Johns Hopkins University
arxiv_id: '2608.14036'
url: https://arxiv.org/abs/2608.14036
pdf_url: https://arxiv.org/pdf/2608.14036
published: '2026-08-13'
collected: '2026-08-20'
category: Eval
direction: Agent 技能效用与失效机制评估
tags:
- Agent Skills
- Procedural Memory
- Skill Retrieval
- Trajectory Analysis
- Evaluation
one_liner: 用 8135 条轨迹的对照分析提出 3 类/12 模式技能效用分类，证明技能主要靠程序锚定而非知识注入
practical_value: '- 在推荐/Agent 系统中，把历史成功/失败轨迹蒸馏成紧凑的程序性技能卡（步骤、检查点、坑位），比直接注入原始 workflow
  memory 成功率更高；尤其适合环境搭建、输出 schema、服务生命周期等可复用操作，可优先沉淀。

  - 检索与执行解耦：skill pool 变大或混淆度高时，离线 top-1 命中率下降但下游成功率未必崩；不要只优化离线命中率，要监控执行时实际调用 ground-truth
  skill 的 precision/recall，并允许 agent 调用相关但非 ground-truth 的技能。

  - 失败模式要显式建模：技能可能被机械套用或忽略（skill_guidance_misapplied 约 10%），而 workflow memory 常见 timeout/budget
  过载；建议在技能执行层增加适用性判断、运行时验证与放弃机制。

  - 生成技能时保留成功/失败 outcome 标注：一旦轨迹池里混入失败样本，去掉标注会显著掉点；在经验回放 / skill distillation 中应保留结果信号。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
Skills 被普遍用于 LLM agent 推理时增强，但以往只看聚合成功率，无法解释何时有效、为何有效、何时失效。该问题对自进化 agent 尤其关键：不理解机制只能靠 prompt 试错，无法可靠地生成、检索、修订技能。

## 方法关键点
- 受控对照：同一批成功/失败轨迹分别蒸馏为 Workflow Memory 与 SKILL.md，比较 Raw / Workflow / Skill 三臂。
- 混合网格：5s0f 到 0s5f 的轨迹配比，隔离过程表征与 outcome 标注影响；no-hint 设置去掉成功/失败信号。
- 跨框架迁移：用 Codex 采集经验，在 Gemini CLI 评估，测试技能可移植性。
- 检索三实验：embedding 排序、agent 显式选择、全池真实执行，pool size 5–100，distractors 随机/相似/不相似。
- 轨迹归因：归一化 8135 条 trial，开放编码 240 条轨迹，得到 238 个有效标签，归为 3 大类 12 模式，human 验证 κ=0.952。

## 关键结果
- 技能比 Raw 成功率只高约 2.8 个点，但比同一轨迹构建的 Workflow Memory 高 +6.06 点（95% CI [+0.76,+11.36]）。
- 机制标签中 procedural_anchor 占 65.7%，knowledge_injection 仅 4.5%；技能主要是稳定动作顺序，而非补事实。
- 环境/输出格式/后台服务类失败大幅下降，例如 environment_infrastructure_failure 从 Raw 5.3% 降到 Skill 0.2%。
- 技能引入新失败：skill_guidance_misapplied_or_ignored 从 Raw 0.8% 升到 Skill 10.0%；algorithmic_logic_error 与静态验证失败仍顽固。
- 检索瓶颈独立于执行：pool 从 5 到 100，Arm 3 实际使用 precision 从 29.6% 降到 3.3%，但下游成功率只从 36.4% 变为 39.3%；精确命中 ground-truth skill 既不充分也不必要。
- outcome 标注在轨迹含失败样本时很关键：如 Gemini TB-2 3s2f，normal 0.7462 vs no-hint 0.4000。

## 最值得记住
技能系统的核心不是把更多经验塞进上下文，而是把噪声轨迹蒸馏成可复用、可验证、可放弃的程序锚点；检索命中率必须与执行中真实使用解耦评估。
