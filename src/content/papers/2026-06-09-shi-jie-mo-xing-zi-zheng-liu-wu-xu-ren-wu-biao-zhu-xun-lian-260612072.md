---
title: 'World Model Self-Distillation: Training World Models to Solve General Tasks'
title_zh: 世界模型自蒸馏：无需任务标注训练指令跟随视频智能体
authors:
- Sebastian Stapf
- Pablo Acuaviva Huertos
- Aram Davtyan
- Paolo Favaro
affiliations:
- Department of Computer Science, University of Bern
arxiv_id: '2606.12072'
url: https://arxiv.org/abs/2606.12072
pdf_url: https://arxiv.org/pdf/2606.12072
published: '2026-06-09'
collected: '2026-06-11'
category: Other
direction: 世界模型 · 自蒸馏 · 强化学习
tags:
- self-distillation
- video world model
- reinforcement learning
- VLM reward
- instruction following
one_liner: 通过自蒸馏将详细描述知识迁移到简洁指令模型，并结合VLM反馈RL超越教师
practical_value: '- 自蒸馏思路：用大模型生成丰富描述（如推荐理由、多模态内容），将其蒸馏到轻量指令跟随模型，降低线上成本。在电商文案生成或对话Agent中可复现。

  - VLM弱奖励+RL：利用VLM作为零样本评估器为生成结果打分，指导强化学习迭代，避免人工标注。适用于推荐解释、搜索query改写等生成任务。

  - 蒸馏奖励与任务奖励混合：用教师模型提供密度正则化，防止RL策略崩溃，这一平衡技巧可迁移到基于LLM的推荐策略优化。

  - 数据生成范式：用VLM从未标注图像自动产出任务-解方案对，类似用LLM从用户行为日志生成训练样本，缓解语义ID生成或交互推荐中的数据稀缺。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
预训练视频生成模型具有涌现任务解决能力，但需要详细文本描述，无法直接用于规划与决策。现有方法要么外包推理给语言模型，要么依赖昂贵的有监督微调数据。该工作探索一条无任务-执行视频标注的可扩展路径：将详细描述下的“演示者”转化为仅需简短指令的“执行者”，并利用VLM反馈进行强化学习，使执行者超越演示者。

**方法关键点**  
- **自蒸馏框架**：演示者（教师）接收图像+详细执行描述生成视频；执行者（学生）仅接收图像+简短任务指令。通过分布匹配蒸馏，将演示者行为迁移到执行者，无需成对任务-执行视频。  
- **蒸馏奖励**：在学生轨迹上计算教师-学生速度场差异作为负奖励，鼓励学生轨迹与教师一致。  
- **VLM任务奖励**：用Qwen3.5-27B判断生成视频是否完成任务，输出对数概率差作为奖励，再利用一致性奖励抑制不合理生成。  
- **复合训练目标**：结合策略梯度RL（使用蒸馏奖励+任务奖励）和锚定损失（在采样状态上直接回归教师速度），防止策略漂移。  
- **数据集**：从MiraData筛选2万张图像，用VLM生成八组任务-解决方案对，构建包含14.6万条训练提示的WorldTasks数据集，并构建200个样例的WorldTasks-Bench评估基准。

**关键实验**  
- 在WorldTasks-Bench上，LTX-2 8步模型+WMSD获得0.605任务完成率、0.691主体正确率、0.882物理一致性（平均0.726），远超基线。  
- 消融显示on-policy自蒸馏优于off-policy，结合RL后执行者超越演示者，而纯RL很快饱和。  
- 在DreamGen机器人基准上，零样本WMSD在Object/Behavior/Environment三项指标上均接近甚至超越部分有监督模型（如Cosmos SFT），展现跨领域泛化。
