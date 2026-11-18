---
title: 'CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon
  Agent Training'
title_zh: CrossEnv：跨环境可验证长程 Agent 任务合成与课程训练
authors:
- Zhengfeng Yu
- Tian Lan
- Zhijing Wu
- Enbo Zhao
- Xuannan Liu
- Feihu Jiang
- Qianghuai Jia
- Longyue Wang
- Zhao Xu
- Weihua Luo
affiliations:
- Beijing Institute of Technology
- Alibaba Group
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.22777'
url: https://arxiv.org/abs/2611.22777
pdf_url: https://arxiv.org/pdf/2611.22777
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 跨环境任务合成 · 课程 RL
tags:
- Cross-Environment
- Environment Synthesis
- Curriculum RL
- Tool Use
- Long-Horizon Agent
one_liner: 用实体-工具图对齐跨环境数据，自动合成可验证长程 Agent 任务，并以课程 RL 提升协同能力
practical_value: '- 电商/广告跨服务 Agent 可用 entity–tool graph 把商品、订单、用户、地址、履约等共享实体作为连接点，自动合成跨服务长程任务，而不是手工设计
  benchmark。

  - 合成时先对齐独立构建的各服务数据记录，确保同一实体在多个工具中一致可执行；生成 reward/verification rules 时同时检查 tool outputs、状态变更和跨服务约束，例如“优惠券适用于当前订单”“配送地址在服务范围内”。

  - 训练策略建议先 SFT 单服务轨迹，再按 同域双服务→同域多服务→跨域多服务→加入用户澄清 的课程做 outcome RL；论文显示相同 GPU 预算下比混合训练成功率更高，且能迁移到未见服务组合与更长
  workflow。

  - 小模型 8B 即可在长程规划与服务协调上获得明显提升；对已有 API/工具环境，可复用 tested tool implementations 和实体关系，新环境接入只需补局部图与缺失工具，降低合成成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

动机

现有 programmatic environment synthesis 大多只生成单环境任务，但真实长程 workflow 常跨多个服务，一个服务的动作依赖另一个服务的信息（例如订机票后酒店选址和餐厅预约要满足到达时间、距离和饮食偏好约束）。自动合成这类训练任务的核心难点是跨环境数据一致性：独立构建的环境数据可能冲突，无法执行和验证。

方法关键点

- CrossEnv 五阶段流水线：单环境研究 → 局部 entity–tool graph 抽取 → 通过共享实体类型合并图并采样连通子图作为任务骨架 → 工具合成与测试 → 任务实例化与验证。
- 任务实例化时进行数据对齐：联合规划初始数据与参考动作，补充缺失记录、解决冲突，保证必要记录初始存在或由早期动作创建。
- 从任务目标与参考执行生成 executable verification rules，同时检查 tool outputs、状态变更和跨环境一致性；再用 reference replay 与独立 agent attempts 过滤任务。
- CrossEnv-Curriculum：L1 单环境 SFT 打基础，L2–L5 逐步 RL（两环境同域 → 三环境同域 → 跨域多环境 → 加入用户交互）。

关键实验

在 τ2-bench、DeepPlanning-Shopping、VitaBench、Claw-Eval 四个外部基准上，基于 Qwen3 1.7B/4B/8B 训练。CrossEnv-8B 仅用 2,954 条训练记录（约 EnvScaler 的四分之一），DeepPlanning 从 1.7 提升到 10.8，VitaBench 从 7.0 到 14.0，Claw-Eval 从 14.4 到 23.6；在 1.7B–8B 模型中 DeepPlanning 与 Claw-Eval 最高，VitaBench 与 Agent-World-8B 并列。课程训练在相似 GPU 小时下比混合训练有更高 strict success 并积累更多 rollouts；跨环境训练相比单环境训练在 output reuse、later-step success、joint success 上明显更好。未见环境组合与 16–18 / 24–28 步更长 workflow 上也有提升。

最值得记住的一句话

跨环境任务合成的关键不是堆更多工具，而是用共享实体对齐数据并生成可执行验证规则，让 agent 学会跨服务协调完成共同目标；配合课程 RL 能更高效地获得泛化能力。
