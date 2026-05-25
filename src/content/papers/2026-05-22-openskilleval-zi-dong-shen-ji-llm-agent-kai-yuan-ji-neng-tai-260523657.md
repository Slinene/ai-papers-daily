---
title: 'OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents'
title_zh: OpenSkillEval：自动审计 LLM Agent 开源技能生态
authors:
- Jiahao Ying
- Boxian Ai
- Wei Tang
- Siyuan Liu
- Yixin Cao
affiliations:
- Singapore Management University
- Fudan University
- JD
arxiv_id: '2605.23657'
url: https://arxiv.org/abs/2605.23657
pdf_url: https://arxiv.org/pdf/2605.23657
published: '2026-05-22'
collected: '2026-05-25'
category: Agent
direction: Agent 技能生态审计与评估
tags:
- Agent
- Skill
- Evaluation
- LLM
- Benchmark
- Augmentation
one_liner: 提出动态任务生成与轨迹‑产出联合评测框架，揭示技能可用≠有效使用，且收益强依赖模型与设计先验
practical_value: '- **技能不一定带来提升，选型前需实测**：许多社区高分技能在实际任务中并未超越无技能基线，且会增加 3‑5 倍 token
  开销。在电商 Agent 中引入生成式推荐或工作流技能前，应先在自身任务上做成本‑性能对比。

  - **设计先验比流程约束更重要**：对视觉类输出（商品图、海报、详情页），技能内嵌的模板、参考代码等设计资产能有效拉高低能力模型的下限，而强约束（大量 MUST/NEVER）常导致多样性下降。可借鉴“资产优先”思路构建内部技能库。

  - **推理密集型任务需提供分析框架**：当前报表、数据洞察类技能因缺乏假设检验、对比分析等分析框架，增益有限。若用 Agent 做评论分析、销量归因，技能应嵌入因果推断步骤或统计检验模板，而非仅提供工具链。

  - **动态评测比静态基准更贴近业务**：论文自动从真实网页、数据集反向生成任务实例，保持用例与用户需求同步。电商场景可类似地利用商品链接、Campaign 素材自动构建
  Agent 评测集，持续跟踪能力变化。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
开源技能（Skills，即预定义的 agent 工作流指令）生态迅速膨胀，但技能质量参差不齐，不同模型‑框架组合如何真正利用技能、哪些技能在实践中能带来性能提升，均缺乏系统评估。静态基准无法反映动态变化的用户需求，也难以审计技能的真实效用。  
**方法**  
作者提出 OpenSkillEval，包含三个核心组件：  
- **动态任务生成**：针对 PPT 生成、前端网页设计、海报生成、数据可视化和报告生成五类任务，从真实网页、设计获奖作品、数据平台等高质量成品反向推测用户意图，自动生成结构化任务实例（>600 个），并通过 LLM 验证一致性。  
- **技能收集**：从 clawhub.ai、skills.sh 等社区筛选 30 个下载量较高的技能，按任务归类。  
- **双维度自动评估**：分析 agent 执行轨迹（是否读取技能、遵循步骤），并用视觉/内容/功能打分评判最终产物，对网页还加入交互模拟，对报表和图表验证数据准确性。  
**关键结果**  
- 默认设置下，agent 仅 48% 情况下显式读取技能文件；强制指引后虽提升至 94%，但仍有 10‑30% 的步骤被跳过或违背。  
- GPT‑5.5 和 Claude Opus 整体最强，GPT‑5.5 在 Codex 框架下 token 效率突出；DeepSeek V4 提供高性价比。  
- 技能并非普遍有效：视觉类任务中，资产丰富（模板、图标）的技能（如 ppt‑master）能将弱模型性能从 3.9 提升到 4.3 分，接近强模型无技能水平；但推理密集型任务（报表、数据洞察）几乎没有技能增益，大多数技能得分与无技能基线持平。  
- 输出多样性与约束强度负相关；丰富设计资产常伴随更高 token 消耗。  
**核心洞察**  
技能可用不代表 agent 会有效使用，效果高度依赖模型本身能力与框架配合；当前技能的价值主要在视觉先验，缺乏深度分析增量。
