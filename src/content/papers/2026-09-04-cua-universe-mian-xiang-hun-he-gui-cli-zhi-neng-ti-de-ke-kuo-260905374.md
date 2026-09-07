---
title: 'CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents'
title_zh: CUA-Universe：面向混合 GUI+CLI 智能体的可扩展动态环境
authors:
- Haoting Shi
- Wenhao Wang
- Weicheng Fang
- Yaozhong Liang
- Tian Jin
- Pengxiang Zhao
- Guangyi Liu
- Siheng Chen
- Yanfeng Wang
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2609.05374'
url: https://arxiv.org/abs/2609.05374
pdf_url: https://arxiv.org/pdf/2609.05374
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: 混合 GUI+CLI 智能体训练环境
tags:
- Computer-Use Agent
- GUI+CLI
- Environment-to-Data
- Post-training
- Tool Use
- Automation
one_liner: 通过环境到数据管线将真实桌面软件转为混合 GUI+CLI 环境，训练 9B 智能体显著提升成功率与效率
practical_value: '- 在电商后台自动化（商品上下架、批量改价、库存调整、报表生成）中，可借鉴混合 GUI+CLI 思路：让 Agent 同时具备页面视觉检查能力与命令行/脚本批量操作能力，避免纯
  GUI 点击的低效和纯 CLI 脚本的脆弱。

  - 环境到数据管线值得迁移：将内部业务系统封装为可复现 VM 并暴露 CLI 接口，基于可重用操作和种子文件自动合成不同难度的任务，持续产出训练轨迹，形成数据飞轮。

  - Path-Steer 的引导式 rollout 与轨迹收割可作为后训练数据工程手段：在业务 Agent 中采集人工修正或规则约束下的高效动作序列，蒸馏到模型，使模型从低效
  GUI 交互转向高效 GUI+CLI 编排。

  - 评估不只盯成功率，同时关注步骤数和 token 消耗。业务上除任务完成率外，应把操作步数、API 调用成本纳入核心指标，优化 Agent 的长期效率与成本。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**

Computer-use agents 在 OSWorld 等基准上虽有进展，但主流方法仍以 GUI 操作为主，轨迹冗长、效率低。真实计算机工作往往是混合的：既要视觉检查界面状态，又要用命令行做精确、高吞吐的批量操作。但构建支持 GUI+CLI 的可扩展环境需要大量手工工程，现有智能体也难以互补使用两种接口——CLI-native 智能体缺乏视觉感知，GUI-native 智能体对适合命令执行的操作低效。

**方法关键点**

CUA-Universe 是一套环境到数据管线，包含三个组件：
- **App-Forge**：将真实桌面应用适配为可复现 VM，并发现、包装或生成命令行接口，扩展到 16 个应用。
- **Task-Weave**：基于种子文件和可重用操作合成多样化、难度可控的混合任务，让每个环境成为持续的任务来源。
- **Path-Steer**：引导 rollout 沿高效混合路径执行，并收割验证过的轨迹用于后训练。

训练后模型行为从低效 GUI 交互和脆弱 CLI 脚本转向有效的 GUI+CLI 编排。

**关键结果**

9B 模型在 CUA-Verse 上 Score +39.3 pts，步数 -37%，token 数 -60%；在 OSWorld 上 SR +16.8 pts，步数 -57%，token 数 -44%；在 OSWorld-MCP 上 Score +7.84 pts，步数 -27%，token 数 -30%。
