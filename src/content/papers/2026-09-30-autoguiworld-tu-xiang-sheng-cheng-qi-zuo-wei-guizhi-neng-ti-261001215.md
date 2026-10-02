---
title: 'AutoGUIWorld: Image Generators as Visual World Models for GUI Agent'
title_zh: AutoGUIWorld：图像生成器作为GUI智能体的视觉世界模型
authors:
- Cheng Yang
- Yifan Wu
- Yutao Huang
- Zhaohua Zhang
- Beiduo Chen
- Muxi Chen
- Chenchen Zhao
- Hexuan Deng
- Haolin Yang
- Geyuan Zhu
affiliations:
- Hunyuan AI Data Team
arxiv_id: '2610.01215'
url: https://arxiv.org/abs/2610.01215
pdf_url: https://arxiv.org/pdf/2610.01215
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: GUI Agent 数据合成与训练
tags:
- GUI Agent
- Trajectory Generation
- Image Generation
- Visual World Model
- Fine-tuning
one_liner: 利用图像生成器与规划器合成无环境依赖的GUI交互轨迹，提升GUI智能体真实任务性能
practical_value: '- 在电商/推荐场景中，可借鉴“无环境数据合成”思路：用图像生成器模拟商品详情页、购物车、下单等界面状态变化，低成本生成多步交互轨迹，用于训练购物助手或导购Agent，避免依赖真实App部署。

  - 规划器+图像生成器迭代编辑的方法可生成多样化的用户旅程模拟数据，覆盖冷启动场景或长尾界面状态，增强Agent对异常布局、少见控件的泛化能力。

  - 动作接地（action grounding）和过渡级质量过滤是关键步骤：在合成数据中显式校验动作坐标与视觉变化的对应关系，保证轨迹可用性，类似推荐系统中对合成样本做标注质量校验。

  - 微调大模型（如Qwen3.5-35B-A3B）在真实基准上的显著提升（OSWorld +7.8pt, ScienceBoard +18.2pt）表明合成轨迹对Agent有效，电商领域可尝试用类似方法微调多模态模型处理商品页面操作任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：GUI agent 依赖大量高质量交互轨迹学习软件环境对动作的响应，但真实环境采集受限于应用多样性、界面状态覆盖和部署成本，扩展性差。

**方法关键点**：AutoGUIWorld 结合图像生成器的视觉先验与规划器的任务知识，在部署实际软件的情况下合成交互轨迹。首先从结构化规范（OS上下文、视觉外观、界面状态）采样初始 GUI 场景，用图像生成器生成 seed 截图；接着规划器指定原子动作及其预期的视觉后果，图像生成器迭代编辑当前截图生成后续观察，形成截图-动作-截图序列。通过动作接地（校验动作坐标与视觉变化）和过渡级质量过滤，最终得到 79,266 个带空间标注的 step-level 训练样本，覆盖 Ubuntu、Windows、macOS 和 Chrome 四个平台。

**关键结果**：用 AutoGUIWorld 轨迹微调 Qwen3.5-35B-A3B 后，在 OSWorld 上的平均任务分数从 33.0% 提升至 40.8%，在 ScienceBoard 上的任务成功率从 14.0% 提升至 32.2%，表明生成轨迹有效提升 GUI agent 在真实桌面与科学任务上的表现。
