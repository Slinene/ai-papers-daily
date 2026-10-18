---
title: 'MotionCoach: Constructing Multimodal Guidance for Video Professional Motion
  Editing'
title_zh: MotionCoach：构建多模态引导实现视频专业动作编辑
authors:
- Siyi Qian
- Hanqing Yang
- Weihuang Lin
- Zihao Yang
- Yichen Lu
- Yuanhong Zheng
- Sheng Li
affiliations:
- Peking University
- Alibaba Token Hub, Alibaba Group
- University of Science and Technology of China
- Zhejiang University
arxiv_id: '2610.12963'
url: https://arxiv.org/abs/2610.12963
pdf_url: https://arxiv.org/pdf/2610.12963
published: '2026-10-09'
collected: '2026-10-18'
category: Agent
direction: Agent 多模态引导视频编辑
tags:
- Video Editing
- Multimodal Agent
- GRPO
- Self-Verification
- Reference Selection
- VLM Judge
one_liner: 训练多模态Agent自动搜索、验证并裁剪动作参考，输出grounded prompt与reference clip，显著提升冻结视频编辑模型的专业动作编辑能力。
practical_value: '- 借鉴“冻结生成模型 + 轻量 Agent 策略”的分离架构：在商品视频生成、广告创意生成中，不重新训练底模，训练一个 VLM
  Agent 来构造可靠的参考素材和 grounded prompt（包含关键卖点、时间结构、负向约束），可低成本适配垂直类目。

  - 借鉴 self-verification 与 tool use：类似 RAG 中的检索后验证，在电商视频编辑中 Agent 可以搜索候选商品素材、检查是否展示正确商品和动作，自验证后裁剪出最有用的片段，避免错误参考导致生成偏差；该逻辑可用于广告素材自动剪辑和生成。

  - 借鉴 RL 奖励设计：用三个奖励（prompt 质量、下游生成结果、格式）训练 Agent，尤其以冻结编辑器实际生成的视频作为奖励信号；在推荐/搜索中，可训练
  Agent 生成 query 解释或推荐理由，奖励包括文本质量和最终转化/点击模型评分，形成闭环。

  - 数据流水线：teacher 模型生成轨迹 + VLM/程序化检查 + 人工抽检，快速构建 SFT/RL 数据，适合缺少标注的垂直领域。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

## 动机
专业动作编辑（舞蹈、运动、武术）要求编辑后的视频具备正确的运动技术和时间结构，但短指令往往无法描述这些细节，视频编辑模型又缺乏垂直领域的运动知识，常把 Stoppie 错生成为 Wheelie。已有方法依赖参考视频，但默认参考已经存在，不负责获取和验证。MotionCoach 旨在为冻结的视频编辑模型自动构建可靠且充分的多模态指导。

## 方法关键点
- 训练一个多模态 Agent，输入源视频和编辑指令，通过多轮工具调用（search / inspect / clip）检索专业演示，检查候选视频，裁剪出清晰、完整、低干扰的目标动作片段，并执行 self-verification；通过自检后输出 grounded prompt 和 reference clip，作为多模态引导注入冻结的视频编辑模型（如 MiniMax-H3、Seedance 2.0）。
- 数据构建：收集 5–10 秒、≥720p 的人类中心视频，由 Gemini 3.5 Flash 筛选分类；GPT-5.5、Claude Opus 4.7、GLM-5.2 提出专业原子动作并经 web 检索验证；Gemini 3.5 Flash 生成 ReAct 轨迹，程序化检查、VLM 检查与人工抽检过滤，得到 MotionCoach-SFT-10k 和 MotionCoach-RL-2k。
- 训练策略：用 Qwen3-VL-8B-Instruct 先 SFT 冷启动，再用 GRPO 做 Agentic RL。奖励由三部分组成：prompt 奖励（与 teacher prompt 比较）、video 奖励（冻结编辑器生成视频按 MP/PP/VQ 等打分）、format 奖励（工具调用和输出结构）；prompt:video 权重取 0.7:0.3。RL 约 28 小时，16 GPU 训练 + 8 GPU 推理。

## 关键实验
- 构建 VPMEBench：314 个人工验证的专业动作编辑任务，覆盖 3 个顶级类、10 个二级类、25 个叶子类，提供 reference clip、语义关键帧、时间结构、运动技术和负约束注释；VLM judge 评分 MP/PP/VQ，权重 0.5/0.2/0.3。
- 在冻结的 MiniMax-H3 上，Overall 从 51.2 提升到 64.5；在 Seedance 2.0 上，从 55.1 提升到 65.6。
- 消融：去掉 grounded prompt 损失 13.2/15.9 分，去掉 reference clip 损失 5.8/0.8 分，去掉 self-verification 损失 7.5/9.9 分；clip 工具成功率从 62.2% 提升到 98.3%。
- 与人类判断的 QWK 达到 0.846，支持自动评估可靠性。

最值得记住的一句话：把外部垂直知识转化为“可验证的参考片段 + grounded prompt”，用 Agentic RL 训练一个轻量策略，能让冻结的视频生成模型在不重新训练的情况下显著提升专业动作编辑能力。
