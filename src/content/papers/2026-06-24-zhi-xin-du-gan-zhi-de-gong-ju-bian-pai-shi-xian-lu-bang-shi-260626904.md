---
title: Confidence-Aware Tool Orchestration for Robust Video Understanding
title_zh: 置信度感知的工具编排实现鲁棒视频理解
authors:
- Yangfan He
- Yujin Choi
- Jaehong Yoon
affiliations:
- NTU Singapore
- University of Minnesota, Twin Cities
- UNIST
arxiv_id: '2606.26904'
url: https://arxiv.org/abs/2606.26904
pdf_url: https://arxiv.org/pdf/2606.26904
published: '2026-06-24'
collected: '2026-06-26'
category: Agent
direction: Agent 工具编排 · 置信度感知推理
tags:
- Robust-TO
- Tool Orchestration
- Confidence-Aware
- Video Reasoning
- GRPO
- Multi-modal Agent
one_liner: 提出 Robust-TO 框架，通过逐帧可靠性评估与异构工具编排，将视频推理在干净/受损输入下的准确率提升至 56.4%/54.3%，远超基线。
practical_value: '- 多媒体内容理解鲁棒性：商品视频/直播切片中存在模糊、遮挡等问题，可引入逐帧置信度评分，避免“盲目信任”导致的预测偏差。

  - 工具编排与证据合成：将异构感知模块（OCR、目标检测、动作识别）抽象为统一证据接口，在推荐系统多模态特征融合时，按可靠性加权，提升融合质量。

  - 置信度引导的强化学习奖励设计：GRPO 奖励结合正确性、证据可靠性和效率，可用于训练推荐模型在信息不足时主动请求高价值特征，实现成本-收益平衡。

  - 在 Agentic 系统中，面对传感器或日志噪声，类似的三层置信度合成策略（高/中/低）可用于动态调整决策权重。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前视频推理模型假设所有帧同等可靠，但在运动模糊、眩光、遮挡等真实扰动下，准确率会骤降 15-30%，且模型对退化无感知，即“盲目信任问题”。

**方法**：提出 Robust-TO 框架，为每帧计算可靠-相关分数，筛选可信帧。异构视觉工具（检测、轨迹、OCR、动作标签）以统一证据格式返回预测、时间定位和校准的可靠性分数。推理时，采用三层证据合成策略（高/中/低置信度）加权综合；并定义置信度-成本 GRPO 奖励，同时优化正确性、证据可靠性和效率。

**结果**：在两个基准的 8 个任务上，干净输入平均准确率 56.4%，比最强开源基线高 10.6 个百分点，超越 Gemini-2.5-Pro（46.2%）。在五种损坏类型下，平均准确率 54.3%，领先开源基线 5.8 个百分点，且干净到损坏的降幅最小。
