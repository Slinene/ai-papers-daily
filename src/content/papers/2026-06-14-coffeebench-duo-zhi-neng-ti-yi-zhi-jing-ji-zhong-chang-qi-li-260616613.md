---
title: 'CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent
  Economies'
title_zh: CoffeeBench：多智能体异质经济中长期 LLM 代理的基准评测
authors:
- Issa Sugiura
- Daichi Hattori
- Kazuo Araragi
- Keita Ogawa
- Shota Onose
- Taro Makino
- Teppei Usuki
- Takashi Ishida
affiliations:
- Sakana AI
- KPMG AZSA LLC
arxiv_id: '2606.16613'
url: https://arxiv.org/abs/2606.16613
pdf_url: https://arxiv.org/pdf/2606.16613
published: '2026-06-14'
collected: '2026-06-27'
category: MultiAgent
direction: LLM 多智能体长期经济决策基准
tags:
- LLM agents
- multi-agent systems
- economic simulation
- long-horizon decision making
- supply chain
- benchmark
one_liner: 构建咖啡供应链多智能体经济模拟，评估 LLM 代理在 90 天内的利润与通信行为，揭示主动交易与 idle-drift 分化
practical_value: '- **多智能体供应链模拟可直接迁移至电商平台协同**：咖啡供应链的农民-烘焙商-零售商三层结构类似电商中供应商-平台-客户的链状关系，可用
  ReAct 代理模拟商家竞价、采购、定价，评估 LLM 在自动谈判与利润最大化中的表现。

  - **主动通信是盈利能力的关键指标**：高利润模型（GPT-5.5）日均发送 1.5 条消息以上，而低利润模型通信极少。在电商 Agent 设计中应鼓励主动询价、报价与协商，而非仅被动响应。

  - **警惕 idle-drift 失败模式**：Claude Haiku 4.5 在保持推理连贯的同时反复选择“等待下一天”，导致长达 40 天的不作为。实践中需为代理设置“活跃度监控”与强制唤醒机制（如超时重启、消息回复强制动作），防止陷入虚假的推理但无行动的状态。

  - **利润与销售额解耦，定价谈判比交易量更重要**：Gemini 3.1 Pro 与 Kimi K2.6 营收相近但利润差异大，原因在于前者实现了更高的平均售价。推荐系统或广告出价中同样适用：关注单次成交利润率而非仅追求
  GMV 量，Agent 应具备动态定价与 margin 核算能力。

  - **长期记忆管理是必须的工程化手段**：当上下文超过 160k tokens 时，论文采用模型自身对中间轨迹做摘要，保留首尾最新步骤。对构建长会话 Agent
  的推荐系统有直接启发：可定期对对话历史做压缩总结以适配上下文窗口。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 LLM 代理基准多为单代理与静态环境交互，但真实经济系统是多代理、异质的，代理需要长期沟通、谈判、交易并最大化自身利润。为此，论文提出 CoffeeBench，一个面向多智能体异质经济的长期决策基准。  

**方法关键点**  
- 环境模拟：咖啡供应链包含 2 个农民、2 个烘焙商、2 个零售商，彼此可任意交易，模拟周期 90 天。  
- 代理设计：所有代理基于 ReAct 框架，拥有共享工具（发消息、出价、接受报价、挂牌）和角色专属工具（生产、烘焙、设定零售价）。  
- 评估方式：待测模型控制其中一个烘焙商，其余 5 个代理由固定参考模型（Claude Sonnet 4.6）控制，目标最大化累计净利润。  
- 需求模型：基于价格竞争、忠诚度系数和季节性需求激增（春假节日 3 倍需求）。  
- 经济约束：每日固定成本、库存损耗（0.5%/天）、净 30 天信用期与逾期罚息、破产退出。  
- 长上下文处理：当历史超过 160k tokens 时，使用模型自己总结中间内容，保留开头和最近 20 步。  

**关键结果**  
- GPT-5.5 净利最高（$3,109），Claude Opus 4.7 紧随其后（$2,782），均大幅超越被动基线（-$2,765）。  
- Claude Haiku 4.5 净利为 -$630，出现“idle-drift”：平均有 40 天仅执行 `wait_for_next_day()`，尽管推理内容仍保持连贯。  
- 高盈利模型平均发送 88~140 条主动消息，而低盈利模型仅 14~52 条；各代理几乎不与同行竞争者通信（最多 1 条）。  
- 盈利能力不完全取决于库存或交易量：Gemini 3.1 Pro 与 Kimi K2.6 的营收、库存水平相近，但前者定价更高，利润高出 $1,241，表明有效的谈判与定价策略比交易量更重要。  
- 最佳模型仅达到简化理论净利上限（约 $23,800）的 13%，说明长期战略协调能力仍有极大提升空间。  
- 在纯收入激励压力测试中，未观察到循环交易或复杂串谋，显示当前前沿 LLM 在长期策略上仍不成熟。  

**核心一句话**  
“在长期多智能体经济环境中，主动沟通与有效的边际定价是 LLM 代理盈利的关键，而推理连贯不代表决策积极，需警惕 idle-drift 这类隐性失效模式。”
