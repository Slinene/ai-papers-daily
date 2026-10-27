---
title: The Price of Scale in Proactive Memory Recall
title_zh: 主动记忆召回中的规模代价：误报随记忆库增大的幂律恶化与控制
authors:
- Yichuan Chen
- Xin Wang
affiliations:
- Zhejiang Sci-Tech University
arxiv_id: '2610.34507'
url: https://arxiv.org/abs/2610.34507
pdf_url: https://arxiv.org/pdf/2610.34507
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 长期记忆主动召回
tags:
- proactive memory
- false alarm control
- multiple testing
- conformal prediction
- LLM agents
- memory retrieval
one_liner: 证明主动召回门控的误报率随存储规模幂律上升，提出免标签 conformal 门控并验证其控制误报
practical_value: '- 做主动 push/选品/召回时不要用固定相似度阈值：先对每个用户/上下文做 per-cue z-score 标准化，再让阈值随候选池
  N 增长；embedding 分数用 √(2 ln N) 量级，词法 tf-idf 用 ln N 更快，否则 N 从几十到几千误报会从 5% 飙到 80%+。

  - 无标签门控可直接落地：用用户历史 session/消息作为 reference，对当前候选打分，计算 conformal p-value（rank = (1
  + #{ref ≥ current})/(K+1)），设定 α=0.05 即有有限样本 FPR 保证；适合 push 文案/商品/消息的发送决策，无需标注是否打扰。

  - 两阶段 LLM judge 值得用：先用向量/词法召回 top-5 候选，再让 LLM 读候选判断是否打扰/相关；在 N=2048 时 14B judge
  达到 28% hit@4% FA，优于纯相似度 gate，但延迟和成本更高，且要确保召回覆盖（top5 含 evidence 仅 36%-65%）。

  - 容量受表示分离度限制，投入 embedding 质量/多模态上下文比堆更多记忆更划算：binormal 模型下容量随分离度平方指数增长；当候选池极大且 score
  分布重叠大时，可控误报下的命中率会掉到个位数。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
长期助手的主动记忆召回需要在每个回合判断是否打断用户。该判断本质是对整个记忆库做多重比较：阈值固定时，N 增大导致无关记忆最大相似度上升，误报失控。已有工作未系统刻画误报和命中随 N 的 scaling。

**方法关键点**  
- 将主动召回建模为 N 个无关记忆分数 + 1 个相关记忆分数的最大值检验。固定整体假阳性率 α 时，实际 per-item p_N = 1-(1-α)^{1/N} ≈ -ln(1-α)/N，命中率被钉在单比较 ROC 曲线最左端，随 N 呈 N^{-κ} 幂律衰减；binormal 模型下容量随分离度平方指数增长。
- 用 LongMemEval 和 LoCoMo 做 streaming replay，对比 fixed cosine、tf-idf、recall-v1、EVT、oracle、LLM judges 等门控。
- 提出 cue-swap conformal gate：将当前 cue 与用户自己其他 cue 在同一 store 上的最好分数比较，得到 conformal p-value，无需标签且 exchangeability 下有有限样本误报保证。

**关键结果**  
N=8 调 5% 误报的阈值到 N=2048 时，cosine 达 87%、tf-idf 100%、recall-v1 66%、EVT 31%；语义 null max 增长 ~√ln N，词法 ~ln N，需按通道选择阈值律；per-cue 标准化在匹配误报下命中率约翻倍。在 LongMemEval-M 上，cue-swap gate 误报保持 2.8-5.9%，命中率与 label-tuned threshold 相当（N=2048 时 22% vs z-score oracle 18%）；LLM 14B judge 在 N=2048 达 28% hit@4% FA，优于相似度 gate。标注显示约 90% 的自动误报确实是无关打断。

最值得记住：可控误报下，主动召回命中率随记忆库增大幂律衰减，容量由分数分离度决定；提升表示或引入 LLM judge 读候选是主要出路。
