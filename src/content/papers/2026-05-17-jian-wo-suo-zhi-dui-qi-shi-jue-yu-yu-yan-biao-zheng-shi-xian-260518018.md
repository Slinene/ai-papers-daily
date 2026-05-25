---
title: 'See What I Mean: Aligning Vision and Language Representations for Video Fine-grained
  Object Understanding'
title_zh: 见我所指：对齐视觉与语言表征实现视频细粒度对象理解
authors:
- Boyuan Sun
- Bowen Yin
- Yuanming Li
- Xihan Wei
- Qibin Hou
affiliations:
- VCIP, CS, Nankai University
- Tongyi Lab, Alibaba Group
- NKIARI, Shenzhen Futian
arxiv_id: '2605.18018'
url: https://arxiv.org/abs/2605.18018
pdf_url: https://arxiv.org/pdf/2605.18018
published: '2026-05-17'
collected: '2026-05-25'
category: Multimodal
direction: 多模态对齐 · 细粒度视频对象理解
tags:
- Multimodal
- Vision-Language Alignment
- Cross-Attention
- Fine-grained Understanding
- Referring Expression
- MLLM
one_liner: 提出SWIM，训练时用掩码监督对齐跨注意力图，推理仅用文本提示即可定位视频中用户指定的对象，超越视觉提示方法
practical_value: '- **电商视频对象定位**：在商品讲解或直播视频中，只需文本查询（如“左边红色的包”）即可精确框定对象，避免手工标注视觉提示，可直接集成到内容理解流水线。

  - **跨模态注意力对齐训练 trick**：发现属性词产生尖锐激活而名词分散，可借鉴对特定词类（如商品名词、属性）施加空间掩码监督，提升模型遵循细粒度指令的能力。

  - **NL-Refer 数据集构建范式**：为每个对象掩膜配精确自然语言指代表达式，可复用至商品图像或视频标注，增强多模态模型的指代消歧能力。

  - **Agent 视觉定位模块**：在多智体框架中，若 Agent 需根据用户模糊描述（如“右下角的红色鞋子”）操作界面或理解视频，可借鉴该对齐方法，仅凭文本提示即可定位，省去额外视觉提示开销。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 MLLM 虽能全局理解场景，但对用户指定的细粒度对象常定位不准。通过分析跨注意力图发现：属性词产生局部尖锐激活，而对象名词因语义参照偏差和高层分布式表示，激活分散模糊，导致文本-视觉对齐差。

**方法**：提出 SWIM，训练时引入掩码监督——从多层跨注意力图中提取对象名词对应的注意力图，强制其与真实掩膜空间一致。同时构建 NL-Refer 数据集，为每个对象掩膜配精确的自然语言指代表达（而非简单名词）。模型在训练中学习将文本查询对应到精确对象区域，推理时抛弃视觉提示，仅用文本即可自动聚焦用户指定对象。

**结果**：在多个细粒度对象理解基准上，SWIM 显著优于依赖掩膜、点等视觉提示的传统方法，大幅提升文本-视觉对齐性能，表明纯文本查询的细粒度定位是可行的，并更具实用性。
