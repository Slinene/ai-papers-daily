---
title: 'Draft-OPD: On-Policy Distillation for Speculative Draft Models'
title_zh: Draft-OPD：投机草案模型的在线策略蒸馏
authors:
- Haodi Lei
- Yafy Li
- Haoran Zhang
- Shunkai Zhang
- Qianjia Cheng
- Xiaoye Qu
- Ganqu Cui
- Bowen Zhou
- Ning Ding
- Yun Luo
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Tsinghua University
- The Chinese University of Hong Kong
- Peking University
arxiv_id: '2605.29343'
url: https://arxiv.org/abs/2605.29343
pdf_url: https://arxiv.org/pdf/2605.29343
published: '2026-05-27'
collected: '2026-06-02'
category: Training
direction: 投机解码 · 在线策略蒸馏
tags:
- Speculative Decoding
- On-Policy Distillation
- Draft Model
- KL Divergence
- LLM Inference
one_liner: 提出 Draft-OPD，通过错误位置重放的在线蒸馏，解决草案模型 SFT 的分布偏移，将接受长度与加速比提升超过 20%。
practical_value: '- **错误驱动的在线训练思路可迁移至生成式推荐**：将物品推荐视为逐 token 生成，模仿草案模型接收目标模型验证的过程，对推荐序列中被“拒绝”的错误
  token 进行重播与针对性蒸馏，提升生成质量。

  - **接受/拒绝的非对称 KL 设计可复用于轻量级打分模型**：在排序或召回阶段，用目标模型（如大模型）监督轻量级模型时，对正确预测和错误预测分别使用 forward
  KL 和 reverse KL，让轻量模型更专注于自身易错模式。

  - **利用验证阶段的暴露错误进行针对性训练**：在 Agent 多智体协作中，可记录交互过程中被另一智能体“拒绝”的决策点，对这些状态进行重放学习，使策略模型更聚焦于合作失败的关键状态。

  - **解耦 rollout 稳定性和策略信号的思想**：在强化学习或蒸馏中，当学生无法独立生成高质量轨迹时，可借助教师辅助 rollout 维持稳定性，再通过锚点重放学生自身的错误决策，兼顾训练稳定与策略改进。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
投机解码（Speculative Decoding）通过轻量级草案模型（draft model）提前生成多个 token，再由目标模型并行验证来加速推理。主流草案模型（如 EAGLE-3、DFlash）采用离线 SFT 在目标模型生成的轨迹上训练，但训练曲线会快速达到平台期，接受长度不再提升。原因是训练与推理的状态分布存在偏移：SFT 使用的所有前缀均由目标模型生成，而推理时草案模型是在自己提出的 token 块上接受验证，SFT 无法覆盖草案模型自身导致的错误状态。在线策略蒸馏（OPD）是自然解法，但直接应用于草案模型面临两难：草案模型无法独立生成完整序列（退化严重），而目标辅助 rollout 又会抹去草案特有的错误信号，使训练退化为目标分布上的 SFT。

**方法关键点**  
- **带错误位置记录的 rollout**：使用标准投机解码流程生成完整序列，同时记录每块草案 block 的起始位置作为锚点（anchor），保证了 rollout 质量且保留了草案动作的位置信息。  
- **从锚点重放计算 log-prob**：后续对每个锚点进行重放，计算草案模型和目标模型在同一草案诱导前缀下的 token 级对数概率，得到接受与拒绝 token 的集合。  
- **接受感知的蒸馏损失**：对接受 token 使用正向 KL（使草案覆盖目标分布），对拒绝 token 使用反向 KL（惩罚草案高概率但与目标不符的模式），并按指数衰减降低块内靠后位置拒绝 token 的权重，聚焦早期错误。  

**关键实验**  
在 Qwen3 系列模型（4B/8B/30B-A3B-Thinking）上，使用数学推理（GSM8K、MATH-500、AIME）、代码生成（MBPP、HumanEval、SWE-Lite）和 MT-Bench 等基准，与 EAGLE-3、DFlash 在匹配的训练 FLOPs 下对比。开启思维链时，Draft-OPD 平均加速比达到 4.88×，比 EAGLE-3 提升 23%，比 DFlash 提升 13%；在 SGLang 部署环境下，实测吞吐量最高提升 17%。消融实验表明，错误位置重放、非对称 KL 和位置衰减权重均对接受长度有显著贡献。
