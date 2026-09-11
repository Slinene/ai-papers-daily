---
title: 'Show-Harness: Just a VLM Agent Can Play Robots'
title_zh: Show-Harness：仅用 VLM Agent 通过语义接口控制机器人
authors:
- Yanzhe Chen
- Zechen Bai
- Zhijun Cao
- Wenzheng Zeng
- Kevin Qinghong Lin
- Yiqi Lin
- Guoqiang Liang
- Kevin Yuchen Ma
- Qiming Huang
- Mike Zheng Shou
affiliations:
- Show Lab, National University of Singapore
arxiv_id: '2609.10522'
url: https://arxiv.org/abs/2609.10522
pdf_url: https://arxiv.org/pdf/2609.10522
published: '2026-09-08'
collected: '2026-09-11'
category: Agent
direction: VLM Agent 语义接口机器人控制
tags:
- VLM
- Agent
- Embodied AI
- Semantic Interface
- Zero-shot
- Fine-tuning
one_liner: 通过离散语义动作单元与解释器接口，让 VLM Agent 零样本或轻量微调后直接控制机器人
practical_value: '- 借鉴“语义动作单元 + 确定性 interpreter”两层架构：让 LLM/VLM 只输出离散标准化意图标签（如 MV_FWD、GRASP），由业务侧
  interpreter 落地为具体执行动作，可迁移到推荐/Agent 系统中降低模型生成复杂控制序列的出错率，同时兼容 App、网页、机器人等多端。

  - 对闭源大模型直接 zero-shot 使用同一套接口，开源小模型仅需 few GPU-hours 微调即可替换，说明业务侧可保持接口不变、灵活切换底层模型，降低迭代成本。

  - GUMI 的 GUI 操作采集 demonstrations 思路可复用：无需专用硬件，通过浏览器/GUI 操作轨迹构建 fine-tuning 数据，适合
  UI 自动化、商品操作、Agent 行为采集等场景。

  - 强调跨任务、跨 embodiment、跨环境泛化评测，建议推荐系统也构造跨场景/跨页面/跨库存的泛化测试集，避免单一环境过拟合。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基础 VLM 具备通用世界知识，但难以直接转化为机器人控制；现有方法往往依赖专门预训练或复杂动作空间，成本高且泛化有限。

**方法关键点**：
- 提出 Show-Harness，一个 Embodied Harness，通过紧凑语义接口连接意图与动作：暴露离散语义动作单元（如 MV_FWD、GRASP、ROTATE_CW），VLM 只负责在语义空间决策；
- embodiment-specific interpreter 将语义动作确定性映射为本地机器人动作，保持 VLM 对细粒度物理决策的直接责任，同时解耦模型与硬件；
- 同一接口支持闭源 frontier VLM zero-shot 控制和开源小模型少 GPU-hours 微调；
- 开发 GUMI（GUI Manipulation Interface），将相同语义动作空间扩展到 GUI 演示采集，人类和 Agent 无需专用遥操作硬件即可跨 embodiment 操作机器人。

**关键结果**：
- Show-Harness 使 VLM Agent 在多种任务、机器人形态和环境中稳健泛化，超过代表性 agentic 和 VLA 方法；
- 闭源 VLM 无需微调即可 zero-shot 部署，开源小模型仅需几 GPU-hours 微调即可获得可用控制能力，验证了接口设计而非模型容量是解锁 embodied capability 的关键。
