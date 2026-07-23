---
title: 'DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable
  Environment'
title_zh: DeepSearch-World：确定性搜索环境中智能体的自蒸馏训练框架
authors:
- Xinyu Geng
- Xuanhua He
- Sixiang Chen
- Yanjing Xiao
- Fan Zhang
- Shijue Huang
- Haitao Mi
- Zhenwen Liang
- Tianqing Fang
- Yi R. Fung
affiliations:
- HKUST
- Tencent
- HKUST(GZ)
arxiv_id: '2607.07820'
url: https://arxiv.org/abs/2607.07820
pdf_url: https://arxiv.org/pdf/2607.07820
published: '2026-07-07'
collected: '2026-07-23'
category: Agent
direction: Agent 自进化 · 确定性搜索环境
tags:
- Self-Distillation
- Agent
- ReAct
- Multi-hop QA
- Wikipedia
- Deterministic Environment
one_liner: 在确定性 Wikipedia 离线环境中，通过 scaffold 教师轨迹生成与监督自蒸馏，让 9B 搜索智能体自进化至开源领先水平
practical_value: '- **构建确定性离线环境用于 Agent 训练**：可借鉴 Wikipedia 离线索引 + 工具模拟，将线上搜索/浏览工具映射为确定性函数，便于大规模生成可验证的训练轨迹，避免线上环境噪声与成本。

  - **Scaffold 教师轨迹中的规划与反思注入**：利用三阶段教师 (Plan-Act-End) 生成包含进度追踪、反思与错误恢复的轨迹，再通过 Scaffold-to-ReAct
  转换将结构化状态、反思改写为 ReAct 的 thinking 块，让普通 ReAct agent 学会规划、记忆与自我纠错。

  - **自进化循环的异步生成与重要性采样混合**：生成与训练解耦，使用指数衰减的重要性采样混合多轮轨迹，优先新高质量样本同时保留早期数据以防遗忘，稳定提升长程工具使用能力。

  - **可微调的动作/工具使用行为示例**：全流程以 SFT 实现，无需复杂 RL 奖励设计，从正确性验证 + 质量过滤即可提升工具调用成功率与多跳推理深度，适合快速在业务
  Agent 中尝试自进化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有搜索 Agent 的自进化受限于稀疏奖励（RL）或固定教师分布（SFT），缺少对中间工具使用步骤的密集过程监督。长程交互中故障来源（查询表达、工具选择、证据抽取）难以定位，因此需要一个可验证的确定性环境来暴露步骤级反馈。

**方法关键点**：
- 构建 DeepSearch-World 离线 Wikipedia 环境，含 420K 多跳 QA 任务，通过实体级随机游走生成；工具为 BM25 搜索与 SQLite 页面访问，观察和噪声完全可控，并支持实体级进度验证。
- 设计 Scaffold 教师：三阶段 Plan-Act-End，维护结构化状态（已完成/待办列表、经验、证据），环境在检索失败时提供递进式反思，引导查询改写与恢复。
- 自进化循环 DeepSearch-Evolve：每轮由当前模型生成 Scaffold 轨迹，经答案正确性过滤和 LLM 质量过滤后，转换为标准 ReAct 格式（将进度状态与反思重写入 thinking 块），然后用 SFT 更新模型。使用重要性采样混合多轮数据 (γ=0.5)。
- 最终模型再经少量线上 GRPO 微调缓解 sim-to-real 差距。

**关键结果**：
- DeepSearch-World-9B 在 BrowseComp 达 31.2%，GAIA 61.5%，HotpotQA 93.4%，远超微调前 Qwen3.5-9B-Instruct (+23.8 到 +48.1 点)，并接近或超过多数开源 Agent（如 Marco-DR 31.4% BrowseComp）。
- 从工具使用行为看，平均交互轮次从 4.7 升至 18.0，visit 调用从 0.9 升至 5.4，高级能力评分由 19% 升至 70%。
- 消融表明：拒绝采样 + 质量过滤联合使用、反思重写与状态内部化均对最终效果有显著贡献；任务池规模从 100K 扩至 420K 可进一步提升和稳定后期进化。

**一句话总结**：可验证的确定性搜索环境使得 Agent 无需蒸馏更强模型就能通过自生成轨迹的监督蒸馏持续进化。
