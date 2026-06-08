---
title: Hierarchical Certified Semantic Commitment for Byzantine-Resilient LLM-Agent
  Collaboration
title_zh: 层次化认证语义承诺：面向拜占庭容错的 LLM 智能体协作最终性控制
authors:
- Haoran Xu
- Lei Zhang
- Iadh Ounis
- Xianbin Wang
affiliations:
- University of Glasgow
- University of Western Ontario
arxiv_id: '2606.07316'
url: https://arxiv.org/abs/2606.07316
pdf_url: https://arxiv.org/pdf/2606.07316
published: '2026-06-05'
collected: '2026-06-08'
category: MultiAgent
direction: Agent 多智体协作 · 拜占庭容错 · 语义承诺
tags:
- Byzantine resilience
- LLM agents
- semantic commitment
- typed finality
- multi-agent collaboration
one_liner: 为多 LLM 智能体协作提出一种层次化最终性控制原语，输出语义提交、裁决提交或安全中止三类带证书的承诺。
practical_value: '- **结构化提案 + 确定性编码**：在电商多 Agent 辩论或事实核查场景中，可要求每个 Agent 输出结构化字段（裁决、置信度、证据链），并对该结构进行确定性语义编码（如
  Sentence-Transformer），为后续几何分析或证书绑定提供统一基础。

  - **层次化最终性决策**：借鉴三类承诺机制（semantic_commit / verdict_commit / abort），根据嵌入一致性和投票 margin
  分级决定是否提交及提交类型，避免在不一致时强行输出无保证的结果，提升系统可审计性。

  - **不依赖外部真相的证书**：协议仅使用嵌入几何与投票计数，不依赖 gold truth 或外部法官。在设计多 Agent 协作流程时，可将最终决策与有噪声的外部标签解耦，通过
  2f+1 签名证书提供可验证的安全保证。

  - **嵌入级安全中止**：当语义核心不可信时主动 abort，防止拜占庭语义投毒污染下游任务。在推荐场景的 Agent 辩论或内容安全审核中，可设置类似半径阈值作为自动安全兜底。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
多 LLM 智能体协作进行事实核查、路由决策等任务时，智能体输出的自然语言提案虽语义一致但文本各异，传统拜占庭容错（BFT）协议要求字节级一致，无法直接适用。软投票或多数聚合没有证书、不区分语义一致性，且容易受到拜占庭语义投毒——恶意智能体生成的文本流畅、接近诚实提案的嵌入分布，却能恶意翻转下游分类器。  
因此需要一种能从嵌入几何和投票信号中自动判断“应提交何种类型结果”的最终性控制原语。

**方法关键点**  
- **结构化提案与确定性编码**：每个智能体输出包含裁决、置信度、证据 ID、理由等字段的提案；协议对提案文本进行规范化和共享嵌入编码，得到单位球面上的嵌入向量。  
- **层次化决策管道**：  
  1. 按裁决分组，选出最大组作为候选（需 ≥2f+1）。  
  2. 在候选组内通过角度图找出满足 2f+1 大小且半径 ≤θ_α 的连通分量，作为语义核心。  
  3. 若语义核心存在 → 聚合为嵌入中位数并量化，生成 `semantic_commit`，绑定 2f+1 证书。  
  4. 若语义核心不满足但裁决 margin≥1 → 生成 `verdict_commit`，仅包含裁决负载和证书。  
  5. 否则 → 输出带类型原因的 `abort`。  
- **证书与安全**：所有提交均绑定 2f+1 个不同签名者证书，保证至少 f+1 个诚实节点参与。协议不依赖外部真相或证据校验。

**关键实验与数字**  
- 控制诊断基准 **BCS_v1**：在 BFT 可行区（n≥3f+1），语义偏离低至 0.31°–2.04°；超出 BFT 时 100% 中止。  
- 真实智能体基准 **MVR-50**（50 个 Climate-FEVER 任务，10 个 Agent，f=2）：  
  - 提交率：静态 0.90 / 抢先 0.92。  
  - 诚实参考无效提交率（invalid_hmaj）仅 0.02 / 0.00，与带证书的多数基线（B3）相近，但额外贡献了 74%/72% 轮次的 `semantic_commit`（带嵌入溯源）。  
  - 若去掉判决回退（严格语义 CSC），提交率降至 0.54/0.48，证明层次化回退对覆盖率提升 +0.36/+0.44 不可或缺。  
  **核心贡献**：不是简单的多数投票，而是区分语义级与裁决级最终性的类型化承诺，使下游可以查验是否达成语义聚合或仅达成交互一致。
