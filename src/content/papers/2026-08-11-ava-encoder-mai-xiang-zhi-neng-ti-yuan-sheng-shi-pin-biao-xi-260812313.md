---
title: 'AVA-Encoder: Towards Agent-Native Video Representation Learning'
title_zh: AVA-Encoder：迈向智能体原生视频表示学习
authors:
- Chuyue Li
- Jinpeng Yu
- Haozhe Wang
- Tian Xueyun
- Zhijing Zhang
- Bingnan Li
- Shuqi Gu
- Kan Ren
- Jiaming Liu
- Ruihua Hua
affiliations:
- Qwen Business Unit of Alibaba
- ShanghaiTech University
- The Hong Kong University of Science and Technology
- Institute of Computing Technology
- Southeast University
arxiv_id: '2608.12313'
url: https://arxiv.org/abs/2608.12313
pdf_url: https://arxiv.org/pdf/2608.12313
published: '2026-08-11'
collected: '2026-08-17'
category: Agent
direction: Agent 原生视频表示学习
tags:
- Agentic Auto-Encoder
- Video Knowledge Graph
- Textual Gradient
- Video Reconstruction
- LLM Agent
- Multimodal Representation
one_liner: 提出 AVA-Encoder，将视频编码为知识图谱并用文本梯度优化，提升智能体视频重建与编辑能力，较最强外部基线提高 20.7%
practical_value: '- 知识图谱作为多模态内容统一表示：在电商/推荐场景中，可将商品视频、图片、描述组织为 KG，节点存结构化文本，资产层链接原始媒体，类型化边保留关系，便于
  Agent 查询、编辑和生成推荐理由。

  - 文本梯度优化可自动化 prompt 策略调优：将评估反馈转化为自然语言更新方向，对推荐/搜索 Agent 的系统提示进行伪训练，减少人工调 prompt 成本，并可在线细化。

  - 分层策略优化：外循环数据无关伪训练与测试时数据相关优化分离，轻量级 inner loop 降低 token 消耗；适用于低延迟推荐 Agent 或在线广告文案生成。

  - 建立可重建评测基准：强调保真度与可编辑性平衡，电商多模态理解可借鉴其评测方法，避免只优化表面指标。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：创意智能体缺乏从高质量人类电影中学习的有效方式，缺少既忠实于电影内容又可直接用于智能体推理和操作的视频结构化表示。

方法：提出 AVA-Encoder，一种智能体原生视频自编码器。将视频转换为知识图谱（KG）表示，再重建回视频。KG 包含层次和状态节点存储结构化文本，链接资产层存放生成的图像、音频、视频；类型化边保留文本描述与资产之间的关系，方便智能体理解、查询和编辑。重建差异驱动文本梯度优化框架，将评估反馈表达为自然语言更新方向，用于外循环数据无关编码策略伪训练，以及可选的测试时内循环数据相关 KG 表示细化。

结果：AVA-Encoder 比最强外部基线提升 20.7 个百分点；在仅策略控制设置下，其伪训练的镜头级智能体视频编码策略优于人工调优策略，同时系统提示 token 减少 74.3%。该工作发布了完整的 AVA-Encoder 框架、可靠的智能体视频重建基准以及首个高质量电影 KG 表示数据集。
