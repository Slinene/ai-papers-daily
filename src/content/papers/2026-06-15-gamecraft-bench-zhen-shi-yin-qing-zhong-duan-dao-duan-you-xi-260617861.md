---
title: 'GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game
  Engine?'
title_zh: GameCraft-Bench：真实引擎中端到端游戏可玩性基准
authors:
- Tongxu Luo
- Rongsheng Wang
- Jiaxi Bi
- Chenming Xu
- Zhengyang Tang
- Jianlong Chen
- Juhao Liang
- Ke Ji
- Shuqi Guo
- Yuhao Du
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
- Hunyuan Team, Tencent
- USTB
- DualverseAI
arxiv_id: '2606.17861'
url: https://arxiv.org/abs/2606.17861
pdf_url: https://arxiv.org/pdf/2606.17861
published: '2026-06-15'
collected: '2026-06-17'
category: Agent
direction: 游戏生成基准 · Agent 评估
tags:
- game generation
- coding agents
- benchmark
- Godot
- interactive verification
- multimodal judging
one_liner: 提出基于交互验证的游戏生成基准，评估编码智能体在 Godot 引擎中端到端构建可玩游戏的能力
practical_value: '- 评估框架中“引擎接地”概念可迁移至推荐或对话 Agent：确保模型输出能在真实业务环境中执行并产生可观测结果，而非仅产生文本。

  - “产物完整性”指标提醒生成式推荐系统需评估整个推荐列表或页面的连贯性与内容充足性，避免只关注单点准确率。

  - 多模态评审（rubric-guided multimodal judging）可借鉴用于对推荐理由、广告创意等富媒体输出进行自动化质量评估。

  - 回放演示的交互验证思路可用于对话推荐 Agent 的端到端评测，关注完整对话流的可玩性而非轮次级评分。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：游戏生成是编码智能体的新兴应用，但现有基准多为文本或代码片段，未涉及真实游戏引擎内的端到端评估，忽略了资产完整性、视觉反馈、交互可玩性等关键维度。
**方法**：将端到端游戏生成形式化为在 Godot 引擎中根据自然语言规格生成完整可玩游戏的问题，提出三个评估要求：引擎接地（Engine Grounding）、产物完整性（Artifact Completeness）、交互验证（Interactive Verification）。构建 GameCraft-Bench，包含 140 个任务，覆盖 15 个游戏品类（如平台跳跃、Roguelike、卡牌等）。评估时，用回放演示替代人工互动，结合评分标准引导的多模态评审（MM-judge）自动打分。
**结果**：前沿编码智能体在该基准上表现普遍不佳，最高分模型仅达 41.46%，多数低于 40%。分析显示，智能体常能实现可识别的核心机制，但难以产出足够的游戏内容、功能性的视觉反馈和连贯的呈现，暴露了从脚本创作到完整游戏体验之间的巨大差距。
