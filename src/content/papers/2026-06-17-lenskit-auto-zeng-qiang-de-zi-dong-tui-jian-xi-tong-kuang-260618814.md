---
title: LensKit-Auto
title_zh: LensKit-Auto：增强的自动推荐系统框架
authors:
- Max Breit
- Anass Amezian El Idrissi
- Rishikesh Giriraj Kulkarni
- Luca Quade
affiliations:
- University of Siegen
arxiv_id: '2606.18814'
url: https://arxiv.org/abs/2606.18814
pdf_url: https://arxiv.org/pdf/2606.18814
published: '2026-06-17'
collected: '2026-06-20'
category: RecSys
direction: 自动推荐系统工程与优化
tags:
- AutoRecSys
- Hyperparameter Optimization
- LensKit
- Tree Parzen Estimator
- Meta-learning
- Usability
one_liner: 升级框架兼容新版 LensKit，引入 TPE 优化与可视化，提升自动算法选择的工程易用性
practical_value: '- 将 Tree Parzen Estimator 用于推荐模型超参调优，比随机搜索更高效，可集成进电商推荐算法实验流水线

  - 黑盒易用性设计让非专家也能快速找到最佳算法，适合业务团队快速验证推荐方案

  - 可视化优化过程能帮助监控调参进展与模型性能，可借鉴实现类似的实验看板

  - 框架预留了元学习接口，未来可考虑用历史任务经验热启动新数据集搜索，降低冷启动成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

为不同数据集寻找最优推荐算法与超参数组合是工业界常见痛点，现有自动推荐系统工具 LensKit-Auto 虽能解决此问题，但已过时。本工作将其升级至新版 LensKit 底层，新增了 Tree Parzen Estimator（TPE）作为贝叶斯优化方法，补充了算法复用、优化过程可视化和完整文档，并准备了元学习所需数据集以支持未来扩展。

动机：推荐算法性能高度依赖数据特性，手动搜索效率低，需要自动化方案。
方法关键：
- 重构代码以适配 LensKit 0.14 新接口
- 集成 TPE 优化器，替代原有随机搜索与网格搜索，提升搜索效率
- 实现实验记录可视化，辅助用户观察调优轨迹
- 构建元数据集生成流水线，为后续元学习跨数据集推荐算法做准备
结果：更新后框架更易用、更现代，非专业人员可零代码为自定义数据集找到推荐算法，但论文主要展示工程增强而非量化性能提升。
