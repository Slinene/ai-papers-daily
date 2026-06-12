---
title: 'Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?'
title_zh: Robust-U1：MLLMs能否自恢复损坏视觉内容以实现鲁棒理解？
authors:
- Jiaqi Tang
- Jianmin Chen
- Youyang Zhai
- Wei Wei
- Runtao Liu
- Mengjie Zhao
- Xiangyu Wu
- Qingfa Xiao
- Qifeng Chen
affiliations:
- The Hong Kong University of Science and Technology, Hong Kong
- Northwestern Polytechnical University, Xi’an, China
- Northeastern University, Shenyang, China
- Nanjing University of Science and Technology, Nanjing, China
- The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China
arxiv_id: '2606.08063'
url: https://arxiv.org/abs/2606.08063
pdf_url: https://arxiv.org/pdf/2606.08063
published: '2026-06-05'
collected: '2026-06-12'
category: Multimodal
direction: 多模态大模型 · 视觉自恢复 · 鲁棒性增强
tags:
- visual self-recovery
- robustness
- reinforcement learning
- multimodal reasoning
- image corruption
- MLLM
one_liner: 赋予多模态大模型显式视觉自恢复能力，通过SFT+RL双奖励训练显著提升损坏图像下的鲁棒性。
practical_value: '- **商品图像鲁棒理解**：电商场景中用户上传图片常有模糊、遮挡、水印等损坏，可借鉴Robust-U1的自恢复模块进行预处理，提升后续商品识别或属性抽取的鲁棒性。

  - **多模态Agent的视觉容错**：Agent接收实时视频流或截屏时可能出现压缩伪影或抖动，采用修复-推理双路径（同时输入原图和恢复图）比单纯去噪更可靠，避免信息丢失。

  - **训练范式可直接复用**：用SFT打底 + RL双奖励（像素SSIM保证保真度，语义CLIP相似度保证高层一致性）的方法比直接微调生成模型更稳定，适合在业务数据上微调小规模修复模型。

  - **质量感知的推理增强**：论文证明修复质量（SSIM）与下游VQA分数高度相关，业务中可通过监控图像质量指标来主动触发修复流程或调整推理置信度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态大模型（MLLMs）在现实世界视觉损坏（如噪声、模糊）下性能急剧下降。现有方案要么是黑盒特征对齐缺乏可解释性，要么是纯文本推理无法恢复像素级细节，亟需赋予模型自我修复能力。

**方法**：提出Robust-U1框架，通过三阶段训练将视觉自恢复能力融入MLLM：（1）监督微调（SFT）在合成损坏-原图对上训练模型生成初始修复图像；（2）强化学习（RL）采用双奖励函数——像素级SSIM和语义级CLIP相似度，在保证视觉质量的同时对齐高层语义；（3）多模态推理阶段同时输入损坏图和恢复图，让模型协同理解两路信息。

**结果**：在真实世界损坏基准上达到SOTA鲁棒性，对抗性损坏下通用VQA性能领先。分析表明高质量视觉恢复直接提升推理准确率，验证了自恢复是鲁棒视觉理解的关键机制。
