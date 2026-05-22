---
title: 'Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet
  Tasks via Reinforcement Learning'
title_zh: Spreadsheet-RL：在真实 Excel 环境中通过强化学习训练电子表格代理
authors:
- Banghao Chi
- Yining Xie
- Mingyuan Wu
- Jingcheng Yang
- Jize Jiang
- Zhaoheng Li
- Shengyi Qian
- Minjia Zhang
- Klara Nahrstedt
- Rui Hou
affiliations:
- University of Illinois Urbana-Champaign
- Meta
arxiv_id: '2605.22642'
url: https://arxiv.org/abs/2605.22642
pdf_url: https://arxiv.org/pdf/2605.22642
published: '2026-05-20'
collected: '2026-05-22'
category: Agent
direction: 电子表格代理 · 强化学习训练 · 工具设计
tags:
- Spreadsheet Agent
- Reinforcement Learning
- GRPO
- Tool Use
- Domain-Specific
- Microsoft Excel
one_liner: 首个面向电子表格的端到端 RL 后训练框架，将 4B 开源模型 Pass@1 从 12.0% 提升至 23.4%
practical_value: '- **多步交互的 tool harness 设计**：将电子表格操作抽象为专用工具（find_cells、fill_formula、delete_rows），并强制遵循
  inspect→modify→verify 的工作流。这种结构化 action space 对于长链路 agent 的稳定 RL 训练至关重要，可类比于电商多步任务中的工具路由与执行规则设计。

  - **无 SFT 的 RL 冷启动技巧**：在 RL 前通过 spreadsheet-native harness 提供更强初始策略（Pass@1 从 12.0%
  到 15.6%），避免完全依赖代码生成导致的低级失败。对于难以获得 step-by-step 标注数据的业务场景（如库存规划、价格调整），可先构建结构化工具和交互协议，再直接应用
  GRPO。

  - **异步奖励计算模式**：由于 Excel 重计算耗时且依赖 Windows，采用异步提交-轮询的 verifier 实现可扩展的 RL 训练。这与电商 agent
  需调用线上服务获取真实反馈的场景相似，可借鉴其 per-rollout 工作空间隔离和异步奖励设计。

  - **领域泛化的数据构造策略**：通过自动化管道从论坛收集初始-最终电子表格对，并引入领域模板生成 Domain-Spreadsheet 基准。对于生成式推荐或
  agent 的多领域迁移，这种低成本合成专业任务的方式值得参考，尤其当业务域缺乏标注数据时。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
电子表格（Excel/Google Sheets）是数据密集型工作流的核心工具，但现有 prompt-based 电子表格代理依赖通用大模型，难以完成真实场景中的复杂多步操作。强化学习微调在数学、编码、计算机使用等领域已验证有效，但应用于电子表格面临两大挑战：① 缺乏大规模初始–最终电子表格对用于训练；② 代理必须从弱交互策略起步，而获取逐步监督数据成本极高。  

**方法关键点**  
- **自动化数据管道**：Spreadsheet Data Agent 从在线论坛自动收集讨论帖，利用强 coding agent（如 Claude Code）根据任务描述和解决方案生成 oracle 最终电子表格，并经规则过滤，最终获得 5928 个高质量训练任务。  
- **电子表格智能体交互 Gym**：基于真实 Microsoft Excel 的强化学习环境，提供 per-rollout 文件系统隔离工作区，支持并发训练。  
- **结构化工具 harness**：将电子表格操作封装为 spread‑native 工具（find_cells、inspect_range、fill_formula、delete_rows 等），强制代理遵循 inspect → modify → verify 工作流，并通过并发只读调用、串行写入操作的路由规则降低执行错误，使初始 Pass@1 从 12.0% 提升至 19.3%。  
- **异步 RL 训练**：采用 GRPO 与结果奖励（所有单元格精确匹配），并设计异步提交-轮询的 verifier 以适应 Excel 重计算的耗时，使用 VeRL 框架支持多轮交互训练。  

**关键结果**  
- 在 SpreadsheetBench（912 任务）上，Qwen3-4B-Thinking-2507 经 harness + 工具 + RL 训练后，Pass@1 从 12.0% 依次提升至 15.6% → 19.3% → 23.4%，超越 OpenAI o3 的 23.3%。  
- 新构造的 Domain-Spreadsheet 基准（1660 任务，涵盖金融、供应链等 7 个领域）上，RL 训练后整体 Pass@1 从 8.4% 提升至 17.2%，金融领域提升最大（如中级从 7.7% 到 16.2%）。  
- 训练动态显示，随着 RL 进行，响应长度和交互轮次均显著下降，同时代理更倾向于输出备用计划和 fewer speculative statements，表明 RL 同时提升了效率和合规性。
