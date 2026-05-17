---
title: Language-Induced Priors for Domain Adaptation
title_zh: 语言诱导先验的冷启动域适应框架
authors:
- Qiyuan Chen
- Jiayu Zhou
- Raed Al Kontar
arxiv_id: '2605.14301'
url: https://arxiv.org/abs/2605.14301
pdf_url: https://arxiv.org/pdf/2605.14301
published: '2026-05-14'
collected: '2026-05-17'
category: LLM
direction: 利用LLM文本先验指导冷启动域适应
tags:
- Domain Adaptation
- Cold Start
- LLM Priors
- EM Algorithm
- Transfer Learning
one_liner: 用LLM将目标域文本描述转化为源选择先验，嵌入EM算法解决冷启动负迁移
practical_value: '- 电商推荐场景冷启动物品/用户：若有文本描述（标题、属性），可用类似LIP的方法通过LLM生成对相似源域（如成熟品类）的偏好概率，减少迁移时的负迁移风险。

  - 多智体协作中的经验复用：当任务用自然语言描述时，可借助LLM先验快速筛选相关历史任务数据，提升少样本策略学习效率。

  - 与现有预估模型兼容：框架仅要求模型有似然函数，可无缝集成到CTR/CVR预估的线性或深度模型，无需改动结构。

  - 工程实现轻量：先验可离线通过LLM计算文本嵌入相似度得到，在线阶段只是简单的概率加权，延迟可控。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：域适应在目标数据极少（冷启动）时面临根本性难题：统计准则无法可靠区分相关与不相关源域，直接迁移常导致负迁移。实际中常有的专家文本描述资源（如对目标场景的语义刻画）却未被利用。

**方法**：提出语言诱导先验（LIP）框架，将文本描述通过预训练LLM转化为源域选择的概率先验。具体做法：用LLM的上下文学习能力，比较目标描述与各源域描述的语义相似度，输出一个偏好分布作为先验。该先验融入期望最大化（EM）算法，在E步中引导源域权重估计：当目标样本极少时，后验主要由先验主导；随着目标数据增多，似然逐渐占优，实现自动过渡。该框架兼容任何参数模型，只要存在似然函数即可。

**理论**：证明在正确先验下，冷启动均方误差（MSE）能与已知最优源域的oracle估计器匹配；即使先验不完美，估计量仍渐近一致，保证安全收敛。

**实验**：在三类任务上验证：描述性任务（高斯均值估计）、预测性任务（C-MAPSS涡扇发动机剩余寿命预测）和规范性任务（MuJoCo hopper控制策略迁移）。结果显示，LIP在极冷启动（如目标样本仅1-5个）下显著优于无先验的EM和传统域适应方法，负迁移几乎消除，且随样本积累性能稳健提升。
