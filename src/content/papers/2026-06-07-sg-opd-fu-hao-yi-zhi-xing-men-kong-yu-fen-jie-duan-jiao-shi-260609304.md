---
title: 'SG-OPD: Sign-Gated On-Policy Distillation via Sign-Consistency Gating and
  Phased Teacher Sampling'
title_zh: 'SG-OPD: 符号一致性门控与分阶段教师采样的在线策略蒸馏'
authors:
- Haoran Xu
- Hongyu Wang
- Yifei Gao
- Jiaze Li
- Xiaofeng Zhang
- Xiaosong Yuan
affiliations:
- Zhejiang University
- Hunan University
- Tianjin University
- Shanghai Jiao Tong University
- Jilin University
arxiv_id: '2606.09304'
url: https://arxiv.org/abs/2606.09304
pdf_url: https://arxiv.org/pdf/2606.09304
published: '2026-06-07'
collected: '2026-06-12'
category: Training
direction: 训练方法 · 在线蒸馏与符号一致性
tags:
- On-policy Distillation
- Sign Consistency
- Verifier-guided
- Mathematical Reasoning
- Student-Teacher
- Cold-start
one_liner: 用验证器信号在轨迹和 token 层面过滤教师噪声，显著提升数学推理中的在线蒸馏效果
practical_value: '- 在蒸馏冷启动阶段，使用验证器认可的教师轨迹按比例混入学生采样，能缓解轨迹对齐脆弱性问题；对电商场景下从大模型向小模型蒸馏对话或推荐理由时，可参考该分阶段策略以稳定初期训练。

  - 符号一致性门控根据验证器与教师偏好的方向一致性，外推或内插蒸馏更新，相当于给 token 级监督赋予可调信任权重；在生成式推荐或 Agent 动作生成中，可引入类似的二值验证器来鉴别教师
  token 的可靠性，降低噪声标签对蒸馏的负面影响。

  - 整体框架强调用验证器作为学生和教师之外的第三方信任信号，这为多智能体系统中的知识迁移提供了新思路：可以设计一个专门的验证 Agent，监督教师智能体对学生智能体的指导质量。

  - 尽管实验集中在数学推理，但方法不依赖任务特定设计，可直接迁移至任意序列生成任务的在线蒸馏，例如商品描述改写、搜索 Query 扩展等。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：标准在线策略蒸馏（OPD）假设学生轨迹始终与教师对齐，且教师每个 token 的偏好同等可靠，但在强到弱的蒸馏场景下这两个假设经常失效，尤其在冷启动阶段。

**方法**：提出 SG-OPD，引入一个二值验证器作为教师可信度信号。在轨迹层面，采用分阶段教师采样，初始阶段混合验证器批准的教师轨迹与学生轨迹，逐渐过渡到纯学生采样；在 token 层面，设计符号一致性门控，当验证器与教师方向一致时外推蒸馏梯度，不一致时内插，从而动态调整每个 token 的监督强度。

**结果**：在竞赛级数学推理基准上，SG-OPD 相比标准 OPD 平均每样本提升 1.98，每问题提升 7.50，效过显著且稳定。
