---
title: 'RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via
  Ranking-Based Reward Construction'
title_zh: 通过基于排名的奖励构造释放生成式奖励模型在LLM强化学习中的潜力
authors:
- Chenglong Wang
- Ziming Zhu
- Yifu Huo
- Bei Li
- Qiaozhi He
- Yan Ding
- Xiaoyang Hao
- Yuxin Gao
- Tianhua Zhou
- Xiaojia Chang
affiliations:
- School of Computer Science and Engineering, Northeastern University, Shenyang
- NiuTrans Research, Shenyang
- Independent Researcher, Beijing
- CAS Key Laboratory of Behavioral Science, Institute of Psychology, CAS
- Kunming University of Science and Technology
arxiv_id: '2608.06310'
url: https://arxiv.org/abs/2608.06310
pdf_url: https://arxiv.org/pdf/2608.06310
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 生成式奖励模型RL训练 · 排名奖励构造
tags:
- Generative Reward Model
- Reinforcement Learning
- Reward Construction
- GRPO
- Ranking-based Reward
one_liner: 将生成式奖励模型从标量评分转为利用其排名能力构造奖励信号，解决RL中比较优势与评分范式不匹配的问题
practical_value: '- **生成式评估器用于策略优化**：在电商/推荐场景中，若使用LLM作为评估器（如评价推荐理由、对比候选素材），可直接沿用RRC思路：不要求LLM打绝对分，而是让LLM对同一查询的多个候选进行两两比较，将胜出次数作为奖励，再用GRPO等RL算法优化生成策略。这比强求标量分数更稳定且能利用LLM的推理能力。

  - **锚点引导减少推理开销**：RRC-AGR用少量固定参考响应（锚点）替代全量两两比较，将查询复杂度从O(m²)降至O(m×n)。在线上系统延迟敏感时，可预生成锚点集（如历史高赞推荐理由），新样本只需与少量锚点比较即可获得有效奖励信号，极大降低推理成本。

  - **投票增强鲁棒性**：对于生成式评估，单次判断可能随机，多数投票（voting@k）能显著提升奖励质量。在涉及文案生成、排序合理性判断等主观任务时，通过多轮采样聚合偏好可降低噪声，且可控制推理预算。

  - **避免评估与策略耦合**：锚点由固定参考策略生成，而非当前演化中的策略，能保持比较基准稳定。在迭代优化生成式推荐模型时，建议使用冻结的基线模型生成参考样本作为锚点，防止奖励漂移。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
生成式奖励模型（GRM）在响应排序上远优于判别式模型，但在强化学习（RL）中作为标量评分器时优势消失。原因在于：GRM擅长两两比较，却被强求输出标量分数（如偏好token概率），导致概率崩塌和置信度噪声，未能发挥比较优势。因此，需要一种方式让GRM在RL中保留其排序本质。

**方法关键点**  
1. **基于排名的奖励构造（RRC）**：不直接使用GRM的概率输出，而是利用GRM进行两两偏好判断，将胜出次数作为奖励值。  
2. **自竞争排名（SCR）**：对同一输入采样的多个响应进行全量两两比较，奖励等于击败其他响应的次数，自然满足序保留和边际感知。结合多数投票（voting@k）增强鲁棒性，并使用基于Kemeny规则的冲突消解处理循环偏好。  
3. **锚点引导排名（AGR）**：引入少量固定锚点响应（来自参考策略），将每个采样响应与锚点比较，奖励为胜过锚点的数量。复杂度从O(m²)降至O(m·n)，支持大规模采样，且锚点提供稳定基准。  
4. **与RL算法集成**：构造的标量奖励可直接输入GRPO、DAPO等RL算法。

**关键实验与结果**  
- **基准**：AlpacaEval2、ArenaHardV2、WildBench、MMLU-Redux、MATH-500等。  
- **基线**：概率奖励构造（PRC）、去除推理的PRC、判别式奖励模型（DRM）、DPO/SimPO。  
- **主结果**：在8B GRM配合voting@8的AGR下，AlpacaEval2从PRC的35.8%提升至41.3%，ArenaHardV2从8.0%提升至11.2%；SCR同样大幅优于基线。  
- **缩放行为**：增加投票数和锚点数均能提升性能，但呈边际递减；少量锚点（如8、16）即可带来主要增益。

**核心结论**：GRM用于RL时，应将其定位为比较器而非评分器，通过排名构造奖励可解锁其全部潜力，且具有推理计算的缩放特性。
