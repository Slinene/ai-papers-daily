---
title: 'Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved
  Harnesses'
title_zh: Mage-VL-Cowork：从进化式 Harness 学习混合计算机使用的完整训练配方
authors:
- Xiaoyi Zhang
- Haoqing Wang
- Xinjie Zhang
- Xiang Ming
- Xing Wang
- Senqiao Yang
- Kaichen Zhang
- Zhaoyang Jia
- Andong Tan
- Xinjiang Wang
affiliations:
- Microsoft Mage Team
arxiv_id: '2610.40747'
url: https://arxiv.org/abs/2610.40747
pdf_url: https://arxiv.org/pdf/2610.40747
published: '2026-10-28'
collected: '2026-11-04'
category: Agent
direction: 计算机使用智能体 · 多阶段课程训练
tags:
- Computer Use Agent
- Hybrid GUI-Code
- Curriculum Learning
- RL
- Synthetic Data
- On-Device
one_liner: 4B混合计算机使用智能体，通过五阶段课程与技能化数据生成，在OSWorld-Verified达66.0%同尺寸SOTA
practical_value: '- 技能条件化数据生成可迁移：用「技能定义 + 可复用工作流 + 应用特定 preparer」替代逐任务构造，在电商 GUI 智能体（购物车、下单、订单查询等）中可显著降低合成数据成本，并规模化覆盖长尾技能。

  - 五阶段课程（midtraining → SFT → RL）值得借鉴：先做通用多模态对齐，再注入任务完成能力，最后用 RL 优化决策质量；对训练面向搜索/推荐业务的
  Agent 策略有直接参考价值。

  - 进化式教师 harness 提供高质量监督信号：不直接蒸馏默认大模型，而是为不同训练阶段定制教师策略，有助于提升小模型轨迹质量，可复用于蒸馏电商场景的 4B/7B
  级端侧助手。

  - 小参数模型也能逼近前沿性能：4B 在 OSWorld-Verified 达 66.0%，说明数据与课程设计比单纯堆参数更关键，对需要在端上部署低成本 Agent
  的业务是积极信号。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：混合计算机使用智能体需在单一策略内同时处理视觉 GUI 交互、代码与终端执行，但小参数模型性能不足，大规模训练数据构造昂贵，教师轨迹质量不稳定。  
**方法**：Mage-VL-Cowork 从通用多模态对齐 checkpoint 出发，经过 midtraining、SFT、RL 五个渐进阶段。数据侧用 Mage-CUA-Forge，以可复用的技能条件生成工作流和应用特定 preparer 取代逐任务构建，合成 293,806 个桌面/web 任务，覆盖 6,915 个技能，重复任务开销降低 82.6%。训练侧不直接蒸馏默认教师，而是进化教师 harness 并实例化专用 CUA harness，为不同阶段提供高质量轨迹与阶段特定监督。  
**结果**：4B 模型在 OSWorld-Verified 达 66.0%，低于人类 72.4%，但超越同尺寸及部分更大开源模型（如 Qwen3.5-27B 63.9%、EvoCUA-32B 56.7%），推理成本更高效，达到该参数规模 SOTA。
