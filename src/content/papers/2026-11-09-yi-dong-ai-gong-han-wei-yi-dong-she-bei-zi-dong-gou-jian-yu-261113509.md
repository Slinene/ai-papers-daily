---
title: 'Mobile AI Factory: Building Specialized Language Models for Your Mobile Device'
title_zh: 移动 AI 工厂：为移动设备自动构建专用小语言模型
authors:
- Evan Li
- Krishna Deshpande
- Wen Cheng
- Shyamnath Gollakota
affiliations:
- University of Washington
arxiv_id: '2611.13509'
url: https://arxiv.org/abs/2611.13509
pdf_url: https://arxiv.org/pdf/2611.13509
published: '2026-11-09'
collected: '2026-11-17'
category: Training
direction: 面向移动端的自动化 SLM 训练与量化搜索
tags:
- SLM
- Agent
- Fine-tuning
- Quantization
- On-device
- AutoML
one_liner: 用 agent 编排的自动化系统，针对具体任务和手机搜索并微调、量化出最优小语言模型，在多个任务上超越 5-shot 前沿模型。
practical_value: '- 在移动端/边缘部署个性化推荐或生成式模型时，可借鉴「orchestrator LLM + 固定规则回滚」的自动微调流程：让
  LLM 决策调超参、挖真实数据或生成合成数据，用规则阻止精度回退，减少专家调参成本。

  - 模型选型必须结合真实设备测量，而非只看模型规格或理论算力；同一模型在不同手机、不同推理引擎和后端上最优配置可能变化，业务中在 App 内跑小模型前应有自动化实测闭环。

  - 从小模型到大模型、自适应精度目标的搜索策略，可在资源受限场景下节省大量试错时间；例如冷启动或边缘推理时，先试小模型，达到业务精度阈值即停，避免无谓的大模型开销。

  - 当真实标注数据不足时，由 orchestrator 判断挖掘真实数据还是生成合成数据，这对电商冷启动、长尾品类或小语种场景的微调数据获取有直接参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：移动端运行 SLM 能保护隐私、离线可用，但需针对任务和手机进行微调和量化，专家反复调优成本高。

方法：Mobile AI Factory 提供 agentic 自动化流程，给定任务规格和目标手机，由 orchestrator LLM 循环决策——调超参、挖掘真实数据或生成合成示例，并用固定规则回滚损害精度的改动；搜索从较小模型开始，覆盖不同基础模型和量化方式，自适应调整精度目标；同时在实际目标手机上测量不同推理引擎和后端的性能，指导最优部署配置选择。

关键结果：在 10 个任务、4 台 Android 手机的评测中，未见测试集上的端侧模型在 5 个任务上超过两个 5-shot 前沿模型，最高领先 0.34，在 3 个任务上持平；实体抽取任务上，搜索效果与穷举训练全部 27 个模型变体仅差 0.03，但 GPU 时间减少 19 倍；缺少手机实测时，Claude Opus 5.5 即便拿到完整硬件和模型规格，在 25% 简单/中等场景和 60% 困难场景中仍会错过应用要求。
