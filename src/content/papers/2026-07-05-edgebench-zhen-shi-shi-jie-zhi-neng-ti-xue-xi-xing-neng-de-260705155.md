---
title: 'EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments'
title_zh: EdgeBench：真实世界智能体学习性能的对数S型缩放定律
authors:
- Deyao Zhu
- Xin Zhou
- Shengling Qin
- Xuekai Zhu
- Hangliang Ding
- Shu Zhong
- Zixin Wen
- Zhonglin Xie
- Chenhui Gou
- Linxuan Ren
affiliations:
- ByteDance
arxiv_id: '2607.05155'
url: https://arxiv.org/abs/2607.05155
pdf_url: https://arxiv.org/pdf/2607.05155
published: '2026-07-05'
collected: '2026-07-07'
category: Agent
direction: 智能体环境学习缩放定律
tags:
- Agent Learning
- Scaling Laws
- Real-World Tasks
- Benchmark
- Log-Sigmoid
- Continuous Feedback
one_liner: 首次发现智能体在真实环境中的长时间学习遵循精确的对数S型缩放定律，R²达0.998
practical_value: '- **长时间运行智能体的性能预测**：在电商广告自动优化、推荐系统持续调参等场景下，可借鉴对数S型曲线（$S(t) = \frac{S_{max}}{1
  + (t_{mid}/t)^\beta}$）刻画智能体从环境反馈中学习的规律，预估性能饱和点，避免无效等待。

  - **任务设计与评估框架**：EdgeBench 要求单任务至少 12 小时连续运行并提供多级丰富反馈，类似方式可用于构建电商场景的长期智能体评测集（如七天不间断选品与出价），量化模型在真实业务流中的持续学习能力。

  - **学习速度的迭代改进**：论文发现智能体学习速度约每三个月翻倍，这启发我们在推荐智能体迭代时，关注模型代际的策略学习效率提升，将“学习速度”作为选型指标。

  - **反馈机制设计**：任务提供多级环境反馈（即时奖励、子任务完成信号等）是性能规律显现的关键，推荐系统中的智能体也应引入多层次、非延迟的反馈信号，以支撑稳定学习。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：预训练缩放定律仅揭示模型在静态数据上的性能增长，但智能体部署后与真实环境连续交互中的学习规律尚不明确，这阻碍了对长期自主系统的理解和优化。

**方法**：构建 EdgeBench，包含 134 个超长时真实世界任务，覆盖科学发现、软件工程、组合优化、专业知识工作、形式数学和交互游戏六大领域，每个任务要求智能体连续运行至少 12 小时，并接收丰富的多级环境反馈。累计记录约 38,000 小时的智能体交互数据，对多种前沿模型在环境学习过程中的整体性能变化进行建模。

**关键结果**：首次发现整体性能随环境交互时间精确遵循对数S型缩放定律 $S(t) = \frac{S_{max}}{1 + (t_{mid}/t)^\beta}$，平均 $R^2$ 高达 0.998，表明模型在真实任务中的学习过程具有高度可预测性。同时观察到，模型代际的学习速度大约每三个月翻倍，展现出与环境交互学习的快速演进趋势。

**贡献**：提供了首个真实环境智能体学习缩放定律的实证证据，并公开 51 个任务及完整评估框架，推动长期环境学习的研究。
