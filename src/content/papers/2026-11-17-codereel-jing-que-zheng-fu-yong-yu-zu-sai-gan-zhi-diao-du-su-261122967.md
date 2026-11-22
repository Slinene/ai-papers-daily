---
title: 'CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware
  Scheduling'
title_zh: CodeReel：精确帧复用与阻塞感知调度加速代码到视频 Agent
authors:
- Junyi Shen
- Yao Lu
affiliations:
- National University of Singapore
arxiv_id: '2611.22967'
url: https://arxiv.org/abs/2611.22967
pdf_url: https://arxiv.org/pdf/2611.22967
published: '2026-11-17'
collected: '2026-11-22'
category: Agent
direction: 代码 Agent 执行层优化与延迟降低
tags:
- Code Agents
- Execution Layer
- Frame Reuse
- Scheduling
- Latency Optimization
- Video Generation
one_liner: 训练无关执行层，用精确帧复用和阻塞感知调度将编码 Agent 视频构建等待降低最高57.9%
practical_value: '- 在 Agent 迭代生成场景（如广告文案、推荐解释、搜索 query 生成）中，可对中间计算结果按输入命令或参数做精确键控缓存，避免重复
  LLM 推理或渲染，尤其当后期迭代与早期失败版本有大量重合时。

  - 借鉴阻塞感知调度：流水线中先执行轻量校验（如规则检查、语法检查）并同时以空闲优先级启动重计算（模型推理、特征生成），根据近期成功率动态调整并行策略，可显著降低用户感知延迟。

  - 建立可回放的 Agent 会话基准（记录输入、中间命令和最终结果）用于测量执行层优化效果；在业务推荐 Agent 中可类似建立离线回放集，量化缓存与调度策略的收益。

  - 对多模态生成（如视频/图像广告素材）的迭代优化，可复用按内容寻址的缓存机制，但需考虑业务中生成内容多样性较高时命中率受限，可结合时间窗口或局部哈希。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：编码 Agent 以 build-inspect-edit 循环制作视频，构建阻塞占耗时三分之一；分析发现37.5%后期帧重复出现过，一半构建在检查处停止但需等完成才知。

**方法关键点**：CodeReel 是训练无关执行层，置于 Agent 现有命令之后。精确帧复用：每帧按绘制命令作为键，不考虑时间位置，键相同即复用，使后期版本可复用失败版本渲染的帧。阻塞感知调度：先跑 checks，同时以 idle priority 启动 render，除非会话近期构建表现显示通过可能性低；CPU 换更快答复，复用则回收 CPU。另引入 EditLoop 基准，可回放 Agent 会话并与从头渲染对照。

**关键结果数字**：在 EditLoop 上，CodeReel 将等待时间比 Rebuild（已并行渲染的暖管道）减少36.3%，比 Sequential 减少57.9%。在时间平移编辑上复用渲染43.9%帧，接近新像素43.0%，而 Manim 风格缓存渲染99.8%。真实 Agent 中，Claude Code 中位等待为 Rebuild 的0.62，Codex CLI 为0.67，提升跨5个模型和2个框架保持。
