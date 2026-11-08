---
title: 'VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding'
title_zh: VFlash：通过 Flash Primitive Decoding 实现快速精确视觉规划
authors:
- Yu-Cheng Chou
- Shihao Wang
- Jin Huang
- Chi-Pin Huang
- Chiao-An Yang
- Xianzhe Fan
- Jing Wang
- Zhiqi Li
- Yuanguo Kuang
- Ruijie Zheng
arxiv_id: '2611.08449'
url: https://arxiv.org/abs/2611.08449
pdf_url: https://arxiv.org/pdf/2611.08449
published: '2026-11-04'
collected: '2026-11-08'
category: Multimodal
direction: VLM 视觉规划解码加速
tags:
- VLM
- Visual Planning
- Speculative Decoding
- Trajectory Prediction
- Structured Decoding
- Robotics
one_liner: 利用视觉原语结构，以轻量 drafter 单次前向生成整个原语，提升规划精度并大幅降低解码延迟
practical_value: '- 在 LLM 业务中输出结构化结果（商品属性、推荐理由、tool call 参数）时，可以借鉴 VFlash 的思路：按 schema
  把输出分块，用轻量 drafter 一次前向生成整个块，再由主模型 verify；这比逐 token 解码快，且能减少格式崩溃。

  - 对于有明确结构先验的输出（如图像中的商品 bounding box、区域定位、搜索 query 模板），可以设计非逐 token 的并行解码头，直接生成完整原语，避免长序列自回归的延迟。

  - “不要求与 AR 序列完全一致，只要求结构合法”这一准则对 speculative decoding 有启发：结构化解码可以用 schema validator
  替代 token 级 agreement，降低拒绝率，提高接受率。

  - 整体面向机器人/自动驾驶规划，业务可借鉴点有限；若做多模态推荐、图像搜索中的空间定位或 Agent 的动作规划，可以参考其分块并行解码与结构约束验证的工程实现。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：物理 AI 任务（机器人、自动驾驶）常用视觉规划——点、边界框、轨迹——来表达空间目标与运动。自回归 VLM 逐 token 生成坐标，预测越丰富延迟越高。

**方法关键点**：VFlash 利用视觉原语的已知结构，将预测按 primitive 分块；轻量 drafter 在单个 forward pass 中生成整个原语，布局根据类型、维度、长度自适应，支持紧凑框和变长 2D/3D 轨迹、密集点运动。关键设计是不要求与 AR 模型的 token 序列完全一致，直接接受结构合法的预测，模型在标注原语上训练；文本/子任务仍采用 verified speculative decoding。

**关键结果**：在 2D/3D 机器人轨迹任务上，VFlash 相比 AR 解码降低了预测误差；3D 点运动预测单 rollout 约 25 倍加速；以 VFlash plan 为条件的 world action model 在 MolmoSpaces 四个任务套件上平均成功率为 70.2%，高于 baseline 62.6%；在 Jetson Thor、DGX Spark 上解码总延迟降低约 80%。
