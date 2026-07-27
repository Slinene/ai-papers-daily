---
title: 'Small Vision-Language Models Know When They Are Wrong But Cannot Say So: A
  Two-Model Study of Stated versus Internal Confidence Under Realistic Image Degradation'
title_zh: 小视觉语言模型知道错了但说不出来：真实图像退化下的内部与口头置信度对比
authors:
- M M Asif Ferdous
affiliations:
- Independent Researcher
arxiv_id: '2607.22034'
url: https://arxiv.org/abs/2607.22034
pdf_url: https://arxiv.org/pdf/2607.22034
published: '2026-07-24'
collected: '2026-07-27'
category: Eval
direction: 小模型自我认知与置信度评估
tags:
- VLM
- confidence calibration
- uncertainty estimation
- token probability
- image degradation
- error detection
one_liner: 小VLM的口头置信度近乎恒定且无法检测错误，但内部token概率却能有效分离正确与错误答案
practical_value: '- **用内部 token 概率做 deferral 信号**：当小 VLM 用于商品图片理解、图像文本审核等任务时，直接解析模型输出的口头置信度（如"我确定答案是..."）并不可靠，应改用生成序列的平均
  token 概率作为置信度指标，尤其在模型需要自动放弃回答的场景。

  - **低质量图像输入要双重预警**：在用户上传图片可能严重欠曝/模糊的实际业务中（如直播间截图、用户随手拍），内部概率的 error detection AUROC
  会骤降到随机水平，此时应结合图像质量评估模块，严重退化时直接拒绝模型输出，不再依赖任何置信度。

  - **小模型的 uncertainty 并不体现在口语化表达里**：Qwen2-VL-2B 的口头置信度均值稳定在 0.87-0.90，几乎不随输入质量或答案正确性变化，说明对小模型做
  prompt engineering 让其自我评估准确性几乎是无效的，必须依赖 hidden state 或 token 概率等信息。

  - **SmolVLM 的口头置信度解析成本高到不可用**，尝试三种 prompt 模板只有一次成功解析出置信度值，这提醒我们在工程化时，若模型输出格式不可控，则结构化置信度输出方案需要更严格的约束（如强制
  JSON 格式），否则直接使用内部概率是更稳定的选择。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：小参数 VLM 越来越多部署在消费级硬件上，输入图像常被压缩、抖动或欠曝。这类场景下，模型能否给出可靠的置信度，决定系统何时应停止响应（defer），而非强行回答。但小模型口头表达的置信度是否真实反映其自我认知？

**方法**：作者在 Qwen2-VL-2B-Instruct 和 SmolVLM-Instruct 上，对六种真实图像退化（Gaussian blur, JPEG压缩，欠曝等）各三个严重等级，收集 3800 条预测。对比两种置信度：① 自然语言中口头声称的置信度（verbalized confidence）；② 模型生成答案的平均 token 概率（internal confidence）。主要指标是置信度区分正确与错误答案的 AUROC。

**关键结果**：Qwen2-VL 的口头置信度近乎恒定（均值 0.87-0.90），误差检测 AUROC 仅 0.39-0.75，多在随机水平 0.5 附近；而同模型的内部 token 概率 AUROC 高达 0.92-0.99。SmolVLM 的口头置信度几乎无法解析（三种 prompt 模板仅一次成功），但其内部概率 AUROC 仍达 0.54-0.92。两种模型在严重欠曝下均彻底失效：Qwen2-VL 准确率从 0.99 暴跌至 0.22，SmolVLM 从 0.97 跌至 0.42，同时两种置信度信号都无明显变化，内部 error detection AUROC 也降至随机水平。结论：小 VLM 编码了可用的自我知识，但无法通过语言表达；内部 token 概率是更适合受限部署的 deferral 信号，但低光照条件下什么信号都不可信。
