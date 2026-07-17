---
title: Long-term User Engagement Optimization through Model-agnostic Downstream Rewards
  Learning
title_zh: 通过模型无关的下游奖励学习优化长期用户参与
authors:
- Dingsu Wang
- Filip Ryzner
- Kelly He
- Armando Ordorica
- David Woo
- Aditya Mantha
- Liyao Lu
- Usha Amrutha Nookala
- Haoran Guo
- Jiacong He
affiliations:
- Pinterest
arxiv_id: '2607.14192'
url: https://arxiv.org/abs/2607.14192
pdf_url: https://arxiv.org/pdf/2607.14192
published: '2026-07-15'
collected: '2026-07-17'
category: RecSys
direction: 长期留存优化 · 下游代理奖励
tags:
- Downstream Rewards
- User Retention
- Proxy Rewards
- Model-agnostic
- Long-term Engagement
- A-B Test
one_liner: 提出模型无关的下游奖励框架，用会话级代理信号近似长期留存，在 Pinterest 多表面 A/B 测试中稳定提升活跃度与深度参与。
practical_value: '- **离线筛选代理奖励的思路**：通过用户患病率归一化（与基线比较）去除曝光偏差，再用随机森林检验会话行为与未来留存的关联，可迁移到电商/广告场景筛选长期价值
  proxy（如深层浏览、收藏、加购后的继续行为）。

  - **三类可复用的奖励信号**：①深度会话奖励（对后续 save/下载等行为做折扣求和）；②负面奖励（惩罚短停留+无后续高意图动作的浅层浏览）；③新用例采纳奖励（推荐超出历史兴趣簇的内容并带来正向行为），可与现有排序模型多目标融合。

  - **奖励标签在线生成基础设施**：用序列化存储每日行为事件并在数据加载时动态计算标签，替代预计算表，大幅缩短新奖励迭代周期（从 3 周→2 天），适合需要快速实验的业务。

  - **多目标权重解耦调优**：奖励 head 权重在模型外通过 HyperOPT 单独搜索，不强制端到端联合训练，可保持即时指标不劣化，同时方便添加新 reward
  head。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
直接优化长期留存面临标签稀疏、延迟和归因困难。Pinterest 观察到浅层高量浏览不可靠，深层 P2P 探索、save、跨品类深度交互才是用户回访的真正前兆，因此需要一种模型无关的代理奖励方案，以更低延迟、更高密度的信号替代远期留存标签。

### 方法
- **离线筛选框架**：对 pivot 日行为做用户患病率归一化（对比历史基准），用随机森林预测用户是否会从低频转入高频活跃状态，筛选出同时满足（1）与留存相关、（2）会话级可观测、（3）在多元模型中增量预测的候选信号。
- **三类下游奖励设计**：
  - **深度会话奖励**：对推荐点击后一条轨迹中的 save、download 等行为做折扣求和，鼓励引发深度探索的推荐。
  - **负面奖励**：识别浅层 closeup（停留极短且无后续高意图行为），按用户状态分阈值惩罚，减少低效曝光。
  - **用例采纳奖励**：当推荐 item 与用户历史兴趣簇相似度低于阈值且发生正向行为时给予奖励，引导品类拓展。
- **奖励标签生成基础设施**：从预计算表（DRv1）演进到 DRv2，存储每日行为序列，在 Ray 数据加载时通过可配置 UDF 动态计算标签，迭代周期缩短约 10 倍。
- **平衡即时与下游奖励**：多目标评分线性加权，权重在模型外通过 HyperOPT 调节，保持即时动作中性，提升留存指标。

### 实验
在 Pinterest Homefeed 进行 4 周 A/B 测试（1.5% 流量）：深度会话奖励使 Site‑wide 成功会话数（SS）提升 +0.36%，总花费时间 +0.10%；负面奖励优化后 SS +0.16%，总时间 +0.35%，短时关闭减少；用例采纳奖励带动 Homefeed save +0.42%，多品类活跃用户比例 +0.18%。框架已部署到 Search（搜索满足率 +0.25%）、Related Pins（SS +0.15%）、Notifications（WAU +0.11%）等多表面，显示一致增益。

> **核心启示**：用规范化后的深层会话行为作为长期价值的即时代理，正负信号组合、离线严格筛选，是工业级长期优化的低成本有效路径。
