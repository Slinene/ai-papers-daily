---
title: 'Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation
  for Agentic Tasks'
title_zh: Agentic-OPD：用历史 checkpoint 蒸馏恢复智能体遗忘能力
authors:
- Tingcheng Bian
- Kangye Gong
- Jinchang Luo
- MingQuan Cheng
- Feiran Liu
- Ni Li
- Xiaoling Xia
- Haiwei Wang
- Hui Li
affiliations:
- Baidu, Inc.
- Beijing Jiaotong University
arxiv_id: '2611.12799'
url: https://arxiv.org/abs/2611.12799
pdf_url: https://arxiv.org/pdf/2611.12799
published: '2026-11-09'
collected: '2026-11-10'
category: Training
direction: Agent RL 后能力遗忘恢复与蒸馏
tags:
- On-Policy Distillation
- Agentic RL
- Checkpoint Reuse
- Capability Forgetting
- Teacher Scheduling
- GRPO
one_liner: 把单次 RL 运行的所有 checkpoint 当作免费教师池，用 HCN 动态选教师、LAD 局部过滤监督，在五类 agent 任务上恢复被遗忘能力
practical_value: '- 在电商搜索 Agent / 对话式推荐 RL 中，不要只保留 best-validation checkpoint：训练轨迹中早期
  checkpoint 常包含互补能力（多跳推理、工具调用、属性理解），可以按验证集覆盖率把历史 checkpoint 冻结成教师池，用 on-policy 蒸馏做后训练，提升上线单模型能力，几乎零额外训练成本。

  - 教师调度可借鉴 HCN：不要按全局最高分选教师，而按学生当前失败样本的加权覆盖来选择；权重更新让持续未解决且未被当前教师覆盖的问题获得更高优先级，适合冷启动/缺陷驱动迭代。

  - 蒸馏监督必须局部过滤：只在教师经验成功率高于学生且学生失败的 rollout 上做 KL，避免覆盖学生已经掌握的行为；在 agentic 轨迹中只对模型生成的
  think/action/answer 位置计算 loss，排除环境观测、工具返回和 padding。

  - 工程上：保留全部 checkpoint 成本低；只需在验证集上记录每个 checkpoint 的 solved set，调度时重新评估学生；推理部署只用一个学生模型，额外成本主要是采样和教师
  forward，可接受。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**

RL 训练 LLM agent 的主流做法是只保留 best-validation checkpoint，其余全部丢弃。这篇工作发现这种做法是有损的：在 GRPO 训练的五个 agent 域（DeepSearch、Tool-use、WebShop、SciWorld、ALFWorld）中，best checkpoint 会在很多早期 checkpoint 已经解决的问题上失败，所有 checkpoint 解决任务的并集远超任意单个 checkpoint。例如 DeepSearch 在 step 500 时，current checkpoint 解决 2,808 个任务，而至少有 3 个 checkpoint 都解决的任务有 4,553 个，差距 62%。历史 checkpoint 构成了无额外训练成本的教师池。

**方法关键点**

Agentic-OPD 把 best-validation RL checkpoint 作为学生，所有历史 checkpoint 作为冻结教师候选。核心是围绕学生当前能力缺口来组织蒸馏：
- **HCN（Highest Coverage Next）**：构造 gain matrix，记录每个教师覆盖学生当前未解决任务的集合。每次调度步，按加权覆盖率选教师；问题权重动态更新——被学生解决置 0，被当前教师覆盖但未解决回到 1，其他未解决且未被覆盖的问题权重递增。
- **LAD（Locality-Aware Distillation）**：三级过滤监督。问题级：仅保留教师经验成功率高于学生的问题；rollout 级：仅保留学生失败的 rollout；turn 级：只在学生生成的 think/action/answer 位置计算 top-k renormalized KL 散度，排除环境观测、工具返回和 padding。
- 训练循环每 K 步重新评估学生、刷新覆盖、重选教师；用 DAPO 式过采样补齐过滤后的 batch。

**关键结果**

在 24 个 benchmarks/task subsets 上，Agentic-OPD 在每个领域都超过 GRPO。DeepSearch 三个 backbone（Qwen2.5-3B/7B、Qwen3-4B）平均准确率分别 +2.8、+7.4、+2.6 个点；4B 模型达到 50.4%，超过 GPT-5.6（25.4%）和 DeepSeek-V4.1（42.7%）。Tool-use mean pass@1 从 26.1% 到 32.1%，WebShop 从 71.8 到 75.0，ALFWorld 从 88.5% 到 91.0%，SciWorld 从 14.4 到 18.0。消融显示去掉 HCN 或 LAD 都显著掉点；与 model soup、TIES、DARE-TIES、Temporal Sampling、GTR-Turbo 相比，Agentic-OPD 单策略推理下效果最好。

**最值得记住的一句话**

RL 训练中最好的 checkpoint 并没有保留所有学到的能力，把历史 checkpoint 当作按学生能力缺口动态调度、只在局部优势处蒸馏的教师池，可以在不重新训练的情况下恢复被遗忘的覆盖率，进一步提升单模型上限。
