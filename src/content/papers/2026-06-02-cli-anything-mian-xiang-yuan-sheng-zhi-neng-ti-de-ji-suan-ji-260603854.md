---
title: 'CLI-Anything: Towards Agent-Native Computer Use'
title_zh: CLI-Anything：面向原生智能体的计算机交互界面设计
authors:
- Yuhao Yang
- Tianyu Fan
- Chao Huang
affiliations:
- University of Hong Kong
arxiv_id: '2606.03854'
url: https://arxiv.org/abs/2606.03854
pdf_url: https://arxiv.org/pdf/2606.03854
published: '2026-06-02'
collected: '2026-06-03'
category: Agent
direction: 面向Agent的软件接口设计
tags:
- Agent-Native Interface
- CLI Harness
- Computer Use
- Tool-Use
- GUI Replacement
- Stateful CLI
one_liner: 放弃脆弱的GUI视觉操控，为Agent直接生成可编程、有状态且可验证的CLI操作接口。
practical_value: '- **为内部工具构建Agent友好的CLI表面**：当你有复杂的内部平台（如标注工具、配置中心、A/B实验平台）需要由Agent自动操作时，可按CLI-Anything的“harness
  lift”方法生成有状态的CLI接口，代替脆弱的GUI点击流，大幅提升Agent执行可靠性。

  - **状态管理和可恢复执行**：借鉴其JSON项目文件、undo/redo栈和会话持久化设计，让Agent能在任务中途检查状态、回滚错误步骤并继续执行，这对长时多步的电商工作流（如自动搭建活动页）尤其重要。

  - **预览协议与验证对称性**：在Agent工具中加入preview命令，输出结构化摘要与可视化产物，人类可审阅而Agent可验证，且验证边界与执行边界保持统一（都用真实后端渲染），避免Agent做出“命令返回0但实际产出错误”的判断。

  - **工具发现与分发基础设施**：如果公司内有多个Agent团队，可参照CLI-Hub构建一个工具注册与发现系统，让Agent按任务需求自动查找、安装并调用标准化接口，避免重复造轮子。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**
当前让LLM Agent操作桌面应用的主流方案是GUI Agent，通过截图理解、UI元素定位和鼠标点击来模仿人类操作。这种方式存在根本性错位：像素级交互脆弱、依赖时序与坐标、界面变更即失效，且迫使Agent重建人类的感知局限，未能发挥其在结构化数据处理和编程控制上的天然优势。论文主张一种“agent-native”的设计：不再让Agent去适应GUI，而是为现有应用创建贴合Agent操作模式的命令行接口（CLI），将功能暴露为结构化命令、显式状态和确定性反馈，从而消除视觉到计算的有损转换。

**方法关键点**
- **Harness Lift 方法论**：通过“界面考古”识别应用的后端引擎、数据模型和可编程入口，设计双模式CLI（有状态REPL + 一次性子命令），为真实软件套上Agent可解析的接口。每个harness包含命令树、持久化项目状态（JSON）、会话管理、undo/redo、后端真实渲染导出及程序化验证测试。
- **最小原生接口契约**：定义H=(S,C,I,R,V,D)，S为状态空间，C为领域命令词汇，I为检查表面，R为后端渲染出口，V为验证层，D为发现层。六条不变性原则：状态显式化、动作类型化、低代价检查、后端真实渲染、程序化验证以及可发现性。
- **预览协议**：将中间渲染状态打包为稳定磁盘目录（manifest.json, summary.json, artifacts/），使Agent与人共享同一视觉证据，但始终以后端真实产物为源头，拒绝玩具渲染和GUI截图。
- **CLI-Hub生态**：提供安装器、注册表和技能文档(SKILL.md)，让Agent能按需发现、安装和调用harness。当前已收录65个CLI、18个第三方条目、61个配套技能。
- **Blender案例研究**：将Blender的成熟bpy API后端提升为CLI表面，含54条命令、JSON场景合约、bpy脚本生成和真实Blender后端渲染，视觉预览通过后端产生，实现从命令到像素的完整可验证闭环。
- **Slay the Spire II案例**：对于运行时状态嵌入进程的游戏，通过在进程内部架设桥接器读取运行状态和调度动作，暴露15种决策状态和24个动作动词，将GUI操作等价类折叠为稳定命令，展示了当缺乏现成后端时如何创建接口边界。

**关键结果与证据**
论文以架构实现和可行性证明为主，而非定量对比。主要成果：
- 构建了一套可复用的harness生成流程和6条质量准则（图2），并用Blender进行全面覆盖，拥有228项测试，涵盖单元测试、E2E测试和真实后端验证。
- Slay the Spire II的桥接器说明了对运行中应用的界面考古如何将原生的屏幕可见状态转化为结构化决策接口，并在不影响游戏主线程的情况下安全地调度操作。
- CLI-Hub提供了生产级的工具发现和安装基础设施，并支持跨应用的预览消费。
- 通过两个截然不同的案例展示了从“软件已有成熟后端”和“需要先构建内部边界”两种模式，验证了agent-native设计的广泛适用性。

**一句话关键句**： “Agent需要的不是更好的屏幕阅读器，而是将应用的控制点从像素移到语义边界，让构造与验证共享同一个结构化真相表面。”
