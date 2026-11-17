---
title: 'VideoNexus: Video Perception Beyond the Reasoning Context'
title_zh: VideoNexus：感知与推理分离的长视频理解框架
authors:
- Yancheng Long
- Xuanyu Zheng
- Wei Chen
- Luoyuan Zhang
- Haoyang Xu
- Bin Wen
- Tingting Gao
affiliations:
- The Chinese University of Hong Kong
- KlingAI Research
- The Hong Kong University of Science and Technology
arxiv_id: '2611.21392'
url: https://arxiv.org/abs/2611.21392
pdf_url: https://arxiv.org/pdf/2611.21392
published: '2026-11-16'
collected: '2026-11-17'
category: MultiAgent
direction: 视频多智能体协作 · 紧凑证据交换
tags:
- video understanding
- multi-agent
- long-video reasoning
- adaptive perception
- compact evidence
- training-free
one_liner: 训练免费框架分离视频感知与规划，子代理独立处理并返回紧凑时间证据，长视频准确率提升且成本下降
practical_value: '- 在电商直播/商品短视频理解中，可借鉴“planner 定向检查 + 感知子代理独立处理”的分离架构：主 Agent 只提出要查看的时间段/细节（如商品外观、价格标签、主播话术），子
  Agent 返回带时间戳的紧凑 JSON 证据，避免把整段视频或大量帧塞入主上下文。

  - 自适应采样策略：由 planner 根据问题和中间观察动态决定采样密度，关键片段密集、无关片段稀疏，兼顾证据完整性和 token/API 成本；论文中准确率提升同时成本仅为内置
  agentic 处理的 44%，对需要控制推理成本的线上服务有参考意义。

  - 迭代搜索与验证：感知子代理每次返回局部证据供 planner 校验，若发现矛盾或缺失再追加查询，可迁移到多模态商品审核、直播切片标签、广告素材理解等任务。

  - 该框架无需训练，直接套用现有多模态 LLM，适合快速实验落地；但在推荐排序/召回主链路中更多是作为多模态特征抽取或 Agent 工具，不适合直接替代主模型。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：长视频理解需要在大量无关视觉序列中定位证据、解析细节并整合答案，即使相关证据存在，长密集序列也会同时拖累感知和推理。现有 video agent 虽能选择性检查，但把帧返回给 planner 仍会造成视觉信息在推理上下文里累积；完全委派感知可减轻负担，但稀疏采样容易漏掉关键细节，逐帧描述又不能真正控制上下文增长。

**方法**：VideoNexus 是一个无训练框架，把详细视频感知与证据驱动规划/推理分离。Planner 决定检查哪些位置、解决哪些细节、以多密集采样；多个感知子代理在独立上下文处理原生音视频，返回紧凑、带时间定位的证据，供迭代搜索与验证。

**结果**：在完整 LVBench 上，Gemini 3.8 Flash 同 backbone 下达到 88.6% 准确率，比静态输入高 3.6 点、比内置 agentic 处理高 1.1 点，实测 API 成本仅为后者 44%；配对子集消融显示 planner 输入更少、准确率更高。换用 Kimi K3 后，比官方 Video-GAIA ReAct harness 高 8.5 点。
