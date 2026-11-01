---
title: 'ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender'
title_zh: ShallowDefend：利用浅层安全对齐实现多轮防御
authors:
- Qiyao Ma
- Xiaodong Liu
- Weiwei Yang
- Mingqian Feng
- Chengquan Guo
- Jialin Song
- Carolyn Buractaon
- Zhe Zhao
- Junshan Zhang
- Sandeep Atluri
affiliations:
- University of California, Davis
- Microsoft Research
arxiv_id: '2610.40627'
url: https://arxiv.org/abs/2610.40627
pdf_url: https://arxiv.org/pdf/2610.40627
published: '2026-10-29'
collected: '2026-11-01'
category: Training
direction: LLM 安全对齐 · 多轮防御
tags:
- safety alignment
- multi-turn defense
- reinforcement learning
- shallow alignment
- decision token
one_liner: 提出 Assess→Decide→Respond 框架，用显式安全决策 token 和自验证奖励训练多轮防御模型，在 14 个基准上取得最强多轮安全性
practical_value: '- 在对话式购物助手/客服 Agent 中，对安全敏感请求可引入“评估→决策→回复”阶段，强制模型先输出可解析的安全标签（如 SAFE/UNSAFE
  或分级），再基于该决策生成回复，使安全行为集中在可控 token span，便于审计与干预。

  - 采用自验证奖励：无需人工标注或 judge，只需比对决策标签与对话已知性质（如对抗轨迹或历史违规日志）作为规则奖励，可大幅降低安全 RL 训练成本；电商场景可用用户举报/售后投诉日志构造弱标签。

  - 利用浅层对齐机理做高效微调：安全/合规行为主要集中在前几个 token，训练时可以仅对决策 span 施加更强 KL 约束或集中梯度更新，避免主模型整体能力退化；对需要保持推荐/销售效用的系统，可通过只优化决策段减少
  helpfulness 损失。

  - 多轮攻击在电商场景同样存在（用户分多轮绕过商品推荐限制或诱导客服），该思路可作为多轮对话安全中间件，前置轻量决策模块或决策 token，无需大改主模型。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：安全对齐模型在直接拒绝有害请求上可靠，但同样请求分散在多轮对话中仍经常成功；机制根源是安全对齐“浅层”——安全行为集中在前几个输出 token，现有防御只监督回复表层形式，未让模型学习显式安全决策。

**方法**：提出 Assess→Decide→Respond 框架：防御者先评估用户意图，输出可解析的显式安全决策（token span），再基于该决策生成回复；在 payload 轮用 RL 训练该承诺。奖励可分两种：自验证规则奖励直接比对决策标签与对话已知性质，无需 judge/标注；或 LLM-as-judge 在分级决策空间上打分，支持安全重定向。

**结果**：在 2 个模型家族、14 个基准（安全、utility、helpfulness）上，防御者取得受控比较中最强多轮安全性，安全领先同时保持 utility，helpfulness 有适度代价。per-token KL 和干预探针表明训练效果集中在决定整个回复轨迹的短 deliberation 上，该决策是因果控制点；攻击者利用的浅层性反成为防御机制。
