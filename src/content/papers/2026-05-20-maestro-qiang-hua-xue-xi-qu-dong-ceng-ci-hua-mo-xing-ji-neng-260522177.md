---
title: 'Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles'
title_zh: Maestro：强化学习驱动层次化模型-技能集成编排
authors:
- Jinyang Wu
- Guocheng Zhai
- Ruihan Jin
- Yuhao Shen
- Zhengxi Lu
- Fan Zhang
- Haoran Luo
- Zheng Lian
- Zhengqi Wen
- Jianhua Tao
affiliations:
- Tsinghua University
- Zhejiang University
- The Chinese University of Hong Kong
- Nanyang Technological University
- Tongji University
arxiv_id: '2605.22177'
url: https://arxiv.org/abs/2605.22177
pdf_url: https://arxiv.org/pdf/2605.22177
published: '2026-05-20'
collected: '2026-05-22'
category: Agent
direction: 多模态Agent · 模型-技能强化学习编排
tags:
- Model-Skill Orchestration
- Reinforcement Learning
- Multimodal Agent
- GRPO
- Hierarchical Skills
- POMDP
one_liner: 用 4B 编排器通过 RL 动态组合冻结专家与层级技能，在多模态基准上超越 GPT‑5 并实现即插即用扩展
practical_value: '- 用 RL 训练编排策略取代硬编码路由：可借鉴到电商多智能体系统，让轻量级策略模型动态选择哪个 LLM 执行哪个工具，避免手工规则。

  - 层次化技能库压缩动作空间：将细粒度技能组织为两级，编排器只选粗粒度 Level‑1 技能，内部再用关键词或模型分类路由到 Level‑2，降低搜索复杂度，适合大规模工具集管理。

  - 即插即用扩展：新增专家模型和技能无需重新训练编排器，直接加入注册表即可提升性能，适合业务中不断引入新模型和工具的演进场景。

  - 结果驱动的稀疏奖励设计：仅用答案正确性 + 格式惩罚训练，无需步骤级监督，实践上易于实现。格式奖励保证多步协议合规，避免生成混乱轨迹。'
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
多模态任务的异质性要求不同类型专家的协同，但现有智能体框架通常依赖单一骨干模型和固定逻辑调用工具，无法利用不同模型与技能之间的互补优势。例如几何证明、医学报告解析和高分辨率目标计数需要截然不同的归纳偏置。同时，启发式检索或静态路由难以发现模型‑技能的潜在协同。为此，本文提出 MAESTRO，将异构多模态任务视为在层次化模型‑技能注册表上的序列决策问题，通过强化学习训练一个轻量级编排策略，动态组合冻结专家模型与两级技能库。

## 方法
- **POMDP 建模**：将任务分解为有限步的序列决策，动作空间包含内部思考、组合搜索（同时选择模型 `m` 与技能 `s`）和终止回答。状态由上下文历史累积。
- **层次化技能库**：五类 Level‑1 技能（几何、图表、计数、感知、科学）暴露给编排器，内部通过关键词或分类路由到八种 Level‑2 精细技能，压缩动作空间。
- **RL 训练**：使用 GRPO 优化策略，仅依赖结果奖励（答案是否正确）和格式奖励（协议标签闭合、步骤数匹配等），无需步骤级标注。训练时对观察 token 施加掩码，仅对策略生成的动作 token 计算损失。
- **专家模型池**：包括 GLM‑4.6V、Chart‑R1、Qwen3‑VL 等五个冻结专家，各具视觉、推理或领域专长。

## 实验与结果
在 10 个多模态基准（Geometry3K、ChartQA、Slake、VStar、HRBench 等）上评估。MAESTRO 的 4B 编排器平均准确率达 70.1%，超越 GPT‑5 (69.3%) 和 Gemini‑2.5‑Pro (68.7%)。尤其在 Geometry3K 达到 77.4%，远远高于 GPT‑4o 的 34.1%。在未训练的 OOD 数据集上同样表现出色，加入两个新专家和四个新技能后，无需重训即从 52.7% 提升至 59.5%，超过所有闭源基线。推理延迟仅 2.88 秒，token 消耗 648，效率远超“Think with Images”类方法。消融实验证明模型池和技能库缺一不可，格式奖励对维持多步协议至关重要。
