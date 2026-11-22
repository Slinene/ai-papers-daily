---
title: Suppressing the Shortcut Hidden Behind the Gains of VideoLLM Fine-Tuning
title_zh: 抑制 VideoLLM 微调收益背后的文本捷径
authors:
- Youngwoo Shin
- Jongsuk Kim
- Junmo Kim
affiliations:
- KAIST
- PYLER
arxiv_id: '2611.25776'
url: https://arxiv.org/abs/2611.25776
pdf_url: https://arxiv.org/pdf/2611.25776
published: '2026-11-18'
collected: '2026-11-22'
category: Training
direction: VideoLLM 微调去捷径
tags:
- VideoLLM
- Shortcut Learning
- SFT
- Orthogonal Projection
- Distribution Shift
- Fine-tuning
one_liner: 提出 VETO：把微调更新投影到纯文本子空间的正交补，跨 7 个 VideoLLM 抑制捷径并提升分布外泛化
practical_value: '- 多模态商品/视频内容理解微调时，模型常走文本捷径（如标题-属性、品牌-品类共现），绕过图像/视频证据。可复用 VETO 思路：先用
  base model 在纯文本输入上标定文本子空间，再把 LoRA/全参更新投影到正交补，无需人工定义哪些文本模式是捷径。

  - 电商 catalog、广告素材频繁更新，训练/测试分布容易漂移。该投影方法保持同分布 SFT 增益，同时提升 OOD 鲁棒性，适合多模态 ranking、短视频理解、直播间内容分析等下游微调。

  - 工程实现轻量：只需收集 base model 在 text-only input 上的 activation 估计子空间，再在 optimizer step
  投影梯度；可与 LoRA/QLoRA 结合，不增加推理开销。

  - 在 Agent 微调中，如果担心模型只靠 system prompt、工具名或检索标题做动作，而忽略真实观察/返回结果，可以类似地投影掉“无证据文本子空间”，强制模型依赖检索结果、执行反馈或图像证据。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：VideoLLM 在 SFT 阶段既提升视频推理能力，也容易学会仅靠训练文本规律作答，这类 shortcut 不受训练 epoch、数据规模或 backbone 影响。它藏在同分布精度上升背后，但在分布偏移下会损失视频带来的增益。

方法关键点：提出 VETO（Video-Evidence Training via Orthogonal projection），不在数据层面删除 shortcut，而是干预微调更新。先用 base model 在纯文本输入上标定激活中的文本子空间，再把 SFT 的更新投影到其正交补上，从而保留跨模态 grounding 更新，抑制纯文本捷径随时间形成。

关键结果：在 7 个 VideoLLM 上，VETO 保持训练分布的 SFT 增益并抑制 shortcut；在 6 个分布偏移 benchmark 上优于 SFT，且模型更多依赖完整视频输入而非文本 regularities。代码已开源。
