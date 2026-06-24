---
title: 'Dialogue to Discovery: Attribute-Aware Preference Elicitation for Conversational
  Product Search Assistants'
title_zh: 对话到发现：属性感知的对话商品搜索助手
authors:
- Sarthak Harne
- Natwar Modani
- Debabrata Mahapatra
- Shubham Agarwal
affiliations:
- Adobe Research
- Microsoft Research
- UC Berkeley
arxiv_id: '2606.24194'
url: https://arxiv.org/abs/2606.24194
pdf_url: https://arxiv.org/pdf/2606.24194
published: '2026-06-23'
collected: '2026-06-24'
category: RecSys
direction: 对话产品搜索 · 属性感知策略
tags:
- Conversational Product Search
- attribute-based preference elicitation
- patience modeling
- LLM
- user simulation
- Amazon Reviews
one_liner: D2D通过属性不确定性引导与推荐时机控制，成功率提升22–30%，弃标率降低，成功对话缩短27.5%
practical_value: '- **属性选择的可解释启发式**：用属性不确定性（APU）与累积熵（ACE）的乘积选择询问属性，比完全依赖 LLM 判断更可控、可解释，可直接迁移到电商搜索助手的槽位填充（slot-filling）模块。

  - **推荐时机的置信区间重叠准则**：当 top- k 项目得分置信区间重叠度低于阈值时才推送商品，避免过早推荐导致用户反感。这一规则简单、无模型依赖，适合嵌入实际对话推荐引擎的决策层。

  - **耐心建模用于仿真评估**：结合推荐相关性、问题冗余度、认知负荷等多因素更新用户耐心，构建更真实的离线用户仿真，可用于 A/B 测试前的策略选优。

  - **模块化 LLM 调用降低成本**：将属性偏好更新、推荐决策、响应生成拆分成独立的小模型调用，每轮输入 token 远小于全上下文 LLM，实测输出 token
  减少 51%，适合成本敏感的在线服务。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
传统关键词搜索返回过多结果，对话搜索助手（CPS）虽自然但面临两大挑战：过度追问导致用户流失，过早推荐不符合偏好则体验差。现有方法多假设用户无限耐心，未显式建模对话质量与弃标的关系，亟需能平衡提问效率与推荐时机的框架。  

**方法关键点**  
- **属性偏好画像（AVP）**：每轮用 LLM 更新用户对所有属性-值对的偏好分数及不确定性，进而计算项目得分与置信区间。  
- **推荐时机决策**：计算 top-1 项目的置信区间与其余项目的重叠比例（TOI 集合），若重叠度低且项目数量≤展示槽数才推荐，否则继续提问。  
- **属性选择**：同时考虑两个信号——属性偏好不确定性（APU，反映系统对用户偏好的未知程度）和属性累积熵（ACE，衡量该属性区分 top-n 产品的能力），乘积排名后选取最关键的属性进行询问。  
- **用户耐心模型**：综合推荐相关性、问题重复性、信息量、认知负荷四个因子动态更新耐心值，耐心耗尽即终止会话，用于离线仿真。  

**关键实验**  
- 数据集：从 Amazon Reviews 中抽取 Electronics、Home & Kitchen、Sports & Outdoors 三个类别，每类 2000 个商品，筛选 200 名用户，用最新评价商品作为目标。  
- Baseline：传统 BM25 与稠密检索，以及零样本 LLM 推荐（ZS Recommender）和加入耐心提示的 Full-LLM。  
- 主要结果（D2D vs. Full-LLM 最佳基线）：目标查找成功率相对提升 22.2–29.9%（平均 52.5% vs. 41.7%），会话弃标率降低 6.6–16.1%（平均 45.3% vs. 51.5%），成功会话的平均回合数缩短 27.5%，输出 token 减少约 51%。用户研究也表明 D2D 的提问精准度和推荐时机更受偏好。  

**核心洞察**：结构化的属性驱动对话设计，配合基于置信区间的推荐时序控制，比单一扩大 LLM 上下文更有效且高效。
