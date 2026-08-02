---
title: 'Change2Task: From Repository Changes to Executable Coding Agent Tasks and
  Environments'
title_zh: Change2Task：从仓库变更自动构建可执行编码代理任务与环境
authors:
- Haomin Qi
- Xingliang Wang
- Xuanqi Gao
- Baihui Sang
- Xin Zhang
- Minghua Ma
- Pengfei Gao
- Yu Kang
- Qingwei Lin
- Saravan Rajmohan
affiliations:
- Microsoft
- University of California San Diego
- Zhejiang University
- Xi’an Jiaotong University
- Nanjing University
arxiv_id: '2607.28591'
url: https://arxiv.org/abs/2607.28591
pdf_url: https://arxiv.org/pdf/2607.28591
published: '2026-07-30'
collected: '2026-08-02'
category: Agent
direction: 代理任务自动构建与验证
tags:
- Coding Agent
- Task Construction
- Environment Engineering
- Training Data
- Software Engineering
one_liner: 利用合并 PR 逆向重建健康代码库上的可验证编码代理任务，成功率达 79.6%，比 PR 基线多恢复 29.2%
practical_value: '- **历史操作逆向为可复现环境**：可借鉴 Patch Reversal 思路，将推荐系统的用户行为日志或实验配置「逆向」生成可重复执行的
  Agent 训练任务，降低构造成本。

  - **任务生命周期验证**：从健康基础状态 → 任务状态 → 修复状态的全流程验证，可用于确保离线仿真环境的一致性和可靠性，避免训练与上线偏移。

  - **环境基础复用节约开销**：论文中重用现代基础镜像降低 10.8% 端到端成本，类似地，在推荐 Agent 的持续训练中通过共享基础镜像可减少重复构建。

  - **多任务统一构造框架**：覆盖 Bug 修复、特性添加等多类任务，启示搜索推荐 Agent 训练也可统一构造排序、召回、文案生成等不同任务，提升泛化性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：编码代理（coding agent）的训练和评估需要大量可执行任务，手动构建仓库任务环境成本高且容易过时。如何从现有历史变更中低成本、大规模地生成可靠任务？

**方法**：Change2Task 系统直接从合并的 PR 出发，将历史证据与现代代码库对齐，通过三种方式重建任务状态：补丁反转（Patch Reversal）回退到修复前状态；代码映射（Code Mapping）适配已演进代码；代理重建（Agent Reconstruction）自动迁移。整个过程严格验证「健康基础状态 → 引入缺陷的任务状态 → 应用补丁后的修复状态」的完整生命周期，并自动适配依赖环境。支持 Bug 修复、特性添加、测试生成、API 迁移、安全修复五类常见任务。

**结果**：在 1,130 个源变更上，平均 79.6% 成功构建出可验证任务，比直接使用 PR 的基线方法多恢复 29.2% 的任务。在代理执行评估下，历史任务与重建任务的结果一致性高达 98%。同时，重用现代基础镜像使端到端流水线耗费降低 10.8%。
