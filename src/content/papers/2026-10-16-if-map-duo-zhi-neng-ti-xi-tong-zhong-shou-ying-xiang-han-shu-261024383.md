---
title: 'IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems'
title_zh: IF-MAP：多智能体系统中受影响函数启发的智能体优先级排序
authors:
- Jie Mao
- Pingchen Lu
- Zikun Qu
- Jiahang Sun
- Xiangyi Wang
- Zhiwei Shang
- Zhiyong Wang
- Guojun Xiong
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Harbin Institute of Technology
- School of Engineering and Applied Sciences, Harvard University
arxiv_id: '2610.24383'
url: https://arxiv.org/abs/2610.24383
pdf_url: https://arxiv.org/pdf/2610.24383
published: '2026-10-16'
collected: '2026-10-24'
category: MultiAgent
direction: 多智能体优先级排序与黑盒优化
tags:
- Multi-agent Systems
- Influence Function
- Agent Prioritization
- Prompt Optimization
- Black-box Optimization
one_liner: 提出 IF-MAP 黑盒方法，通过提示扰动与局部响应模型估计 agent 改进潜力，为多智能体系统确定优化优先级
practical_value: '- 在多 Agent 搜索/推荐链路（如 query 改写、召回、排序、文案生成各由一个 LLM agent 负责）中，用 IF-MAP
  式探测确定高杠杆 agent：对每个 agent 的 prompt 做少量语义扰动，记录端到端指标变化，优先调优影响最大的节点，避免平均分配算力

  - 不需要访问模型参数/梯度，适合采用 API 或第三方模型的业务；只依赖 prompt embedding 与最终 loss，可在生产环境旁路低成本采样，不影响线上

  - 拟合正则化局部响应模型，用系数范数做打分，可作为轻量级优先级评估器；工程上可在小样本上快速执行，并将得到的优先级迁移到不同底层模型（论文显示跨模型有效），适合先在小模型上探测、再决定生产模型升级顺序

  - 成本收益：相比全量优化所有 agent，该策略可节省 35–74% token，同时提升宏观指标，适合需要频繁迭代 prompt 或替换模型的团队'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM-based 多智能体系统里，同时改进所有 agent 成本过高，需要判断优先改进哪个 agent 才能最大化系统级收益。传统的失败归因只能说明责任，不能直接反映改进潜力。

方法关键点：IF-MAP 受影响函数启发，对每个 agent 在受控语义 prompt 扰动下测量端到端损失变化；在低维 prompt-embedding 子空间中拟合带正则的局部响应模型；用响应范数作为 agent 优先级分数。整个过程黑盒，无需模型参数或梯度。得到优先级后，可用于 prompt 优化或模型升级。

关键结果：在六个多智能体工作流（代码生成、问答、数学推理）上评估。用相同优先级做 prompt 优化，宏观平均增益 3.81 个百分点，高于均匀选择 agent 的 1.85；在五个目标模型上升级所选 agent 获得 7.62–16.42 个百分点增益，优于均匀选择的 3.81–8.62。尽管有探测成本，相比全量优化可减少 Qwen3-8B 74.2%、DeepSeek-V3.2 35.2% token，且升级目标模型 token 减少 63.6–64.9%。
