---
title: 'DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation'
title_zh: DuoMem：双空间蒸馏赋能边端记忆智能体
authors:
- Peyman Hosseini
- Ondrej Bohdal
- Ahmed Alajrami
- Andrea Maracani
- Ignacio Castro
- Matthew Purver
- Mete Ozay
- Savas Ozkan
- Taha Ceritli
affiliations:
- Samsung R&D Institute UK
- Queen Mary University of London
arxiv_id: '2606.29961'
url: https://arxiv.org/abs/2606.29961
pdf_url: https://arxiv.org/pdf/2606.29961
published: '2026-06-28'
collected: '2026-07-04'
category: Agent
direction: 智能体记忆蒸馏 · 边端部署
tags:
- Memory Agents
- Knowledge Distillation
- LoRA
- On-Device
- Dual-Space Distillation
- ALFWorld
one_liner: 通过上下文与参数双空间蒸馏，将大模型过程记忆能力迁移至小模型，4B模型成功率从4.3%升至77.9%，速度提升3倍
practical_value: '- **上下文蒸馏可迁移至对话式推荐**：用大模型为历史交互生成优质推理记忆（如用户偏好演化链），将其作为前缀注入小模型，提升多轮推荐一致性。

  - **参数蒸馏成本极低**：仅用教师成功轨迹微调LoRA，参数增量<10M，可快速适配现有电商或搜索智能体的规划模块。

  - **双空间协同效果突出**：单独上下文或参数蒸馏效果有限，两者合并产生互补增益；在构建推荐Agent时，可同时注入教师记忆并微调编解码器。

  - **边端实时性提升**：蒸馏后小模型推理速度大幅提高，适合手机端或低延迟场景下的个性化推荐回复生成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基于LLM的智能体在多步交互任务中表现卓越，但依赖大模型、长上下文与多次推理，难以部署到资源受限设备。

**方法**：提出DuoMem双空间蒸馏框架，将大型教师模型的过程性任务解决能力迁移到小型学生模型。
1. **上下文空间蒸馏**：用教师生成的高质量过程记忆（如过去动作序列、观察）替换学生自身生成的记忆，预置于输入序列前，直接改善学生决策上下文。
2. **参数空间蒸馏**：收集教师成功生成的完整轨迹，微调学生模型的轻量LoRA适配器，使其模仿教师的行为分布。

**结果**：在具身决策基准ALFWorld上，DuoMem将4B学生模型的成功率从4.3%提升至77.9%，接近72B教师模型的87.1%；仅增加不到10M可训练参数，预计算记忆仅需数MB。同时，增强后的4B模型端到端任务完成时间比教师快3倍以上。消融实验表明，两种蒸馏轴互补，组合效果远超单独使用。
