---
title: 'Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving
  LLM Agents'
title_zh: 超越能力边界：零阶优化驱动的自进化LLM智能体
authors:
- Bingzhen Liu
- Xiaomeng Fan
- Yuwei Wu
- Zhi Gao
- Mingyang Gao
- Chuanhao Li
- Yunde Jia
affiliations:
- 北京理工大学计算机学院智能信息技术北京市重点实验室
- 深圳MSU-BIT大学广东省机器感知与智能计算实验室
- Alaya Lab
arxiv_id: '2608.09292'
url: https://arxiv.org/abs/2608.09292
pdf_url: https://arxiv.org/pdf/2608.09292
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: Agent 自进化 · 零阶优化突破能力边界
tags:
- Self-Evolving
- Zeroth-Order Optimization
- LLM Agents
- Deep Research
- LoRA
- SFT
one_liner: 通过零阶梯度估计扰动LoRA参数，使Agent在困难样本上也能采样正确轨迹，突破能力边界。
practical_value: '- 零阶优化思想可迁移至推荐系统模型更新：当环境反馈为黑盒（如点击、转化）无法直接求梯度时，可通过对服务策略参数（如召回或排序的LoRA分支）施加随机扰动，利用线上指标变化估计梯度，实现无需过程监督的自优化。

  - 并行扰动推理机制大幅降低零阶优化的采样开销：只计算一次骨干预网络输出，多个轻量LoRA支路并行评估，适合在线服务中低延迟要求下进行策略探索。

  - 自适应查找缓存（Adaptive Lookup）对重复工具调用（如搜索相同关键词、访问同一页面）做命中复用，节省30%-50%的交互时间，在推荐系统中可类比为缓存用户画像/点击日志，避免重复计算，加速多臂老虎机策略评估。

  - 答案困惑度损失（Answer Perplexity Loss）提供平滑、稳定的信号，比稀疏的二元奖励更利于优化收敛；在推荐场景中可用商品描述或用户评论的对数似然作为过程级信号，缓解结果奖励稀疏问题。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
自进化LLM智能体（如Deep Research）通常需要从自身采样轨迹中进行SFT或RL训练提升能力。然而，现有方法受限于智能体自身的能力边界：对于困难样本，智能体无法采样到正确轨迹，则后续训练无有效信号，模型无法突破。论文提出零阶自进化框架，通过对LoRA参数施加随机扰动、利用最终答案损失估计梯度，使智能体在无轨迹标注的情况下也能适应困难样本，生成高质量轨迹，再用于SFT形成闭环进化。

**方法关键点**  
- 为每个困难样本附加实例级LoRA模块，随机扰动方向并采样完整轨迹，计算扰动前后答案损失差，用有限差分估计梯度更新LoRA参数（零阶优化），避免反向传播依赖。
- 并行扰动推理：共享骨干预网络输出，并行计算多个扰动支路的LoRA增量，显著降低采样时间。
- 自适应查找机制：缓存近期工具调用结果，根据查询类型使用精确或语义匹配，减少重复搜索/访问，进一步压缩算时。
- 答案困惑度损失：以轨迹为条件计算标准答案的对数似然作为损失，提供平滑、有判别力的信号，改善零阶优化稳定性。

**关键结果**  
- 在GAIA和WebWalkerQA两个深度研究基准上，使用Qwen-3-8B主干，方法准确率达47.5% (GAIA) 和34.8% (WebWalkerQA)，显著优于ReAct (23.3% / 15.5%) 及多个基于GPT轨迹蒸馏的强基线。
- 在训练集上，初始策略Pass@1仅22.0%，优化后提升至53.9%；在50个困难样本上，零阶优化解决23个，而RL仅16个、最佳N采样仅6个。
- 消融表明，答案困惑度损失比BERT相似度或LLM-as-Judge更稳定；并行推理使采样时间减少30%~53%；自适应查找节省约400~1290秒。

**一句话精华**：扰动LoRA + 仅用答案损失 + 零阶梯度估计 = 让Agent在学不会的样本上也能挖出成功轨迹，打破自进化的天花板。
