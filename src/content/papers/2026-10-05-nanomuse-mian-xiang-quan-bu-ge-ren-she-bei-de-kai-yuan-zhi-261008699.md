---
title: 'nanoMuse: An Open-Source Personal Agent for Every Device You Own'
title_zh: nanoMuse：面向全部个人设备的开源智能体
authors:
- Guangyi Liu
- Yong Liu
- Jiangning Zhang
affiliations:
- Zhejiang University
arxiv_id: '2610.08699'
url: https://arxiv.org/abs/2610.08699
pdf_url: https://arxiv.org/pdf/2610.08699
published: '2026-10-05'
collected: '2026-10-08'
category: Agent
direction: 个人 Agent 多设备协同与开源实现
tags:
- Personal Agent
- Open Source
- Multi-device
- Action Guard
- Memory Provenance
- Hands
one_liner: 开源多设备个人 Agent，手机/桌面 Hands、共享会话、动作审核与文件记忆
practical_value: '- **多设备 Agent 架构可借鉴**：relay 统管设备注册与消息同步，手机/桌面端各自携带 Hands 操作屏幕，适合电商场景下“手机端操作
  App + 桌面端处理表格”的混合任务；把会话状态放在 relay，客户端只做执行，降低状态同步复杂度。

  - **动作审核层（Sentinel）值得落地**：所有 agent 动作先经过审核，能拦截高风险操作；在广告投放、自动下单、批量改价等场景，可把 Sentinel
  做成策略引擎，按风险分级决定自动执行/人工确认。

  - **用可读文件做记忆，带溯源**：memory 以用户可读文件保存，并记录来源；推荐/客服 agent 可把用户偏好、历史行为写成结构化文件，支持人工编辑和审计，避免黑盒记忆。

  - **开源可替换模型降低合规成本**：企业可自托管 relay 和 agent，模型可选，适配数据合规；但 Hands 操作手机屏幕在真实电商环境需考虑系统权限和稳定性，初期可用于桌面端任务自动化。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：2011 年的助手只会回答后等待，2023 年的 agent 只执行单次任务；Meta Muse 展示了一个能为个人长期服务、跨账号设备记忆的 agent，但闭源、云托管、单地区。论文定义个人 agent 的五个问题与三个时间范围，还原 Muse 的构建方式，并推出开源对应实现 nanoMuse。

方法关键点：nanoMuse 采用 GPL-3.0 开源，每台设备运行一个 agent，手机和桌面端具备 Hands 可直接操作屏幕，iPhone 无 Hands 时可请求其他设备代为执行；所有设备通过可自托管的 relay 共享同一会话，relay 负责设备签名、传递 frames 和同步文本；每个动作经过 Sentinel 审核，memory 存放于用户可读文件，模型可替换，桌面端 Hands 以轨迹形式保存支持回放审计。

关键结果：给出系统规模与成本估计，开源路线图包括 memory 溯源、Hands 评测套件与开源操作模型。
