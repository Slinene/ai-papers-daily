---
title: 'SplatLab: Autonomous Scientific Discovery for 3DGS Research'
title_zh: SplatLab：面向3DGS研究的自主科学发现系统
authors:
- Seemandhar Jain
- Manmohan Chandraker
affiliations:
- University of California San Diego
arxiv_id: '2610.30468'
url: https://arxiv.org/abs/2610.30468
pdf_url: https://arxiv.org/pdf/2610.30468
published: '2026-10-20'
collected: '2026-10-24'
category: Agent
direction: Agent 自主科研流水线 · 3DGS
tags:
- Autonomous Discovery
- 3DGS
- Agent
- LLM
- Elo Tournament
- Traceability
one_liner: SplatLab 实现端到端自主3DGS研究流水线，通过模块化变异、Elo锦标赛与实验绑定生成可追溯论文，PSNR最高提升3.78dB
practical_value: '- 可借鉴「已验证骨干 + 模块化插件变异」思路：在推荐模型迭代中，固定召回/排序主框架，只变异可插拔模块（如特征交叉、损失项、负采样），降低实验方差并快速定位增益来源。

  - Elo tournament 多候选评估机制可用于广告/推荐离线 A/B 前的高效筛选：对候选算法按多个数据集/指标进行配对比较并引入淘汰压力，比单独跑全量评估更省资源。

  - 实验数字绑定日志、未备份则不允许输出报告的做法，可直接迁移到实验平台，强制所有在线离线指标可追溯，避免口头结果。

  - 常驻 falsifier（压力测试）用于鲁棒性筛选：在电商大促、冷启动等极端场景下自动验证策略，淘汰脆弱候选。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
复现一篇 3DGS 论文需数周专家工程，现有自主研究系统受限于固定模板、低可执行性和弱可追踪性，且未在活跃 CV 子领域端到端验证。

**方法关键点**
- 在已验证复现基座上对插件进行变异，保证基线一致性；
- 八岛 cascaded-weight Elo 锦标赛，用 GPU PSNR 和 verbal-gradient 反馈选择候选；
- 常驻 falsifier 在候选失败时扣除 Elo，把压力测试生存能力纳入选择；
- 每个报告数字绑定到训练日志，若存在无日志支撑的声明，运行不得终止；
- 七类 3DGS taxonomy 包装 EVOLVE-BLOCK 标记，使变异模块可跨仓库迁移。

**关键结果**
PSNR 提升 +0.18 到 +3.78 dB，其中天文星云渲染 +3.78 dB（此前无 3DGS 方法）；研究周期从数月研究生工作量压缩至数天自主计算。
