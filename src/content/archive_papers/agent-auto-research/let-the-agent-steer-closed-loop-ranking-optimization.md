---
title: "Let the Agent Steer: Closed-Loop Ranking Optimization via Influence Exchange"
authors: Yin Cheng, Liao Zhou, Xiyu Liang, Dihao Luo, …, Jian Dong, Andy Zhang (Sortify Team, 10 人)
affiliation: Shopee
date: 2026-03
venue: arXiv (Sortify Technical Report)
topic: agent-auto-research
topic_name: Agent Auto-Research
topic_icon: 🔬
idea: 把电商排序调参重构为持续的「影响力交换」，交给一个全自治的 LLM 智能体闭环优化。关键不是让 LLM 直接调那 7 个排序权重，而是让它当「二阶元控制器」：站在更高一层校准「线下指标↔线上效果」的迁移映射(Belief 通道)和约束惩罚强度(Preference 通道)——两者按 Savage 主观期望效用公理正交解耦(信念 vs 偏好)，底层用 Optuna TPE 搜参，Memory DB 跨轮沉淀经验，4 小时一轮全程无人。整个项目(9.8 万行代码+30 轮实验+本报告)号称由一人指挥 AI agent 群完成，是「AI 造 AI」的范式样本。
paperUrl: https://arxiv.org/abs/2603.27765
codeUrl: null
tags:
- Autonomous Agent
- LLM Meta-Controller
- Closed-Loop Optimization
- Ranking Tuning
- AI-Generating-AI
unverified: false
detail:
  contribution: |
    提出 Sortify——一个部署在 Shopee 的全自治 LLM 闭环排序调参系统，把排序优化重构为「影响力交换」问题。核心三件套：(1) 双通道自校准——Belief 通道(LMS 回归 + LLM 离散跳变)校准线下→线上迁移映射，Preference 通道(非对称乘法更新)调约束惩罚，依 Savage SEU 公理把「信念误差(epistemic)」与「偏好误差(axiological)」正交解耦；(2) LLM 元控制器——二阶控制，只动 framework 级元参数(截距/惩罚乘子)不动底层 7 维参数 θ，读 20 轮历史做证据驱动反思；(3) 7 表持久 Memory DB 跨轮沉淀。还提出 Influence Share——可分解、和为 100% 的排序归因指标，替代不可分解的 Kendall τ。Country B 冷启动走完全生命周期到推全量，7 天 A/B GMV/UU +4.15%、Ads Revenue +3.58%。
  background: |
    工业排序公式是一堆可调权重的加权组合，标准调参流程(线下搜参→线上 A/B→人工决策)有三个结构性顽疾：① 线下↔线上迁移漂移——Country A 实测 R2 线下 I_gmv +18.2% 但线上 GMV −3.6%，R7 线下 +41.6% 才换来线上 +9.2%，且不同业务指标的乐观偏差各不相同，单一校准系数修不过来；② 诊断信号纠缠——线上掉点时分不清是「预测错了(映射偏乐观)」还是「约束设松了」，二者需要相反的修正；③ 经验不沉淀——每轮从零开始的「土拨鼠日」效应。作者把调参重新定义为业务因子(自然相关性/广告出价/价格力)之间抢「影响力份额」的交换问题，并主张这三个痛点必须在架构层而非调参层解决。
  method: |
    三层闭环。Layer1 人类设目标/约束；Layer2(核心)=双通道+LLM 元控制器；Layer3=Optuna TPE(5000 trials×25 workers 搜 7 维参数)。Belief 通道：对每个指标对建线性迁移 û_online=α·u_offline+β，双速更新——LMS(η=0.2)做平滑渐进校准(突变需~15 轮收敛)，LLM 当从 20 轮历史识别出「连续 5 轮 GMV 迁移偏悲观」这类模式时直接给截距 β 打 ±0.1 离散跳变(一次顶十几轮)，且 LLM 只动截距不动斜率(关系结构交给更保守的 LMS)。Preference 通道：违反压力 p_j=v_j/阈值，非对称乘法更新 λ←λ·exp(δ)，δ=+0.25(违反时收紧) / −0.08(满足时放松)，收紧速度≈放松 3 倍体现「损失厌恶」。LLM 元控制器经 OpenAI Codex CLI exec 沙箱调用，reasoning_effort=high、zero-shot(防锚定历史)，每个提议必须引用 episode key 作证据、低置信度返回空提议；经七层安全管道(JSON 三策略解析→schema 校验→白名单→硬钳位 Δβ∈[−0.1,0.1]/m∈[0.5,2.0]→全局边界→失败回退 no-op)确保 LLM 即使胡说也搞不垮系统(「有边界的顾问」)。
  experiments: |
    30 轮真实生产实验、两个东南亚市场、PDP 商详页。Exp-401838(Country A,热启动,7 轮)：线上 GMV −3.6%(R2)→+9.2%(R7)，Orders +12.5%，R4–R7 连续 4 轮 GMV 为正，LLM 纠正项从 5→2 收敛。Exp-437160(Country B,冷启动,23 轮=V1 11+V3 12,走完探索→冻结→7 天 A/B→推全量)：冷启动首轮无先验即识别出 baseline 严重低配自然点击信号(ps_org_wc 1.0→3.71,+271% 全实验最大单参调整)，R7 冻结参数 7 天 A/B(10% vs 20%)拿到 GMV/UU +4.15%、GMV +4.10%、Ads Revenue +3.58%、CPC +4.19%、Ads Load −2.64%，GMV 涨主要来自客单价(GMV/Order +3.97%)。Country B 用「高点击、低 GMV/订单权重」结构绕开了 Country A 的广告-自然跷跷板。运营成本极低：单 LLM API 调用/轮、无 GPU、主成本是 3.5 小时数据积累。
  pros: |
    真实生产环境、跨两市场、30 轮、走完上线全链路的工业证据，可信度远高于 toy simulation；「线下→线上 transfer gap 可建模可持续校准」是全文最硬的发现，迁移价值大；Savage SEU 把双通道正交解耦讲成自洽理论故事，framing 优雅；「LLM 只当二阶元控制器、有硬钳位、要求引用证据、低置信返回空」是很好的 agent 安全范式；Influence Share(可分解、和为 100%)的归因思路实用；Country B 冷启动跨市场泛化 + 推全量是最可信的成功证据。
  cons: |
    方法学硬伤——几乎无可比 baseline、零消融：所谓实验基本是部署前后/轮次间纵向对比，没有「人工调参 vs Sortify」并行对照，也没测「去掉 Belief 通道/去掉 LLM 只留 LMS」，性能提升无法干净归因到所提机制，更像优秀的工业部署复盘而非可证伪的科学论文；头条数字采自最不可靠窗口——Country A +9.2% GMV/+12.5% Orders 来自 R7 一个 ~12K 曝光的清晨低流量窗口，统计功效弱；广告主利益被系统性牺牲(Country A Advertiser Value 除 R2 外全程负,R7 达 −8.9%)却被轻描淡写；参数未真正收敛(ps_ads_wo 仍有 4.5× 钟摆残余震荡,单目标+惩罚根治不了多目标张力)；强烈的自我宣传腔调(结尾大段「AI 造 AI 范式跃迁」「孤独决策者的认知穿透与编排艺术」)削弱客观性；依赖 Shopee 内部数据+Codex CLI+私有架构,外部不可复现。
  inspiration: |
    对「Agent 优化电商业务」方向是一个完整工业样本：(1) 「线下指标涨≠线上涨」的 transfer gap 可建模、可持续校准——Belief 通道思路能迁移到任何「离线评估→在线业务」的 Agent 优化场景(如 SEO 推词线下评估 vs 线上效果)；(2) LLM 别直接操纵业务参数,让它当「二阶元控制器」——只动框架级偏差/权重、有硬钳位、要求引用证据、低置信返回空,这套「有边界顾问」模式对 simulator 优化/多智体编排都是好的安全范式；(3) 钟摆效应暴露「单目标+惩罚」建模多目标张力的根本不足,后续应直接上多目标 Pareto + 把广告主当第三方利益相关者显式建模；(4) 非对称损失厌恶(收紧 3× 放松)的约束自适应思路可直接复用。
  takeaway: |
    把电商排序调参重构为「影响力交换」、用 Savage SEU 给「双通道正交解耦」找理论正当性、并跑通真实生产全自治闭环——framing 优雅、工程扎实、Country B 推全量证据可信；但缺 baseline 与消融导致性能无法归因、头条数字采自低流量窗口、叙事自我宣传过浓，是工业界 AIOps / Agent-for-RecSys 方向上工程价值高、科学严谨性偏弱的一份进展。
---
