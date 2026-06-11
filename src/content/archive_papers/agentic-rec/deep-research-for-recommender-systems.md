---
title: 'Deep Research for Recommender Systems'
authors: Kesha Ou, Chenghao Wu, Xiaolei Wang, Bowen Zheng, …, Wayne Xin Zhao, Ji-Rong Wen (9 人)
affiliation: Renmin University of China (人民大学高瓴) × Meituan (美团)
date: 2026-03
venue: arXiv
topic: agentic-rec
topic_name: Agentic Recommendation
topic_icon: 🧭
idea: |
  把推荐系统的最终产物从「一串商品列表」重定义为「一份帮用户做决策的研究报告」——借 Deep Research 范式让系统替用户去逛、去比、去综合。双 Agent：T5+GRPO 的轨迹模拟 Agent 生成「探索→决策」行为轨迹并召回候选，DeepSeek 驱动的自进化报告 Agent 把候选按多维兴趣拆成榜单+理由写成报告。核心是交互范式从「被动过滤器」转向「主动 agent 助理」。
paperUrl: https://arxiv.org/abs/2603.07605
codeUrl: https://github.com/RUCAIBox/RecPilot
tags:
- Agentic Recommendation
- Deep Research
- Trajectory Simulation
- GRPO
- Report Generation
unverified: false
detail:
  contribution: |
    首次把推荐系统的交互界面从 item-centric 列表重构为 user-centric 决策报告，提出推荐的「Deep Research 范式」。落地为 RecPilot 多智体框架：(1) 用户轨迹模拟 Agent——把推荐建模成生成式「探索→决策」轨迹，用 T5 编解码 + GRPO 强化学习 + 免模型过程奖励，替用户探索 item 空间并召回候选；(2) 自进化报告生成 Agent——把候选按多维兴趣拆解并行排序，结合 rubric+经验双通道写成可解释报告，并用免训练自进化持续更新偏好。轨迹模拟 Recall@5 相对最强基线 +52%，报告新颖性对最强 Agent 基线取得 77% 胜率。
  background: |
    推荐技术从协同过滤→深度模型→LLM 一路演进，但交互范式几十年没变：系统只负责把相关商品摆出来，用户仍要自己逐个点开、对比、综合才能决策，认知负担重(高价品尤甚)。作者刻意脱下算法研究员身份、站用户视角发现：技术进步并没简化决策过程，推荐系统始终是「被动过滤器(tool)」而非「主动助理(assistant)」。灵感来自 Deep Research——搜索领域已把「用户读一堆网页」变成「Agent 替你读完写报告」，作者主张推荐同理：让系统而非用户承担探索苦活，产出带解释、可信赖的报告，把推荐从被动过滤转为主动 agent 服务。
  method: |
    双 Agent。① 轨迹模拟 Agent：把 item ID 作为原子 token 并入 T5 词表，同类连续行为压成动作前缀做 Session-Aware Tokenization；先 SL(下一个商品 token 预测,公式2)打底并端到端学出 item ID embedding(协同语义空间)；再 GRPO 强化学习，复合奖励=结果奖励(末位预测命中真实购买)+过程奖励(Max-Sim：生成商品与真值商品 ID embedding 的最大余弦相似度均值,跳出 ID 硬匹配以保留行为多样性,公式4)+约束奖励(长度指数衰减+格式硬罚)；推理时 top-p 采样 N 条多样轨迹,每条末态 hidden state 过 item embedding 矩阵取 top-K,合成 N×K 候选按整条轨迹 log-likelihood 去重排序。② 自进化报告 Agent(DeepSeek-V3.2)：rubric(属性优先级分,骨架)+经验记忆(key-value,情境化隐式偏好,血肉)双通道刻画偏好；LLM 把轨迹压成意图摘要→检索经验→拆成多个属性子集(aspect)→每 aspect 内按 rubric 加权打分并行排序(公式11)→跨 aspect 求和成总榜→写成「轨迹+意图+总榜+分维度榜+理由」四段报告(公式12)；免训练自进化=best-of-n(按真实购买 NDCG 选最优榜单反更新 rubric)+对比式经验固化+从 click session 挖负偏好补经验(不污染 rubric)。
  experiments: |
    数据 Tmall(click/collect/cart/purchase 四行为)，过滤<5次后 28.8万用户/55.6万商品/129万 session，预测 purchase。轨迹模拟骨干是极小 T5(hidden 仅 64,2+2 层)，报告骨干 DeepSeek-V3.2，经验文本检索用 Qwen3-Embedding-8B。轨迹模拟主结果：Recall@5 0.1025(最强基线 MB-STR)→0.1557 即 +52%，NDCG@5 +49%；消融 w/o RL 跌最狠(R@5→0.1187)证明 RL+过程奖励是关键,top-p=0.95/temp=1.0 最佳、轨迹越长越好。报告生成(6 维 1-5 分,真人+Gemini-3-flash 模拟用户,Cohen Kappa 0.7064)：RecPilot 均分 4.14 vs 最强基线 Plan-and-Solve 3.88 / GPT-5.2 3.83，优势主要集中在新颖性(4.09 vs 所有基线≤3.13)，对 Plan-and-Solve 新颖性胜率 77%、清晰度 66%、准确率 60%。但报告侧消融差异极小(4.14→4.08~4.10)。
  pros: |
    范式 framing 是最大价值——首次把推荐输出从 item list 重定义为 decision report，方向性强、想象空间大；Max-Sim 协同语义过程奖励巧妙解决生成式推荐 RL 奖励稀疏 + ID 硬匹配扼杀多样性的通病；多维兴趣拆解并行排序、rubric+经验双通道、免训练自进化是合理的工程组合；极小 T5 也能 +52% 说明收益来自范式而非堆参数；真人+LLM 双评测且报告 Cohen Kappa=0.71，比多数 LLM-as-judge 论文严谨。
  cons: |
    只有 Tmall 单数据集单域(电商)，跨域泛化完全未验证，对主打新范式的论文是硬伤；核心卖点「减少用户努力」全靠主观 5 分制，没有真实决策耗时/点击次数的客观度量,claim-evidence 缺口明显；方法-指标可能循环——多维拆解显式去挖「额外兴趣」,而 Novelty 指标定义恰好是「是否提出额外兴趣」,77% 新颖性胜率说服力打折；报告侧消融差异在噪声内(4.14→4.10),难证各组件真有用,暗示报告增益大半来自结构化格式本身；原子 ID 方案对长尾/冷启动 embedding 学不动(故过滤<5次),item pool 扩展性未解(作者自己点了 large-scale item pool 效率是 open problem)；报告生成 max 16384 token + 多次 LLM 调用,延迟/成本未量化。
  inspiration: |
    对电商生成式召回/Push 的直接借鉴：(1) 把「探索→决策」轨迹当显式 reasoning chain 来生成、再用末态做候选召回,比纯判别式多了可解释中间推理,可嫁接到生成式召回；(2) Max-Sim 协同语义过程奖励正解决「生成式推荐 RL 奖励太稀疏/ID 硬匹配」通病,可试用语义相似度替 0/1 命中做 reward(对 simulator click-AUC 那条线可能是新杠杆)；(3) 要落地百万/亿级 item 必须把原子 ID 换成语义 ID(码本分解),否则长尾+冷启动直接崩,过程奖励也要从 item 向量余弦改成码序列层面相似度；(4) 报告范式真正缺的是客观省力度量,落地前应先建真实决策耗时/转化的 online 评测。作者给的务实出路是「快列表+慢报告」双模式、只对高客单价品开报告模式。
  takeaway: |
    把推荐输出从「商品列表」重构为「决策报告」是范式级 framing，配生成式轨迹模拟 + Max-Sim 协同语义过程奖励的扎实组合；但单数据集验证、核心省力卖点缺客观证据、新颖性指标与方法设计存在循环，是生成式推荐 × Deep Research 交叉方向上一次方向性大于工程性的开创探索。
---
