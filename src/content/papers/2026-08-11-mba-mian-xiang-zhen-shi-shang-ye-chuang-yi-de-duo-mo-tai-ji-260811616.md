---
title: 'MBA: Multimodal Benchmark and Agents for Real-World Business Ideation'
title_zh: MBA：面向真实商业创意的多模态基准与智能体
authors:
- Hojun Choi
- Jaeyo Shin
- Suin Lee
- Hyunjung Shim
affiliations:
- KAIST AI
arxiv_id: '2608.11616'
url: https://arxiv.org/abs/2608.11616
pdf_url: https://arxiv.org/pdf/2608.11616
published: '2026-08-11'
collected: '2026-08-14'
category: Other
direction: 多模态业务创意生成代理
tags:
- Multimodal
- Business Ideation
- GRPO
- MLLM-as-Judge
- LoRA
- Benchmark
one_liner: 构建首个多模态商业创意基准 MBA-Bench，并训练基于 GRPO 的代理，在 blind/known 双设置下显著超越基线
practical_value: '- 多模态视觉线索驱动创意生成：在电商商品卖点、广告文案、活动策划生成中，不要只用文本属性，把商品图、场景图抽成视觉线索（自动
  caption + MLLM），补充形状、材质、空间布局等独特卖点，这些视觉信号往往直接影响点击转化。

  - 检索增强合成（RAG for ideation）：生成前先根据任务生成检索 query，取回市场证据（竞品、用户评论、趋势数据），再做 evidence-augmented
  synthesis。可用于选品文案、push 文案：先检索用户近期关注与竞品卖点，再生成差异化创意。

  - 奖励设计分离 creativity 与 feasibility：训练生成代理时，将奖励拆为创造力（新颖性）与可行性（实现路径、成本等），并可将已知业务指标（点击率、转化率）作为
  disclosed criteria 加入 GRPO 优化，避免盲目 hack 指标。

  - 轻量训练栈：LoRA SFT + GRPO 在小算力下即可微调多模态模型，业务侧可在已有 MLLM 上快速构建创意代理与自动化评测闭环。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有基于 LLM 的商业创意生成代理仅处理文本，忽略真实场景中的多模态视觉线索。为此构建 MBA-Bench，首个多模态商业创意基准，包含 30K 样本、六个领域（如空间布局、拥挤度、技术特征、形状纹理），每个领域都有文本无法完全传达的视觉条件。

方法：数据构建采用自动 caption 图片，并用 GPT-4o 通过检索 query 生成、市场证据检索、证据增强合成三步，为每张图三个商业问题各生成五个参考想法。评估使用 MLLM-as-a-Judge，设定六个商业导向指标，并区分隐藏标准（MBA-b）与已知标准（MBA-k）两种设置。两个代理均采用 LoRA 监督微调后接 group relative policy optimization（GRPO），基础奖励为 creativity 和 feasibility；MBA-k 额外优化六个已知标准，共八个奖励目标。

结果：在 MBA-Bench 上，MBA-b 与 MBA-k 分别超过纯 caption 基线 63.9% 和 77.1%，超过多模态基线 25.6% 和 35.8%，部分指标接近闭源模型表现，验证多模态输入与分层奖励优化的有效性。
