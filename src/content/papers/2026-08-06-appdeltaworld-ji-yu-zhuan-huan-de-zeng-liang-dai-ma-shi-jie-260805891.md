---
title: 'AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents'
title_zh: AppDeltaWorld：基于转换的增量代码世界模型用于移动GUI智能体
authors:
- Weikai Xu
- Yunren Feng
- Haoxiang Lei
- Kun Huang
- Yuxuan Liu
- Kang Zhao
- Xiaolin Hu
- Shuo Shang
- Bo An
affiliations:
- Nanyang Technological University
- University of Electronic Science and Technology of China
- Gaoling School of Artificial Intelligence, Renmin University of China
- Xiamen University
arxiv_id: '2608.05891'
url: https://arxiv.org/abs/2608.05891
pdf_url: https://arxiv.org/pdf/2608.05891
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 增量代码世界模型用于GUI Agent训练
tags:
- Mobile GUI Agents
- World Model
- Delta Code
- HTML Generation
- SFT Data Construction
- Test-Time RL
one_liner: 提出增量代码世界模型，将GUI变化预测为可执行HTML更新，实现高保真模拟和策略自适应提升
practical_value: '- 若需为电商App构建GUI自动化测试或用户模拟Agent，可利用AppDeltaWorld生成高保真合成轨迹，降低对真实交互数据的依赖。

  - 过渡基约束与两层HTML生成思路可复用于生成推荐界面模拟环境，快速构建大规模交互训练数据。

  - 测试时强化学习通过世界模型在线微调策略，可为生产环境中的Agent探索提供安全、低成本的试错途径。

  - Code2World评估机制可指导推荐系统界面生成模块的优化，提升生成结果的布局合理性和元素复原度。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：移动GUI Agent依赖真实交互轨迹训练，但敏感App和隐私操作导致数据稀缺，现有模拟环境扩展成本高，且已有世界模型存在生成不稳定、模态覆盖有限、动作-状态转换逻辑不一致等问题。

**方法**：提出AppDeltaWorld，一种过渡基增量代码世界模型，将下一GUI预测为可达的代码更新而非图像或文本。模型先根据动作约束检索App专属一级HTML参考，然后基于当前屏幕、动作、预测的下一屏文本和检索结构，生成二级可执行HTML，并将生成的视觉资源插入图像槽，经浏览器渲染得到最终界面。

**结果**：在CMGUIBench-500的Code2World评估下，AppDeltaWorld保真度最优，结构和UI元素重建显著优于纯图像和纯代码基线。结合过滤闭环SFT数据与公开监督训练的AppDeltaAgent，在AndroidLens达到SOTA，MobileGym和MobileWorld持续提升。基于世界模型的测试时强化学习进一步实现策略自适应，无需额外真实App交互即获增益。
