---
title: Context-Grounded Skill Internalization for Vision-Language Agents
title_zh: 视觉语言智能体技能内化中的上下文对齐修正
authors:
- Jinlin Liu
- Yumeng He
- Qihan Huang
- Kevin Qinghong Lin
- Han Peng
affiliations:
- Ant Group
- The University of Hong Kong
- Shanghai Jiao Tong University
- University of Oxford
arxiv_id: '2611.30075'
url: https://arxiv.org/abs/2611.30075
pdf_url: https://arxiv.org/pdf/2611.30075
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: Agent 技能内化与上下文对齐
tags:
- skill internalization
- context misalignment
- vision-language agents
- SFT
- loss masking
- trajectory audit
one_liner: 提出 CGSI，用句级检测器定位失去技能支持的引用并做 loss mask/改写，大幅降低技能内化后的 CoMi 而不牺牲成功率
practical_value: '- 在把 SOP/技能文档/检索知识蒸馏进电商 Agent 或推荐解释模型时，若训练阶段移除原始 context，模型会在生成中引用不存在的“guidance/skill”。CGSI
  的检测思路可直接复用：对同一句话分别计算有技能 vs 无技能上下文下的 token log-prob 差（mean gap + peak-4 gap），再拼无技能上下文的
  last-layer hidden state，训练轻量 logistic 分类器即可定位 CoMi，避免逐条用大模型审计。

  - 工程上损失掩码只作用于被选中句子的 target tokens，且分母仍计全部 tokens，保持后续 token 条件依赖不变；论文显示只需掩码 0.08–1.21%
  的 tokens 就能显著降低 CoMi，比 down-weight 和随机掩码都有效。这适合直接在 trajectory SFT 数据管线里加一个轻量过滤层。

  - 如果业务里用 RL 继续优化 agent，先做 SFT 阶段 CoMi 修正再进入 RL 更划算：任务奖励不会消除引用幻觉，CoMi 水平基本由 SFT 决定；CGSI
  Mask/Rewrite + GRPO 在 ALFWorld 达到 96.35/95.62% 成功率，CoMi 仅 1.82/0.36%。

  - 成本方面，CGSI 用本地特征提取+分类器替代全量 VLM 审计，ARC 数据处理 API 成本从 $1378 降到 $165（Rewrite）或 0（Mask）；一次开发
  detector 后可跨轨迹复用。对小规模团队做 Agent 内化很有参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

技能内化的常见做法是：先用带技能上下文采样成功轨迹，再移除技能对同一批轨迹做 SFT。问题在于，轨迹里常包含“According to the skill/guidance…”这类依赖技能上下文的引用；移除技能后这些引用失去支撑，但仍是训练目标。论文将这种现象定义为 context misalignment（CoMi），并量化其严重性：成功 teacher 轨迹中 CoMi 比例在 ALFWorld/WebShop/ARC-AGI-1 上为 18.3–75.4%，直接 skill-dropped SFT 后，测试轨迹 CoMi 达 12.2–46.0%。

**方法关键点**

- **问题形式化**：用 VLM auditor A(·) 定义 paired label：b = A(u; c−) [1 − A(u; c+)]，只标记“有技能时成立、移除技能后不成立”的引用。
- **CGSI 流程**：generate with skill → sentence detector → mask/rewrite → no-skill SFT。
- **检测器特征**：对同一句分别计算 c+ 与 c− 下的 token log p 差，聚合为 mean gap 和 peak-4 gap；再拼无技能上下文的 last-layer hidden state（mean pool + L2 normalize），标准化后训练 logistic classifier；使用 class-balanced BCE + L2。
- **修正方式**：Mask 只掩码被选中句子的 target tokens，保持 teacher-forced prefix 不变，正常项仍计全部 tokens；Rewrite 用 VLM 将选中句子改写为不依赖技能的表达。
- **成本控制**：检测器开发一次后冻结复用，避免对每条轨迹做完整 VLM 审计。

**关键实验**

在 ALFWorld、WebShop、ARC-AGI-1 上，用 Qwen3.5-4B/9B 做 full-parameter 与 LoRA SFT。SFT (skill dropped) 比 SFT (skill kept) 成功率高 3.8–8.0 点，但 CoMi 从 0–2.2% 升至 12.2–46.0%。CGSI (Mask) 在六个设置下相对直接 fine-tuning 降低 CoMi 72.5–94.6%，且成功率无显著下降：WebShop-4B CoMi 从 46.0% 降到 3.4%，ALFWorld-4B 在 1.25 小时训练达到 85.0% 成功率，优于 Skill0 的 81.0%/19.1 小时。CGSI 只掩码 0.08–1.21% 的 target tokens，随机掩码相似比例仍剩 49.4% CoMi，说明定位是关键。后续 RL 实验显示，GRPO 不能自动消除 CoMi：SFT (skill dropped) 后 RL 仍保留 69–86% 的 CoMi，而 CGSI 修正后仅 0.4–5.2%。ARC-9B 数据处理 API 成本从 VLM Audit (Rewrite) 的约 $1378 降至 CGSI (Rewrite) 的 $165，Mask 为 0。

**最值得记住的一句话**：CoMi 是技能移除式 SFT 的隐性代价；用 log-prob 差 + hidden state 的轻量句级检测器做 loss mask/rewrite，可在几乎不损失成功率的情况下把 CoMi 降一个数量级。
