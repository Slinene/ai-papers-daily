---
title: 'ToolRec: Calibrated Preference Alignment for Query Recommendation in On-Device
  Assistants'
title_zh: ToolRec：面向设备助手的校准偏好对齐查询推荐
authors:
- Zihan Luo
- Lingkui Chen
- Ruike Zhang
- Hong Huang
- Boyang Zhang
- Ziniu Chen
- Lizhong Wang
affiliations:
- Huazhong University of Science and Technology
- OPPO AI Center
arxiv_id: '2606.08466'
url: https://arxiv.org/abs/2606.08466
pdf_url: https://arxiv.org/pdf/2606.08466
published: '2026-06-07'
collected: '2026-06-09'
category: QueryRec
direction: 查询推荐 · 偏好对齐 · 点击率优化
tags:
- Query Recommendation
- Preference Alignment
- On-Device Assistant
- KTO
- Calibration
one_liner: 提出双层校准机制与加权KTO，在OPPO小布上显著提升工具调用查询的CTR和总点击量
practical_value: '- **双层点击校准可迁移至电商行为建模**：根据用户活跃度（浏览/加购/购买频次）分桶校准点击权重，减少沉默用户噪声；同时对工具型行为（如领券、收藏、直达搜索）提权，强化可执行动作的引导，提升转化率。

  - **样本级加权KTO简化偏好对齐**：无需构造正负样本对，直接利用隐式反馈（点击/未点击）和校准权重优化LLM，适合电商推荐中大量单点隐式反馈的排序或查询生成场景。

  - **工具检索增强的查询生成范式**：预先构建系统工具库（如加购、下单、查物流），在生成推荐查询或广告文案时，通过检索确保可执行性，避免“不可点击”的无效推荐，可直接嵌入对话Agent或多任务推荐系统。

  - **在线A/B验证的实用迭代思路**：工作已在亿级月活平台验证，证明在校准后的偏好信号上做对齐，能同时提升CTR和总点击量，为相关业务提供了可直接参考的离在线优化路径。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有LLM查询推荐对齐方法多针对通用聊天，而移动助手场景下用户期望快速调用系统工具（如打开应用、设置闹钟）。直接从点击日志对齐会引入噪声：不同用户活跃度导致点击可靠性差异，且工具调用型查询未被强调。

**方法**：提出ToolRec框架。首先构建包含708个系统工具的SysToolKit，并用上下文感知检索保障推荐查询的可执行性。然后设计双层校准机制：1）按用户活跃度（低/中/高）分桶校准点击信号权重，抑制低活跃度用户的随机点击噪声；2）对能触发系统工具的查询点击信号进行上加权。最后采用样本级加权KTO损失进行偏好对齐，避免构造负样本对，直接利用校准后的信号优化模型。

**结果**：在OPPO小布（月活超1.5亿）上在线A/B测试，相较于SFT、DPO等基线，ToolRec在CTR和总点击量上均有显著提升，同时保证查询的高相关性。
