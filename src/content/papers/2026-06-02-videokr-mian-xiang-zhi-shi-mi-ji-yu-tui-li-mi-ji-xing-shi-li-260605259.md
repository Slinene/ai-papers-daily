---
title: 'VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding'
title_zh: VideoKR：面向知识密集与推理密集型视频理解
authors:
- Lin Fu
- Zheyuan Yang
- Yang Wang
- Tingyu Song
- Arman Cohan
- Yilun Zhao
affiliations:
- Zhejiang University
- Tongji University
- University of Chinese Academy of Sciences
- Yale University
arxiv_id: '2606.05259'
url: https://arxiv.org/abs/2606.05259
pdf_url: https://arxiv.org/pdf/2606.05259
published: '2026-06-02'
collected: '2026-06-05'
category: Multimodal
direction: 多模态视频理解 · 知识密集推理
tags:
- video understanding
- knowledge-intensive reasoning
- training corpus
- data curation
- human-in-the-loop
- GRPO
one_liner: 提出首个大规模知识密集视频推理训练语料 VideoKR，并证明数据设计是提升视频推理性能的关键
practical_value: '- 数据设计驱动能力突破：VideoKR 证明，针对特定能力（如知识密集推理）构建高质量、多难度的训练数据，比简单扩大通用数据更有效。在电商推荐中，可针对性构建商品知识推理、用户意图深层理解等微调数据，提升模型复杂决策能力。

  - 人类参与、技能导向的生成流水线：通过人工设计技能树、难易分级、思维链验证，确保数据可靠且覆盖渐进式推理能力。可借鉴其流程，为 Agent 规划、多轮对话等场景合成高质量
  SFT 数据，减少幻觉并增强逻辑性。

  - SFT→GRPO 训练范式：先监督微调再强化学习的二阶段训练，有效增强模型长期推理和自省能力。对于多智体协作、生成式推荐等任务，可用 RL 进一步对齐人类偏好或业务目标，提升策略质量。

  - 避免评估捷径：VideoKR-Eval 的设计刻意防止模型利用文本线索或表面统计假依赖，这提示我们在评估推荐解释、对话系统时应设计对抗性评估，确保模型真正理解了语义和上下文，而非文本匹配。'
score: 7
source: huggingface-daily
depth: abstract
---

现有视频理解模型往往过度依赖文本线索，缺乏深层知识调用与多步推理能力。为此，VideoKR 构建了首个大规模知识密集视频推理训练语料，包含 145K 专家领域视频上的 315K 推理示例，涵盖医疗、社科、工程等 10 个领域。通过人类参与、技能导向的生成流水线，从感知到归纳、演绎、批判性思维逐步提升示例难度与多样性，并结合思维链标注保障可靠性。同时构建了严格评估基准 VideoKR-Eval，确保问题需真正理解视频内容与外部知识，无法通过文本捷径回答。

在 SFT→GRPO 训练范式下，基于 VideoKR 微调的模型在知识密集视频推理上全面超越先前数据集 LLaVA-Video-178K、Video-STaR 等，同时在通用视频问答上保持竞争力。消融实验进一步证实数据规模、领域混合、技能覆盖及 GRPO 阶段对性能的独立贡献，揭示了以数据设计驱动视频推理进步的有效路径。
