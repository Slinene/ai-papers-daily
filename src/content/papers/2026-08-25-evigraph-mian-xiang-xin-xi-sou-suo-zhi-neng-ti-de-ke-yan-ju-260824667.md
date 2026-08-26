---
title: 'EviGraph: Towards Verifiable Evidence Construction for Information-Seeking
  Agents'
title_zh: EviGraph：面向信息搜索智能体的可验证证据构建
authors:
- Jiashun Chen
- Yirong Mao
- Wenhui Que
affiliations:
- WeChat, Tencent Inc., Beijing, China
arxiv_id: '2608.24667'
url: https://arxiv.org/abs/2608.24667
pdf_url: https://arxiv.org/pdf/2608.24667
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 搜索证据图与过程奖励 RL
tags:
- Agentic Search
- Evidence Graph
- Process Reward
- RL
- Verifiable Reasoning
- LLM
one_liner: 将智能体网络搜索重构为可验证证据图构建，以共享策略分离搜索与证据记录，用稠密过程奖励直接监督证据基础
practical_value: '- 对电商导购/搜索 Agent：把「检索到的商品或卖点」与「用户查询约束」显式建图，每个卖点必须锚定来源 span 并标记 support/conflict；可避免用相关但时间、地区、数值错误的页面回答，适合商品事实校验、选品问答、推荐理由生成。

  - 采用「冻结 verifier + 确定性 structural validator + 可学习 policy」的分离架构：把不可靠的语义判断和结构化校验分开，policy
  只提图编辑请求，错误可局部归因；工程上可用规则引擎做图校验，降低对单一 LLM 的依赖和幻觉。

  - 过程奖励设计可迁移：coverage 用 potential-based shaping，配合 canonical signature 去重、per-triple
  bonus cap、KL penalty，能抑制 reward hacking 和重复记录；可用于训练搜索/推荐 Agent 的中间 grounding。

  - 多约束查询可拆成 candidate–constraint claim，每个 tag 独立追踪 MISSING/SUPPORT/CONFLICT，适合电商商品属性（产地、年份、价格、代言人）验证和
  push 文案事实核查，让 Agent 明确知道还缺哪些约束。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Agentic Web search 通常只优化最终答案正确性，但答案正确不等于证据充分：检索相关页面可能提到正确实体却用错时间、地点或数值；citation 也不说明哪个 span 支撑哪个 claim。多约束研究任务中，一个页面往往只满足部分约束，需要显式构建证据来联合满足所有约束。现有线性轨迹无法监督中间 grounding，因此需要把搜索过程重构为可验证的证据构建。

**方法关键点**
- 将 agentic search 形式化为构建 typed、span-grounded claim–evidence DAG：节点分为 Document、Span、Atomic Claim、Answer Candidate；边包括 CONTAINS 和带 polarity（support/conflict）的 evidence 边。
- 同一策略 πθ 承担两个可训练角色：executor 只根据图快照发查询或停止；evidence-proposal 角色将冻结 verifier 返回的证据 item 映射为 add/support 图编辑请求。冻结 verifier 读页面并返回 verbatim span、约束 tag、relevance 和 polarity；确定性 structural validator 只检查语法与图不变量，不做语义判断。
- 图状态是持久工作记忆，executor 看到 O(C+|T|) 压缩快照，不用重读原始页面。
- RL 采用 role-conditioned GRPO：executor 奖励包含 retrieval novelty + coverage potential shaping − search cost；evidence-proposal 奖励包含 acceptance bonus + graph-quality potential（coverage − unresolved conflict − off-task penalty）。使用 potential-based shaping、canonical signature、per-triple bonus cap 和 KL penalty 防止 reward farming。
- 训练使用 Search-R1 的 question-query 数据，无监督冷启动，过程奖励在线生成。

**关键实验**
在 BrowseComp-Plus 830 题上，Qwen3-8B EviGraph RL 达到 35.9%，无 RL 双角色架构为 26.9%，单 agent 仅 2.7%；同 backbone 消融显示 RL 在搜索次数几乎不变的情况下将准确率提升 9 个百分点，并把平均生成 token 从 1878 降到 1689。LiveVQA 上 Qwen3-VL-8B EviGraph + Web search 达到 78.0%，显著高于 no-search 51.0% 和 direct 47.0%。在 BrowseComp、GAIA、XBench 上，Qwen3-8B RL 分别达到 17.8%、53.4%、56.0%，Qwen3-32B 为 19.5%、55.0%、58.0%，均超过同级别 ReAct 和部分专用系统。

**最值得记住的一句话**
将 agentic search 重构为可验证证据图构建，用稠密过程奖励直接监督证据记录，而不是只监督最终答案；answer correctness does not imply evidential sufficiency。
