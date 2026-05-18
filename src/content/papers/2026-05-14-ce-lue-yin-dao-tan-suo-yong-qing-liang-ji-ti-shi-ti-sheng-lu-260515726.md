---
title: 'Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for
  RLVR'
title_zh: 策略引导探索：用轻量级提示提升RLVR探索效率
authors:
- Chanuk Lee
- Sangwoo Park
- Minki Kang
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2605.15726'
url: https://arxiv.org/abs/2605.15726
pdf_url: https://arxiv.org/pdf/2605.15726
published: '2026-05-14'
collected: '2026-05-18'
category: Training
direction: 强化学习探索 · 策略级上下文
tags:
- RLVR
- exploration
- strategy-nudging
- GRPO
- distillation
- math-reasoning
one_liner: 提出 NudgeRL，通过策略级上下文进行结构化探索，在仅 8 次采样下超 8 倍采样 GRPO
practical_value: '- **低成本探索增强**：使用轻量级 LLM（如 gpt-4o-mini）离线生成策略级关键词（如数学定理名），在训练时随机采样并拼入
  prompt，即可大幅提升采样多样性。电商推荐场景可类比生成“商品类别/用户意图”等标签作为上下文，引导 Agent 探索不同推荐路径，无需昂贵 oracle
  标注。

  - **上下文控制优势估计**：Inter-Intra Group Advantage 将奖励分解为组内与组间信号，λ 参数可调节探索-利用倾向（λ>1 倾向可靠上下文，λ<1
  鼓励探索新上下文）。在 Agent 多策略协作中，可对不同的策略组分配不同 λ，动态平衡已知高转化策略与新策略尝试。

  - **知识蒸馏回基础策略**：通过优势加权蒸馏，将上下文条件下发现的有效轨迹迁移回原始无上下文的策略，使推理时无需外部提示。在多智能体系统中，可将智能体在辅助信号下学到的技能蒸馏至主策略，避免上线时的输入依赖。

  - **采样效率提升的工程启示**：论文证明结构化探索可以显著减少所需采样数（8 次 vs 32 次 GRPO），且 pdrop=0.5 随机丢弃上下文能保持稳定训练。在生成式推荐中，若用类似方式对候选生成过程注入多样性（如不同
  decoding 技巧或 prompt 模板），可降低大规模采样的计算开销。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
RLVR（如 GRPO）依赖采样轨迹进行优化，但策略容易坍缩到高频的推理模式，导致大量正确但低概率的轨迹无法被探索，形成性能瓶颈。常见扩增采样次数的做法计算成本高且边际收益递减。  

**方法关键点**  
- **策略轻推 (Strategy Nudging)**：为每个 prompt 预生成 2 个轻量级策略关键词（如“勾股定理”），训练时每个 rollout 随机采样一个上下文或按概率 dropout 为原始 prompt，强制策略覆盖多种推理路径。  
- **组间-组内优势 (Inter-Intra Group Advantage)**：将同一 prompt 下的 rollout 按上下文分组，优势 = (个体奖励 - 组平均) + λ × (组平均 - 全局平均)，λ 控制对不同上下文的偏好（>1 倾向高奖励组，<1 鼓励探索低奖励组）。  
- **蒸馏增强目标**：在上下文条件下进行 RL 的同时，通过优势加权蒸馏项将高质量轨迹行为迁移回基础策略（无上下文），使推理时不再依赖上下文。  

**关键实验与结果**  
- 数据集：AIME24, AIME25, AMC23, MATH500, APEX 五个竞赛数学 benchmark。  
- 基线：基础模型、不同采样数的 GRPO（8/16/32/64）、POPE（oracle 前缀引导）。  
- NudgeRL 在 Qwen3-4B 上以 8 次采样达到平均 pass@1 0.489，超过 GRPO 的 32 次采样 (0.487) 和 64 次采样 (0.451)；在 Olmo3-7B 上同样以 0.285 超 32 次采样的 GRPO (0.281)。  
- 随机采样策略词优于挑选最高质量的上下文，蒸馏系数 λdistill=0.1、pdrop=0.5 时效果最佳。  

**最值得记住的一句话**  
*“结构化探索的效率源于让策略在语义有别的策略级上下文中强制多样化，再通过蒸馏将发现的技能迁移回裸策略，而非简单扩大采样或注入答案信息。”*
