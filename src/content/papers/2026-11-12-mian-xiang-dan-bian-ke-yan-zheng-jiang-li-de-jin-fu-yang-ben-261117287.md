---
title: Negative-Only Policy Optimization for One-Sided Verifiable Rewards
title_zh: 面向单边可验证奖励的仅负样本策略优化
authors:
- Jiacheng Xu
- Shuo He
- Fuxiang Zhang
- Chaojie Wang
- Bo An
affiliations:
- Nanyang Technological University, Singapore
- Skywork AI
arxiv_id: '2611.17287'
url: https://arxiv.org/abs/2611.17287
pdf_url: https://arxiv.org/pdf/2611.17287
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: LLM 强化学习 · 单边可验证奖励
tags:
- RLVR
- Policy Optimization
- Negative-Only
- Reward Hacking
- LLM Reasoning
- Verifiable Rewards
one_liner: 提出NOPO，仅抑制可信负样本，避免在部分验证器下强化错误正样本的奖励捷径
practical_value: '- 在推荐/广告场景中，若只有弱信号能判定“差”（如用户投诉、审核不通过、低转化），而没有可靠正样本，可借鉴 NOPO：只对可信负样本做抑制，不强化未验证的正样本，避免奖励黑客。

  - 组级适配器根据批次中未被否决样本的比例缩放更新幅度，能缓解标签噪声和验证器误报对策略漂移的影响；可迁移到 LLM 排序/文案生成中的 RLHF 或 DPO，尤其当自动化评估器只能部分检查规则时。

  - 参考相对负抑制损失（reference-relative negative suppression）适合作为安全约束：在不完全验证器环境中，保持策略不远离参考模型，同时压制已确认失败模式。

  - 论文显示仅负样本训练在 code/logic/math 上跨基准可迁移且推理时扩展稳定，说明在工业 Agent 任务里，用廉价规则过滤负样本构建训练信号是可行且稳健的。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：RLVR 通常依赖完整验证器判断解是否正确，但很多真实场景只有廉价的部分检查，只能可靠识别失败样本；被标记为“正确”的样本可能包含大量假阳性。标准 RLVR 会强化这些假阳性，导致奖励捷径和性能退化。

方法：将这种设定形式化为单边可验证性（OSV）。提出 NOPO：把验证通过的样本视为未标记，不给予正奖励；策略更新仅通过抑制可信的验证失败负样本完成。具体包含两个组件：参考相对负抑制损失（以参考策略为基线压制负样本对数概率）和组级适配器（用每个采样组中未被否决样本的比例缩放更新幅度）。

结果：在单元测试、约束检查、LLM 自验证器三种验证器设置下，NOPO 在代码、逻辑、数学基准上相比 GRPO、EM-RL、w-Reinforce 等 baseline 提升 pass@k；在 oracle reward 不可用时优势明显。Qwen3-4B/8B 平均 pass@16 提升，跨基准迁移和推理时扩展（pass@k 随 k 增长）均保持增益。
