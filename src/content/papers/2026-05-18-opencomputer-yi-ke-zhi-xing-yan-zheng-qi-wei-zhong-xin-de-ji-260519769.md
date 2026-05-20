---
title: 'OpenComputer: Verifiable Software Worlds for Computer-Use Agents'
title_zh: OpenComputer：以可执行验证器为中心的计算机使用智能体任务合成框架
authors:
- Jinbiao Wei
- Qianran Ma
- Yilun Zhao
- Xiao Zhou
- Kangqi Ni
- Guo Gan
- Arman Cohan
affiliations:
- Yale NLP Lab
- University of Pennsylvania
- University of North Carolina at Chapel Hill
arxiv_id: '2605.19769'
url: https://arxiv.org/abs/2605.19769
pdf_url: https://arxiv.org/pdf/2605.19769
published: '2026-05-18'
collected: '2026-05-20'
category: Agent
direction: 计算机使用智能体 · 可验证任务合成与评估
tags:
- computer-use agents
- programmatic verification
- self-evolving verifier
- desktop task synthesis
- benchmark
- LLM-as-judge vs hard-coded
one_liner: 构建以应用状态程序化验证器为核心的桌面任务合成框架，覆盖33款软件共1000个任务，揭示前沿GUI智能体端到端完成仍存显著差距
practical_value: '- **用可执行状态检查替代LLM评判**：在电商 Agent 或生成式推荐评估中，对商品属性、金额、文件状态等可结构化查询的指标，应优先构建硬编码验证器，避免
  LLM-as-judge 在细粒度状态上的误判，本工作中硬编码验证器与人类判断任务级对齐度达 94.1%，远超 LLM 评判的 79.2%。

  - **自我进化验证层思路**：利用强 Agent 跑简单校准任务，对比程序化验证器与 LLM 参考判定的分歧，自动修验证器端错误并记录根因（如数据库 schema
  迁移），可用于在线场景中持续改善业务规则检查器或 RL 奖励信号的可靠性。

  - **任务合成的可验证前置设计**：在设计推荐或对话评测集时，应先将成功标准编码为可执行检查项（如查询数据库、比对文件），再反向生成任务描述与初始状态，有效避免生成无法自动判定的示例，提升数据可用性。

  - **跨接口能力评估启示**：GUI 与 CLI Agent 在共享任务子集上的对比显示，视觉交互仍提供有效 grounding，但命令行执行速度更快（141s
  vs 288s），对电商后台操作或流程自动化场景，可针对性地混合使用两类接口，并统一用程序化验证器衡量最终应用状态。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
构建计算机使用智能体的真实桌面任务需要手动准备文件、配置等初始环境，并编写定制化的状态检查脚本，成本极高且难以规模化。现有基准多依赖人工或 LLM 评判，后者对截图可见错误不敏感，无法可靠捕捉隐藏应用状态（如数据库、文件元数据、终端日志）中的关键失败。亟需一种将验证器作为核心约束的任务合成方式，使每个任务天然附带可执行、可审计的成功标准。

### 方法关键点
1. **应用状态验证器生成**：为 33 款桌面软件构建 Python 验证器模块，通过 SQLite、CDP、D-Bus、文件解析等稳定接口暴露结构化状态检查端点（如 `check_tag_exists`、`check_cell_value`），并经历单元测试和集成测试的 debug-fix-retry 循环。
2. **自我进化验证层**：用强 Agent 执行约 15 个简单校准任务，冻结轨迹和最终状态；对比 LLM 参考判定与程序化验证器结果，识别验证器侧错误（如 schema 漂移），自动修复并记录教训，迭代后验证器与人判断一致性从 85.2% 提升至 94.1%，修复率达 89.4%。
3. **验证器感知的任务合成**：先按用户目标多样性提议候选任务，再按复杂度、数据可生成性和状态可检查性过滤，仅保留可由现有或扩展验证器端点可靠判定的任务，最终生成任务描述、初始环境脚本和成功标准清单。
4. **可审计的评估工具**：在干净沙箱中运行智能体，录制全轨迹，通过执行验证器命令计算部分成功得分（通过数/总检查项），避免截图模糊性。

### 关键实验
- **数据集**：覆盖浏览器、办公、创作、开发等 33 款桌面应用，共 1000 个最终任务，平均每任务 6.9 项检查点。
- **智能体表现**：GPT-5.4 成功率 68.3%（平均步数 19.0），Claude-Sonnet-4.6 64.4%，Kimi-K2.6 58.8%；开源模型下降剧烈，GUI-OWL-1.5-8B 仅 5.7%（OSWorld 上报 52.3%）。
- **验证器可靠性**：硬编码验证器与人类任务级对齐 94.1%，LLM 评判仅 79.2%；在密集界面（如 Calc）和终端任务中硬编码验证器能避免视觉误判。
- **GUI vs CLI**：在 343 个 CLI 兼容任务上，GUI 成功率更高（75.2% vs 67.2%），但 CLI 平均耗时仅为 141s（GUI 288s）。

### 最值得记住的一句话
**OpenComputer 证明了以程序化应用状态检查为核心的任务合成管线，既能规模化生成可审计的桌面智能体基准，又能暴露当前模型在端到端完成上的脆弱性，同时显著提升了评估的人类对齐度。**
