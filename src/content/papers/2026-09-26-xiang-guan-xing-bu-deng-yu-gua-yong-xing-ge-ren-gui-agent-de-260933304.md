---
title: 'Relevance Does Not Imply Applicability: Experience Activation for Personal
  GUI Agents'
title_zh: 相关性不等于适用性：个人 GUI Agent 的经验激活框架
authors:
- Fuyao Zhang
- Xuan Wang
- Zherui Li
- Jiaming Zhang
- Longtao Huang
- Wei Yang Bryan Lim
affiliations:
- NTU
- Alibaba
arxiv_id: '2609.33304'
url: https://arxiv.org/abs/2609.33304
pdf_url: https://arxiv.org/pdf/2609.33304
published: '2026-09-26'
collected: '2026-10-13'
category: Agent
direction: Agent 个性化 · 经验激活
tags:
- Personal GUI Agents
- Experience Activation
- Personalization
- In-context Learning
- Training-free
one_liner: 提出 ExpActivator，将个性化从检索历史改为按当前情境激活适用经验，提升执行与主动建议效果。
practical_value: '- 在 Agent 或推荐系统中，不要把大量相关历史一次性塞入上下文；改用“按当前决策时状态匹配历史动作/经验”的方式，可显著减少
  token 并提升每步效果。

  - 主动推送/建议（如 push 文案、routine 触发）可引入“条件充分才激活，否则 abstain”的机制，降低打扰率，提高 MCC 类指标。

  - 使用冻结骨干的 latent 空间做 screen/state 匹配作为参考动作，无需微调，容易接入现有 LLM/VLM 系统；对电商 Agent 多步操作（如下单、搜索）可借鉴。

  - 评估个性化不应只看整体成功率，需区分第一步与后续步骤，关注经验是否在每个决策都“适用”；可设计类似 step-level success 指标。'
score: 7
source: huggingface-daily
depth: abstract
---

研究动机：个人 GUI Agent 通常检索任务相关历史并追加到策略上下文，默认“相关经验对任务内每个决策都有用”。但实验发现，这种帮助主要集中在第一步决策：检索历史显著改善 episode 的开头步骤，却对剩余 90% 步骤几乎没有持续帮助，对是否应该触发主动建议也指导很弱。核心问题在于，相关性是在任务层面判断的，而适用性取决于决策时刻的具体情境。

方法关键点：将个性化重新定义为“经验激活”，提出 training-free 框架 ExpActivator。执行过程中，ExpActivator 将每个新屏幕与冻结 GUI backbone 潜在空间中的历史状态进行匹配，并把对应动作作为参考提供给策略，只激活当前情境下可复用的经验。执行前，它只在当前时间与场景提供足够支持时激活 recurring intent，否则保持 abstain，避免不必要打扰。

关键结果：在四个 GUI backbone 上，ExpActivator 将轨迹内步骤成功率平均提升 28%，在所有 backbone 上取得最佳个性化执行效果，历史 token 使用量约为传统检索方法的 1/5；主动建议的 Matthews correlation coefficient 达到最强 baseline 的约 2.3 倍。
