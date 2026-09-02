---
title: Towards Effective Structured Context Modeling for Conversational Recommender
  Systems via Dual-node Monte Carlo Tree Search
title_zh: 面向对话推荐系统的双节点蒙特卡洛树搜索结构化上下文建模
authors:
- Jincheng Zhang
- Chen Huang
- Wenqiang Lei
- See-Kiong Ng
- Yang Deng
affiliations:
- College of Computer Science, Sichuan University
- Institute of Data Science, National University of Singapore
- School of Computing and Information Systems, Singapore Management University
- Engineering Research Center of Machine Learning and Industry Intelligence, Ministry
  of Education, China
arxiv_id: '2609.00618'
url: https://arxiv.org/abs/2609.00618
pdf_url: https://arxiv.org/pdf/2609.00618
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 对话推荐 · 结构化状态 + MCTS
tags:
- Conversational Recommendation
- MCTS
- Structured State
- Preference Tracking
- LLM
one_liner: 提出 DREAMS，用双节点 MCTS 在结构化偏好状态上联合优化偏好引导与利用，平均成功率提升约 7.4%
practical_value: '- 用显式结构化偏好状态（JSON key-value）替代直接用对话历史做 embedding 或 prompt，把隐含负面偏好（如“不喜欢
  Spike Lee 风格”）解析成可消费的约束，并跨轮累计。电商导购/客服可维护用户属性状态（不喜欢品牌/材质/价格段），避免重复推荐已否定属性。

  - 将“何时问/何时推”建模为 MCTS 搜索，节点保存结构化状态而非自由文本，用 LLM 先验 + UCT 选择动作，可减少粗粒度动作错误和无效追问。电商导购机器人可借鉴树搜索模拟用户反馈，决策澄清问题或直接推荐。

  - 偏好利用侧做 query refinement：从累积状态生成多个候选查询（删冗余、转成机器可读约束），逐个检索并用属性匹配打分，选最优查询，而不是用整个对话历史编码。可迁移到电商搜索的
  query 改写/意图澄清：先结构化成约束，再生成检索请求。

  - 工程上，MCTS 延迟可用经验库（EKB）缓存成功/失败轨迹，检索相似案例 warm-start，减少在线搜索，论文中延迟降到 9s 且性能仍可接受（R@1=0.467）。适合低延迟电商场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
对话推荐中，用户偏好是在多轮交互中逐步揭示的，但现有 LLM 系统通常把整个对话历史直接注入 prompt 或编码为 embedding，造成信息过载、检索噪声和偏好跟踪缺失。JSON 状态快照忽略跨轮演化，MCTS 方法节点缺乏语义偏好表示，均无法同时支持偏好引导和利用。论文先导实验显示现有方法粗粒度动作错误（CGE2）和偏好利用错误（PE2）居高不下。

**方法关键点**
DREAMS 把 CRS 建模为 MDP，将对话状态显式表示为 JSON 结构，明确记录正面、负面、缺失和纠正偏好。
- **ELNode**：从用户话语解析结构化偏好更新，用 MCTS 在动作空间（如 DirectorInquiry、FailureReflection、ItemRec）中搜索，UCT 选择，LLM 先验剪枝，模拟 rollout，层次奖励（态度、信息获取、轮次惩罚）回传，决定何时问、何时推。
- **EXNode**：从累积偏好状态生成多个候选查询，删除冗余、转成机器可读约束，检索后用属性匹配评分选最优查询，再生成推荐。
- 两者共享同一演化偏好状态：ELNode 更新状态，EXNode 消费状态，拒绝反馈写回后续决策。

**关键结果**
在 Redial 和 OpendialKG（Movie/Book）上用 GPT-4o-mini 模拟器评估。DREAMS 在三个数据集上 R@1 分别为 0.507/0.600/0.550，SR 为 0.560/0.639/0.594；比最强非 MCTS baseline ChatCRS 平均 R@1 提升 8.57%，SR 提升 9.07%；比 MCTS 基线 SAPIENT-LLM 和 T-EPL 显著更高。错误指标 FGE2/CGE2/PE2 均最低。消融显示结构化状态、状态搜索和检索精炼三者缺一不可。人类评估 60 人结果最优。经验增强版 DREAMS(EA) 将延迟降到 9s，R@1 0.467。

**最值得记住的一句话**
有效的对话推荐需要“结构化状态 + 结构化搜索”，仅 JSON 表示或仅 MCTS 都不够。
