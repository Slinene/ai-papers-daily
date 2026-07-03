---
title: 'EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments'
title_zh: EvoPolicyGym：交互环境中自主策略进化的评估基准
authors:
- Zhilin Wang
- Han Song
- Runzhe Zhan
- Jusen Du
- Jiacheng Chen
- Tianle Li
- Qingyu Yin
- Yulun Wu
- Zhennan Shen
- Tong Zhu
affiliations:
- University of Science and Technology of China
- The Chinese University of Hong Kong
- University of Macau
- Tsinghua University
- Zhejiang University
arxiv_id: '2607.02440'
url: https://arxiv.org/abs/2607.02440
pdf_url: https://arxiv.org/pdf/2607.02440
published: '2026-07-02'
collected: '2026-07-03'
category: Eval
direction: 自主策略进化评估
tags:
- Autonomous Agents
- Policy Evolution
- Interactive Environments
- Benchmark
- LLM
- Reinforcement Learning
one_liner: 提出自主策略进化评测框架，在固定交互预算下诊断Agent迭代改进策略的过程与机制
practical_value: '- 策略迭代中的预算分配诊断可直接迁移到推荐策略线上实验，通过分析每次改进尝试的“编辑类型/反馈利用”诊断迭代效率，避免盲目重试。

  - “反馈转化为参数调优”思路可应用于推荐模型在线学习：将用户反馈映射为模型参数（如Embedding、权重）的精细调整，而非重新训练全量参数。

  - 环境紧凑但多样化的设计理念可借鉴到离线策略评估：为搜索/推荐Agent构建一组交互式沙盒环境，低成本验证策略改进能力。

  - 轨迹级别诊断（trajectory diagnostics）可作为评估推荐系统Agent改进行为的分析工具，区分“偶然胜利”与“真实机制发现”，提升迭代方案的上线信心。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有Agent评测将改进过程压缩为最终分数，掩盖了盲目重试、过拟合反馈、脆性特例等失败模式，缺失过程诊断。

**方法**：提出“自主策略进化”可控评测范式：一个harness-model agent在固定交互预算内反复编辑可执行的策略系统（如RL策略代码），基于环境反馈改进。构建EvoPolicyGym基准，包含16个紧凑的交互式RL环境，评估Agent的迭代改进能力，并提供轨迹级诊断（预算分配、参数调优行为等）。

**结果**：GPT-5.5在全部16个环境上排名前二，综合排名分数最高；分析表明强自主策略进化不仅靠单次任务胜利，更依赖发现任务合适的机制并在有限反馈下精细调优策略。
