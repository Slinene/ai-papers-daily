---
title: 'Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks'
title_zh: Memento 3：通过反思式规则簿实现基于模型的递归自我改进
authors:
- Haoyu Zhao
- Zhengxu Yu
- Zhiyuan He
- Meng Fang
- Rasul Tutunov
- Haitham Bou-Ammar
- Weilin Luo
- Jun Wang
affiliations:
- University College London
- Huawei Noah's Ark Lab, UK
- University of Liverpool
arxiv_id: '2610.11794'
url: https://arxiv.org/abs/2610.11794
pdf_url: https://arxiv.org/pdf/2610.11794
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: LLM Agent 通过可执行世界模型递归自改进
tags:
- LLM Agent
- World Model
- Recursive Self-Improvement
- Rulebook
- Code-as-Model
- ARC-AGI
one_liner: 让冻结 LLM Agent 用自然语言规则簿+可执行代码作为显式世界模型，通过反思与验证递归自改进，在 ARC-AGI-3 全部 25 个游戏达到人类动作效率天花板
practical_value: '- 在电商搜索推荐 Agent 中，可把「用户意图/商品属性/召回规则」维护成 natural-language rulebook
  + 可执行代码，作为显式世界模型；用 action-observation 轨迹做 exact replay 验证，只接受能复现历史交互的规则/代码，避免 LLM
  幻觉。

  - 引入 Git 版本化记忆：每次规则修订/代码编译提交 commit，能 diff、回滚，便于线上排查与衰减实验；相当于把模型的「学习轨迹」变成可审计资产。

  - population 扩展：同时维护多个世界模型假设，共享交互证据，用行为等价类采样保证探索多样性；在不确定用户意图或流量分布变化时，可以做多臂/集成式探索，降低单一错误假设的自我确认风险。

  - 如果业务中需要 Agent 在无 reward 的交互环境中做事，可直接借鉴「反思→修订规则→编译为代码→验证」loop，把策略改进外置到可执行模型，而不是微调
  LLM 参数，适合 rapid iteration 和低成本 rollback。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
Agent 在陌生交互环境必须推断世界运作规则并随证据修正，有限观测可能支持多个解释，泛化难。模型必须保持可修订假设，避免过拟合历史。

## 方法关键点
- **Code as Model**：自然语言 rulebook（world_model.md）作为持久语义记忆，编译为 Python world_model_engine.py 可执行世界模型；规则簿表达可泛化假设，代码用于预测、replay、planning。
- **五阶段循环**：观察、反思、规则修订、编译、验证。验证要求 cell-exact replay 复现所有历史 transition + LLM 判断代码忠实于规则簿；只接受两者都通过的候选。
- **模型选择**用最小描述长度偏置（简化），允许信息寻求探索；无规划时探索未解决机制。
- **population 扩展**：N 个世界模型并行，共享交互历史，按行为等价类采样规划，修被 falsify 成员，减少单假设自我确认。

## 关键实验
- ARC-AGI-3 25 个公共游戏全部通关，mean RHAE 100.0 天花板，动作数 7,518，仅人类 17,135 的 44%。对比 baseline1 99.0 RHAE 使用 8,347 动作；其他系统未能全通。
- 消融：去除规则簿在 easy/medium/hard 游戏上动作数从 677 降到 617（-9%），agent turns 从 830 降到 678（-18%）。
- population N=2 在 wa30 动作数从 899 降到 597（0.66×），所有 level RHAE 100。
- Atari Pong：学习到的反馈控制器在三种开局 21:0 获胜，执行时无 LLM 调用。

## 最值得记住的一句话
让冻结 LLM 维护显式可执行世界模型，并用 replay 验证 + 规则簿语义一致性来接受更新，能把模型改进外置到记忆而非参数。
