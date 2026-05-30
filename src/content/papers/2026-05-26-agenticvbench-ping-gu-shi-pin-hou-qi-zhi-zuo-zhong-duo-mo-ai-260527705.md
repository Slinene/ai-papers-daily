---
title: 'AgenticVBench: Can AI Agents Complete Real-World Post-Production Tasks?'
title_zh: AgenticVBench：评估视频后期制作中多模态 AI 代理的基准
authors:
- Zongheng Cao
- Yi Zheng
- Rui Song
- Xinyu Hu
affiliations:
- Philo Labs Research
arxiv_id: '2605.27705'
url: https://arxiv.org/abs/2605.27705
pdf_url: https://arxiv.org/pdf/2605.27705
published: '2026-05-26'
collected: '2026-05-30'
category: Agent
direction: 多模态代理 · 视频后期制作基准
tags:
- Multimodal Agents
- Video Production
- Benchmark
- VLM
- Tool Use
- Harness Design
one_liner: 首个覆盖视频后期全流程的代理基准，揭示脚手架设计对代理性能的一阶影响
practical_value: '- **脚手架（harness）是一阶变量**：同一模型在不同脚手架下的得分差距可达20个百分点。在构建电商/Agent系统时，应像重视模型选型一样重视底层工具链和规划循环的设计。

  - **为多模态代理提供专用工具原语**：OpenClaw提供的image、tts、video_generate等类型化原语在Sequencing任务中胜出，而通用shell工具使模型在Assembly上表现差。构建电商视频处理或广告合成的Agent时，应封装高层级、参数化的多模态操作，而非让模型从零编写ffmpeg命令。

  - **代理失败模式分析指导工程方向**：Repurpose任务中83%的失败源于长上下文信息丢失，Repair中24%由模态错位导致。在电商场景中，类似的产品视频压缩或修复任务应优先设计更鲁棒的长期记忆和跨模态对齐机制。

  - **基准设计覆盖真实工作流**：任务源于20位行业专家的日常流程，涉及0.5小时到一周的人力耗时。这种设计方法可迁移到电商售后、内容生成等Agent任务的真实度校验——从从业者工作流出发定义任务和评分标准，避免脱节。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**
现有视频理解基准多为单轮问答，而当前的代理基准多聚焦软件工程，无法评估模型在真实视频制作中所需的复合能力（跨文本、图像、音频、视频的推理，长程规划，工具使用）。为填补这一空白，本文构建了AgenticVBench，一个由行业专家驱动的视频后期制作代理基准。

**方法关键点**
- **任务家族**：包含四大任务——Assembly（根据故事板选择并拼接镜头）、Repair（定位并修复技术缺陷）、Sequencing（恢复打乱镜头的叙事顺序）、Repurpose（将长视频压缩为符合规定的短视频），覆盖影视后期全流程。
- **构建流程**：由20位来自传统影视、AI影视、独立创作者、视频AI公司的专家（平均6年经验）联合设计。任务和评分规范均出自专家之手，结合程序化验证和人工二元评分，确保客观性与编辑要求。
- **评估矩阵**：在100个任务上评估了7个前沿VLM（Claude、GPT、Gemini、Qwen等），搭配5种脚手架/CLI（原生的Claude Code、Codex CLI、Gemini CLI，以及开源的OpenCode、OpenClaw），共20种模型-脚手架组合，每组重复3次。

**关键结果**
- **代理-专家巨大差距**：最佳组合总分仅31%，比人类编辑低43–65个百分点（分别对应Assembly和Repurpose）。Repurpose上最佳仅有0.30（专家0.95），Sequencing上最佳仅有0.51（专家0.76）。
- **脚手架效应显著**：同一GPT-5.5在Codex、OpenCode、OpenClaw上的Assembly得分分别为0.38、0.37、0.18，最大落差20pp。OpenClaw凭借多模态专用原语在Sequencing上最优，但在Assembly上因像素细节损失而下滑。
- **失败模式分析**：Repurpose主要失败于长上下文信息丢失（83%失败案例），Repair失败于时间推理错误（65%）；模态错位和幻觉也是常见原因。
- **消融实验**：提供缺陷位置能将Repair分数提升13pp；提供场景描述将Sequencing提升22pp；移除叙事描述使Assembly降27pp，而去除摄影参数（如镜头尺寸）影响极小，说明代理尚未利用专业电影语法。

**值得记住的一句话**：在视频代理这类多模态、长程任务中，**脚手架的设计（工具原语、规划循环、模态路由）对最终性能的影响与模型本身同等重要**，仅比较模型而忽略脚手架会得出错误结论。
