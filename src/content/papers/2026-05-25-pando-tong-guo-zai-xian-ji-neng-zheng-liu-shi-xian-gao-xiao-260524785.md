---
title: 'PANDO: Efficient Multimodal AI Agents via Online Skill Distillation'
title_zh: PANDO：通过在线技能蒸馏实现高效多模态AI智能体
authors:
- Yubo Li
- Yidi Miao
- Yuntian Shen
- Yuxin Liu
affiliations:
- Carnegie Mellon University
arxiv_id: '2605.24785'
url: https://arxiv.org/abs/2605.24785
pdf_url: https://arxiv.org/pdf/2605.24785
published: '2026-05-25'
collected: '2026-05-30'
category: Agent
direction: 多模态Web Agent · 在线技能学习与推理效率
tags:
- skill_distillation
- token_efficiency
- web_agent
- online_learning
- VisualWebArena
- cache_aware_prompting
one_liner: 单一rollout在线技能蒸馏框架，以结构化技能库配合缓存感知路由，使Web Agent在提升成功率的同时大幅降低token消耗。
practical_value: '- **结构化技能库用于重复子任务**：将操作经验提炼为规则（模式触发）和参数化例程（如 apply_price_filter(min,max)），用确定性的关键词匹配替代嵌入检索，可直接借鉴到电商自动化流程（自动比价、筛选排序），减少Agent反复规划的开销。

  - **分层路由与视觉压缩降低推理成本**：仅对规划/反思调用强模型（如Claude Opus），高频执行由廉价模型（如GPT-5.2）完成，并压缩截图分辨率，适合商品详情页抓取、浏览器自动化等视觉输入密集的场景，在保证准确率的同时控制API成本。

  - **在线学习与置信度降级保持技能库健康**：采用Beta分布估计技能置信度，失败多次后自动降级并加入黑名单，阻止“发现-失败-再发现”的死循环，这一机制可迁移到推荐系统的在线策略更新，避免陈旧或低效策略的持续消耗。

  - **缓存感知的提示布局提高KV-cache命中**：将稳定的指令、工具Schema、技能摘要放在抖动较小的前缀位置，配合Anthropic的cache_control，使整个任务流的缓存利用率从约10%提升到72%，对于生产环境下长链路Agent降低延迟和成本有直接参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前多模态Web Agent的性能提升主要依赖增加推理token（如多轮rollout、验证器、离线工具发现），导致推理成本高昂、延迟增加。作者分析了VisualWebArena上的轨迹，发现重复动作循环、离线发现成本未被计入以及提示缓存重用率低（<11%）是主要的效率瓶颈，从而提出核心问题：能否让Agent在积累经验的过程中变得更便宜？

**方法关键点**：
- **结构化技能库**：包含基于模式触发的规则和参数化的例程，使用关键词精确匹配检索，而非向量搜索，保证库的可审计性和缓存稳定性。
- **在线蒸馏与降级**：在测试流中提取成功子轨迹作为候选技能，用Beta分布的置信度（通过/失败次数）估计可靠性；设置降级阈值（θ=0.5，最低触发次数3）和极性对合并（如最贵↔最便宜合并为同一函数加方向参数），防止库单调膨胀。
- **分层路由与视觉压缩**：将昂贵模型（Claude Opus）用于规划和反思，廉价模型（GPT-5.2）执行具体动作；对截图下采样和ROI裁剪，减少视觉token。
- **缓存感知的提示布局**：将稳定指令、技能索引放在前缀位置，配合API缓存功能，大幅提高KV cache利用率。

**实验结果**：在VisualWebArena全部910个任务上，PANDO达到58.3%的成功率，比SGV（54.0%）高+4.3pp，比复现的WALT（45.2%）高+13.1pp；同时平均每任务仅用115K tokens，分别比SGV和WALT节省58%和61%的token消耗。消融实验中，技能学习组件贡献了主要成功率提升（+18.7pp），而路由/压缩/缓存优化在几乎不损失成功率的前提下额外减少30K tokens。引入的行动重复率（ARR）降至9.1%，步骤开销比（SOR）为1.8×，提示缓存利用率达72.4%，均显著优于基线。随任务流进行，技能命中率上升，平均步数和token消耗递减，表明系统确实实现了“越用越高效”的目标。

**核心启示**：将过去的token开销转化为可复用的“资本”——通过在线蒸馏形成持久化的技能库，并配合架构层面的效率设计，可以让Agent在性能与成本之间达成更优的平衡。
