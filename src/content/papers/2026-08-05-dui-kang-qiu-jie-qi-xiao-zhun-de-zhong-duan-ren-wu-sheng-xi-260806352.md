---
title: 'CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal
  Tasks'
title_zh: 对抗求解器校准的终端任务生成系统CalibForge
authors:
- Fanzhe Meng
- Guoxin Chen
- Jiale Zhao
- Shuang Sun
- Zhiyu Lin
- Wayne Xin Zhao
- Ruihua Song
- Ji-Rong Wen
- Kai Jia
affiliations:
- Renmin University of China
- Independent Researcher
- AweAI Team
arxiv_id: '2608.06352'
url: https://arxiv.org/abs/2608.06352
pdf_url: https://arxiv.org/pdf/2608.06352
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: Agent 训练数据合成 · 难度对抗校准
tags:
- Terminal Agent
- Task Synthesis
- Adversarial Calibration
- Learnability
- SFT
one_liner: 通过对抗性多求解器校准生成难度适中的终端任务，显著提升agent训练效果与泛化能力
practical_value: '- **Agent 训练数据构建范式**：用强弱求解器对比（Strong-Pass/Weak-Fail）定位“可学习难度区间”，过滤过难/过易样本，可直接用于电商
  Agent 任务合成（如购物决策、客服问答）来提升数据效率。

  - **多求解器对抗校准**：利用异质求解器池的不一致性来生成训练信号，类似集成/分歧挖掘，可借鉴用于搜索推荐 Agent 的多模型协作场景，例如用不同规模模型筛选高信息量训练样本。

  - **任务难度自适应生成**：通过迭代对抗修订（adversarial revision），让任务难度贴合当前模型能力边界，该方法可复制到生成式广告文案评估、自动化测试等需要动态难度控制的
  Agent 任务中。

  - **跨任务泛化验证**：在 Terminal-Bench、SWE-bench、Doc2Repo 上均大幅提升，说明校准后的训练数据增强了 Agent 的通用规划与推理能力，对构建电商领域跨场景的通用
  Agent 有参考价值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：训练终端 Agent 需要大规模可执行且难度恰当的任务，单纯验证可行性无法保证任务处于模型的可学习区。现有方法缺乏对任务相对于求解器难度的量化与校准。

**方法**：提出 CalibForge 系统，通过对抗性求解器校准自动合成任务。核心思想是利用已验证可解性，引入多求解器校准（Multi-Solver Calibration）和对比求解器校准（Contrastive Solver Calibration）。多求解器校准利用异质求解器池的预测不一致性来筛选任务；对比校准则指定一个强求解器通过、弱求解器失败的难度关系，精确定义可学习区。系统通过迭代对抗修订，将候选任务逐步校准至目标难度。

**结果**：用 CalibForge 构建 5,431 个校准后任务。消融实验表明，两种策略的监督效果显著优于纯验证或单求解器反馈。在 Terminal-Bench 2.0 上，模型分别达到 32.58% 和 47.57%，相对基模型最大提升 24.71 个百分点；在 OOD 测试 SWE-bench Pro 和 Doc2Repo 上分别提升 27.68 和 30.04 个百分点，验证了校准方法的泛化性与迁移性。
