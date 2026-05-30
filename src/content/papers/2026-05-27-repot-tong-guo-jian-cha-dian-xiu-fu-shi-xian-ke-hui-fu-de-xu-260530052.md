---
title: 'REPOT: Recoverable Program-of-Thought via Checkpoint Repair'
title_zh: REPOT：通过检查点修复实现可恢复的程序化思维
authors:
- Parsa Mazaheri
affiliations:
- University of California, Santa Cruz
arxiv_id: '2605.30052'
url: https://arxiv.org/abs/2605.30052
pdf_url: https://arxiv.org/pdf/2605.30052
published: '2026-05-27'
collected: '2026-05-30'
category: Agent
direction: 可恢复的 LLM 规划 · 检查点修复
tags:
- Program-of-Thought
- Checkpoint Repair
- Planning
- Verified Replay
- Suffix Repair
- LLM
one_liner: 在一次性程序化思维中引入确定性验证重放与单次修复调用，将静默失败变成可恢复的推理过程。
practical_value: '- **Agent 动作序列的断点恢复**：当 Agent 生成多步操作时，可利用环境接口实时验证每一步，保留已成功的动作前缀，仅让
  LLM 从失败点续写剩余动作，避免全盘废弃，节省 token 成本。

  - **电商推荐策略的鲁棒执行**：例如生成式推荐产生的 action 序列在真实环境（库存、价格等约束）中可能中途失效，借鉴 REPOT 的检查点机制，可保留前缀合法动作，仅修复后缀，提升端到端成功率。

  - **成本控制的恢复预算**：REPOT 只对首次失败的问题额外调用一次 LLM（~14% 的问题），保持平均成本接近原 POT，适合线上高吞吐场景，可作为
  Agent 类系统的基线恢复策略。

  - **环境即权威验证器**：利用确定性环境（如数据库状态、API 返回码）做真实的下一步状态验证，比模型自我反思更可靠，在电商有明确规则域（库存校验、优惠券有效期等）中可直接复用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 在生成多步规划（如程序化思维 PoT）时，一次非法动作就会导致整个轨迹静默失败，而现有补救方法（多次采样、树搜索、自我批评）要么成本高，要么无法利用已成功的部分。该工作瞄准的是“可恢复的执行崩溃”——多数失败轨迹拥有很长的有效前缀，只需修复错误后的后缀。

**方法关键点**：
- **确定性验证重放**：将候选动作序列逐步送入环境，记录直到第一个无效动作之前的所有合法动作（验证前缀），返回失败点状态和错误信息，无需额外 LLM 调用。
- **单次后缀修复**：仅当重放未达目标时，用一次 LLM 调用从检查点（已验证状态）续写剩余动作，同时展示最后 4 个合法动作和验证器错误信息。
- **自适应路由**：当验证前缀过短时（<15% 总长度），改回全新重试（ADAPTIVEREPOT），避免在低质量前缀上浪费修复调用。

**关键实验**：
- 在 PUZZLEZOO-775（覆盖河内塔、跳棋、渡河、积木世界）上，REPOT 在四个闭源模型上比 PoT 提高 +3~+11pp，最强配置（gpt-5.4-mini-medium）达到 96.9% vs 86.3%。
- 与等成本（首次失败后重试一次 PoT）基线相比，REPOT 在 Gemini 上显著胜出（+3.8pp），但在能力较弱的模型上落后，呈现能力缩放规律。
- 在控制恢复基准 DERAIL-550 中，提供检查点状态的方法恢复率达 80.7%，而仅错误反馈仅 20.7%，证明检查点信息是关键恢复信号。
- 在 PLANBENCH Blocksworld 上复制了提升（+1.1~+11.4pp），开源模型复制了能力缩放趋势。

**核心结论**：可信的检查点状态，而非文本自我批评，是恢复规划的关键信号；REPOT 以极低额外成本（平均 1.06× PoT LLM 调用）将一次性规划升级为可恢复执行。
