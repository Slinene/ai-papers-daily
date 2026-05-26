---
title: 'Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents'
title_zh: 预见与学习：释放主动式智能体的空闲计算能力
authors:
- Haoyi Hu
- Qirong Lyu
- Xianghan Kong
- Weiwen Liu
- Jianghao Lin
- Zixuan Guo
- Yan Xu
- Yasheng Wang
- Weinan Zhang
- Yong Yu
affiliations:
- Shanghai Jiao Tong University
- Tencent
arxiv_id: '2605.25971'
url: https://arxiv.org/abs/2605.25971
pdf_url: https://arxiv.org/pdf/2605.25971
published: '2026-05-25'
collected: '2026-05-26'
category: Agent
direction: 主动式智能体 · 空闲计算优化
tags:
- Proactive Agent
- Idle-Time Compute
- Future-State Prediction
- Memory
- ProActEval
- LLM
one_liner: ProAct架构利用空闲时间预测未来需求并主动准备，在ProActEval上减少交互轮次14.8%，降低用户努力11.7%，幻觉率下降28.1%
practical_value: '- **对话式推荐中的前瞻计算**：可借鉴 ProAct 的“对话历史 + 持久记忆 → 未来需求预测”管道，在电商对话助手场景下，利用提问间隙预取候选商品、生成推荐解释，降低用户显式询问轮次。

  - **价值感知的主动推送**：论文的 \(S(z)\) 评分（用户相关性、知识缺口、增量价值、时效性）和 PushScore 门控（信息价值 vs. 打断成本）可直接迁移到主动推荐系统中，决定是否向用户推送推荐卡片，避免骚扰。

  - **持久记忆与主动维护**：ProAct 的 memory layer 持续抽取用户偏好、事实、未决缺口，并将其转化为预测需求，这相当于一种“记忆驱动的意图发现”机制，可嵌入用户长期画像系统，驱动个性化主动触发。

  - **分离响应与前瞻计算**：将部分算力从“请求时推理”迁移到空闲期预计算，尤其适合电商大促等高负载场景，可离线生成候选项并缓存至 KV cache，在线仅需轻量匹配，降低延迟。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：当前 AI 智能体以被动响应用户请求为主，交互间的空闲时间完全浪费，无法主动准备未来需求。受心理学主动应对策略启发，论文提出将空闲时间转化为“预测—准备—记忆更新”循环，使智能体从静态响应转向持续进化。

**方法关键点**：
- **架构**：ProAct 由持久记忆层、未来状态预测（Future‑State Prediction）和空闲时获取（Idle‑Time Acquisition）组成。记忆层维护用户画像、实体事实、对话摘要与待填补的知识缺口。
- **未来状态预测**：基于对话历史 \(H_t\) 与记忆 \(M_t\) 生成候选未来需求集 \(Z_t\)，包括局部场景外推、关联主题扩展以及记忆缺口填充，经置信度过滤与去重后输出。
- **空闲时获取与门控**：对每个候选 \(z\) 计算价值分数 \(S(z) = w_r r + w_g g + w_v v + w_\tau \tau\)（相关性、缺口、增量价值、时效性），仅对通过阈值者分配搜索预算，生成带溯源的知识工件，并通过效用感知门控决定立即推送（push）、排队整合（queue）或静默存储（store）。
- **基准**：配套提出 ProActEval，包含 200 个场景、40 个领域，附有可预测需求链与多样化认知画像，用于严格评估主动能力。

**关键结果**：
- 在 ProActEval 上，相比纯被动基线，ProAct 将完成任务的交互轮数 (\(T_{100}\)) 减少 14.8%，用户显式提问次数（User Effort）降低 11.7%，幻觉率下降 28.1%。
- 消融实验表明，无方向性的空闲搜索仅带来微小增益，而定向预测是实现提质减轮的核心。
- 在 MemBench 反射记忆任务上，ProAct 达到 10k 上下文 84.3% 和 100k 上下文 86.3% 的准确率，验证记忆系统对长期主动行为的支撑。

**一句话**：真正的主动智能体不是替用户做决策，而是用价值函数在正确时机交付恰到好处的准备，让帮助无感发生。
