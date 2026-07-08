---
title: 'UI-MOPD: Multi-Platform On-Policy Distillation for Continual GUI Agent Learning'
title_zh: UI-MOPD：面向持续GUI智能体学习的多平台在线蒸馏方法
authors:
- Niu Lian
- Alan Chen
- Zhehao Yu
- Chengzhen Duan
- Fazhan Liu
- Hui Liu
- Pei Fu
- Jian Luan
- Yaowei Wang
- Shu-Tao Xia
affiliations:
- Tsinghua Shenzhen International Graduate School, Tsinghua University
- Xiaomi
- Harbin Institute of Technology, Shenzhen
- Zhejiang University
- Peng Cheng Laboratory
arxiv_id: '2607.04425'
url: https://arxiv.org/abs/2607.04425
pdf_url: https://arxiv.org/pdf/2607.04425
published: '2026-07-04'
collected: '2026-07-08'
category: Agent
direction: GUI Agent 持续学习与跨平台适应
tags:
- GUI Agent
- Continual Learning
- On-Policy Distillation
- Multi-Platform
- Catastrophic Forgetting
one_liner: 提出多教师在线蒸馏持续学习框架，动态选择平台教师，缓解跨平台GUI智能体的灾难性遗忘与行为冲突
practical_value: '- 电商多端（APP/PC/小程序）自动化运营 Agent 可采用多教师在线蒸馏，避免不同平台操作惯例冲突，保留端侧特有行为模式，减少为每端单独维护模型的成本。

  - 平台条件蒸馏通过环境信号动态路由选择特定教师，能使统一策略模型灵活适应多端环境，适合搜索推荐系统中跨端交互流程的自动化。

  - 构建跨平台操作轨迹数据时，可借鉴 Uni-GUI 的收集策略（如多源采集、平台覆盖、操作可执行性过滤），提升训练数据质量与平台泛化性。

  - 策略回放机制可迁移至电商 Agent 的持续学习中，防止新增端侧任务时旧端侧能力的灾难性遗忘。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态基础模型推动 GUI 智能体从单平台向跨平台交互发展，但面临高质量跨平台轨迹数据稀缺、不同平台交互惯例冲突导致联合训练或持续训练中出现行为模式混合与灾难性遗忘。
**方法**：构建了高质量跨平台 GUI 数据集 Uni-GUI，并提出 UI-MOPD——首个将多教师在线蒸馏融入持续学习的 GUI 智能体框架。新平台到来时，UI-MOPD 依据当前环境动态选择平台专属教师，通过平台条件蒸馏将平台特定的行为先验传递给共享策略，并利用策略回放保留旧平台能力，避免参数合并或混合 SFT 造成的行为冲突。
**结果**：在桌面 OSWorld 和移动端 MobileWorld 上，UI-MOPD 分别取得 38.2% 和 12.0% 的任务成功率，显著优于模型合并与混合训练基线，有效平衡了跨平台能力保留与新平台适应。
