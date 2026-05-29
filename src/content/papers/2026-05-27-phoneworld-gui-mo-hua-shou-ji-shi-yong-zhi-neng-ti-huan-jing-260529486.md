---
title: 'PhoneWorld: Scaling Phone-Use Agent Environments'
title_zh: PhoneWorld：规模化手机使用智能体环境
authors:
- Zhengyang Tang
- Yuxuan Liu
- Xin Lai
- Junyi Li
- Pengyuan Lyu
- Jason
- Yiduo Guo
- Zhengyao Fang
- Yang Ding
- Yi Zhang
affiliations:
- Tencent Hunyuan
- The Chinese University of Hong Kong, Shenzhen
- Renmin University of China
- Wuhan University
arxiv_id: '2605.29486'
url: https://arxiv.org/abs/2605.29486
pdf_url: https://arxiv.org/pdf/2605.29486
published: '2026-05-27'
collected: '2026-05-29'
category: Agent
direction: 手机使用Agent环境构建与训练数据生成
tags:
- phone-use agent
- environment construction
- mock app
- training data
- scaling
- AndroidWorld
one_liner: 将真实GUI轨迹转化为可重置、可验证的手机mock应用环境，并支持训练数据生成与评估。
practical_value: '- 借鉴用真实用户轨迹还原 app 页面优先级与导航图的方法，为电商 App 内的智能体训练构建高覆盖率 mock 环境，避免手动编写费时费力。

  - 将只读业务内容（商品、店铺信息）与可写状态（购物车、收藏）分离，并在 SQLite 中做确定性状态管理，既可重置环境，又能用 SQL 查询实现自动化任务验证，适合电商任务（如下单、收藏）的批量奖励信号生成。

  - 在固定训练步骤预算下，将少部分源自有业务 app 轨迹的 PhoneWorld 数据混入通用 AndroidWorld 数据，可同时提升域内与域外 benchmark，尤其在商品搜索、下单等场景能快速获得额外提升。

  - 缩放 app 覆盖率比单纯增加轨迹数收益更大，建议优先扩展覆盖的 app 种类（如不同电商子场景），再适当增加每个 app 内的轨迹量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：手机使用智能体的进步受限于缺乏大规模、可控制且可复现的环境。现有移动端 benchmark 仅聚焦于评估，未解决如何持续构造新环境的问题。PhoneWorld 提出一套可复用的流水线，将真实用户 GUI 轨迹和截图转化为可运行、可重置的 mock 安卓应用，并自动生成可执行任务与验证器，从而规模化供应环境。

**方法关键点**：
1. 从真实 app 使用录制中恢复屏幕清单、页面访问频率与跳转图，确定必须构建的页面优先级（P0/P1/P2）。
2. 依据恢复的结构，用 VLM 为每个页面生成 PRD，并构建跨应用可复用组件库（搜索、评论、消息等 18 个模块）。
3. 采用只读应用内容 + 可重置 SQLite 状态的数据架构，使环境离线运行、可重复重置，且便于用 SQL 查询实现确定性 verifier。
4. 通过编码智能体（Claude Code）迭代生成 Kotlin/Jetpack Compose 源码、编译、自查并修复，最终人工审核确保关键页面和交互功能正确。
5. 基于环境内只读数据和 schema，自动生成 7936 个可验证任务，并筛选成功 rollout 作为训练数据（3354 条成功轨迹，36193 步）。

**关键实验**：
- 基准模型：Qwen3.5-9B，在 AndroidWorld 基础语料（36193 步）上训练。
- 实验 1：固定 72386 步训练总预算，用 PhoneWorld 的 10000 步替换等量 AndroidWorld 辅助语料，HYMobileBench +17.7，AndroidControl +6.0，AndroidWorld +14.7，PhoneWorld +52.5。
- 实验 2：完全替换辅助语料，PhoneWorld 最高，但 AndroidWorld 下降 10.3，表明两者互补。
- 实验 3：缩放 PhoneWorld 步数（0→36K），PhoneWorld 任务成功率从 14.2% 单调升至 73.3%。
- 实验 4：固定 10K PhoneWorld 步数，app 源头从 5 个扩展到 34 个，PhoneWorld +18.3，HYMobileBench +18.3，AndroidWorld +10.4，证明 app 覆盖率是最强缩放信号。

**最值得记住的一句话**：缩放手机使用智能体，不仅要增加训练数据量，更要扩展可控环境的多样性与覆盖面。
