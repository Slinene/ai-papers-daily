---
title: An Exam for Active Observers
title_zh: 主动观察者考试：多模态大模型视觉闭环感知评测
authors:
- Jiarui Zhang
- Muzi Tao
- Shangshang Wang
- Ollie Liu
- Xuezhe Ma
- Willie Neiswanger
affiliations:
- University of Southern California
arxiv_id: '2607.16165'
url: https://arxiv.org/abs/2607.16165
pdf_url: https://arxiv.org/pdf/2607.16165
published: '2026-07-16'
collected: '2026-07-25'
category: Eval
direction: 多模态模型主动视觉评估基准
tags:
- Active Vision
- MLLM Evaluation
- Benchmark
- Perception-Reasoning Loop
- Multimodal
one_liner: 提出 ActiveVision 基准，发现前沿多模态模型在需要多次视觉交互的任务上近乎失败，与人类差距悬殊
practical_value: '- 若业务中存在需要反复视觉确认的任务（如商品瑕疵检测、图像合规审核），可借鉴 ActiveVision 的任务设计，自建测试集评估内部多模态模型的主动观察能力，避免将单次前向的准确率等同于真实可用性。

  - 使用多模态 Agent 执行复杂图像分析时，不应假设模型能自主重看或验证；工程上可考虑强制多步交互（如分区域截图、用目标检测器先提取候选区域再提问），以弥补被动视觉的缺陷。

  - 该基准中模型生成视觉代码但仍失败的实验提示：在涉及视觉的任务里轻易让模型“写代码分析”可能不可靠，需确保代码执行环境的可干预性和结果的可解释性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：人类视觉是闭环过程，通过反复注视验证假设，而当前多模态大模型（MLLM）的评测往往只需单次前向视觉，无法反映真正需要主动观察的能力。为此，论文设计了首个衡量 MLLM 主动视觉能力的基准 ActiveVision。

**方法**：基准包含 3 类共 17 个任务：（1）分布式扫描（如计数图像中分离的区域）；（2）顺序遍历（如沿曲线追踪并记录经过的标记点）；（3）视觉属性传递（如判断右图中多少轮廓是左图模板的精确拷贝）。所有任务强制要求多次、有目的的视觉感知，而非一次性描述。人类平均得分 96.1%。

**结果**：最强模型 GPT-5.5（最高推理力）仅解决 10.6% 的条目，17 个任务中 11 个得分为零；Claude Fable 5 仅 3.5%。即使允许模型生成并执行 Python 视觉代码，性能依然极低，因为代码在真实图像上不可靠，且模型无法主动发现代码的失败。结果表明当前 MLLM 缺乏稳健的“感知—推理”闭环。
