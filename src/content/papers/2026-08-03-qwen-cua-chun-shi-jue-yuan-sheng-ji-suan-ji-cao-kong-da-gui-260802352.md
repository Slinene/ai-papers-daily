---
title: 'Qwen-CUA: Native Computer Use for (almost) Everything'
title_zh: Qwen-CUA：纯视觉原生计算机操控，大规模迭代训练攻坚长程任务
authors:
- Dunjie Lu
- Shuai Bai
- Tianyi Bai
- Sicheng Fan
- Chang Gao
- Jian Guan
- Feng Hu
- Mianqiu Huang
- Xingyang Huang
- Yizhen Jiang
affiliations:
- Qwen Team
- Xlang Lab
arxiv_id: '2608.02352'
url: https://arxiv.org/abs/2608.02352
pdf_url: https://arxiv.org/pdf/2608.02352
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 原生计算机使用Agent · 大规模RL+迭代训练
tags:
- Computer-Use Agent
- Reinforcement Learning
- Screenshot-Only
- Long-Horizon
- Mixture-of-Experts
- Iterative Training
one_liner: 仅凭截图与键鼠的原生计算机使用Agent Qwen-CUA，在八大基准上全面超越Qwen3.7并媲美GPT-5.5与Claude Opus 4.8
practical_value: '- **可验证交互式训练范式可迁移至电商/推荐Agent**：构建4万可验证任务 + 云端近10万vCPU并发环境完成大规模RL训练，该思路可直接用于训练电商商品操作用户界面Agent、客服流程自动化Agent。

  - **长上下文视觉管理trick值得直接复用**：保持20张活跃截图 + 每10步折叠旧截图，既保留近期视觉证据又维持前缀稳定以改进KV缓存重用，可迁移到需要长步骤的购物引导、商品浏览、多页面操作场景。

  - **迭代式数据刷新与RL任务校准**：每轮用当前模型分析失败案例，针对弱领域补充SFT数据、重校准RL任务（仅保留有提升空间的样本），可应用于推荐策略Agent的渐进式优化，避免过度重复无效训练。

  - **混合动作空间（GUI操作+Bash命令）**：实验证明混合操作能大幅缩短交互轮次，对电商自动化（如批量商品上下架、价格调整）可直接借鉴，但需注意当前模型的路由策略尚未完美，可配合显式路由监督提升实用性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
计算机使用Agent需在真实桌面与应用场景中完成长程、个性化工作，面临视觉上下文爆炸、环境交互昂贵、稀疏奖励等挑战。现有模型要么依赖DOM/API，要么在长任务中表现急剧下降，亟需一种仅凭像素感知、原生键鼠操控且能稳定处理长上下文的通用Agent。

**方法关键点**
- **纯视觉原生接口**：模型仅接收截图，输出键盘/鼠标事件，不依赖DOM树、无障碍元数据或任务专用API，跨应用无缝迁移。
- **长视觉上下文管理**：维持20张活跃截图，当历史超出预算时每10步折叠一组截图（用固定占位文本替换），保持前缀稳定以提升KV缓存复用；RL训练中同样使用该折叠策略，将完整轨迹切分为多个上下文有界片段，继承终端奖励。
- **大规模可验证训练**：基于阿里云ECS部署近10万vCPU、数万并发环境，构建约4万可验证任务（涵盖环境操作、用户交互、长程phase-state chaining），收集个性化专家长轨迹并补充动作级推理。
- **软自适应策略优化（SAPO）**：全轨迹共享终端奖励，采用温度控制的门函数取代传统截断重要性比率，在长轨迹、混合专家架构上更稳定。
- **迭代式训练**：每轮模型用于分析失败SFT查询和弱领域，刷新教师演示、补充人类轨迹、校准RL任务（仅保留当前策略能部分解决但非饱和的任务），然后重新训练，多轮提升。

**关键实验**
- **OSWorld-Verified**：Qwen-CUA得分86.2，超越Qwen3.7（73.3）、GPT-5.5（78.7）、Claude Opus 4.8（83.4）；万亿参数版Qwen-CUA-Max升至87.6。
- **OSWorld 2.0**：二元/部分完成度从Qwen3.7的2.5/22.5提升到18.5/48.4，Max版进一步提升至21.2/53.3。
- **RedTeamCUA安全**：攻击成功率从36.6降至16.4，同时任务成功率从70.5升至74.0。
- **混合工具效率**：加入Bash后Qwen-CUA平均回合数从63.6降至49.1，但任务成功率略降，揭示混合路由潜力。

**核心结论**
“原生计算机使用是覆盖几乎所有软件的足够通用接口，可结合代码与命令行形成混合Agent，取得通用性与效率的平衡。”
