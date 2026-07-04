---
title: 'ESC: Emotional Self-Correction for Reliable Vision-Language Models'
title_zh: 情感驱动自纠正：免训练提升视觉语言模型可靠性
authors:
- Tien-Huy Nguyen
- Minh-Nhat Nguyen
- Nguyen Nhat Huy
- Hung Viet Nguyen
- Huy Nguyen Minh Nhat
- Thanh-Huy Nguyen
- Cuong Tuan Nguyen
- Hoang M. Le
- Dat Nguyen
- Phat Kim Huynh
affiliations:
- University of Information Technology, Ho Chi Minh City
- Carnegie Mellon University
- Harvard University
- Northwestern University
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.02089'
url: https://arxiv.org/abs/2607.02089
pdf_url: https://arxiv.org/pdf/2607.02089
published: '2026-07-01'
collected: '2026-07-04'
category: Reasoning
direction: 情感信号触发VLM自纠正
tags:
- Emotional Feedback
- Self-Correction
- Vision-Language Models
- Training-Free
- Reliability
- Multimodal Reasoning
one_liner: 发现情感信号可零训练激活VLM自我反思，提出外部验证+情感提示的免训练自纠框架ESC
practical_value: '- 在对话推荐/商品问答中，当模型首次回复可能不可靠时，注入情感提示（如“再仔细想想，这个推荐似乎有问题”）触发自我纠正，提升解释质量。

  - 无需微调，低成本增强多模态模型在商品图片理解、广告文案生成等场景的准确性，尤其适合资源受限的线上系统。

  - 结合简单的验证器检测潜在错误响应，可作为Agent内部反思模块，在输出前自动触发二次推理，减少事实错误和幻觉。

  - 情感作为控制信号的想法可迁移至用户交互设计，例如用户不满时自动触发模型重新生成更谨慎的回答，改善体验。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：VLM在多模态任务上表现优异，但推理可靠性不足，现有自纠方法多依赖训练或复杂反馈，成本高。本文探索能否利用情感线索零训练地激活VLM的潜自纠能力。
方法关键点：提出ESC（Emotional Self-Correction）框架，包含外部验证器与情感反馈注入。验证器检测初始响应中的潜在错误，若存在风险则向模型追加情感化提示（如“请再仔细检查，你确定正确吗？”），促使模型反思并生成修正答复，全程无需额外训练。
关键结果：在安全性、幻觉、视觉感知、多模态推理等主流基准上，ESC将LLaVA的VLSafe攻击成功率从28.4%降至90.1%（提升3倍），并在POPE、HallusionBench等指标上显著优于基线，同时保持通用任务性能不降。实验证明情感不仅是被识别对象，更可作为实用的可扩展自纠控制信号。
