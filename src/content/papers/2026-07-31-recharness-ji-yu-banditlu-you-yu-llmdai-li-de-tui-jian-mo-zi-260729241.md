---
title: 'RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender
  Systems'
title_zh: RecHarness：基于Bandit路由与LLM代理的推荐模型自进化框架
authors:
- Haoran Ling
- Yuecheng Li
- Zeyu Song
- Jing Yao
- Shuwen Kang
- Chi Lu
- Wenjin Wu
- Peng Jiang
affiliations:
- Georgia Institute of Technology
- Kuaishou Technology
arxiv_id: '2607.29241'
url: https://arxiv.org/abs/2607.29241
pdf_url: https://arxiv.org/pdf/2607.29241
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: Bandit路由+LLM生成·推荐模型自动迭代
tags:
- Bandit Routing
- LLM Agent
- Automated ML
- Recommender Systems
- Self-Evolving
- Thompson Sampling
one_liner: 用Thompson采样选择编辑方向，LLM负责具体代码修改，在有限预算下稳定优化推荐模型
practical_value: '- **分离方向决策与代码生成**：把“试什么方向”交给Bandit（基于历史成功/失败后验），把“怎么改代码”交给LLM，避免LLM在巨大搜索空间内盲目发散。推荐系统工程师可借鉴此架构，用简单统计路由控制尝试领域（架构、损失、特征），用LLM执行具体编辑。

  - **Jump-Basin机制跳出局部最优**：当近期提升速率低于阈值时，自动开放结构跳跃臂（如更换序列编码器）。线上A/B显示，这一机制在短期局部精调无收益后自动激活，产出了可部署的结构改进。在广告排序或CTR模型迭代中，可设置类似机制自动触发大改。

  - **实验技能（Experiment Skill）作为文本记忆**：动态总结成功编辑、失败原因和趋势，形成紧凑的文本上下文注入LLM提示，避免模型重复犯错。可直接迁移到工业Agent中，用于维护试验记录、提炼可复用策略。

  - **有限试验预算下的高效分配**：Thompson采样在每一轮集中分配试验给高潜力臂，使47.92%的非基线试验刷新了best-so-far分数（随机分配仅22.45%）。在电商搜索/推荐中，当单次全量训练和评估成本高时，此路由可显著提高试验效率。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐模型优化依赖工程师反复迭代架构、目标和训练策略，LLM代理虽能自动化试错，但让其同时选择方向与生成具体假设在有限试验预算下搜索极不稳定。因此，需要一种将方向决策与代码生成解耦的框架，让验证反馈既指导试验分配，又帮助LLM形成改进假设。

**方法关键点**：
1. **三层控制**：Level 1由人类定义优化目标、验证指标和候选编辑臂（如学习率、dropout、嵌入维度、损失函数、序列编码器）；Level 2用Thompson采样的Bandit路由器根据标量验证改善（归一化后二元成功信号）更新Beta后验，选择下一轮编辑方向；Level 3用Experiment Skill（文本记忆，记录成功/失败片段和趋势）与LLM推理生成具体代码突变。
2. **局部与跳跃臂分离**：将编辑臂分为局部精细臂和结构跳跃臂，当滑动窗口内提升速率低于阈值时激活跳跃臂，允许进行架构级修改，并通过重训练（retuning）窗口判断跳跃是否有效。
3. **并行试验组**：每轮选多个臂并行执行，候选改善基于组内平均归一化过滤，仅优于组均值和历史最佳的才被接受。

**关键实验**：
- 在4个Amazon序列数据集和KuaiRec视频观看时长数据集上，对GRU4Rec、BERT4Rec、NextItNet、SASRec、HSTU、D2Q、TPM、GR共8种模型进行优化。RecHarness将GRU4Rec的平均HR@10从0.2685提升至0.499（+85.85%），HSTU从0.4723升至0.5317（+12.58%），在TPM上将WT-MAE降低26.41%。
- 消融实验（SASRec）显示，RecHarness在验证集HR@10的搜索速度和最终效果均优于随机路由、LLM选臂和无Bandit自由搜索，且47.92%的非基线试验刷新了best-so-far分数。
- 快手短视频广告平台7天在线A/B测试：ADVV +2.084%，Revenue +0.534%，Exposure +0.559%。

**核心洞见**：让Bandit根据验证反馈“决定去哪”，让LLM根据文本记忆“决定怎么改”，比让LLM同时做两件事更稳定高效。
