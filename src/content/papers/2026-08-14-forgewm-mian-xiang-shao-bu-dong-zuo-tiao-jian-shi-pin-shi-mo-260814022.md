---
title: 'ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video
  World Models'
title_zh: ForgeWM：面向少步动作条件视频世界模型的渐进式因果训练
authors:
- Xinye Li
- Lingshuai Lin
- Lei Wang
- Liuzhou Zhang
- Jialin Cui
- Qingshan Li
- Guanchu Wang
- Qingbin Liu
- Xi Chen
- Jiang Bian
affiliations:
- CUHK
- Tencent PCG
- FDU
- Shanghai AI Laboratory
- HKUST
arxiv_id: '2608.14022'
url: https://arxiv.org/abs/2608.14022
pdf_url: https://arxiv.org/pdf/2608.14022
published: '2026-08-14'
collected: '2026-08-22'
category: Multimodal
direction: 少步动作条件视频世界模型
tags:
- Video World Model
- Causal Distillation
- Few-Step Generation
- Action-Conditioned
- On-Policy Matching
one_liner: 提出 ForgeWM 框架，将双向视频生成器蒸馏为 1/2/4 步动作条件世界模型，并支持低延迟生成与事后细化
practical_value: '- 若业务中需要实时交互式生成（如对话式推荐、生成式搜索补全），可借鉴按计算预算训练多个专用学生（1/2/4 步），针对不同延迟
  SLA 选择对应模型，避免单一大模型的算力浪费。

  - 双路径部署思路值得迁移：线上用极低步数模型快速生成草稿并保存，异步回流时再用更高质量路径对草稿进行重噪细化，与推荐系统中的粗排-精排/异步重排相似，能显著降低在线延迟。

  - 蒸馏过程中引入因果一致性约束和在线策略匹配，能缓解自回归生成中的曝光偏差，对于需要根据用户交互实时生成下一步内容的 Agent 或生成式推荐系统有借鉴意义。

  - 主要贡献集中在视频世界模型领域，与电商/搜索推荐直接关联度有限，更适合作为实时生成式交互系统的工程参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：动作条件视频世界模型需要低延迟因果生成，并能可靠响应游戏原生控制。虽然因果蒸馏已能实现少步视频合成，但将其扩展到交互式世界模型仍面临挑战：离散键盘状态与连续鼠标运动必须与时间压缩的潜块在因果训练和自回归推理过程中保持对齐。

**方法**：ForgeWM 采用渐进式四阶段蒸馏框架：域适应、教师强制因果训练、因果一致性蒸馏，以及与双向教师模型的在线策略分布匹配。该框架将双向动作条件视频生成器转化为预算专属学生模型，分别支持 1、2、4 步去噪预算。同时提出双路径部署协议：交互时使用一步学生快速生成草稿，可选回放时通过重噪再细化提升质量。

**结果**：在配对的 Minecraft 轨迹上，ForgeWM 在成像质量、参考对齐运动轮廓一致性、动作符号准确率、鼠标控制准确率四项指标上均领先，且参考 LPIPS 最低；同一四阶段方法可迁移至游戏手柄控制的 FPS 场景。回放时细化与四步参考质量相当，且相比从噪声重新生成更接近实际经历轨迹约 3 倍。
