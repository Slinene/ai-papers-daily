---
title: Attacking and Defending Multi-Agent Collaborative Filtering Systems Through
  Connectivity
title_zh: 多智体协同过滤中连接性对攻击与防御的影响研究
authors:
- Anjun Hu
- Hanting Xie
- Saranya Govindan
- Jas Kandola
- Kurt Cutajar
affiliations:
- University of Oxford
- Amazon
arxiv_id: '2608.03272'
url: https://arxiv.org/abs/2608.03272
pdf_url: https://arxiv.org/pdf/2608.03272
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 多智体协同过滤 · 连接性安全评估
tags:
- Multi-Agent
- Collaborative Filtering
- Adversarial Attack
- Connectivity
- Defense
- LLM
one_liner: 系统揭示候选数与目录集中度如何不对称地调制攻击与防御效能，发现语义攻击更持久，静态图度量可预估风险
practical_value: '- **系统设计时监控连接度两极分化**：每轮推荐候选数 k 和物品目录重叠度 ρ 对攻击传播的影响呈角色不对称性。增加 k 会加速隐私提取的早期泄漏，但几乎不推高稳态泄露率；增大
  ρ 则推高物品侧污染，对用户侧影响非单调。在调整召回策略或扩量时，建议分用户/物品侧分别评估安全指标，避免单侧失守。

  - **红队测试优先采用语义攻击**：记忆更新步骤（LLM 重写摘要）会自然修正词法扰动，但完整保留语义注入。因此像 DrunkAgent（注入语义概念到物品记忆）比
  RecTextAttack（词法扰动）存活率更高。内部安全测试应重点检验语义注入的耐久性，而非仅防御提示词级别的扰动。

  - **防御部署需考虑角色隔离**：G-Safeguard 等 GNN 检测防御在用户侧有效，但在物品侧稀疏时失效 (ρ 小时毫无安全增益)。建议对不同角色训练独立的异常检测模型，或为物品
  Agent 设计无监督 (如 BlindGuard) 但针对度数不对称性优化的编码器。

  - **用静态图指标替代昂贵模拟做初步风险评估**：论文尝试用基于 SIS 模型的恢复感知一阶连接度预测器 (R_U, R_I) 来排序不同配置的风险，虽相关有限但节省资源。在工程上可先计算类似
  \(1-(1-α_I)^k / ((1-α_I)·k·γ+r)\) 的静态分数，快速筛查高危配置后再进行小规模攻击仿真。

  - **选用对齐良好的 LLM 并保留反思步骤**：较新模型 (Claude 4.5) 因丰富世界知识和安全对齐，在良性交互中能自我纠正记忆污染，降低攻击持久性。建议在
  Agent CF 中保留记忆更新后的反思/摘要步骤，并优先使用最新对齐 LLM 作为 Agent 大脑。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多智体协同过滤（Multi-Agent CF）将 LLM 驱动的用户与物品 Agent 通过网络化对话进行偏好精炼与推荐，其通信通道同时引入传播（如偏见扩散）与提取（如隐私泄露）两大威胁。连接性由系统设计（每轮推荐候选数 k）和历史数据（物品目录重叠度 ρ）共同决定，如何调制攻击效果尚未被系统研究。工作将通用 MAS 的攻击防御方法迁移到协同过滤，并在 AgentCF 上表征连接性的影响。

**方法关键点**  
- **双轴连接性**：k ∈ {1,2,3} 控制每用户每轮交互物品数，ρ = n_U/n_I ∈ {0.5,1,2} 控制目录集中度，独立操纵以观察效应。  
- **攻击重现**：传播型（CORBA 递归阻塞载荷、NetSafe 偏见注入）、提取型（MAMA 隐私字段提取、MASLeak 系统 IP 恢复）、双向型（TOMA、MASTER 先反推拓扑再扩散），均通过记忆表面注入或提示覆盖。  
- **防御重现**：G-Safeguard（GNN 有监督检测）、BlindGuard（无监督对比检测）、T-Guard（拓扑信任评估与三层访问控制）、M-Guard（提示泄露检测+分层监控+预硬化指令）。  
- **评测框架**：每轮 LLM 裁判判定非攻击方 Agent 的污染/泄露率，区分用户侧 (U) 和物品侧 (I)，并分解为暂态斜率 (tr) 与稳态均值 (ss)，记录不对称性。  

**关键结果**  
- 攻击成功率普遍呈 S 形增长并饱和，但用户与物品分区的增长曲线和稳态值存在显著角色不对称（F1, F2）。  
- 增大 k 加速提取攻击的早期泄漏，但稳态泄露率在 k≥2 后不再上升；ρ 对提取攻击几乎无影响。  
- 传播攻击：CORBA 的 DoS 率受 k 和 ρ 双重调制且非单调；NetSafe 的用户侧污染随 k 非单调，物品侧随 ρ 单调升高。  
- 语义攻击（DrunkAgent）比词法攻击（RecTextAttack）污染率高约3-5倍，因记忆摘要步骤会修正词法扰动却保留语义注入。  
- 防御：G-Safeguard 对用户侧有效，但对物品侧稀疏配置几乎无效；增加 k 或 ρ 往往提升防御的绝对安全增益，但规律因防御类型而异。  
- 静态预测指标（恢复感知一阶连接度）与部分攻击结果的相关性中等，需考虑高阶传播才能准确。  

**核心洞见**  
在 agentic CF 中，一个全局 ASR 不足以描述系统脆弱性——必须按角色分开、按暂态/稳态分开，且连接性因素需作为设计变量进入安全评估。
