---
title: Robust Soft Skill Adaptation via Behavioral Localization in Tool-Using Agents
title_zh: 工具型智能体中基于行为定位的鲁棒软技能适配
authors:
- Zijian Jiang
- Xilu Wang
affiliations:
- University of Surrey
arxiv_id: '2610.30041'
url: https://arxiv.org/abs/2610.30041
pdf_url: https://arxiv.org/pdf/2610.30041
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Tool-Using Agent 软技能行为定位适配
tags:
- soft prompt
- behavioral localization
- tool-using agents
- trajectory distillation
- skill adaptation
one_liner: 提出 Behavioral Localization，定位技能真正改变行为的少量轨迹位置来训练短 soft prompt，减少漂移并提升任务成功率
practical_value: '- 如果你的电商导购/搜索/客服 Agent 用长 system skill 控制工具调用，可尝试从成功轨迹中选 top-k 关键
  token 蒸馏成短 soft prompt；相比全轨迹蒸馏，只学行为变化最大的位置，能减少对基座已有能力的破坏。

  - 定位分数 = logprob gain × JS divergence，可迁移到 prompt/example 剪枝：保留那些既提高正确答案概率、又明显改变
  next-token 分布的轨迹节点或 few-shot 示例，删掉基座模型本来就会的冗余内容，降低上下文与 KV cache 成本。

  - 训练时在未选中位置用 no-skill 分布做 KL anchor，这种「选择性正则」适合在线更新推荐文案生成、搜索 query 改写等 Agent 策略时使用，避免更新引入不必要行为漂移。

  - 业务中不一定要替换成 soft prompt；top 10% 关键位置可作为高价值数据，用于构造短 prompt、压缩演示示例，或生成局部偏好对做后续对齐。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
工具型智能体常依赖长文本技能提示引导行为，但长 prompt 会抬高上下文与推理成本；soft prompt 压缩虽然紧凑，从完整成功轨迹学习却容易把基座模型已会的行为也改掉，造成灾难性漂移。本文观察到技能带来的正向行为变化高度稀疏。

### 方法关键点
- 在冻结 Qwen3.6-35B-A3B 上，沿成功轨迹逐 token 计算三种条件分布：text skill、no skill、soft prompt。
- 定义正向增益 G = log p_skill(y_t) - log p_none(y_t)；分布偏移 JSD = 0.5 D_KL(p_s||m) + 0.5 D_KL(p_n||m)，其中 m = (p_s + p_n)/2；定位分数 U = G × JSD。
- 取 top k% 位置做监督：选中位置最小化 text skill 与 soft prompt 的全词表 KL；未选中位置以 no-skill 分布为 anchor 做 KL 正则，防止不必要行为漂移。
- soft prompt 长度 8，用 text skill 前几个 token embedding 初始化；训练数据为 GPT-5.5 生成的 SpreadsheetBench 成功轨迹。

### 关键结果
- top 10% 轨迹位置捕获 96.12% 的总正向技能增益。
- Shared soft prompt：全轨迹 SoftSkill 30.36%，10% selective 提升到 36.79%，但仍低于在线蒸馏 OPCD 38.21%。
- Task-specific：10% selective 达 57.38%，超过 full text skill 52.46% 与 OPCD 49.18%。

### 最值得记住的一句话
只学技能真正改变模型行为的少量关键位置，其余位置锚定基座分布，能更稳地压缩 Agent 技能。
