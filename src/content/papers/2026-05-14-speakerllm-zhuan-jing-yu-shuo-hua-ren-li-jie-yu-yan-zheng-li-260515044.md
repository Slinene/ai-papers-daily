---
title: 'SpeakerLLM: A Speaker-Specialized Audio-LLM for Speaker Understanding and
  Verification Reasoning'
title_zh: SpeakerLLM：专精于说话人理解与验证推理的音频大语言模型
authors:
- KiHyun Nam
- Jungwoo Heo
- Siu Bae
- Ha-Jin Yu
- Joon Son Chung
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
- University of Seoul
arxiv_id: '2605.15044'
url: https://arxiv.org/abs/2605.15044
pdf_url: https://arxiv.org/pdf/2605.15044
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 音频LLM的说话人理解与验证推理
tags:
- Audio LLM
- Speaker Verification
- Hierarchical Tokenizer
- Reasoning
- Decision Composition
one_liner: 通过层级说话人 tokenizer 和结构化推理轨迹，统一了说话人画像、录音条件理解和证据组织的验证推理。
practical_value: '- 在语音交互的电商客服Agent中，可借鉴层级说话人 tokenizer 设计：粗粒度嵌入快速匹配用户身份，细粒度帧级特征捕获情绪、口音等属性，用于个性化服务与内容推荐。

  - 结构化推理轨迹（录音条件、证据、决策）的分离模式，可迁移到推荐系统的可解释理由生成，提供可审计的决策链。

  - 决策复合策略分离证据收集与最终判断，可用于多Agent协作场景，让不同Agent负责信息收集，由决策Agent综合证据，提升系统可靠性。

  - 利用LLM自动构建带结构化元数据的监督数据集的方法，可复用至生成式推荐的对齐训练，低成本生成推荐理由与用户画像的标注数据。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：音频优先的Agent（如物理AI、对话机器人）需要理解说话人身份、声音属性和录音条件，以支持用户授权、个性化等。现有说话人验证系统仅给出分数而缺乏语言解释，通用音频LLM对说话人信息的组织能力有限。
**方法**：提出 SpeakerLLM，一个专精于说话人的音频LLM框架。核心是 **层级说话人 tokenizer**（Hierarchical Speaker Tokenizer）：话语级嵌入总结身份/画像线索，帧级特征保留细粒度声学描述。模型将单话语说话人画像、录音条件理解、话语对比较和证据组织的验证推理统一在自然语言接口中。训练时，构造了验证推理目标和一个 **决策复合策略**（Decision-Composition Policy），将画像证据与最终“相同/不同”判决分离，并组织成结构化的推理轨迹（录音条件、画像证据、判决）。
**结果**：实验表明，SpeakerLLM-Base 在说话人画像和录音条件理解上优于通用音频LLM；SpeakerLLM-VR 在生成判决准确率上保持强性能，同时产生与监督验证推理 schema 一致的决策轨迹。作者将公开带元数据的监督数据集和构建代码。
