---
title: 'G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving
  Demands'
title_zh: G-CAST：面向电商智能体演进需求的受控持续自训练
authors:
- Yuechun Yu
- Wenzheng Kong
- Xiaofeng Mao
- Jin Zhang
affiliations:
- Alibaba Group
arxiv_id: '2611.17814'
url: https://arxiv.org/abs/2611.17814
pdf_url: https://arxiv.org/pdf/2611.17814
published: '2026-11-12'
collected: '2026-11-17'
category: Agent
direction: 电商 Agent 持续自训练 · 奖励治理
tags:
- Continual Self-Training
- Reward Evolution
- Data Orchestration
- E-Commerce Agent
- Entropy Prioritization
- Checkpoint Transition
one_liner: 提出 G-CAST 受控持续自训练系统，用奖励路由+熵优先级数据编排与契约驱动奖励演化，同步修复电商智能体模型/数据/奖励三重失配
practical_value: '- 在电商 Agent/生成式推荐场景中，将每次模型上线视为 checkpoint transition，要求候选模型在新增需求切片和所有历史保留切片上同时通过累积评估；建立
  evaluation ledger，记录 rejected checkpoint 和 regression，可有效防止为追新需求而遗忘旧行为。

  - 数据生产用多 rollout（如 8 条/query）并按 reward 模式路由：全失败且有验证目标→SFT、混合结果→RL、全成功→只做监控；池内用 token
  熵第 90 百分位最大值做优先级排序，而不是用熵直接判断正确性，能明显提升有限训练预算下的效果，适合迁移到商品/内容推荐的 LLM 后训练管线。

  - 奖励函数应版本化并与能力契约同步演化，新增工具/技能/流程时不能沿用旧 reward；对高 reward 轨迹做审计，发现 search-result misuse
  和 hallucinated entities 两类假阳性后，引入 grounding penalty 组件，并通过目标用例、已知正确回归、冻结轨迹重打分、replay
  等 gate 才能进入训练，可复用为生成式客服/导购的答案证据校验模块。

  - 工程治理收益显著：自动门控将人工奖励审计从约 2 人日/轮降到 30 分钟，需求到上线从约 1 周缩短到 2 天；建议为 agent 训练链路增加自动验证与门控，不仅能抓坏候选，也能降低持续运维成本。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
电商购物 Agent 部署后，用户需求与 harness 的工具/技能/操作流程持续扩展，固定 checkpoint 会出现三重耦合失配：模型不会用新能力、旧轨迹缺少新能力证据、旧奖励无法正确评判新行为。手动定期重训延迟高、人力成本大，需要治理式持续自训练。

**方法关键点**  
- 以 checkpoint transition 为适应单元，同时版本化已部署模型、能力契约、可执行奖励、学习证据和累积评估账本。  
- 主自进化循环：每条生产查询用已接受 checkpoint 生成 8 个 rollout；先做奖励可靠性检查，分离训练证据与回归监控。  
- 奖励路由+熵优先级数据编排：全失败且有验证目标→SFT，混合结果→RL，全成功→监控；池内用 token 熵第 90 百分位最大值排序，只做池内优先级，不把熵当正确性信号。  
- 奖励演化循环：检测到可能奖励错误时暂停训练，执行契约接地标注、奖励更新提案、离线检查（目标用例、回归、重打分、replay）、试训练和联合评估；可执行奖励为版本化规则组件，随契约累积演化。

**关键实验**  
在阿里 1688 的 Yuancai B2B 采购 Agent 上，覆盖 4 个需求周期，每周期 2000 条 rollout 池 + 100 条评估切片，基座 Qwen3-4B-Thinking-2507。固定 checkpoint 在 P1→P1-4 累计 base reward 从 0.9065 降到 0.6354，P4 新需求仅 0.1877。G-CAST 在 Iteration 3 累计 reward 0.9288 超过 AutoTrainess 0.9210；Iteration 4 累计 0.8078 vs 0.7911，且保留旧期 reward +0.012 而 AutoTrainess -0.017。消融：Reward+Entropy post-RL 累计 0.7930，Reward+Random 0.7721，Random 0.7334。奖励演化：审计高 reward 轨迹发现 search-result misuse 84%、hallucinated entities 82% 假阳性；Static/Ungated/Gated 在 P1-3 累计 0.8810/0.8926/0.9288，技能选择准确率 0.6867/0.6956/0.8667。运营上人工奖励审计从约 2 人日降到 30 分钟/轮，周期从一周到两天。

**最值得记住的一句话**  
部署式电商 Agent 的奖励函数必须与工具/技能/流程契约一起版本化和门控演化；否则固定奖励的后训练会在新增能力上落后，并遗忘旧行为。
