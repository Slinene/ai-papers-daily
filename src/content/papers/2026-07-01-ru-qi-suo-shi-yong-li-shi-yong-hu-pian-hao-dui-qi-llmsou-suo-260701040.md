---
title: 'As It Was: Aligning LLM Search Evaluation with Historical User Preferences'
title_zh: 如其所是：用历史用户偏好对齐LLM搜索评估
authors:
- Ali Vardasbi
- Gustavo Penha
- Enrico Palumbo
- Claudia Hauff
- Hugues Bouchard
- Mounia Lalmas
affiliations:
- Spotify
arxiv_id: '2607.01040'
url: https://arxiv.org/abs/2607.01040
pdf_url: https://arxiv.org/pdf/2607.01040
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: 行为接地增强LLM搜索评估
tags:
- LLM-as-a-judge
- behavioral grounding
- QRI cards
- search evaluation
- inverse propensity scoring
- user preference alignment
one_liner: 提出行为接地（QRI卡片）LLM法官，用极简的去偏交互摘要提升搜索评估与用户偏好的一致性
practical_value: '- **电商搜索评估可直接复用 QRI 卡片**：对每个候选商品聚合历史上相似查询的点击/加购/转化率（经 IPS 去偏）与曝光量，作为
  LLM 评判时附带的「行为证据卡片」。尤其对长尾查询或歧义词（如“苹果”），能有效约束语义偏差，提升评估与线上指标的一致性。

  - **用简易 IPS 获得轻量级去偏信号**：工程上只需一个单调的位置倾向曲线即可计算无偏相关度，无需复杂 click model，适合高时效性系统快速上线。

  - **Prompt 设计上强调辅助而非替换**：明确要求 LLM 将 QRI 视为支持性上下文而非直接答案，仍以语义推理为主，仅在歧义或平局时才启用行为信号，防止历史偏见过度主导。

  - **离线评估替代线上 A/B**：论文证明行为接地法官与线上胜负方向的 alignment 提升（30.6%→36.8%），可加速模型迭代，降低实验成本。关键要保证行为证据窗口与评估窗口无时间重叠，避免数据泄露。

  - **多语言场景增益显著**：多语言人工标注集上，接地后相关性提升+15%，对跨境电商/多市场搜索评估尤其值得尝试。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
大型搜索系统迭代速度远超人工质保伸缩性，LLM-as-a-judge 成为可扩展的评估方案，但纯语义判断容易在歧义、长尾或跨语言查询上偏离真实用户偏好。Spotify 的音乐搜索场景下，需要一种能结合历史用户交互证据的评估方法，既保留语义推理的灵活性，又能对齐实际用户行为。

**方法核心**  
- **QRI 卡片**：为每个 SERP 物品附上一个极简的行为摘要卡片，包含历史上关联的相似查询、该查询下的去偏相关度估计（ˆr）及总曝光量（I）。例如：{“篮球训练音乐”: 0.82, 1200}。  
- **去偏估计**：利用 IPS 对位置偏差进行校正，仅需单调倾向曲线，工程友好。  
- **证据筛选与防泄露**：按语义相似度保留 top-10 历史查询，过滤掉与当前查询余弦相似度 >0.9 的近重复查询（离线评估），生产环境则保留以利用全量证据。  
- **提示策略**：明确定义 QRI 是辅助性行为上下文，LLM 应以语义为主，QRI 仅在歧义或平局时起 tie-breaker 作用。  
- **对比基线**：纯语义法官（无 QRI）作为对照。

**关键结果**  
- 在约 6k 个重构 SERP 的 Logs 集上，BG 法官 Spearman ρ 从 0.416 提升至 0.438（+5%），分歧子集上从 0.147→0.281（相对提升 +91%）。  
- 多语言人工评判集（5 种语言，265 实例）上，BG 的 ρ 从 0.450→0.516（+15%）。  
- 在线 A/B 测试中，BG 对胜负方向的预测对齐率从 30.6% 提升至 36.8%（显著）。  
- 分析表明，接地主要解决三大场景：**消歧**（将用户实际高频解释注入判断）、**校准严厉度**（有/无行为证据时调整惩罚力度）、**提高排序敏感度**（对高行为偏好的实体未排首位更严格）。

**一句话记住**  
“用一张极小的 QRI 卡片，让 LLM 法官在搜索评估中闭上语义猜测的眼睛，睁开用户实际行为的眼睛。”
