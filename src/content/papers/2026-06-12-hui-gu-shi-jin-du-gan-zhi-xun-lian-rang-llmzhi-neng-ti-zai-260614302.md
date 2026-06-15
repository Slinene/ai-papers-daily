---
title: Retrospective Progress-Aware Self-Refinement for LLM Agent Training
title_zh: 回顾式进度感知训练：让LLM智能体在长程任务中自我反思
authors:
- Xinbei Ma
- Congmin Zheng
- Jiyang Qiu
- Jiale Hong
- Yao Yao
- Xiangmou Qu
- Jiaxin Yin
- Xingyu Lou
- Jun Wang
- Weiwen Liu
affiliations:
- Shanghai Jiao Tong University
- OPPO Research Institute
arxiv_id: '2606.14302'
url: https://arxiv.org/abs/2606.14302
pdf_url: https://arxiv.org/pdf/2606.14302
published: '2026-06-12'
collected: '2026-06-15'
category: Agent
direction: LLM智能体训练 · 进度元认知
tags:
- Progress Awareness
- Self-Reflection
- Agent Training
- Reinforcement Learning
- Retrospective Refinement
- Long-Horizon Tasks
one_liner: 提出RePro框架，通过前向执行-回顾反思范式训练智能体从已完成轨迹中学习进度估计，以辅助长程任务决策，无需额外奖励模型
practical_value: '- **长程多步决策中引入进度信号**：在电商导购、多轮对话等 multi-step agent 场景，可借鉴 RePro 的前向-回顾范式，让模型在完成完整交互后重新标定每一步的完成度，以此作为辅助训练信号，缓解稀疏奖励问题。

  - **过程奖励设计思路**：复合奖励（进度塑造 + 在线-回顾对齐 + 格式正则化）避免了训练昂贵的独立过程奖励模型，可直接接入 GRPO/GiGPO 等现有
  RL 训练管线，适合需要快速迭代的工业界 agent 训练。

  - **元认知评估指标**：使用 Intermediate Discrimination（成功与失败轨迹的最终进度差）作为进度估计质量的代理指标，可应用于 agent
  上线前的离线评估，判断模型是否具备可靠的自我诊断能力。

  - **低成本冷启动模板**：利用少量外部 LLM 生成的回顾演示进行 SFT 预热，即可建立格式正确的反思行为，然后通过 RL 逐步内化，适合在业务数据上以较少样本启动
  agent 的自我反思能力。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM agent 在长程交互中缺乏对任务进度的元认知，在线自我评估往往引入噪声并损害性能，而基于完整轨迹的事后回顾却能带来显著提升。先导实验表明，在线进度提示平均降低成功率 8.6%，而回顾性演示提升 7.9%，但这一能力无法通过结果奖励训练自然涌现，需要专门训练。

**方法**：提出 RePro（Retrospective Progress-Aware Training），包含两个阶段。
- **前向-回顾范式**：agent 执行动作时同步生成在线进度估计，任务完成后利用已知结果和完整轨迹，回顾性重新评估每步的真实进度，得到更可靠的回顾进度序列。
- **回顾性热身（Retrospection Warmup）**：用外部强 LLM 在少量成功轨迹上标注回顾进度，构成演示数据，对 agent 进行 SFT，使其学会回顾反思的格式，但尚无任务奖励基础。
- **RePro-PO 策略优化**：将回顾进度信号融入 RL 训练，设计复合奖励——进度塑造（相邻步进度差）、在线-回顾对齐（缩小在线估计与回顾值的差距）、格式正则化（首尾进度边界约束），并结合分组策略优化（GiGPO）计算层级优势，用 PPO 进行策略更新。整个过程不需要持续的外部监督或额外奖励模型。

**实验**：在 WebShop、ALFWorld、Sokoban 三个基准上，基于 Qwen2.5-1.5B/3B/7B 和 Qwen3-4B 进行验证。对比基线包括 GRPO、GiGPO、Meta Prompt（仅加入进度提示无奖励）、L1（仅格式惩罚）等。RePro 在 WebShop 上相对 Meta Prompt 提升绝对值 +8.98%（1.5B）、+11.57%（3B）、+5.82%（7B）；在 ALFWorld 上提升 +11.72（1.5B）、+4.69（7B）。消融实验表明，仅 SFT 热身无用，去除热身或移除回顾机制性能均大幅下降。
- **进度质量分析**：RePro 的回顾进度在 Intermediate Discrimination 指标上远优于基线（1.5B 时从 1.11 升至 6.37），且失败轨迹出现非平凡的进度衰退，成功轨迹保持高单调性，证明 agent 习得了区分任务成败的元认知。

**核心结论**：让 agent 利用已完成轨迹的结果进行回顾式进度反思，并将其作为内部训练信号，能有效提升长程任务性能，同时使 agent 内化可靠的进度感知能力。
