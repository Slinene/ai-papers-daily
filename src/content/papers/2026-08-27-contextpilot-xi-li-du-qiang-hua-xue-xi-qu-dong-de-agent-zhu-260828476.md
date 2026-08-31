---
title: 'ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained
  RL'
title_zh: ContextPilot：细粒度强化学习驱动的 Agent 主动上下文管理
authors:
- Zhuoshi Pan
- Qizhi Pei
- Junru Lu
- Honglin Lin
- H. Vicky Zhao
- Di Yin
- Xing Sun
affiliations:
- Tsinghua University
- Tencent Youtu Lab
- Shanghai AI Lab
arxiv_id: '2608.28476'
url: https://arxiv.org/abs/2608.28476
pdf_url: https://arxiv.org/pdf/2608.28476
published: '2026-08-27'
collected: '2026-08-31'
category: Agent
direction: Agent 主动上下文管理 · 细粒度 RL
tags:
- Proactive Context Management
- Fine-grained RL
- Long-horizon Agent
- Tool Use
- Credit Assignment
- Memory
one_liner: 提出 ContextPilot，扩展规划、长期记忆与软卸载工具，并用 context-aware partial rollout 与快照级信用分配训练
  Agent，在 32K 窗口下超越更大上下文基线。
practical_value: '- 在电商搜索/推荐多轮 Agent 中，把「上下文管理」显式工具化：提供 planning、结构化长期记忆（实体/事件/关系）和软删除/折叠工具，让模型自主决定何时写入记忆、何时压缩旧搜索结果，而不是依赖固定截断或总结规则。可直接借鉴
  ContextPilot 的工具设计，例如将搜索结果中高价值商品信息写入记忆，将低价值长文本 summarize/compress，并用可搜索索引恢复。

  - RL 训练时不要均匀探索所有工具调用：用上下文长度变化和生成熵变化给 context editing 动作打分，对高敏感动作（如删除关键历史、写入记忆）做额外分支采样。在推荐
  Agent 的 GRPO/RLHF 中，可以对“切换推荐策略/更新用户画像”等关键动作增加 rollout，避免把预算浪费在普通检索步骤。

  - 信用分配从 trajectory 级下沉到 snapshot 级：对某个中间上下文状态，取其所有后续分支的奖励均值作为该状态价值，再做组内标准化 advantage。这个
  trick 能降低方差，适合长链路推荐/搜索 agent 的中间决策优化，避免用一个最终结果奖励惩罚/强化无关节点的上下文编辑。

  - 业务上可复用“更小上下文窗口 + 更强性能”的结论：ContextPilot 以 32K 窗口超过 128K 原模型，token 使用稳定在 8-10K vs
  baseline 30K，直接降低线上多轮搜索/推荐的 LLM 成本与延迟。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长时程 Agent 任务需要多轮检索、整合和维护分散信息，工作上下文不断增长。已有 proactive context management 方法存在三类问题：工具集仅限搜索/删除/摘要，缺乏全局规划、长期记忆与自适应压缩；RL 探索对所有上下文管理动作一视同仁，未区分其影响差异；信用分配只做最终 trajectory-level reward，忽视了中间上下文编辑动作的细粒度贡献。

## 方法关键点
- **扩展工具集**：在 StateLM 基础工具上新增 planning、long-term memory（memorize/updateMemory/readMemory，结构化实体/时间/事件与跨 chunk 关联）和 soft context offloading（summarizeContext/compressContext/foldHistory）。
- **轨迹快照**：在 context editing actions 处将轨迹切分为 snapshots，并做 token-level loss masking，避免对重复输出做冗余优化。
- **Context-Aware Partial Rollout**：用 context variation ΔC 和 entropy variation ΔH 计算敏感度 S=αΔC+βΔH，从轨迹中选出高影响上下文管理动作作为分支点，分配额外采样预算，而不是对所有动作均匀探索。
- **Fine-Grained Credit Assignment**：对中间 snapshot S_i，用所有以 S_i 为前缀的 terminal trajectories 的平均 reward 作为 R(S_i)，再按 query 分组标准化得到 advantage；理论上方差降低至 1/n_S。
- **SFT 数据合成**：使用 teacher Qwen3.5-397B-A17B 和上下文管理 harness 动态暴露工具、过滤不当示范，最终保留 3,068 条轨迹、51,469 个 snapshots。

## 关键实验
- Long-context QA：在 NovelQA、∞Bench、LongMemEval-S、BrowseComp+ 上，ContextPilot-8B-RL 平均 69.40，超过 StateLM-8B-RL 的 65.85（+3.55）；14B 版本 72.20 vs 70.11。32K 上下文窗口表现优于 128K 原模型。
- Deep search：在 BrowseComp、BrowseComp-ZH、GAIA、xBench-DeepSearch 上，WebSailor-7B 平均 38.32 vs SUPO 36.31；WebExplorer-8B 平均 50.10 vs SUPO 49.09，整体超过 SUPO 约 1.51 点。
- Token 效率：BrowseComp 上 baseline 输入 token 增长至约 30K，ContextPilot 稳定在 8-10K。
- 消融：工具设计从原始工具平均 77.89 提升到完整工具集 87.16；RL 细粒度信用分配使 BrowseComp+ 从 SFT 48.84 提升到 54.18。

## 最值得记住的一句话
把上下文管理动作当作一等公民，用关键分支采样与快照级 reward 做细粒度 RL，可以在更小上下文窗口里同时提升 Agent 成功率与 token 效率。
