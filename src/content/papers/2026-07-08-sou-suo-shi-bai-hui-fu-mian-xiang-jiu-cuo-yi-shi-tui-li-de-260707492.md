---
title: 'Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning'
title_zh: 搜索，失败，恢复：面向纠错意识推理的训练框架
authors:
- Dmitry Beresnev
- Vladimir Makharev
- Roman Khalikov
- Ivan Oseledets
- Petr Anokhin
affiliations:
- Innopolis University
- Lomonosov Moscow State University
- AXXX
arxiv_id: '2607.07492'
url: https://arxiv.org/abs/2607.07492
pdf_url: https://arxiv.org/pdf/2607.07492
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: 验证器引导的搜索与显式回溯训练
tags:
- Backtracking
- Validation-guided
- Search
- LLM Reasoning
- Correction-aware
- Training Framework
one_liner: 提出Pyligent，利用验证器标记失败分支并显式训练回溯，让小型LLM学会从延迟错误中恢复推理
practical_value: '- **显式引入回溯动作与失败监督**：在多步推理Agent（如对话式商品搜索、多轮筛选）中，可定义`<backtrack>`动作，利用业务规则作为验证器，将失败路径转化为监督信号，训练模型何时撤回错误分支。

  - **逆课程学习策略**：从接近完成的前缀开始探索，逐步向任务起点扩展，可降低早期训练难度，适用于需要多步试错的推荐对话或规划场景。

  - **失败分支的简短摘要（trace）**：回溯后注入失败原因摘要，帮助模型复用失败信息，避免重复错误，可在提示工程中用于记忆管理。

  - **区分回溯质量指标**：定义invalid/valid/correct/perfect回溯等级，评估模型是否回到正确的恢复点，这一评估方式可迁移到Agent策略评估中，衡量纠错精度而非仅看成功率。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
多数推理任务不是线性链：求解者可能需要尝试一个看似合理的分支，延迟发现该分支走入死胡同，然后返回到可以继续的最近选择点。标准链式思维监督只暴露成功路径，隐藏了失败与恢复，导致模型无法学会何时放弃错误分支。Shalev-Shwartz 与 Shashua 的 Diligent Learner 理论指出，若模型能以非零概率生成正确下一步，并学会在分支错误时回溯到可修复前缀，则可用深度优先搜索避免指数爆炸。本文将该理论转化为可实施的小型 LLM 训练管道。

**方法关键点**  
- 将推理表示为部分解链的验证搜索树，动作空间包含 `<node>`、`<done>` 和 `<backtrack>`，节点标识符使分支结构对模型可见。  
- 训练管道：先 SFT-A 用金链教会格式与基础步骤；探索阶段由求解器从选定前缀生成候选，任务验证器标记合法与非法路径，构建 ChainTree；SFT-B 用成功对（继续）、失败对（回溯）、以及可选的带 trace 继续对进行监督。  
- 回溯目标不是最近父节点，而是理论上的 β(c) 最大可修复前缀，通过验证器后验确定。  
- 使用逆课程：从离终点近的前缀开始探索，逐步移向根部，让模型逐步学会更长距离的恢复。  
- traced recovery 在回溯后注入失败摘要，使模型知晓已抛弃分支的原因，降低重复犯错。

**关键实验与结果**  
在四个任务上评估：隐藏有向图、4×4 数独、带推理轨迹的数独、积木世界。基线为仅用金链 SFT 的模型。  
- 隐藏图：Pyligent 成功率 76.5%（金链 SFT 仅 3.8%），提升 72.7pp；平均生成步数减半，完美回溯率从 23.2% 升至 47.7%。  
- 数独（混合难度）：Pyligent 82% vs. 金链 SFT 65%，提升 17pp；专家难度 66% vs. 48%，提升 18pp。  
- 数独 w/ RT：性能普遍低于纯数独，但 Pyligent 依旧显著优于金链 SFT（混合 58% vs. 31%，专家 34% vs. 20%）。  
- 积木世界：Pyligent 50.35% vs. 金链 SFT 29.37%，提升 13pp；回溯对约 11% 的成功任务起到关键作用。  
- 消融表明，去掉 trace 或增加失败路径训练轮次可能降低最终解决率，说明恢复行为的训练需要精细平衡。

**核心洞察**：失败分支不是噪音，而是训练模型理解“何时放弃、退回何处”的最佳信号。
