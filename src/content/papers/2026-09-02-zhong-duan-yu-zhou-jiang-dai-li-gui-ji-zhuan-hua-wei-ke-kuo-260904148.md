---
title: 'Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments'
title_zh: 终端宇宙：将代理轨迹转化为可扩展终端环境
authors:
- Jie Wu
- Zhenru Zhang
- Beichen Zhang
- Xuwu Wang
- Yuhui Su
- Mouxiang Chen
- Peng Wang
- Zhihai Wang
- Que Shen
- Hao Zhou
affiliations:
- Qwen Team, Alibaba Group
- Tsinghua University
arxiv_id: '2609.04148'
url: https://arxiv.org/abs/2609.04148
pdf_url: https://arxiv.org/pdf/2609.04148
published: '2026-09-02'
collected: '2026-09-04'
category: Training
direction: 代码代理环境重建与训练数据合成
tags:
- Code Agents
- Environment Reconstruction
- Synthetic Data
- Multi-turn
- Cross-workspace
- SFT
one_liner: 从终端代理轨迹重建可执行环境，并扩展单轮/跨仓库多轮任务，SFT 大幅提升代码代理基准
practical_value: '- 在电商导购/客服 Agent 中，可借鉴轨迹回放恢复环境：从真实日志（点击/搜索/下单）反向重建决策前状态，再用补全模型补缺失上下文，生成可重用的训练环境，而非只存静态问答对。

  - 广度扩展可用于跨业务域任务构造：挖掘不同店铺/订单/支付等子系统的依赖关系，合成跨系统串联任务，训练模型进行多步工具调用。

  - 深度扩展的 user agent 模式可用于多轮交互训练：模拟用户逐步反馈和需求细化，把单轮意图改写成多轮会话，提升推荐/客服 Agent 的持续交互能力。

  - 环境可重查询特性适合构建推荐/广告模拟器：通过执行反馈做可验证采样或拒绝采样，替代固定轨迹数据。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：终端代码代理轨迹大量积累，但可执行环境稀缺。环境是 post-training 真正需要的数据来源：每个环境可被反复查询生成可验证任务并提供执行反馈，而轨迹只是单次冻结演示。

方法：Terminal-Universe 不从头生成环境，而是从轨迹中重建。它重放轨迹记录的文件操作，恢复 agent 修改前的每个文件，形成部分工作区；补全代理补充缺失文件和依赖。在恢复工作区上，既重构原始意图任务，也合成全新任务。任务扩展分两个轴：广度上挖掘相关环境间的方向性依赖，合成跨仓库查询；深度上用 user agent 模拟多轮用户反馈与需求细化，将单轮扩展为多轮会话。

结果：在公开终端代理轨迹上产出 37.3k 个任务充分环境。用该语料对 Qwen3.5-27B 做 SFT 后，Terminal-Bench 2.1 单轮性能提升 11.9 分，EvoCode-Bench v2 MT@4 多轮性能提升 13.8 分。
