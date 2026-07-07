---
title: 'TREK: Distill to Explore, Reinforce to Refine'
title_zh: TREK：蒸馏拓探索，强化精炼——面向困难提示的路由训练框架
authors:
- Yuanda Xu
- Zhengze Zhou
- Kayhan Behdin
- Jelena Markovic-Voronov
- Hejian Sang
- Xiaomin Li
- Wenhui Zhu
- Xinchen Du
- Aida Rahmattalabi
- Ran He
affiliations:
- LinkedIn Corporation
- Harvard University
- Georgia Institute of Technology
arxiv_id: '2607.05339'
url: https://arxiv.org/abs/2607.05339
pdf_url: https://arxiv.org/pdf/2607.05339
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: RL训练中的困难探索支持扩展
tags:
- GRPO
- Forward-KL
- Distillation
- Exploration
- Reinforcement Learning
- Agent
one_liner: 用教师或自反提案识别并巩固困难提示，以正向KL先行扩展学生支持，再交还GRPO精炼
practical_value: '- **困难样本识别与路由**：在电商搜索/推荐中，同样存在模型反复生成相似低分结果而不探索新模式的“支持塌陷”；可借鉴TREK的硬提示阈值路由（按学生pass
  rate），仅在困难查询上触发热模型或自反推理来生成候选解决路径。

  - **自反思提案生成**：无需外部强模型，仅对当前模型增加推理时上下文（如失败记忆、环境反馈）即可产生优质探索轨迹；推荐系统中可让模型基于前序无效推荐生成反思推词或替代匹配路径，作为蒸馏素材。

  - **正向KL巩固而非模仿**：选择教师/自反轨迹中与学生当前分布距离最近（trimmed NLL）的样本进行短时正向KL微调，避免全盘模仿，保证探索到的模式能快速进入学生采样空间；在推荐Agent的规划或查询改写任务中，可用此方法将RL探索不到的成功交互路径固化。

  - **阶段性训练流水线**：硬提示挖掘→提案筛选→短正向KL热身→常规GRPO，该解耦设计可插入现有在线RL训练流程，特别适用于搜索多轮交互、对话式推荐的稀疏奖励场景，用少量教师查询换取早期训练效率大幅提升。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
标准GRPO在强化学习中依赖学生策略自身的采样，当遇到困难提示时，学生反复生成错误轨迹，奖励信号虽可判定正确解，但正确解模式根本不在采样范围内。这种“探索支持不足”是GRPO在高难度任务上停滞的关键瓶颈。已有蒸馏方法侧重对已有轨迹的信用分配，并未解决最优解从未被采样的根本问题。

**方法关键点**  
- **困难提示识别**：用学生策略多次采样估计pass rate，将低pass rate提示标记为困难。  
- **提案生成与筛选**：对困难提示，调用提案源（外部强模型、白盒教师或同模型加推理上下文）生成候选解答，仅保留验证通过的轨迹，并计算每个轨迹与学生当前分布的修剪长度归一化NLL（trimmed NLL），选择最靠近学生的top-r条轨迹。  
- **正向KL支持扩展**：对筛选出的学生邻近验证轨迹执行短时间正向KL最小化（即最大化学生对其的对数似然），将成功模式拉入学生策略的支持集，但不过分向教师分布坍缩。  
- **返回GRPO精炼**：完成正向KL热身之后，将引导学生返回标准GRPO训练，按正常采样进行群组优势强化，逐步优化被探索到的模式。  
整个流程是阶段式的：硬提示挖掘→提案选择→短正向KL巩固→常规GRPO，无需永久改变学生解码接口。  

**关键实验**  
- **数学推理**：在AIME 2024/2025上，Qwen3系列（1.7B/8B/14B）使用DeepSeek-V4作为外部提案，TREK全面优于直接GRPO。Qwen3-8B在AIME 2025上从36.9%提升至40.3%，AIME 2024从47.9%提升至51.1%（avg@16）。自反思上下文变体（仅用同模型+失败教训）同样稳定提升，如8B分别达38.5%和49.6%，验证了无需外部教师的可行性。  
- **Agent任务**：在ALFWorld上，GRPO仅75.8%，TREK（DeepSeek-V4）提升至82.8%，自反思变体也达80.4%；ScienceWorld从12.5%翻倍至26.7%。困难任务子类（如Examine in Light、Heat & Place）收益最集中，表明支持扩展针对性极强。  
- **训练效率**：TREK在Agent任务中早期训练大幅加速，例如自反思变体在ALFWorld约20步即达60%成功率，而原GRPO需5倍步数。  

**核心启示**  
“蒸馏的应用不应局限于模仿或信用分配，更应被视为拓展学生探索空间的工具；只用验证通过、且学生能力所及的轨迹来短暂牵引，剩余的交给奖励驱动的RL。”
