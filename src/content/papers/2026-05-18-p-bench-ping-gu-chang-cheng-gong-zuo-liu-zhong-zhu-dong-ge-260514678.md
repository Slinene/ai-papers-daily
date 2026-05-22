---
title: 'π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows'
title_zh: π-Bench：评估长程工作流中主动个人助理智能体
authors:
- Haoran Zhang
- Luxin Xu
- Zhilin Wang
- Runquan Gui
- Shunkai Zhang
- Haodi Lei
- Zihao He
- Bingsu He
- Chicheng Qin
- Tong Zhu
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- The Chinese University of Hong Kong
- Fudan University
- University of Science and Technology of China
arxiv_id: '2605.14678'
url: https://arxiv.org/abs/2605.14678
pdf_url: https://arxiv.org/pdf/2605.14678
published: '2026-05-18'
collected: '2026-05-22'
category: Eval
direction: 主动个人助理智能体评估 · 长程交互与隐藏意图
tags:
- proactive agents
- personal assistant
- benchmark
- multi-turn
- hidden intents
- evaluation
one_liner: 提出π-Bench基准，量化智能体在多轮交互中主动发现与解决用户隐藏意图的能力
practical_value: '- **隐藏意图建模**：在电商对话推荐、客服助手等场景中，可显式定义"hidden intents"（如预算、品牌偏好、未明说的限制），并追踪agent是否主动询问或推断，以此作为主动性指标。

  - **跨会话依赖设计**：借鉴跨session依赖的构建方式，模拟用户长期画像的持续利用，评估模型能否从历史交互中提取偏好并应用于新任务，用于电商个性化推荐的持续学习。

  - **双维度评估解耦**：将评估拆解为Proactivity（是否减少用户认知负担）和Completeness（最终交付质量），避免只奖励“用户反复提供信息后完成任务”的假象，适合评估对话式商品搜索、谈判等场景。

  - **自动化用户模拟+评审协议**：使用user agent模拟用户并跟踪意图状态，结合checklist与rubric判分，可为Agent工作流提供可复现的自动化回归测试框架，加速迭代。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有Agent基准多预设清晰目标，忽略真实场景中用户常给出不完整请求，并依赖agent主动挖掘隐藏需求（如偏好、约束、上下文依赖）。长程工作流中，这种主动性至关重要，但缺乏评估。π-Bench针对此缺口，构建了强制要求agent在持续多轮交互中主动发现并解决隐藏意图的测试环境。

**方法**  
- **任务结构**：100个多轮任务，分属5种用户角色（研究员、营销、法务实习、药剂师、金融），每角色20个session构成一集，含跨session依赖。  
- **隐藏意图**：每个任务定义一系列隐藏意图（如格式约定、风险偏好、命名规则），agent需通过推断或聚焦提问主动解决；若未解决，用户代理会主动补充，但会记录为“由用户提供”。  
- **评估指标**：  
  - *Proactivity* = (直接完成数 + 推断后完成数) / 总意图数，衡量agent减少用户负担的程度。  
  - *Completeness* = 基于checklist（含规则和LLM打分）的任务完成度，衡量最终交付质量。  
- **交互机制**：用户代理跟踪意图状态，仅当所有意图终态后会话终止，确保完整的轨迹。

**关键结果**  
- 在9个前沿模型（GPT-5.4、Claude Opus 4.6等）上测试，**平均Completeness 52.1–67.6%，平均Proactivity 43.1–67.0%**，显示主动任务仍有巨大挑战。  
- **Proactivity与Completeness明显解耦**：如Kimi K2.5 Completeness达61.6%但Proactivity仅43.1%，说明模型可依靠用户多次补充信息完成高质量工作，却未主动减少交互负担；Seed2.0 Pro则相反。  
- **历史交互价值**：移除前序session后，Proactivity平均下降9.5个百分点，而Completeness仅降2.5点，证实跨会话记忆对主动意图分辨的关键作用。  
- 按任务类型分析，法律类任务**完成度高但主动性低**（84.1% vs 38.1%），而药物设计类主动性反而高于完成度，揭示不同工作流对模型能力的差异化要求。
