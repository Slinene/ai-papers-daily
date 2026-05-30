---
title: 'ORACLE: Anticipating Scams from Partial Trajectories in Streaming App Usage'
title_zh: ORACLE：从流式应用使用部分轨迹中预测诈骗
authors:
- Wenbo Gao
- Songbai Tan
- Zhongan Wang
- Fei Shen
- Gang Xu
- Huiping Zhuang
- Yunyun Yang
- Ming Li
- Xiaofeng Zhu
affiliations:
- Harbin Institute of Technology, Shenzhen
- Shenzhen University
- Zhejiang University
- National University of Singapore
- Guangming Laboratory
arxiv_id: '2605.16363'
url: https://arxiv.org/abs/2605.16363
pdf_url: https://arxiv.org/pdf/2605.16363
published: '2026-05-08'
collected: '2026-05-30'
category: Agent
direction: 流式跨应用欺诈早期预测智能体
tags:
- scam detection
- agentic framework
- self-distillation
- streaming data
- cross-app reasoning
- early anticipation
one_liner: 提出首个流式跨应用诈骗早期预警智能体框架，通过自演进上下文管理与在线策略自蒸馏实现更早更准的预警。
practical_value: '- 自演进上下文管理可借鉴用于用户行为序列建模：以实体为中心存储历史交互，结合预测反馈动态调整检索规则，缓解长周期行为依赖中的证据碎片化问题，适用于电商推荐中的用户长周期兴趣追踪或风控中的异常模式发现。

  - 在线策略自蒸馏（OPSD）利用“反思”或特权信息作为教师信号，强化模型对早期弱信号的敏感度，该方法可迁移至推荐序列中早期兴趣察觉或欺诈交易的微弱特征捕捉。

  - 技能库的自我进化机制（根据高风险预测结果提炼可复用规则）可启发对话式 Agent 或推荐 Agent 的经验积累设计，让 Agent 在交互中逐步沉淀高价值决策知识。

  - 数据集构建方式（将真实欺诈案例嵌入正常日志合成长期流式轨迹）可为流式推荐中的异常检测基准提供参考，尤其适合需要评估“早期”与“低误报”双重指标的实时系统。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：智能手机诈骗通常以多阶段、跨应用的方式展开，意图逐渐暴露。现有方法多局限于单应用内容分析，无法处理长期、跨应用且证据分散的流式行为轨迹。为在诈骗意图完全显现前有效干预，需从部分轨迹中提前预测风险，但面临证据碎片化和早期信号隐蔽两大挑战。

**方法关键点**：
1. 提出 ORACLE 智能体框架，包含屏幕分析器、以人为中心的记忆存储、技能引导的上下文管理器、诈骗风险评估器四个模块，实现流式跨应用推理。
2. **自演进上下文管理**：记忆按实体（如联系人、账号）组织并实时更新；技能库根据评估器的高风险预测反馈动态进化，指导检索策略，将分散的跨时间证据整合为可复用的诈骗模式。
3. **在线策略自蒸馏（OPSD）**：学生模型仅观察部分窗口，教师模型额外获得反诈反思（对比完整诈骗轨迹生成），通过反向 KL 散度最小化，将早期弱信号的知识蒸馏到学生模型，提升对潜伏欺诈的判别力。
4. 基准数据集：基于真实诈骗案例和正常应用日志，合成 3,061 条长轨迹（平均 15 天，95 个应用，12 种诈骗类型），诈骗与正常行为交织，用于评估流式预警能力。

**关键结果**：在流式跨应用设置下，ORACLE 全面超越 GPT-5.1、Claude、Gemini 等强 LLM：命中率 98.4%（vs 80.8%），最早检测位置 EDP 29.5（vs 46.4），误报率 FAR 仅 1.3%（vs 12.8%），预警覆盖率 PAR 98.2%（vs 77.3%）。消融实验证实自演进上下文和 OPSD 各自贡献显著，案例分析展示了记忆-技能进化如何从碎片行为中逐步构建完整诈骗模式。

**最值得记住**：从部分流式轨迹中早期预测诈骗，需要将跨时间证据整合与弱信号放大相结合，自演进记忆+策略自蒸馏为此提供了有效路径。
