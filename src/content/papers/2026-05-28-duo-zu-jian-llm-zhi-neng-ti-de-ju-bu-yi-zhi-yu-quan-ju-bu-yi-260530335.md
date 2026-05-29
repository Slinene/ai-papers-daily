---
title: 'Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence
  in Multi-Component LLM Agents'
title_zh: 多组件 LLM 智能体的局部一致与全局不一致性界定
authors:
- Anany Kotawala
affiliations:
- Princeton University
arxiv_id: '2605.30335'
url: https://arxiv.org/abs/2605.30335
pdf_url: https://arxiv.org/pdf/2605.30335
published: '2026-05-28'
collected: '2026-05-29'
category: Agent
direction: 多组件智能体组合一致性问题与修复
tags:
- compositional incoherence
- multi-component agents
- coherence monitoring
- projection repair
- e-process
- LLM evaluation
one_liner: 提出组合残差 ε⋆ 量化多组件概率组合的不一致，并给出投影修复和时序监测方法，实证显示 33-94% 的测试团出现全局不一致。
practical_value: '- **运行时一致性监控**：将组合残差 ε⋆（L2 距离）作为多组件 Agent 输出的实时证书，当 ε⋆ > 阈值时触发告警或修复，避免下游策略基于不一致的概率决策。

  - **几何投影修复取代 LLM 修复**：在已知跨组件约束（如分区、否定）时，直接用 Boyle-Dykstra 投影将组合结果修复到联合一致多面体，成本低且确定性强，优于检索增强或提示工程（实验中检索、分区提示、聚合
  LLM 均无效或退化）。

  - **风险预测与阈值门控**：利用 Rayleigh 商从组件协方差预估组合残差量级，可在部署前评估特定任务有多大概率出现不一致，并结合 log-payoff
  后悔曲线设定 γ 门限，仅在高风险时执行修复，节约计算。

  - **时序异常检测**：e-process 构建的任意时间有效检验可用于长期运行 Agent 管道，连续监测组合残差流，一旦累积证据超过阈值即发出相干性告警，无需预设固定区间。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
多组件 LLM 智能体（如规划-检索-预测）中，每个组件只看到部分问题，即使各组件自身校准且局部一致，组合后的联合预测可能违反概率公理（如互斥事件概率之和不为 1），导致 Dutch-book 风险。现有校准、自一致性和共形预测等方法只关注单输出，无法捕捉跨组件约束。该工作旨在定义运行时度量，以检测并修复这种“局部一致、全局不一致”的失败模式。

**方法关键点**  
- **组合残差 ε⋆**：定义为组件局部投影后的组合向量到联合一致多面体（coherent polytope）的 L2 距离；正值意味着全局不一致，可由系统输出和声明约束在线计算。  
- **产品结构二分法**：在 owner-selected 聚合下，局部一致保证全局一致当且仅当联合多面体是局部多面体的 Cartesian 积；否则存在局部一致但组合不一致的输入。  
- **Rayleigh 商预测**：在随机分配组件时，ε⋆² 的期望可由组件间协方差和约束法向量闭式给出，精度在三个关系类上偏差 <7%。  
- **层级投影修复**：Boyle-Dykstra 循环投影到各局部多面体和耦合约束的交集，收敛到全局一致点，将 ε⋆ 降为 QP 求解器下界。  
- **时序 e-process**：利用有界差分构造非负上鞅，构建任意时间有效的顺序检验，不预设停止时刻即可控制误报率。

**关键实验**  
在 Paleka（蕴含、否定、合取、析取）和 Polymarket（分区约束）上，用 Claude-Haiku-4.5、GPT-5.4-mini、GPT-5.4-nano、Llama-3.3-70b 四模型组成1876个团：  
- ε⋆ > 0 的团占比：分区 94%、否定 66%、析取 43%、合取 33%。  
- 层级投影将平均暴露界 √(m⋆)·ε⋆ 从 0.137 降至数值零。  
- 与解析标签相比，JCD 投影显著降低 Brier 分数（否定 -0.014，合取 -0.008，分区 -0.005），析取因标签噪声边际正向（+0.003）。  
- 三种直观 LLM 侧缓解（检索增强、分区提示、聚合 LLM）均未消除残差，甚至回退；几何修复以一次 QP 调用实现零残差。  
- 前沿模型重跑（Claude-Opus-4.7、GPT-5.5 等）仍见 97.8% 团 ε⋆>0，但均值为 0.072（中端 0.118）。  
- 在 1770 次真实赌注中，JCD 修复带来 +0.115 nats 的 log-payoff 收益，且收益随 ε⋆ 四分位单调递增。

**核心结论**  
“组合残差 ε⋆ 是一个可运行时计算的分布无关证书，它捕捉了仅靠单组件校准无法发现的跨组件逻辑违规；几何投影修复相比提示工程更可靠且无额外 LLM 调用成本。”
