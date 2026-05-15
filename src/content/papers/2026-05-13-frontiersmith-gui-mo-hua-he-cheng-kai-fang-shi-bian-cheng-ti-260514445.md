---
title: 'FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale'
title_zh: FrontierSmith：规模化合成开放式编程问题
authors:
- Runyuan He
- Qiuyang Mang
- Shang Zhou
- Kaiyuan Liu
- Hanchen Li
- Huanzhi Mao
- Qizheng Zhang
- Zerui Li
- Bo Peng
- Lufeng Cheng
affiliations:
- UC Berkeley
- UC San Diego
- University of Washington
- Stanford University
- Princeton University
arxiv_id: '2605.14445'
url: https://arxiv.org/abs/2605.14445
pdf_url: https://arxiv.org/pdf/2605.14445
published: '2026-05-13'
collected: '2026-05-15'
category: Training
tags:
- Open-Ended
- Code Generation
- Data Synthesis
- Reinforcement Learning
- LLM
one_liner: 通过变异封闭式编程问题并使用思路分歧度量自动筛选，实现开放式编程问题的规模化合成与强化学习训练
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM在封闭式编程任务（如竞赛题、bug修复）上表现优异，但在缺乏最优解的开放式编码任务（如云调度、启发式算法）上仍远落后于人类。核心瓶颈在于开放式训练数据稀缺且人工构造昂贵。本文旨在从大量现成的封闭式编程问题出发，自动化合成开放式问题，从而训练更强的LLM编码器。

### 方法关键点
- **变异策略**：从竞争性编程题目（HardTests）出发，通过改变目标（如从判定转为优化）、限制输出、泛化输入三种方式将其变异为无已知最优解的开放式变体。
- **思路分歧过滤**：提出“思路分歧”（idea divergence）指标，衡量不同求解器（LLM生成的不同方案）使用的核心算法是否不同。先用LLM-as-a-Judge比较策略差异进行粗筛，再通过执行测试用例与验证器计算分数向量距离进行精筛，保留真正激发多样解法的题目。
- **自动化基础设施构建**：为每个候选问题生成测试用例和连续评分验证器（verifier），并通过交叉验证协议确保正确性，过滤后加入种子池迭代演化。
- **强化学习训练**：使用过滤后的200个合成题目，配合GRPO训练Qwen3.5-9B和27B模型。

### 关键结果
- **性能提升显著**：Qwen3.5-9B在FrontierCS上+8.82分，ALE-bench上+306.36 Elo分；27B模型分别+12.12和+309.12分，训练效果与人工策划数据持平或更优。
- **优于封闭式数据**：直接使用封闭式HardTests训练仅得5.38和397.18，说明变异与过滤步骤将封闭式种子转化为更有效的训练数据。
- **过滤消融**：去掉思路分歧过滤器后，FrontierCS分数下降2.05，ALE-bench也明显下降，证明过滤器关键。
- **开放式特征验证**：合成问题在思路分歧度量上与人工策划的Open-Ended题目（FrontierCS、ALE-bench）相当（~0.4 vs 封闭式的0.14），且导致代码代理产生更多交互轮次与token使用，呈现长时域行为模式。

> **最值得记住的一句话**：FrontierSmith表明，通过变异封闭式题目及思路分歧自动筛选，可以规模化合成长时域、多策略的开放式编程训练数据，且效果不输人工策划。
