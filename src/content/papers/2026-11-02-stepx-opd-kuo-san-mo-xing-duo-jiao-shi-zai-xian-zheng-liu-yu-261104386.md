---
title: 'StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models'
title_zh: StepX-OPD：扩散模型多教师在线蒸馏与少步采样一体化训练
authors:
- Chenru Wang
- Xuanyang Zhang
- Yucheng Han
- Wenbo Nie
- Wei Cheng
- Xianfang Zeng
- Gang YU
- Chi Zhang
affiliations:
- StepFun
- Westlake University
arxiv_id: '2611.04386'
url: https://arxiv.org/abs/2611.04386
pdf_url: https://arxiv.org/pdf/2611.04386
published: '2026-11-02'
collected: '2026-11-08'
category: Training
direction: 扩散模型少步多能力联合蒸馏
tags:
- Diffusion Models
- On-Policy Distillation
- Text-to-Image
- Step Distillation
- Multi-Teacher
one_liner: 把多能力在线蒸馏与少步采样蒸馏合并为单阶段，四步学生超过四十步模型并省约 37% GPU 小时
practical_value: '- 电商广告/商品图生成需要快速出图且兼顾文字渲染、品牌风格等能力；可把多能力蒸馏与少步采样合并训练，而不是先学能力再压缩，降低迭代成本并减少压缩损失。

  - on-policy 蒸馏思路可迁移到 LLM/推荐策略蒸馏：让 teacher 只在学生策略实际生成的状态/轨迹上打分或回归，不要用 teacher 自身的完整轨迹，缓解
  train-inference mismatch。

  - 按阶段/状态重要性加权对齐：发现靠近终态的低噪声区域速度误差更关键，业务中做精排、生成式推荐或 Agent 决策蒸馏时，可对最终输出附近的 state 或高
  reward 轨迹段加大权重。

  - 注意多任务能力整合的副作用：模型可能“溢出”不必要行为（如乱写字），业务生成中应加入显式负样本/条件控制抑制不期望输出。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：可部署的 text-to-image 扩散模型必须同时满足指令跟随、文本渲染、人类偏好等能力，并且要以少步数采样。现有流程分两个串行阶段：full-step 多教师 on-policy 蒸馏先固化能力，再做 step distillation 压缩步数；不仅总成本高，压缩后各能力普遍下滑。

**方法关键点**：StepX-OPD 把两阶段合并为单一训练阶段，学生模型同时学习多能力和少步采样。冻结的专家教师不再沿更长的完整轨迹监督，而是在学生自身 rollout 实际经过的状态上做 on-policy 蒸馏，减少训练与推理的不一致。对 rollout 的 KL 权重分解显示速度不匹配主要集中在靠近干净样本的低噪声端，因此在 rollout 低噪声部分额外回归学生速度。另一发现是能力整合后模型容易把 prompt 中的单词写入图片，即使 prompt 未要求文字；论文给出一个 variant 来抑制该现象。

**关键结果**：在 SD3.5-Medium 和 FLUX.1-dev 上，StepX-OPD 在所有四步方法中平均标准化分数最高，并超过四十步 Flow-OPD；在 SD3.5-Medium 上比串行 DiffusionOPD + step distillation 节省约 37% GPU-小时。
