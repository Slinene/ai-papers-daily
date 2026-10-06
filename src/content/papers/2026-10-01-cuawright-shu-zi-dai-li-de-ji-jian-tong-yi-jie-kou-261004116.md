---
title: 'CUAWright: A Minimal Unified Interface for Digital Agents'
title_zh: CUAWright：数字代理的极简统一接口
authors:
- Yadong Lu
- Theodore Lee
- Yifei Li
- Lawrence Keunho Jang
- Tianci Xue
- Yu Su
- Huan Sun
- Ahmed Hassan Awadallah
affiliations:
- Microsoft Research
- National University of Singapore
- The Ohio State University
- Carnegie Mellon University
arxiv_id: '2610.04116'
url: https://arxiv.org/abs/2610.04116
pdf_url: https://arxiv.org/pdf/2610.04116
published: '2026-10-01'
collected: '2026-10-06'
category: Agent
direction: 数字代理 · 终端统一接口
tags:
- Digital Agents
- Terminal Harness
- LLM
- Tool Creation
- Computer Use
- GUI替代
one_liner: 用 bash 命令和文件系统作为极简接口，让数字代理动态创建工具，大幅提升任务成功率和效率
practical_value: '- 在需要自动化操作浏览器或桌面应用的场景（如电商数据采集、广告投放监控、多步骤订单处理），可以考虑用终端/bash 作为统一动作接口，替代传统
  GUI 点击或 DOM 操作，减少对固定工具的依赖，让 LLM 直接调用命令行工具或编写脚本完成操作。

  - 采用文件系统作为可演化的工具和记忆空间：让 Agent 在任务执行过程中将中间结果、上下文、创建的工具脚本写入文件，后续步骤可读取修改，实现类似长期记忆和动态工具注册表，避免每次重新生成工具定义。

  - 统一接口降低了 harness 的工程复杂度：仅约 3K 行代码即可实现，适合快速搭建 Agent 系统原型，相比维护多套 GUI 特定工具（浏览器、桌面、CAD
  等）更轻量，且跨领域复用性强。

  - 结果提示：在需要视觉理解与命令行交互结合的任务（如 CAD 设计、UI 自动化测试）中，终端接口比纯 GUI 或混合 CLI 接口有显著提升，可以优先尝试将业务自动化流程改造为基于终端命令的交互方式。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有计算机使用代理通常将模型与特定领域的 harness 耦合，例如浏览器或桌面环境，使用预设的人类工程工具，这些工具固定且不易扩展。随着模型编码能力增强，GUI 原生和静态 harness 限制了代理直接以编程方式操作系统状态，也阻碍了灵活构建工具。

**方法关键点**：提出 CUAWright，一个约 3K 行代码的极简终端 harness，只使用 bash 命令作为唯一动作接口，并将文件系统作为可演化空间，让代理可以动态创建工具和管理上下文。相比 GUI 或混合 CLI 接口，代理能够直接通过脚本和命令行操作系统，无需依赖固定的图形界面元素。

**关键结果**：在 OSWorld 2.0 上，相比 GPT-5.5 发布基线，CUAWright 的 partial reward 相对提升 33.2%，估算成本降低 37.5%；在 Online-Mind2Web 和长期规划 Odysseys 基准上，成功率分别比 GUI 原生 harness 高 4.7% 和 44.0%；在 CADGenBench 和 BenchCAD 上，相对其他 CLI 接口，GPT-5.5 使用统一 harness 提升 8.1%-41.6%。结果表明数字环境的可编程性远超 GUI 接口所示，极简终端接口是提高性能和效率的关键。
