---
title: 'Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models'
title_zh: 多模态协同编码 Agent 评估基准 Co-Design Bench
authors:
- Xilin Wei
- Shengyuan Ding
- Xinyu Fang
- Tiancheng Gu
- Yuchi Wang
- Zhixun Li
- Ziyu Liu
- Yuhang Zang
- Weixiang Yu
- Cheng Lu
affiliations:
- Fudan University
- Alibaba Token Hub, Alibaba Group
- Zhejiang University
- The Chinese University of Hong Kong
- Shanghai Jiao Tong University
arxiv_id: '2610.35138'
url: https://arxiv.org/abs/2610.35138
pdf_url: https://arxiv.org/pdf/2610.35138
published: '2026-10-25'
collected: '2026-11-01'
category: Eval
direction: 多模态 Agent 编码评估基准
tags:
- Multimodal Coding Agents
- Benchmark
- Agentic Evaluation
- Reference-free
- Code Editing
one_liner: 构建参考无关的多模态协同编码基准 Co-Design Bench，评估 10 个模型端点，最强模型完全满足率仅 26.4%
practical_value: '- **细粒度评估指标**：借鉴 judge-then-refute 协议，对 Agent 输出先设置多个可检查的验收标准（如
  UI 元素、交互逻辑、功能正确性），再用独立 LLM 挑战正面判断，减少评判幻觉。电商搜索推荐 Agent 可用类似方式评估生成式推荐解释、多模态商品描述改写等任务。

  - **真实用户任务挖掘**：从真实用户会话日志中清洗、去重、规范化请求来构建评测集，能更贴近线上分布，优于纯人工合成任务。推荐系统可复用此流程构建 Query
  改写、会话式推荐的离线评估集。

  - **区分部分满足与完全满足**：不只报告平均分，还要统计完全满足所有标准（全对）的任务比例，以暴露 Agent 在多约束复杂任务中的短板。这适用于多步骤推荐
  Agent（如跨意图理解、多轮交互、最终生成商品卡片）的评估。

  - **多模态输入的融合测试**：在编码任务中加入图像、音频、文档等多模态输入，能考察 Grounded Understanding 能力。电商场景中，商品图+文本描述+用户语音的多模态
  Query 理解可以直接借鉴此类任务设计。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：评估人类-AI 协同设计需要验证编码 Agent 能否将真实用户的多模态请求转化为可运行的应用修订。现有基准缺乏来自真实用户请求、参考无关的评估。

**方法关键点**：Co-Design Bench 从 26,314 个真实用户编码会话中整理出 273 个任务，分为多模态编辑（ME）和仓库编辑（RE）两个赛道，支持图像、音频、视频、文档输入。任务覆盖三个能力维度：Grounded Understanding、UI Transformation、Functional Implementation。隐藏了 2,331 条专家编写的验收标准。采用 judge-then-refute 协议：先用源文件和浏览器证据逐条评判，再用独立 LLM 验证者挑战正面结论，无需参考代码或目标截图即可审计视觉和交互声明。

**关键结果数字**：在共享 agentic harness 下，10 个模型端点中最强的模型平均每个任务通过 69.9% 的标准，但完全满足所有标准的任务仅 26.4%。所有模型在仓库编辑跨 3-4 种变更类型时标准完成率低于跨 1-2 种，表明部分需求满足与完整任务成功之间存在显著差距。
