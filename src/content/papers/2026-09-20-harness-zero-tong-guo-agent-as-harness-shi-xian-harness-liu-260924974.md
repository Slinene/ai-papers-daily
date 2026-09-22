---
title: 'Harness-Zero: Harness Distillation via Agent-as-Harness'
title_zh: Harness-Zero：通过 Agent-as-Harness 实现 Harness 蒸馏
authors:
- Haoran Ye
- Yuxing Lu
- Haonan Dong
- Zhaochen Su
- Guojie Song
affiliations:
- Peking University
- Google
- The Hong Kong University of Science and Technology
arxiv_id: '2609.24974'
url: https://arxiv.org/abs/2609.24974
pdf_url: https://arxiv.org/pdf/2609.24974
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: LLM Agent 蒸馏与外部策略内化
tags:
- LLM agents
- harness distillation
- agent-as-harness
- fine-tuning
- trajectory learning
one_liner: 用 agent-as-harness 把优化 harness 的引导转为目标动作空间修正示范并微调，移除专用 harness 后成功率 23.3%→44.3%
practical_value: '- 业务中若存在按场景/人群/地区切换的规则引擎、多路召回/重排策略、风控或兜底 harness，可借鉴“专家 harness
  引导 + 修正 agent 生成目标动作空间示范 + SFT”的流程，把外部策略内化到统一模型，降低线上策略路由与维护成本。

  - 若优化 harness 与学生目标 harness 的动作空间或可用信息不一致，不要直接拿专家输出做监督；引入 bridging agent 在目标动作空间重写学生响应，是比
  code-as-harness 更稳的蒸馏方式。

  - 实验显示内化后移除专用 harness，模型成功率从 23.3% 升至 44.3%，超过保留原 harness 的 41.7%；可尝试用微调替代部分外部系统，减少推理延迟与策略冲突。

  - 对推荐/搜索 Agent 场景，可将不同场景的 query 改写、选品或 push 选词策略作为 expert harness，蒸馏到一个 base model，支持多场景统一服务，尤其适用于对话式购物/搜索助手中的策略简化。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Agent 性能依赖外部 harness，但最优 harness 因领域、实例、模型而异，部署时无法摆脱，且路由多个专用 harness 成本高。需要把优化 harness 在训练时的引导蒸馏到模型权重，使增益在统一目标 harness 下保留。

方法：提出 Harness-Zero，采用 agent-as-harness 思路。训练时，用领域/实例优化的 harness 引导一个“harnessing agent”，该 agent 在目标 harness 的动作空间内修正学生模型的响应，将专家 harness 的引导转化为训练示范。然后对修正后的轨迹进行微调，使模型内化 harness 诱导的行为，部署时移除专用 harness。

结果：在知识工作、工具使用、科学领域实验：① 对前沿 LLM，使用相同进化 harness 时 agent-as-harness 优于 code-as-harness；② 移除专用 harness 后，Harness-Zero 将基模型宏观平均任务成功率从 23.3% 提升至 44.3%，超过保留该 harness 的 41.7%；③ 在三个领域 28 个行为模式上平均恢复率 82.3%。
