---
title: 'Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities
  in LLM Agents'
title_zh: 扫清迷雾：在 LLM Agent 中植入与精调主动探索能力
authors:
- Zhizhao Guan
- Chen Huang
- Ziming Liu
- Hongru Liang
- Wenqiang Lei
- See-Kiong Ng
- Tat-Seng Chua
- Anthony G Cohn
affiliations:
- Sichuan University
- National University of Singapore
- University of Leeds
- Engineering Research Center of Machine Learning and Industry Intelligence
arxiv_id: '2608.14339'
url: https://arxiv.org/abs/2608.14339
pdf_url: https://arxiv.org/pdf/2608.14339
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: LLM Agent 主动探索训练
tags:
- LLM Agent
- Proactive Exploration
- RL
- DPO
- Tree-structured Context
- WebShop
one_liner: 通过探索性数据构建和对比信号引导强化学习，大幅提升 LLM Agent 在多轮交互任务中的主动探索与决策能力
practical_value: '- **电商购物 Agent 的训练数据要包含探索轨迹**：标准人类专家轨迹中探索动作几乎为 0（如 WebShop 中 Next/Back
  仅 0.1%），导致 SFT 后的 Agent 只会被动执行、不会翻页回溯。可以用强 LLM 配合树结构上下文，合成包含主动搜索、回溯、分支尝试的探索丰富轨迹，作为
  SFT 初始化数据。

  - **用树结构管理会话历史，避免长程任务中的上下文迷失**：在电商搜索、多轮比价等场景，线性的 action-observation 历史会混淆有效路径与废弃分支。借鉴论文中的
  tree-structured history + cognitive notes，在 Agent 内部显式维护分支、回溯指针和状态标注（如 [DEAD END]、[SUB-OPTIMAL]），能显著提升策略的探索质量。

  - **用对比偏好对 + DPO 校准「探索 vs 执行」的决策边界**：在关键状态上，采样学生动作与参考动作，通过 MC rollout 估计各自未来回报，过滤小差距对后做
  DPO。这套机制可以迁移到推荐/搜索 Agent 的策略优化，让模型学会何时继续浏览、何时停止探索并做出购买/点击决策。

  - **探索效率评估与难度分层分析**：论文提出的 Eff = EE - WE 指标（有效探索减浪费探索）以及按任务难度分层统计探索强度，可用于业务中诊断 Agent
  是否在做有效信息获取，而不是盲目增加交互步数。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
LLM Agent 在在线购物等多轮交互任务中，需要主动探索环境以获取信息来支撑未来决策，但现有 SFT+RL 范式存在两个瓶颈：标准专家轨迹剥离了探索步骤（hindsight bias），SFT 后 Agent 缺乏探索倾向，导致 RL 阶段难以采样到探索行为（exploration collapse）。多数方法最终收敛到局部最优，过早选择次优商品或方案。

**方法关键点**  
- **探索性数据构建**：用树结构上下文建模（Tree-Structured Context Modeling）让 GPT-4o 老师生成包含自主回溯、分支创建和认知笔记的探索丰富轨迹。认知笔记缓存环境事实、记录分支状态、编码学到的规则、支持假设修正与检查点恢复。  
- **数据筛选**：对每个任务采样多条轨迹，用长度惩罚奖励 `r_final = r(h) - n·γ` 选出高效探索轨迹，只保留成功轨迹构建 SFT 数据集，初始化学生模型。  
- **RL with Contrastive Signal Guidance**：在参考轨迹的状态上，采样学生动作与参考动作构成对比对，用 forward-only MC rollout 估计每个动作的未来回报，保留回报差距大于阈值 τ_m 的对，用 DPO 优化策略，校准“何时探索、何时执行”的决策边界。  

**关键实验**  
在 WebShop、InterCode-SQL、ScienceWorld 三个基准上，SAFARI 相比最佳基线，任务成功率平均提升约 10%-15%，探索分数平均提升约 8%-18%。8B 学生模型性能可媲美甚至超过 GPT-4o 老师。消融显示树结构上下文和认知笔记贡献显著，去除后 TP 分别下降 9.66% 和 5.03%。探索效率分析表明 SAFARI 能有效抑制浪费探索，同时提升有效探索；探索强度随任务难度自适应增加，在困难任务上增益最大。

**最值得记住的一句话**  
主动探索不是盲目尝试，而是通过结构化的上下文记忆和对比式偏好优化，让 Agent 学会何时探索、何时执行。
