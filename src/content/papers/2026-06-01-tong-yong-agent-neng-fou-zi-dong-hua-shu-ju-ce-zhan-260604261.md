---
title: Can Generalist Agents Automate Data Curation?
title_zh: 通用 Agent 能否自动化数据策展？
authors:
- Feiyang Kang
- Hanze Li
- Adam Nguyen
- Mahavir Dabas
- Jiaqi W. Ma
- Frederic Sala
- Dawn Song
- Ruoxi Jia
affiliations:
- Virginia Tech
- University of Illinois Urbana-Champaign
- University of Wisconsin-Madison
- University of California, Berkeley
arxiv_id: '2606.04261'
url: https://arxiv.org/abs/2606.04261
pdf_url: https://arxiv.org/pdf/2606.04261
published: '2026-06-01'
collected: '2026-06-12'
category: Agent
direction: Agent 自动化数据策展评估
tags:
- Data Curation
- Agent
- Benchmark
- Scaffold
- Data Selection
one_liner: 引入 CURATION-BENCH 基准，发现通用 Agent 能执行数据策展但探索窄，方法适应支架可引导突破
practical_value: '- 在推荐数据管道中引入 **method-adaptation scaffold**：强制 Agent 每轮迭代引用、适配一项已有方法，可避免陷入局部超参（如域权重）调整，驱动真正的新策略探索。

  - 将 **迭代式数据策展** 作为新的计算维度：当数据预算固定时，将额外算力投入搜索更优的数据子集或重写策略，可能优于直接训练更多数据，这在电商推荐中可用于高效利用有限交互样本。

  - CURATION-BENCH 的 **数据隔离 + 污染审计 + 轨迹诊断** 设计，可直接迁移到构建推荐数据选择 Agent 的测试框架，确保可比性与可审查性。

  - **轻量策略列表（源平衡、质量过滤、多样性采样等）** 可帮助 Agent 快速生成候选，但需配合约束性协议（如强制证据锚定）才能真正改变执行行为，避免“vibe
  optimization”。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
训练数据是现代 AI 开发的关键设计变量，但数据策展（选择、过滤、重写等）仍然依赖大量人工迭代：提出策略、实验、评估、修订。现有基准要么固定数据评估静态策略（如 DataComp），要么让 Agent 优化训练配方而数据固定（如 AutoResearch），缺乏对 **Agent 迭代式数据策略发现能力** 的系统评估。本文追问：通用编码 Agent 能否自动化这个策展闭环？

**方法关键点**  
- 提出 **CURATION-BENCH**，固定模型、训练配置和评估套件，仅让 Agent 通过终端交互循环（检查数据→实现策略→提交→固定训练/评估→读取反馈→修订）优化数据策略。  
- 设计原则：① 数据隔离——Agent 只控制策展数据；② 终端真实——通过 CLI 操作，镜像实际工作方式；③ 污染审计——自动检测训练-评估泄露；④ 轨迹可读——记录每次策略、日志与分数，支持过程诊断。  
- 对比条件：**open‑prompt** 和四类支架——数据策略列表、参考文献、强制自研（每次需基于证据写假设）、强制方法适配（每次必须引用、实例化、修改已有方法）。  
- 主要实例化：在 **LLaVA‑665K** 上为 **LLaVA‑1.5‑7B** 选择 10k 样本的多模态指令微调任务。  

**关键结果**  
- open‑prompt 的通用 Agent（Claude Code、Codex 等）在 10 次迭代内达到或超越人类设计的 10k 基线（ICONS、ARDS），恢复约 **59%** 的全数据微调增益，仅用 1.5% 数据。  
- 轨迹诊断揭示 **执行–研究鸿沟**：Agent 主要调整源比例、长度阈值等局部变体，很少切换到新策略家族（新家族迭代仅 27%），且理由常弱证据化（vibe optimization）。  
- **强制方法适应支架** 改变执行轨迹：新家族迭代升至 67%，所有迭代均被证据锚定，浅层操作降为 0%。Agent 自主组合 **EL2N 高损失选择 + 助手损失噪声过滤**，得到 10k 策略平均分 34.9，超过 100k 的 ARDS 基线（34.1），且只用十分之一数据。  
- 增加 Agent 迭代次数至 50 继续带来平均提升，无平台化，表明迭代搜索本身是有效的“策展计算”。重写扩展验证了框架可支持更丰富的数据动作。  

**核心结论**  
当前通用 Agent 可运行策展环路，但实现可靠的数据研究需要 **支架式方法适应** 而非仅开放提示。支架设计是缩窄执行–研究鸿沟的核心杠杆。
