---
title: 'Beyond Generative Decoding: Discriminative Hidden-State Readout from a Native
  Omni-Modal LLM for Multimodal Sentiment Analysis'
title_zh: 基于原生全模态LLM的判别式隐藏状态读出用于多模态情感分析
authors:
- Bin Wen
- Tien-Ping Tan
affiliations:
- School of Computer Sciences, Universiti Sains Malaysia
arxiv_id: '2606.05713'
url: https://arxiv.org/abs/2606.05713
pdf_url: https://arxiv.org/pdf/2606.05713
published: '2026-06-04'
collected: '2026-06-07'
category: LLM
direction: 判别式读出 · 多模态情感回归
tags:
- Multimodal Sentiment Analysis
- Discriminative Readout
- Generative Readout
- Qwen2.5-Omni
- QLoRA
- Hidden-State Regression
one_liner: 用判别式隐藏状态回归替代生成式解码，在连续情感分析中精度更高、更可靠、推理更快
practical_value: '- **连续值输出的LLM应用首选判别式头**：当需要预测连续值（评分、概率、强度）时，不要用生成字符串再解析，直接从最后一token隐藏状态接轻量MLP回归，避免格式错误和精度损失，同时大幅降低推理延迟。

  - **QLoRA + 动态帧采样降低多模态LLM硬件门槛**：在单张32GB消费显卡上跑通7B全模态模型，LoRA rank=32，仅训练1.14%参数，该配方可直接迁移到电商视频评论理解、直播情感监控等任务。

  - **可控读出对比可作为模型诊断工具**：固定骨干、数据和适配方案，只改变读出方式，能定量评估生成式解码的额外误差和不可靠性，类似思路可用于推荐系统中LLM输出评分/理由时选择最优读出策略。

  - **音频预处理合理提点**：用轻量去噪（如DeepFilterNet）清理音频通道，可改善细粒度回归指标，这在金融举报音频、客服录音等场景下值得尝试。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**：多模态情感分析（MSA）需从文本、音频、视频预测连续情感值。主流LLM方案采用生成式读出：让模型采样输出数值字符串再解析，这与连续回归目标存在本质错配——离散自回归解码无法精确刻画强度，推理慢且可能产生不可解析或越界输出。本文首次在相同骨干、数据和适配条件下系统比较两种读出机制，主张用判别式读出替代生成式，并给出可复现的消费级硬件方案。

**方法**：
- 以Qwen2.5-Omni-7B的Thinker为共享编码器，处理文本、视频帧和音频，丢弃原生的语音生成Talker头。
- 判别式读出：取末层最后一个非填充token隐藏状态，经LN→Linear→ReLU→Dropout→Linear的轻量MLP直接回归[-3,+3]标量，单次前向，无解码。
- 生成式基线：在同样骨干上保留语言头，自回归生成数值字符串后解析，训练时使用字符串似然损失。
- 高效适配：骨干4-bit NF4量化，LoRA (r=32)插入注意力与FFN投影，仅训练~1.14%参数；动态采帧与像素上限控制内存，峰值10–21GB。
- 训练目标：判别式用标准化标签的MAE损失，生成式用交叉熵。

**关键结果**：
- 在CMU-MOSI和CMU-MOSEI上，判别式读出精度与SOTA专用融合模型持平（MOSI: MAE 0.551, Corr 0.888; MOSEI: MAE 0.506, Corr 0.790），但无需手工特征和定制融合架构。
- 控制读出对比：固定骨干与LoRA，判别式MAE 0.667，生成式零样本MAE 1.443（2.8%无法解析），监督训练后MAE反升至1.521且相关性暴跌，揭示了生成式损失与连续目标的不匹配。
- 隐藏空间可视化显示情感强度呈平滑梯度，kNN标签平滑度较随机基线降低49.9%，说明骨干已习得线性可分的情感流形，轻量头足以捕获。
- 音频去噪（DeepFilterNet）在MOSI上将MAE从0.598降至0.551，细粒度回归收益显著。

**核心启示**：对于连续值ML任务，
“如何读出”与“如何训练”同等重要，判别式读出在精度、可靠性和效率上全面优于生成式，且可轻松部署于消费级GPU。
