---
title: 'SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise
  SaaS Engineering'
title_zh: SaaSBench：评估编码代理在长周期企业SaaS工程中的能力边界
authors:
- Qingnan Ren
- Shun Zou
- Shiting Huang
- Ziao Zhang
- Kou Shi
- Zhen Fang
- Yiming Zhao
- Yu Zeng
- Qisheng Su
- Lin Chen
affiliations:
- University of Science and Technology of China
- AMAP, Alibaba Group
arxiv_id: '2605.17526'
url: https://arxiv.org/abs/2605.17526
pdf_url: https://arxiv.org/pdf/2605.17526
published: '2026-05-16'
collected: '2026-05-22'
category: Agent
direction: 编码代理评估 · 长周期SaaS基准
tags:
- coding agent
- SaaS benchmark
- DAG evaluation
- multi-component systems
- long-horizon
- enterprise software
one_liner: 首个面向真实企业级SaaS生成的评估基准，揭示当前代理主要瓶颈在于多组件系统集成而非代码逻辑
practical_value: '- 在构建电商业务系统或其他内部工具的 Agent 时，采用依赖感知的 DAG 测试套件进行端到端验证，避免仅用单元测试忽略跨组件交互错误。

  - 长周期任务中优先确保基础部署和系统连通性，再进入复杂业务逻辑；95% 的失败发生在系统未能稳定运行阶段，提示 Agent 工作流应加入环境自检与自动修复环节。

  - 借鉴 PRD + 歧义消除知识库（KB）的输入设计，在需求文档中显式化模糊边界规则，可用于电商商品、订单、权限等复杂业务逻辑的需求澄清，减少 Agent 理解偏差。

  - 失败模式分析表明，代理容易“过早自信”而提前停止，可设计阶段性验证门控，类似 DAG 前置依赖检查，强制 Agent 完成基础工程后才能进入深层次业务实现。'
score: 8
source: huggingface-daily
depth: full_pdf
---

#### 动机
现有编码基准多局限于函数级补全或单个技术栈的项目生成，未能反映真实企业 SaaS 开发的异构性、全栈编排和系统级复杂性。为此，该工作构建了第一个系统设计的企业级 SaaS 编码代理基准，旨在探索代理在长周期、多组件耦合任务中的真实能力边界。

#### 方法关键点
- **任务构建**：从真实商业软件市场出发，选定 6 大 SaaS 领域共 30 个任务，每个任务附带详细产品需求文档（PRD，平均 4,363 行）、消除歧义的知识库（KB）、标准化 Docker 运行环境。
- **评估范式**：设计依赖感知的 DAG 测试套件，包含 5,370 个验证节点和 6,167 条前置依赖边。节点编译为可执行原语链，采用二元、加权和 LLM-as-Judge 三种评分方式，覆盖部署、数据、API、业务逻辑、权限、质量六个工程维度。
- **代理执行**：代理在隔离容器中从零构建并部署可运行的 SaaS 系统，评估时按拓扑顺序执行 DAG 节点，前置失败则下游节点标记为“依赖跳过”，避免级联惩罚。

#### 关键实验结果
- 评估 8 个主流模型在 OpenHands 和 Claude Code 两个代理框架上的表现，最佳成绩仅为 Claude Opus 4.7 + Claude Code 的 Pass@1 20.68%。
- 超过 95% 的任务失败发生在系统稳定运行和基础配置阶段，代理常常在搭建基本系统时就过早停止或陷入无效调试循环。
- 基础部署维度得分最高，业务逻辑与权限维度次之，代码质量维度得分最低，暴露当前代理在工程鲁棒性上的严重不足。

#### 核心收获
**当前编码代理的主要瓶颈不是生成孤立的代码逻辑，而是成功配置并集成一个多组件系统。** 这一发现对长周期、多服务的 Agent 系统设计具有重要警示意义。
