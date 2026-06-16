---
title: Exploring Extrinsic and Intrinsic Properties for Effective Reasoning with Code
  Interpreter
title_zh: 探索代码解释器推理的外在令牌与内在认知特性
authors:
- Patomporn Payoungkhamdee
- Napat Laosaengpha
- Jenta Wonglertsakul
- Pittawat Taveekitworachai
- Pume Tuchinda
- Panjapong Poobanchuen
- Ekapol Chuangsuwanich
- Can Udomcharoenchaikit
- Samuel Cahyawijaya
- Peerat Limkonchotiwat
affiliations:
- Vidyasirimedhi Institute of Science and Technology
- Kasetsart University
- SCB 10X
- King Mongkut's University of Technology Thonburi
- Chulalongkorn University
arxiv_id: '2606.16934'
url: https://arxiv.org/abs/2606.16934
pdf_url: https://arxiv.org/pdf/2606.16934
published: '2026-06-15'
collected: '2026-06-16'
category: LLM
direction: LLM推理 · 代码解释器行为分析
tags:
- Code Interpreter
- Crucial Tokens
- Cognitive Behaviors
- LLM Reasoning
- Fine-tuning
one_liner: 发现有效代码推理依赖关键令牌与验证、回溯等认知行为，并验证其对推理提升和训练增强的作用
practical_value: '- 在电商Agent中若使用代码解释器进行数据查询或逻辑推理，可在推理时追加识别出的关键令牌（如结果验证、步骤回溯）以提升任务准确度。

  - 训练推荐系统的LLM推理模块时，可注入代码思维中的自我验证、反向链推理等认知行为作为数据增强，帮助模型在复杂决策中减少过度思考，提高推理效率。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
基于代码解释器（CI）的推理虽有效，但其行为特性缺乏系统性研究。受自然语言推理中关键令牌与认知行为研究的启发，本文首次从外在特性（关键令牌）和内在特性（认知行为）两个角度分析CI推理。

**方法**
在多个LLM上分析发现，推理更强的模型呈现出更高比例的关键令牌（如与验证、回溯相关的代码片段）以及更丰富的代码特定认知行为（尤其是验证、回溯、反向链推理）。基于此，作者在推理时通过追加*代码特定关键令牌*来引导模型，并在训练时将认知行为模式注入监督微调（SFT）和强化学习（RL）流程。

**关键结果**
推理时追加关键令牌在数学、排序、优化等推理任务上带来显著提升，但在其他任务上收益有限。训练增强在三个受测模型中的两个上取得性能改进，并且这些认知行为有效减少了错误回答中的“过度思考”（overthinking），提升了令牌利用效率。研究还揭示了某一模型增益受限的因素。本文首次系统表征了CI有效推理的特性，并论证了利用这些特性提升推理能力的可行性与当前局限。
