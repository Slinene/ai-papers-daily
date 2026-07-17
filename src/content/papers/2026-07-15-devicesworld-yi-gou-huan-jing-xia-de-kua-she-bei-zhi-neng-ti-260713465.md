---
title: 'DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments'
title_zh: DevicesWorld：异构环境下的跨设备智能体基准
authors:
- Huatao Li
- Xinwei Geng
- Yuheng Wang
- Yutong Li
- Runde Yang
- Hantao Chen
- Shu Yao
- Jingru Fan
- Xuhui Ren
- Yuanyuan Zhao
affiliations:
- Shanghai Jiao Tong University
- Honor Device Co., Ltd
arxiv_id: '2607.13465'
url: https://arxiv.org/abs/2607.13465
pdf_url: https://arxiv.org/pdf/2607.13465
published: '2026-07-15'
collected: '2026-07-17'
category: Eval
direction: 跨设备 Agent 评估基准
tags:
- cross-device agents
- benchmark
- heterogeneous environments
- LLM agents
- task evaluation
- multi-device collaboration
one_liner: 构建统一跨设备基准，含6140个任务，现有最佳Agent成功率仅12.5%
practical_value: '- 在电商/推荐场景中，可借鉴其多端协同任务设计（如手机浏览、PC下单、IoT确认），构建跨设备购物流程的评估集，测试对话/推荐Agent的跨设备信息跟踪与整合能力。

  - 任务自动验证机制（基于设备状态和文件检查）可直接用于生成式推荐中跨场景的单元测试，提高评测效率。

  - 所发现的Agent典型失败模式（卡在信息获取、混淆源与目标设备、过早终止）为实际系统设计防错策略提供参考，例如增加设备角色校验、强制依赖条件检查。

  - 在面向Agent的搜索推荐系统中，引入跨设备依赖的任务可以暴露Agent在分布式环境下的短板，从而针对性地改进多跳推理和状态管理。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：现有LLM Agent评估多局限于单一设备（手机、桌面），但真实任务常需跨设备协作（如从手机获取信息、在桌面处理、输出到另一个设备），缺乏统一评估跨设备协作能力的基准。

**方法**：构建**DevicesWorld**，包含6140个任务，整合手机、桌面、IoT三类异构设备环境为统一交互与评估框架。每个任务定义自然语言目标、参与设备及初始状态、可执行动作、基于规则的自动验证器和清理流程。通过多阶段构建与质量控制流水线保证任务贴近真实需求，且能从设备状态和文件自动判定结果。

**关键结果**：在5个前沿LLM Agent系统上评估，最佳成功率仅**12.5%**；约28.7%的失败案例中Agent至少满足一项评分条件但未完成全部要求。轨迹分析显示Agent常卡在信息获取或界面操作、混淆源与目标设备、在条件未全部满足时提前终止。
