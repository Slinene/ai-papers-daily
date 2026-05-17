---
title: 'Unison: Harmonizing Motion, Speech, and Sound for Human-Centric Audio-Video
  Generation'
title_zh: Unison：人体视频的动作、语音与音效和谐生成框架
authors:
- Shihao Cheng
- Jiaxu Zhang
- Quanyue Song
- Shansong Liu
- Zhizhi Guo
- Xiaolei Zhang
- Chi Zhang
- Xuelong Li
- Zhigang Tu
arxiv_id: '2605.08729'
url: https://arxiv.org/abs/2605.08729
pdf_url: https://arxiv.org/pdf/2605.08729
published: '2026-05-09'
collected: '2026-05-17'
category: Multimodal
direction: 多模态生成 · 动作-音频对齐
tags:
- audio-video generation
- cross-modal alignment
- speech-sound harmonization
- human-centric
- multimodal synthesis
one_liner: 通过语义引导的语音-音效解耦和双向跨模态强制策略，实现人体视频中动作、语音和音效的协同生成。
practical_value: '- 语音-音效解耦思想可借鉴用于直播电商中分离主播语音与背景音效，改善音频质量。

  - 双向跨模态强制策略可用于对齐商品视频中的动作与声音，提升视频内容的一致性。

  - 语义引导的自适应门控机制可应用于多模态推荐中，动态调节不同模态特征的贡献。

  - 主要贡献在视频生成学术领域，直接业务应用场景有限。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：人体视频中动作、语音与音效三个模态时间特性各异，现有模型难以保持跨模态一致对齐，常出现语音-音效相互干扰和动作-音频不同步问题。

**方法**：提出Unison框架，包含两大核心策略。1）语义引导的音频和谐化：在音频生成中解耦语音与音效成分，通过双向音频交叉注意力（bidirectional audio cross-attention）和语义条件门控（semantic-conditioned gating）实现自适应重组，减轻语音主导、保留环境音。2）双向跨模态强制策略：在视频扩散过程中，利用较清晰模态引导较嘈杂模态的去噪，通过解耦的噪声计划表和渐进稳定技术强化动作与音频的时间对齐。

**结果**：大量实验表明，Unison在音频感知质量和跨模态同步性上均达到SOTA，尤其在语音-音效分离清晰度和动作-声音匹配度上显著优于先前方法，验证了显式多模态和谐化的重要性。
