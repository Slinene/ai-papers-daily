---
title: 'SCOPE: Real-Time Natural Language Camera Agent at the Edge'
title_zh: SCOPE：面向边缘部署的实时自然语言PTZ摄像代理
authors:
- Nikolaj Hindsbo
- Sina Ehsani
- Pragyana Mishra
affiliations:
- Armada AI
arxiv_id: '2606.02951'
url: https://arxiv.org/abs/2606.02951
pdf_url: https://arxiv.org/pdf/2606.02951
published: '2026-06-01'
collected: '2026-06-03'
category: Agent
direction: Agent · 语言驱动摄像代理与仿真基准
tags:
- PTZ camera
- SLM
- VLM
- edge deployment
- sim-to-real
- agentic control
one_liner: 通过SLM规划器与VLM感知工具解耦，实现边缘实时PTZ摄像代理，并发布536任务基准与19种模型组合分析
practical_value: '- 规划与感知解耦的架构：将SLM作为调度中心，感知工具（VLM）按需调用，避免图像 token 进入对话上下文，降低延迟和显存压力，适合多模态
  Agent 的边缘部署。

  - MoE SLM 的延迟–准确性平衡：Qwen3-30B-A3B（激活参数 3B）在推理延迟上接近 4B 密集模型，但工具路由和推理能力显著更强，是实时控制环路中的实用选择。

  - 量化几乎无损：FP8 量化在多数配置下准确率持平或略优，且减少显存，对生产环境中的模型压缩与加速有直接参考价值。

  - 仿真–真实的双向评估框架：在 Blender 中精确复现 PTZ 动作空间和工具 API，实现可复现的闭环评测，这一方法论可迁移至其他具身 Agent 或
  IoT 控制的迭代开发中。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**：现有语言模型评测很少关注具身、闭环控制任务中的延迟、错误模式和部署可行性，尤其缺乏可复现的仿真–真实对比基准。SCOPE 为此构建模块化自然语言 PTZ 摄像代理，在边缘设备上完成实时感知、规划与控制，并发布首个大规模仿真基准。

**方法**：
- 架构：SLM 规划器（Qwen3 系列）负责解析指令、规划动作、调用工具；轻量 VLM（Moondream2/3）作为感知后端，仅在被调用时返回结构化结果（计数、OCR 等），避免每帧图像 token 涌入对话上下文。
- 工具接口：统一的 JSON Schema 定义 PTZ 控制（pan/tilt/zoom、预设、截帧）和感知查询（计数、问答、目标跟踪），在物理相机和 Blender 仿真中完全一致。
- 仿真基准：基于 4 个城市 Blender 场景，设置 536 个自然语言任务，覆盖计数、描述、OCR、空间推理、单步/多步命令等，并要求主动视角变化。
- 评估：使用 gpt-oss-120B 作为判决模型，按错误模式（感知、推理、幻觉、工具路由等）分类，衡量 19 种 SLM–VLM 组合的准确率和延迟。

**关键结果**：
- 规划器能力提升可大幅减少幻觉和工具调用错误，之后感知成为主要瓶颈；若修正感知错误，平均准确率从 66.2% 升至 82.0%。
- MoE 规划器（如 Qwen3-30B-A3B）在保持低延迟的同时取得最高准确率，量化几乎无损失；最佳组合 Moondream3 + Qwen3-30B-A3B 达 73.8%。
- 感知延迟主导端到端成本，全景图模式比当前视图慢 22.4%，显示出感知效率的重要性。

**核心结论**：紧凑 MoE 规划器加专用 VLM 感知，是边缘实时语言驱动摄像控制的实用设计点，为具身 Agent 的架构选择和量化策略提供了直接参考。
