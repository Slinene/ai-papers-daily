---
title: 'InterleaveThinker: Reinforcing Agentic Interleaved Generation'
title_zh: InterleaveThinker：多智能体增强交错图像生成
authors:
- Dian Zheng
- Harry Lee
- Manyuan Zhang
- Kaituo Feng
- Zoey Guo
- Ray Zhang
- Hongsheng Li
affiliations:
- CUHK MMLab
- Meituan
- CUHK IMIXR
arxiv_id: '2606.13679'
url: https://arxiv.org/abs/2606.13679
pdf_url: https://arxiv.org/pdf/2606.13679
published: '2026-06-10'
collected: '2026-06-12'
category: MultiAgent
direction: 多智能体交错生成 · 强化学习
tags:
- MultiAgent
- Interleaved Generation
- GRPO
- Planner-Critic
- Image Generation
- Reinforcement Learning
one_liner: 首个解耦规划与评判的多智能体框架，让任意冻结图像生成器具备强交错生成能力，并解决视觉过依赖与误差累积。
practical_value: '- **多步决策解耦范式**：面对长程任务时，可借鉴 Planner-Critic 分离设计，让 Planner 一次性生成全局计划以屏蔽中间视觉反馈，避免“过依赖”导致的中途停滞或目标漂移，Critic
  专注局部校正。该设计可直接迁移至多轮对话推荐、商品序列生成等场景。

  - **双奖励单步RL降本增效**：提出的 accuracy reward（判断准确度）和 step-wise reward（精炼前后质量差）将全轨迹 RL 简化为单步
  RL，大幅降低训练成本，适合长工具调用链的 Agent 训练。在电商文案生成、多步商品图编辑等长序列任务中，可仿效此策略设计局部奖励信号，实现高效全局优化。

  - **高质量训练数据构造流水线**：通过类别树、实体库和模板生成多样化种子提示，再用强模型生成完整规划-执行-评判轨迹，最后用迭代评分过滤并分裂为 SFT/RL
  数据。该方法可用于构建 multi-agent 的规划-反思训练集，尤其适合推荐系统智能体或交互式内容生成场景。

  - **基于评分方差的数据划分策略**：将迭代评分方差大的样本专用于 RL，使 Critic 学习精炼能力；方差小的样本用于 SFT 冷启动。这一技巧可直接复用到任何“建议-执行-评价”的强化学习训练数据准备中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有图像生成器受限于架构，只能单图生成，无法输出交错文本-图像序列。统一多模态模型虽支持交错生成，但在长程任务中陷入**视觉过依赖**（中途停止于视觉相似状态）和**步间误差累积**。为此，本文提出 InterleaveThinker，首个多智能体框架，可赋予任意冻结的生成/编辑模型强大的交错生成能力。  

**方法关键点**  
- **Planner-Critic 解耦流水线**：Planner 一次性输出全局步骤指令，完全屏蔽中间视觉反馈以根除过依赖；Critic 在每一步评估生成图像，若失败则精炼提示并重生成，最多迭代 5 次，从而阻断误差累积。  
- **大规模数据构造**：通过 8 大类、75 子类、30+ 领域实体/动作库和 100+ 模板生成 4 万文本提示，用 Gemini 2.5 Pro 和 Nano Banana Pro 产生完整轨迹，经步骤过滤和迭代评分分裂得到 Planner-SFT-80k、Critic-SFT-112k 和 Critic-RL-13k。  
- **双奖励单步 RL**：引入 accuracy reward（判断准确度）和 step-wise reward（由 Gemini 评判的精炼前后质量差），将长达 25+ 步生成器的全轨迹优化简化为 Critic 的单步 GRPO 训练，大幅降低计算成本。  
- **训练方案**：Planner/Critic 均基于 Qwen3-VL-8B SFT，然后仅对 Critic 进行 RL，使用格式奖励和双奖励加权组合。  

**关键结果**  
- 在 UEval 交错生成基准上，搭配 4 步 FLUX.2-klein 达到 66.3 均分，超越所有开源 UMM，接近 Nano Banana Pro (76.1)。  
- 在 CoMM 任务 3/4 上，风格和实体一致性均超 9.2，大幅领先现有方法。  
- 意外泛化到推理任务：WISE 从 0.47 提升至 0.73，RISE 从 13.3 提升至 28.9。  
- 消融表明多智能体远优于单智能体，双奖励 RL 带来额外增益，数据过滤至关重要。  

**核心洞见**：解耦规划与评判，通过全局指令阻断视觉过依赖，并用双奖励单步 RL 实现低成本长程优化，是赋予任意生成器复杂序列能力的关键。
