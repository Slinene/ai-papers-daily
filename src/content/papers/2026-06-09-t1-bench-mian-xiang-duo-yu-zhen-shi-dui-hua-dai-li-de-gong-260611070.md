---
title: 'T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains'
title_zh: T1-Bench：面向多域真实对话代理的工具调用高保真基准
authors:
- Genta Indra Winata
- Amartya Chakraborty
- Yuzhen Lin
- Swasthi P Rao
- Shikhhar Siingh
- Houhan Lu
- Nadia Bathaee
- Sriharsha Hatwar
- Paresh Dashore
- Anmol Jain
affiliations:
- Capital One
arxiv_id: '2606.11070'
url: https://arxiv.org/abs/2606.11070
pdf_url: https://arxiv.org/pdf/2606.11070
published: '2026-06-09'
collected: '2026-06-10'
category: Agent
direction: 多领域多轮工具调用Agent评估基准
tags:
- agent evaluation
- tool-calling
- multi-domain
- benchmark
- LLM agents
- conversational AI
one_liner: 构建覆盖25个领域、76个工具的自动评估基准，揭示LLM代理在多轮跨域场景下的工具调用短板与一致性挑战
practical_value: '- 对电商客服Agent离线评估可借鉴**双代理角色扮演**：用户代理按策略生成自然对话，助理代理调用工具，自动生成轨迹并复用，大幅降低人工成本。

  - 工具调用评估需分层：**工具选择、参数提取、输出精确匹配**三级，同时使用Pass@K/Pass^K衡量可靠性与一致性；尤其推荐Pass^K捕获单次成功但不可复现的模型。

  - 多域切换时性能坍塌严重（4域以上几乎归零），提示实用系统必须**强化上下文保持与状态追踪**，可引入论文中的Memory Module缓存工具结果，避免重复调用。

  - 工具数量是主要难度源之一（如Food & Dining 15工具），可考虑**层次化工具选择或分阶段推理**，先按意图聚类再在子域内调用，缓解动作空间爆炸。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现有LLM Agent基准多局限于单域或简化的单轮交互，难以反映真实客服场景中多域、多轮、工具调用的复杂性。评估端到端任务完成能力的缺失，导致无法衡量代理在长对话、跨域状态切换和工具编排中的真实可靠性。为此，T1-Bench构建了一个高保真、多域的自动评估平台，以系统衡量工具调用Agent的综合能力。  
**方法关键点**  
- **数据集**：涵盖11个单域（如酒店、航班、餐厅）和14个多域组合（2~4域叠加，乃至8、11域压力测试），共525个用户策略模板，76个可执行工具（搜索、过滤、预订、取消等）。  
- **自动对话生成**：USER AGENT按给定目标、用户画像和对话历史生成用户话语；ASSISTANT AGENT调用工具并生成回复；两者均受结构化策略约束，模拟真实交互轨迹。  
- **评估体系**：工具调用正确率（精确/召回/F1）、参数提取匹配度、工具输出完全匹配率；对话级别Pass@K/Pass^K（K=3）衡量一次性成功与重复一致性；LLM-as-a-judge 5分制评估帮助性、连贯性。  
- **实验模型**：评估了GEMMA4、GPT-OSS、GPT-5.4、Claude等12个开源及闭源模型。  
**关键结果**  
GEMMA4-31B-IT获最高Pass@K 61.33%，但Pass^K仅41.14%，反映一致性不足；Claude Opus工具调用准确率最高。随着域数增加，所有模型性能断崖式下降，4域以上Pass@K接近0。单域中，Food & Dining因包含15个工具，Pass@K仅3.5，远低于其他单域。人工评估与LLM评判相关性中等（Spearman ρ>0.45），验证了自动化评估的参考价值。  
**核心结论**  
工具数量和跨域上下文切换是当前LLM Agent的主要瓶颈，端到端任务成功率和可复现性仍需大幅提升。
