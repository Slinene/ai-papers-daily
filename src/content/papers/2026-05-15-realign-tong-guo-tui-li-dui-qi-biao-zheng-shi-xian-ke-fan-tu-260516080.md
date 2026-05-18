---
title: 'ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation'
title_zh: ReAlign：通过推理对齐表征实现可泛化图像伪造检测
authors:
- Qing Huang
- Zhipei Xu
- Xuanyu Zhang
- Xiangyu Yu
- Jian Zhang
affiliations:
- Peking University
- South China University of Technology
- Guangdong Provincial Key Laboratory of Ultra High Definition Immersive Media Technology,
  Shenzhen Graduate School, Peking University
arxiv_id: '2605.16080'
url: https://arxiv.org/abs/2605.16080
pdf_url: https://arxiv.org/pdf/2605.16080
published: '2026-05-15'
collected: '2026-05-18'
category: Multimodal
direction: 图像伪造检测 · 推理蒸馏
tags:
- Image Forgery Detection
- Reasoning Distillation
- Contrastive Learning
- GRPO
- Multimodal Alignment
- Lightweight Model
one_liner: 利用GRPO优化LLM生成推理文本，通过对比蒸馏训练轻量检测器，兼顾泛化性与效率
practical_value: '- 若业务涉及商品图像真伪鉴别，可借鉴该**推理蒸馏**范式：用GRPO优化LLM生成细粒度、语义敏感的伪造推理文字，再通过对比学习将其蒸馏到轻量视觉模型，在保持推理能力的同时降低部署成本。

  - 联合优化对比损失与分类损失的策略，可迁移到其他需要图文对齐的轻量判别任务（如商品描述一致性校验）。

  - 自建高保真合成数据集UltraSynth-10k的思路，可参考用于构建电商AIGC干扰样本，提升业务模型对新型生成图像的鲁棒性。

  - 对Agent及生成式推荐直接借鉴有限，但其中利用推理文本作为“免费”增强信号提升泛化性的思想，或可启发在推荐解释生成或用户意图推理中的多模态对齐设计。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**  
AI生成图像（AIGIs）泛滥，现有检测方法存在局限：非LLM方法缺乏语义理解，LLM方法计算量大且对低级伪造痕迹不敏感，且LLM生成的推理文本对检测性能的真实贡献未探明。本文旨在挖掘LLM推理文本的泛化与语义错误敏感性，并高效蒸馏至轻量模型。

**方法**  
提出ReAlign框架：首先使用GRPO优化的LLM为图像生成高质量伪造推理文本；然后通过对比学习（CLIP风格）将图像与对应推理文本对齐，训练一个轻量视觉编码器，使其表征具备语义推理能力；同时联合优化分类损失，直接判别真伪。训练仅需图像-文本对，推理时仅用视觉编码器，无需LLM参与。

**结果**  
在AIGCDetectBenchmark、AIGI-Holmes及自建高保真数据集UltraSynth-10k上，ReAlign在准确率和泛化性上均超越现有SOTA，尤其在面对现代生成模型的高保真伪造时优势明显，且参数量与推理速度接近纯视觉轻量模型。
