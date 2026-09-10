---
title: 'GANDR: Claim Auditing for Verifiable Legal Answer Generation'
title_zh: GANDR：面向可验证法律答案生成的逐条声明审计
authors:
- Chen Qian
- Yimeng Wang
- Yu Chen
- Lingfei Wu
- Andreas Stathopoulos
affiliations:
- William & Mary
- Anytime AI
arxiv_id: '2609.10293'
url: https://arxiv.org/abs/2609.10293
pdf_url: https://arxiv.org/pdf/2609.10293
published: '2026-09-09'
collected: '2026-09-10'
category: MultiAgent
direction: 多智能体逐条声明审计与引用验证
tags:
- Multi-Agent
- Claim Auditing
- Grounded Generation
- RAG
- Legal NLP
- LLM Evaluation
one_liner: 用 Drafter-Critic 双智能体逐条审计引用与声明，严格引用准确率 70.8%，领先最强基线 11.3 点
practical_value: '- 在 RAG 生成文案、推荐理由、广告文案等场景，增加独立 Critic agent 逐条核对事实与引用源，避免整体得分掩盖局部幻觉。

  - 引入 protocol-anchored commit：只有 Critic 审计通过才提交答案，否则触发修改；消融显示去掉该规则严格准确率下降 22.7 点，是低成本高收益的工程控制。

  - 将引用验证从整体打分改为逐 claim 的 audit trace，便于线上监控、人工复核和 badcase 定位；对生成式推荐解释或选品理由尤其适用。

  - 在低风险业务中，可只用审计模型的二分类检测器（支持不足 vs 支持充足）过滤高风险内容，而非依赖四分类标签，实验 F1 可达 0.84。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**  
法律等高风险领域，LLM 答案必须能逐条验证引用；现有 grounded-generation 只对整体答案打分，单个错误引用也可能获得高分。  

**方法关键点**  
GANDR 采用双智能体结构：Drafter 按结构化法律推理格式撰写答案；Critic 以人类验证者视角逐条审计每个 claim 与其引用源，每轮输出逐条 audit trace。严格正确性准则要求每个引用必须能解析到检索器返回的 passage。系统还引入 protocol-anchored commit rule，由 Critic 审计通过才提交答案。  

**关键结果**  
在 185 项法律基准上，6 个系统共享同一 backbone、检索面和引用指令，GANDR 在所有主要指标上排名第一，strict accuracy 达 70.8%，领先最强基线 11.3 点（p<0.01）。去掉 protocol-anchored commit rule 后严格准确率下降 22.7 点；在三个额外 backbone 上仍保持 +3.2 到 +6.5 点的领先。与两位法律训练标注者对比，审计 flags 作为二分类检测器 F1 为 0.84，而四分类 verdict 一致性较弱，仅适合辅助。
