---
title: 'Tri-PvP: Exposing Modality Bias in Omni-Modal Large Language Models through
  Perceptual-Propositional Evidence Conflicts'
title_zh: Tri-PvP：通过感知-命题证据冲突暴露全模态大模型的模态偏见
authors:
- Yen-Ting Piao
- Shu-Yun Chen
- Chin-Hui Chu
- Chun-Wei Chen
- Shih-Yun Shan Kuan
- Hung-yi Lee
- Yun-Nung Chen
affiliations:
- National Taiwan University
- NTU AI-CoRE
arxiv_id: '2609.06011'
url: https://arxiv.org/abs/2609.06011
pdf_url: https://arxiv.org/pdf/2609.06011
published: '2026-09-04'
collected: '2026-09-25'
category: Eval
direction: 多模态LLM偏见评估与证据形式解耦
tags:
- Modality Bias
- Omni-modal LLM
- Evaluation
- Cross-modal Conflict
- Perceptual vs Propositional
- Linear Probing
one_liner: 构建8k三模态冲突基准Tri-PvP，解耦感知与命题证据，揭示OLLM视觉偏见及证据形式不对称
practical_value: '- 在多模态电商商品理解、广告素材审核、语音+图文搜索等场景中，要注意OLLM对视觉感知信号（商品图、视频帧）存在系统性偏好；当图文不一致时，模型可能更信图而忽略文字声明，需在prompt或后处理中显式引入文本证据校验。

  - 评测多模态模型时，把证据拆成感知（图片/录音）和命题（文字声明）两类，设计冲突样本分别控制，否则会把证据形式偏见误判为模态偏见；该思路可直接迁移到搜索相关性、商品属性抽取、多模态排序的评估集构建。

  - 线性探测显示模态偏见在早期表示层就已可解码，说明仅靠表面prompt或后处理难以根治；在业务中若要对多模态Agent做去偏，应考虑训练阶段或表示层面的干预，而不是只改推理指令。

  - 对比解码可部分缓解偏见，可作为多模态生成/审核链路中的工程化尝试；音频通道相比视觉更偏命题信号，在语音交互类Agent设计中可侧重结构化文本而非低层声学特征。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有全模态大模型（OLLM）模态偏见基准把同模态内两种证据形式混在一起——感知信号（狗的照片/叫声录音）与命题信号（“这是一只狗”的文本声明），导致测得的模态偏见无法区分是模型偏爱某模态，还是偏爱某种证据形式。

方法：构建 Tri-PvP，一个8000样本的三模态冲突基准，跨越视觉、音频、文本，并让视觉和音频分别以感知或命题形式出现，从而系统解耦模态与证据形式。在5个OLLM上评估冲突答案下的偏向。

关键结果：大多数模型在多数条件下表现出稳健的视觉偏见；证据形式偏见存在不对称——视觉模态更偏感知信号，音频模态更偏命题信号；逐层线性探测与对比解码表明，模态偏见从早期表示层即可线性解码，且只能被部分缓解，提示需要超越表层干预的缓解策略。
