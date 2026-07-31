---
title: 'Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation
  for Large Reasoning Models'
title_zh: 缓解跨教师在线策略蒸馏的风格偏差：Lightning OPD 2.0
authors:
- Yecheng Wu
- Song Han
- Han Cai
affiliations:
- NVIDIA
arxiv_id: '2607.28449'
url: https://arxiv.org/abs/2607.28449
pdf_url: https://arxiv.org/pdf/2607.28449
published: '2026-07-30'
collected: '2026-07-31'
category: LLM
direction: 跨教师在线策略蒸馏的风格偏差校正
tags:
- On-Policy Distillation
- Style Bias
- Cross-Teacher
- Reasoning Models
- Post-Training
one_liner: 通过交叉拟合风格残差化消除教师不一致带来的风格Token偏差，使OPD不再依赖教师一致性
practical_value: '- 在电商/推荐系统的生成式模型蒸馏中，若SFT数据生成器和蒸馏教师不同（如SFT用GPT-4，蒸馏用Gemini），可直接引入风格残差化：构建Token身份与上下文（位置+surprisal）双查找表，用交叉拟合估计风格偏差并从Token级监督信号中减去，避免误伤内容相关token。

  - 工程实现上，离线预计算SFT rollout和教师log概率后，分K折交叉拟合查找表，再用残差信号替换原始教师分数，即插即用于Lightning OPD框架，几乎无额外推理开销。

  - 当因成本或数据来源多样无法维持教师一致性时，此方法解耦了SFT生成器与蒸馏教师的选择，允许独立优化，同样适用于推荐场景中多模型协同蒸馏（如召回、排序模型蒸馏）。

  - 分析思路值得借鉴：用响应平衡(reduce)避免长文本主导估计，用position/surprisal bins代替完整前缀上下文，防止过分稀疏且保留足够泛化性，可推广至其他序列生成任务的跨模型校准。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
在线策略蒸馏(OPD)依赖教师一致性：提供密集Token级监督的教师应与生成SFT示范的模型相同。但实际SFT数据来源混杂或未标记，且最强SFT生成器与最强蒸馏教师往往不同，强制一致会牺牲某一阶段的最优选择。直接换用更强教师反而导致蒸馏失效，根源在于教师-参考分歧中包含与写作风格、格式、推理节奏相关的可预测成分(style bias)，累积惩罚会干扰内容相关的纠正信号。

**方法关键点**  
- **风格代理假设**：可预测的成分体现为token身份和粗粒度上下文（归一化位置、参考策略surprisal）的重复出现分歧，而推理相关的分歧更依赖具体问题上下文。  
- **Lightning OPD 2.0 框架**：在离线预计算的Lightning OPD缓存上，先划分rollout为K折，对每折用其他K-1折数据拟合两个查找表——一个按token identity平均分歧，一个按归一化position bin和surprisal bin平均分歧。用响应平衡(每个回答等权)防止长响应主导。  
- **残差化更新**：对每折token，将两个查找表结果等权平均作为风格偏差估计̂b，从原始教师-参考分歧d中减去，得到残差分歧d*，替换原式中的教师分数后，直接用Lightning OPD的policy surrogate优化。  
- **交叉拟合**：使用其他折估计，避免自拟合；处理未见组时平滑到全局均值。  

**关键实验**  
在跨教师设置下，SFT参考为Qwen3-4B-SFT（SFT生成器为Qwen3-8B）和Klear-Reasoner-8B-SFT（SFT数据来源于DeepSeek-R1），统一使用Qwen3-30B-A3B-Thinking作为OPD教师。对比SFT基线和三种OPD变体（Lightning OPD、IW-OPD、TA-OPD）。  
- **Qwen3-4B-SFT设置**：Lightning OPD 2.0数学推理平均51.7（+3.1 vs Lightning OPD），代码生成平均35.7（+1.4）。  
- **Klear-Reasoner-8B-SFT设置**：AIME 2024达82.4%，LiveCodeBench v5达63.0%，平均数学+1.0，代码+1.4。  
- **偏差分析**：残差化后与老师一致性信号的绝对偏差>1 nat的token比例从8.14%降至3.85%(Qwen3-4B)，从7.19%降至2.02%(Klear-8B)，相对减少52.8%与71.9%。  
- **消融**：同时使用token和context查找且用交叉拟合效果最佳，单查表或不做交叉拟合均次之。  

**核心要记住的一句话**：通过离线交叉拟合的token身份与上下文双查找表，可剥离跨教师OPD中可预测的风格Token偏差，让残差信号专注内容相关监督，从而解除教师一致性捆绑，自由选择SFT生成器与蒸馏教师。
