---
title: 'Remembering Has a Price: Learning Memory Worth under Resource Constraints'
title_zh: 资源约束下学习记忆价值：TokenWorth 终身记忆框架
authors:
- Guannan Lai
- Zi-Yang Bai
- Jun-Peng Jiang
- Han-Jia Ye
affiliations:
- Nanjing University
- National Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2610.26453'
url: https://arxiv.org/abs/2610.26453
pdf_url: https://arxiv.org/pdf/2610.26453
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 资源受限终身记忆价值学习
tags:
- Lifelong Agent
- Memory Worth
- Resource Constraints
- RFM
- Online Learning
- LLM Agent
one_liner: 提出 TokenWorth，在线学习 query-dependent 记忆价值并统一用于检索与记忆淘汰，在资源受限终身智能体任务中成功率最高且输出
  token 最少
practical_value: '- 在电商导购/客服 Agent 的长程记忆或知识库检索中，不要只按 embedding/BM25 相关度取 top-k；可以增加一层轻量
  query-dependent 价值打分，融合历史成功率、可靠性、最近使用等特征，用执行结果（成交/点击/解决率）在线更新，统一指导检索和记忆淘汰。TokenWorth
  的 linear base scorer + RFM 残差可以在几百条反馈内工作，适合预算敏感场景。

  - 用“任务级结果”作为稀疏监督时，目标设为 \(2r-1\) 即可，不必追求反事实归因；这能避免昂贵重执行。对落地来说，可以把成功交互存为候选 memory，把失败反馈用于更新被注入记忆的价值，低成本积累负信号。

  - 记忆管理借鉴 admission/evict 策略：库满后，新经验要么足够新颖，要么 probe-averaged worth 显著超过最差/最优记忆才准入，否则可替换低效用近邻；淘汰时按最近一批
  probe queries 的平均价值最低者出局。类似做法可用于在线更新推荐 Agent 的 few-shot 示例库或商品卖点素材库。

  - 评估记忆/检索模块时，应像该工作一样固定联合预算（输出 token、步数、存储容量、注入长度），并报告“每 token 收益”；否则复杂 reflection/skill
  模块容易在业务中被高估。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
在终身 Agent 场景中，生成、交互和记忆预算通常都受限。已有记忆方法在资源宽松时可能有效，但作者发现当输出 token、交互轮次、记忆容量和注入长度被联合收紧后，多种复杂记忆方法（MemRL、Reflexion 等）相比简单 RAG 甚至无记忆 agent 没有显著优势，甚至更差。核心不再是“检索相关经验”，而是学习哪些经验值得保留和复用。

**方法关键点**  
- 把问题形式化为资源受限终身 agent：固定预算 \(C=(O_{max},J_{max},B_{max},K_{max},L_{max})\)，记忆策略要最大化任务成功率。  
- TokenWorth 用轻量 controller 学习 query-dependent 记忆价值：线性 base scorer 捕获稳定模式，RFM 残差校正捕获非线性 query-specific 偏差。  
- 监督来自稀疏执行反馈：任务 reward \(r_t\in\{0,1\}\) 转为 \(y_t=2r_t-1\)，只对实际选中的 memory 生成 residual target；不做反事实重执行。  
- 两时间尺度 RFM：快速 KRR 拟合残差，慢速 AGOP 更新特征度量。  
- 价值同时用于检索和记忆生命周期：probe-averaged worth 做 admission/evict，只保留成功经验，满后按价值淘汰，新记忆需新颖性或显著价值提升。  
- 不需要 backbone 更新、task replay 或额外 LLM 调用。

**关键结果数字**  
在 LifelongAgentBench 的 DB/OS/KG 三个环境、本地 Qwen2.5-14B 和 API DeepSeek-V4 两种部署下，TokenWorth 成功率全部最高：本地 DB 65.0%（RAG 33.0%）、OS 59.4%、KG 36.7%；API DB 62.2%（此前最好 32.2%）。同时输出 token 全部最低，本地 DB/OS/KG 分别较无记忆 agent 少 9.3%/51.5%/18.7%，API 为 31.6%/58.3%/21.3%。消融显示 Base only 64.2%，加入 RFM 但固定度量降至 63.0%，加上 AGOP 后恢复至 65.0%。

**最值得记住的一句话**  
资源受限下，记忆系统增益来自“学哪些值得记”，而不是“记更多”；轻量在线价值估计 + 有界淘汰，比复杂记忆/反思机制更有效。
