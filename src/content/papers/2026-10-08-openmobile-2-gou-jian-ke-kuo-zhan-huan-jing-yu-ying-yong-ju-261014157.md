---
title: 'OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments
  and App-Native Tools'
title_zh: OpenMobile-2：构建可扩展环境与应用原生工具的通用移动智能体
authors:
- Chenyang Yan
- Yingying Zhang
- Kanzhi Cheng
- Qiushi Sun
- Zhengyuan Pan
- Zheng Ma
- Hang Yan
- Yian Wang
- Nuo Chen
- Jialin Cao
affiliations:
- Nanjing University
- SenseTime
- The University of Hong Kong
- Xi'an Jiaotong University
- National University of Singapore
arxiv_id: '2610.14157'
url: https://arxiv.org/abs/2610.14157
pdf_url: https://arxiv.org/pdf/2610.14157
published: '2026-10-08'
collected: '2026-10-19'
category: Agent
direction: 移动智能体环境与工具混合训练
tags:
- Mobile Agent
- GUI
- RL
- SFT
- Tool Use
- Environment
one_liner: 开源移动智能体OpenMobile-2，提供110+应用环境、12K SFT轨迹与2K可验证RL任务，支持GUI与原生工具混合使用
practical_value: '- 借鉴「GUI + app-native tool」混合模式：在电商 Agent 中，把搜索、加购、下单等关键操作封装为结构化工具，与页面
  GUI 操作交替使用，可降低对视觉解析的依赖，提高动作准确率和可执行性；同时保留 GUI 兜底应对未封装的长尾页面。

  - 用可验证任务 + 自动奖励扩展 RL 训练：借鉴其 2K+ 可执行任务、自动 reward 的设计，在推荐/客服 Agent 训练中构造「完成订单/加入购物车/点击商品」等可自动判定的任务，低成本获取大规模
  RL 数据。

  - 构建跨 App 工作流仿真环境：在电商场景中，模拟搜索、详情、购物车、支付等多 App 跳转与重置，用于离线评测和训练 Agent，避免在真实 App 上试错；其
  MobileGym++ 的 reset/verification 机制可直接迁移。

  - 关注长时程商业任务评测：MobileGym++ Bench 支持 GUI-only 与 hybrid 共享任务套件，可用于对比不同交互范式的效果，帮助选型工具化
  vs 纯视觉方案。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有移动 Agent 训练依赖闭源环境与数据，难以复现和扩展；GUI 操作易出错，需要更可靠的交互方式。  
**方法**：构建 MobileGym++，含 35 个商业风格仿真 App 与 110+ App 的 Android 模拟器环境；整理 12K 条 SFT 轨迹和 2K+ 可验证 RL 任务（自动 reward）；引入混合 GUI 与原生产工具调用，在 50+ App 上封装 300+ 工具；提出 MobileGym++ Bench 支持 GUI-only 和 hybrid 评测。  
**结果**：OpenMobile-2 在 AndroidWorld 达 79.9，MobileWorld 50.4，SPA-Bench 从 31.9 提升到 59.6，接近前沿水平。
