---
title: 'Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in
  Machine Learning Engineering'
title_zh: Frontis-MA1：面向递归自我改进的机器学习工程训练
authors:
- Junlin Yang
- Che Jiang
- Yu Fu
- Tianwei Luo
- Can Ren
- Weizhi Wang
- Kaikai Zhao
- Hongyi Liu
- Yuxin Zuo
- Yuru Wang
affiliations:
- Horizon Research
- Frontis.AI
- Tsinghua University
arxiv_id: '2607.28568'
url: https://arxiv.org/abs/2607.28568
pdf_url: https://arxiv.org/pdf/2607.28568
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: AI4AI 自动化机器学习工程
tags:
- AI4AI
- Recursive Self-Improvement
- Execution-Grounded RL
- Evolutionary Search
- MLE-Bench
- Agent
one_liner: 通过执行反馈训练 Draft/Improve/Debug/Crossover 原子算子并组合长程进化搜索，在有限 GPU 预算下将 MLE-Bench
  Lite 奖牌率从 39% 提升至 71%
practical_value: '- **原子算子训练 + 进化搜索范式**：将复杂任务（如推荐模型自动调参、特征工程）拆解为 Draft/Improve/Debug/Crossover
  四种原子操作，用执行反馈训练这些操作，再通过 OpenMLE-Evo 组合成长程搜索，可直接迁移至 AutoML 或 Agent 自动优化推荐 pipeline
  的场景。

  - **执行反馈 RL 的自适应奖励设计**：使用自适应上下界和熵优势（entropic advantage）将学习信号集中于高质量解，而非仅奖励有效解。在推荐策略搜索或
  SQL 生成等可验证任务中，可避免模型产生“能跑但性能差”的结果。

  - **结构化经验与父代选择策略**：通过结构化经验卡（score/improvement/novelty）进行父代选择，兼顾解的质量、改进幅度和方向新颖性；操作触发式记忆合成避免上下文膨胀。这些可直接用于
  Agent 搜索推荐组合空间、模型结构搜索等需要平衡探索与利用的任务。

  - **预算自适应的监督数据收集**：SFT 阶段每任务设执行预算和接受配额，提前终停止艰难任务，节省计算开销。在标注昂贵或执行成本高的推荐场景（如在线实验）中，可高效获得高质量训练数据。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
递归自我改进（RSI）要求 AI 系统能够改进构建 AI 的过程；机器学习工程（MLE）提供了可执行、可验证的测试平台。现有工作要么只做推理时搜索，要么只做模型训练，缺乏将任务环境、执行接地后训练和进化搜索整合的全栈系统，阻碍了对 RSI 的可靠研究。

**方法**  
- **OpenMLE-Gym**：构建 5,758 个可执行任务（含 Kaggle 竞赛与数据集），提供隔离沙箱、结构化反馈与任务特定评分器，覆盖表格、图像、时间序列等多模态。  
- **OpenMLE-ERL**：训练四个可复用的原子进化算子（Draft, Improve, Debug, Crossover）。先用预算自适应的 SFT 从更强的教师模型收集 26,259 个高质量执行轨迹（奖金驱动采样与进化路径段）。再用执行接地 RL 优化，引入自适应得分边界与熵优势，将学习信号集中到组内最优解；异步 rollout 解耦慢任务；父程序选择融合当前质量、子代奖励方差和访问冷却，确保训练到多样且有信息量的状态。  
- **OpenMLE-Evo**：长程进化搜索，引入结构化经验卡（记录分数、改进幅度、方法族、新奇性等），父代选择基于质量、进度、新颖性三因子效用，记忆合成按需触发，为每个操作构建精简上下文（祖先、兄弟节点、全局统计），避免历史堆积。  
- **Frontis-MA1-35B**：基于 Qwen3.6-35B，经上述 SFT+RL 训练，作为变异引擎在进循环中使用。

**结果**  
- **MLE-Bench Lite**（单卡 RTX 4090，12 GB VRAM，每任务 12 小时）上：与基模型相比，标准 OpenMLE-Evo 将 Medal Average 从 39.39% 提升至 60.61%；用 OpenMLE-Evo-Max 进一步提升到 71.21%，超过 GPT-5.5 + Codex 并接近 GPT-5.6 Sol 和 Kimi K3。  
- **跨模型复制**：30B 版本从 34.85% 提升到 53.03%（标准 Evo）和 66.67%（Evo-Max）。  
- **泛化性**：在 NatureBench Lite 上，固定搜索框架仅换用训练后模型，Match-SOTA 率从 50% 升至 70%；固定模型仅换用 OpenMLE-Evo，从 20% 升至 50%，显示训练和搜索组件可跨域迁移。  

**关键思想**  
将原子程序变换算子作为训练与搜索的统一接口，用执行反馈同时提升单个变换的质量和长程组合的能力，使有限预算下的迭代 ML 工程能力获得显著跃升。
