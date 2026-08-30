---
title: 'GameWAM: A World Action Model for Video Games'
title_zh: GameWAM：视频游戏世界-动作模型
authors:
- Yuncheng Guo
- Zhanqiu Zhang
- Yiwen Guo
- Weijia Li
affiliations:
- Fudan University
- LIGHTSPEED
- Independent Researcher
- Tsinghua Shenzhen International Graduate School
arxiv_id: '2608.26200'
url: https://arxiv.org/abs/2608.26200
pdf_url: https://arxiv.org/pdf/2608.26200
published: '2026-08-24'
collected: '2026-08-30'
category: Agent
direction: 视频游戏世界-动作模型
tags:
- World-Action Model
- Generative Control
- Flow Matching
- Game Agent
- Long-horizon
- LASI
one_liner: 首个面向原生闭环游戏与GUI控制的世界-动作模型，联合生成未来视觉与键鼠动作，支持长程重规划
practical_value: '- 「并行视觉 + 动作生成 + block-causal conditioning」可作为多模态 Agent 联合建模世界状态与下一步决策的架构参考，尤其适用于需要同时预测环境变化和行为的搜索/推荐仿真环境。

  - 「mode 预测 + mode-specific 分布 + 连续动作归一化」可迁移到多任务 Agent 或生成式推荐中处理异构行为（如点击、加购、搜索词），先预测行为类型再用对应分布生成，减少异质输出的冲突。

  - 「block-cycle control」类似模型预测控制：预测多步但只执行短前缀，然后基于新观测重规划，可借鉴到实时推荐策略调整；通过分层历史上下文保持长期一致性，对会话级推荐有参考价值。

  - LASI 发现低频率成分主导生成输出，提示生成式动作/序列模型要监控随机源的低频成分，可通过谱约束或低通滤波增强可控性。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现代视频游戏融合第一人称感知、快速视觉变化、持久状态和异质键鼠控制。现有游戏 agent 直接映射视觉与任务上下文到动作，缺乏显式世界动态建模；交互式世界模型预测未来视觉却不作为任务策略。世界-动作模型（WAM）可统一两者，但在视频游戏开放交互中尚未探索。

方法关键点：GameWAM 是首个原生闭环游戏与 GUI 控制的 WAM。采用并行视觉与动作生成过程，结合 block-causal conditioning 与 flow matching 联合生成未来视觉观测和可执行键鼠轨迹；训练使用同步构建的 gameplay/GUI 轨迹。处理异构控制时，每步预测 gameplay/GUI mode，并用 mode-specific 预测分布与连续动作归一化。长程交互采用 block-cycle control：预测超过承诺视界，只执行短动作前缀并重规划，通过 within-cycle context 和 hierarchical cross-cycle history 保持时序连续性。

关键结果：实验中以更少执行动作取得竞争性任务成功率。还发现低频率动作源烙印（LASI）：采样动作源的低频成分在固定条件下系统性引导生成相机运动，揭示生成控制对源敏感性的失效模式。
