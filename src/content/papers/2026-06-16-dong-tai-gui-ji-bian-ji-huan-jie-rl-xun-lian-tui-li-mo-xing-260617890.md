---
title: Dynamic Rollout Editing for Reducing Overthinking in RL-Trained Reasoning Models
title_zh: 动态轨迹编辑：缓解 RL 训练推理模型的过度思考
authors:
- Zihao Wei
- Wenjie Shi
- Liang Pang
- Jingcheng Deng
- Shicheng Xu
- Shasha Guo
- Zenghao Duan
- Jiahao Liu
- Jingang Wang
- Huawei Shen
affiliations:
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2606.17890'
url: https://arxiv.org/abs/2606.17890
pdf_url: https://arxiv.org/pdf/2606.17890
published: '2026-06-16'
collected: '2026-06-17'
category: Training
direction: GRPO 训练中的动态轨迹编辑
tags:
- overthinking
- GRPO
- rollout editing
- credit assignment
- RLHF
- reasoning models
one_liner: 针对 GRPO 训练中序列级信用分配导致过度思考膨胀，提出训练时动态编辑成功轨迹的冗余部分
practical_value: '- **Agent 多步推理的截断训练**：在电商 Agent 用 RL 训练时，若成功轨迹存在冗余推理，可借鉴 DRE 思路，在答案出现后截断并保留前缀，避免对无用
  token 的正向强化。

  - **GRPO 信用分配的工程修正**：在广告文案生成或推荐解释的 RL 训练中，即使整体生成质量不错，序列级奖励会错误地鼓励拖沓；可引入轨迹编辑，显式偏好简洁版本。

  - **减少线上推理浪费**：训练时压制 overthinking，能降低部署后 Agent 在搜索、问答场景的 token 浪费，直接节省成本。

  - **监控与干预点**：初始化 GRPO 时检查成功轨迹的过度程度，早期干预可避免反馈循环，适合在推荐模型 RL 微调时作为监控指标。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RL 训练（如 GRPO）的推理模型，常常在得出正确答案后仍继续生成无用的推理步骤，即过度思考。这并非简单的解码端问题，而是训练端的信用分配缺陷：GRPO 的序列级奖励无法区分「达到答案的前缀」和「多余的延续」，两者都获得正向更新，导致初期微小的过度思考失衡被放大成严重冗余。

**方法关键点**：
- 提出 **动态轨迹编辑 (DRE)**，在训练时干预成功但含有过度思考的轨迹。
- 对每条成功轨迹，检测答案首次出现的位置，保留该位置之前的已验证推理前缀，对剩余部分进行编辑（截断或压缩）。
- 在同一 GRPO 组内，让模型偏好编辑后的较短轨迹，从而削弱对不必要推理的正向偏好，而不惩罚必要的推理步骤。
- 该方法不改变奖励函数，仅在 RL 的倾向性比较中插入编辑轨迹。

**关键结果**：在多个数学推理和编码任务上，DRE 显著降低了最终生成的推理长度和过度思考比率，同时保持或提升任务精度，并且训练更稳定。
